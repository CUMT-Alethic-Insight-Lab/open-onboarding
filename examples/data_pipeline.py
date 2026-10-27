import argparse
import hashlib
import html
import json
import re
import unicodedata
from pathlib import Path

SEED = 42
MIN_TOKENS = 5
NEAR_THRESHOLD = 0.75


def digest(value):
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def normalize(text):
    text = re.sub(r"<[^>]+>", " ", html.unescape(text))
    return re.sub(r"\s+", " ", unicodedata.normalize("NFKC", text)).strip()


def tokens(text):
    return set(re.findall(r"[\w-]+", text.casefold()))


def jaccard(left, right):
    return len(left & right) / max(1, len(left | right))


def minhash(values, index):
    return min(int.from_bytes(hashlib.blake2b(v.encode(), digest_size=8, key=str(index).encode()).digest(), "big") for v in values)


def near_candidates(records, bands=8, rows=4):
    signatures = {r["id"]: [minhash(r["tokens"], i) for i in range(bands * rows)] for r in records}
    candidates = set()
    for band in range(bands):
        buckets = {}
        for r in records:
            key = tuple(signatures[r["id"]][band * rows:(band + 1) * rows])
            buckets.setdefault(key, []).append(r["id"])
        for bucket in buckets.values():
            for i, left in enumerate(bucket):
                for right in bucket[i + 1:]:
                    candidates.add((left, right))
    return candidates


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, default=Path(__file__).parent / "data/documents.jsonl")
    parser.add_argument("--output", type=Path, default=Path(__file__).parent / "output/data")
    args = parser.parse_args()
    raw = [json.loads(line) for line in args.input.read_text(encoding="utf-8").splitlines() if line.strip()]
    required = {"id", "text", "source", "license", "group", "created_at"}
    stats = {"input": len(raw), "invalid_schema": 0, "empty": 0, "too_short": 0, "exact_duplicate": 0, "near_duplicate": 0}
    clean = []
    seen_exact = {}
    for record in raw:
        if set(record) != required or any(not isinstance(record[k], str) for k in required):
            stats["invalid_schema"] += 1
            continue
        text = normalize(record["text"])
        if not text:
            stats["empty"] += 1
            continue
        record["tokens"] = tokens(text)
        if len(record["tokens"]) < MIN_TOKENS:
            stats["too_short"] += 1
            continue
        record["text"] = text
        record["content_hash"] = digest(text)
        if record["content_hash"] in seen_exact:
            stats["exact_duplicate"] += 1
            continue
        seen_exact[record["content_hash"]] = record["id"]
        clean.append(record)
    candidates = near_candidates(clean)
    kept = []
    near_pairs = []
    for record in sorted(clean, key=lambda r: (r["created_at"], r["id"])):
        duplicate = False
        for previous in kept:
            pair = tuple(sorted((record["id"], previous["id"])))
            if pair in candidates and jaccard(record["tokens"], previous["tokens"]) >= NEAR_THRESHOLD:
                duplicate = True
                near_pairs.append({"removed": record["id"], "kept": previous["id"], "jaccard": round(jaccard(record["tokens"], previous["tokens"]), 3)})
                break
        if duplicate:
            stats["near_duplicate"] += 1
        else:
            kept.append(record)
    groups = {}
    for record in kept:
        groups.setdefault(record["group"], []).append(record)
    ordered = sorted(groups.values(), key=lambda rows: min(r["created_at"] for r in rows))
    if len(ordered) < 3:
        raise ValueError("Need at least three independent groups for train/validation/test")
    split_groups = {"train": ordered[:-2], "validation": ordered[-2:-1], "test": ordered[-1:]}
    split_rows = {name: [r for group in rows for r in group] for name, rows in split_groups.items()}
    for name, rows in split_rows.items():
        if not rows:
            raise ValueError(f"Empty split: {name}")
    for left in split_rows:
        for right in split_rows:
            if left < right:
                assert not ({r["group"] for r in split_rows[left]} & {r["group"] for r in split_rows[right]})
                for a in split_rows[left]:
                    for b in split_rows[right]:
                        if a["content_hash"] == b["content_hash"] or jaccard(a["tokens"], b["tokens"]) >= NEAR_THRESHOLD:
                            raise ValueError(f"Near-duplicate leakage: {a['id']} / {b['id']}")
    args.output.mkdir(parents=True, exist_ok=True)
    serializable = [{k: v for k, v in r.items() if k != "tokens"} for rows in split_rows.values() for r in rows]
    version = digest(json.dumps({"seed": SEED, "min_tokens": MIN_TOKENS, "near_threshold": NEAR_THRESHOLD, "records": serializable}, sort_keys=True, ensure_ascii=False))
    for name, rows in split_rows.items():
        (args.output / f"{name}.jsonl").write_text("".join(json.dumps({k: v for k, v in r.items() if k != "tokens"}, ensure_ascii=False, sort_keys=True) + "\n" for r in rows), encoding="utf-8")
    import pandas as pd
    parquet_path = args.output / "dataset.parquet"
    pd.DataFrame(serializable).to_parquet(parquet_path, index=False)
    restored = pd.read_parquet(parquet_path)
    assert restored["id"].tolist() == [r["id"] for r in serializable]
    stats.update({"kept": len(kept), "splits": {k: len(v) for k, v in split_rows.items()}, "near_pairs": near_pairs, "version_sha256": version, "parquet_roundtrip_verified": True})
    (args.output / "stats.json").write_text(json.dumps(stats, indent=2, ensure_ascii=False), encoding="utf-8")
    (args.output / "dataset_card.md").write_text(f"# Synthetic learning dataset\n\n- Source: original synthetic snippets bundled with this repository; no crawl or personal data.\n- License: CC-BY-4.0 for the snippets; linked tools retain their licenses.\n- Intended use: teach cleaning, deduplication, splitting and versioning only; not an evaluation benchmark.\n- Processing: schema validation, NFKC/whitespace/HTML cleanup, exact hash, MinHash candidates + Jaccard, group/time split.\n- Version: `{version}`; seed {SEED}.\n- Limitations: tiny English sample; MinHash implementation is pedagogical, not production-scale; token Jaccard misses paraphrase semantics.\n- Audit: see `stats.json` for removals and split sizes.\n", encoding="utf-8")
    print(json.dumps(stats, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
