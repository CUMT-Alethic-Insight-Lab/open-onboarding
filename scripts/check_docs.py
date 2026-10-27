#!/usr/bin/env python3
import argparse
import re
import sys
import unicodedata
from collections import defaultdict
from pathlib import Path
from urllib.parse import unquote

CORE = {
    "docs/foundations/prerequisites.md": ("PR", 6),
    "docs/foundations/classical-ml.md": ("ML", 9),
    "docs/foundations/neural-networks.md": ("DL", 10),
    "docs/paths/data-engineering.md": ("DE", 9),
    "docs/paths/efficient-ai.md": ("EA", 3),
}
FIELDS = ["前置", "目标", "指定材料", "学习动作", "最小实践", "完成标准", "卡住时", "下一步", "资源要求"]
LINK = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")
HEADING = re.compile(r"^#{1,6}\s+(.+?)\s*#*\s*$", re.M)
ANCHOR = re.compile(r"<a\s+(?:id|name)=[\"']([^\"']+)[\"']", re.I)
NODE = re.compile(r"\b(?:PR|ML|DL|DE)-\d{2}\b|\bEA-[123]\b")


def slug(text):
    text = re.sub(r"<[^>]+>|[`*~]", "", text).strip().lower()
    result = []
    for char in text:
        if char.isspace():
            result.append("-")
        elif char == "_" or char == "-" or unicodedata.category(char)[0] in {"L", "N", "M"}:
            result.append(char)
    return "".join(result)


def markdown_files(root):
    return sorted(p for p in root.rglob("*.md") if not any(part in {".git", ".venv", "node_modules"} for part in p.parts))


def anchors(text):
    found = {a for a in ANCHOR.findall(text)}
    counts = defaultdict(int)
    for heading in HEADING.findall(text):
        base = slug(heading)
        found.add(base if counts[base] == 0 else f"{base}-{counts[base]}")
        counts[base] += 1
    return found


def sections(text, pattern):
    matches = list(re.finditer(pattern, text, re.M))
    for i, match in enumerate(matches):
        yield match.group(1), text[match.start():matches[i + 1].start() if i + 1 < len(matches) else len(text)]


def main():
    parser = argparse.ArgumentParser(description="Check internal Markdown links, anchors and learning-node contracts")
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    root = args.root.resolve()
    errors = []
    files = markdown_files(root)
    if not files:
        errors.append("No Markdown files found")
    anchor_map = {p.resolve(): anchors(p.read_text(encoding="utf-8")) for p in files}
    for path in files:
        text = path.read_text(encoding="utf-8")
        for raw in LINK.findall(text):
            target = raw.strip()
            if target.startswith("<") and ">" in target:
                target = target[1:target.index(">")]
            elif " \"" in target:
                target = target.split(" \"", 1)[0]
            target = target.strip()
            if not target or target.startswith(("http://", "https://", "mailto:", "tel:", "data:")):
                continue
            file_part, separator, fragment = target.partition("#")
            destination = path if not file_part else (path.parent / unquote(file_part)).resolve()
            if root not in destination.parents and destination != root:
                errors.append(f"{path.relative_to(root)}: link escapes repository: {raw}")
                continue
            if destination.is_dir():
                destination = destination / "README.md"
            if not destination.exists():
                errors.append(f"{path.relative_to(root)}: missing target: {raw}")
                continue
            if separator and fragment and destination.suffix == ".md":
                if unquote(fragment) not in anchor_map.get(destination, set()):
                    errors.append(f"{path.relative_to(root)}: missing anchor #{fragment} in {destination.relative_to(root)}")
    nodes = {}
    for name, (prefix, count) in CORE.items():
        path = root / name
        if not path.exists():
            errors.append(f"Missing core path: {name}")
            continue
        found = list(sections(path.read_text(encoding="utf-8"), rf"^## ({prefix}-\d{{2}}|{prefix}-[123]) .+$"))
        if len(found) != count:
            errors.append(f"{name}: expected {count} nodes, found {len(found)}")
        for node, body in found:
            nodes[node] = body
            for field in FIELDS:
                if f"**{field}**" not in body:
                    errors.append(f"{name} {node}: missing field {field}")
    for name in ["README.md", "docs/start-here.md"]:
        text = (root / name).read_text(encoding="utf-8")
        for target in ["foundations/classical-ml.md", "foundations/neural-networks.md", "paths/data-engineering.md", "paths/efficient-ai.md"]:
            expected = f"docs/{target}" if name == "README.md" else target
            if expected not in text:
                errors.append(f"{name}: no direct navigation to {expected}")
    for node, body in nodes.items():
        prereq = next((line for line in body.splitlines() if "**前置**" in line), "")
        nodes[node] = set(NODE.findall(prereq))
    for node, dependencies in nodes.items():
        for dependency in dependencies:
            if dependency not in nodes:
                errors.append(f"{node}: unknown prerequisite {dependency}")
    visiting, visited = set(), set()

    def visit(node):
        if node in visiting:
            errors.append(f"Prerequisite cycle includes {node}")
            return
        if node in visited:
            return
        visiting.add(node)
        for dependency in nodes.get(node, set()):
            if dependency in nodes:
                visit(dependency)
        visiting.remove(node)
        visited.add(node)

    for node in nodes:
        visit(node)
    history = root / "docs/history/ai-history.md"
    if history.exists():
        count = len(re.findall(r"^\| \d{4}", history.read_text(encoding="utf-8"), re.M))
        if not 25 <= count <= 40:
            errors.append(f"History must contain 25–40 representative nodes, found {count}")
    for pattern in [r"ghp_[A-Za-z0-9]{20,}", r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----", r"AKIA[0-9A-Z]{16}"]:
        for path in files:
            if re.search(pattern, path.read_text(encoding="utf-8")):
                errors.append(f"{path.relative_to(root)}: possible secret pattern")
    if errors:
        print(f"FAIL: {len(errors)} issue(s)")
        print("\n".join(f"- {e}" for e in errors))
        return 1
    print(f"PASS: {len(files)} Markdown files; internal links/anchors valid")
    print(f"PASS: {len(nodes)} core nodes; required fields and prerequisites valid; no dependency cycles")
    print("PASS: history contains 25–40 representative nodes; navigation and secret patterns checked")
    return 0


if __name__ == "__main__":
    sys.exit(main())
