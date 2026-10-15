# Editor & AI Tools | 编辑器与 AI 工具

Goal: VS Code as your editor, plus one AI coding assistant installed and logged in.

目标：装好 VS Code，并安装登录至少一个 AI 编程助手。

## 1. VS Code

Install from [code.visualstudio.com](https://code.visualstudio.com). During setup, check "Add to PATH" and "Open with Code" in the context menu. Useful built-in features for this workflow: the Source Control panel (stage/commit/push without the terminal) and the integrated terminal (open a Git Bash profile).

从 [code.visualstudio.com](https://code.visualstudio.com) 安装，勾选加入 PATH 和右键菜单。本流程常用的内置功能：源代码管理面板（不敲命令也能 stage/commit/push）和集成终端（可切换为 Git Bash）。

Suggested extensions | 建议插件：

| Extension | 用途 |
| --- | --- |
| GitHub Pull Requests | Review and comment on PRs inside the editor / 在编辑器内 review PR |
| Markdown All in One | Preview and lint the docs you will write / 预览你要写的 Markdown 文档 |

## 2. AI Coding Assistants | AI 编程助手

Pick at least one, install it, and log in:

至少装一个并登录：

| Tool | 安装方式 | Notes |
| --- | --- | --- |
| Kimi Code | Install the CLI per the official docs, then run the login command and complete browser authorization | Good default for this org's workflow / 本教程默认示例 |
| opencode | Install per its official docs, then run its auth/login flow to connect a provider | Open-source alternative / 开源替代 |

Verify the install — the exact command depends on the tool, e.g.:

安装后验证（具体命令以各工具文档为准）：

```bash
kimi --version      # or: opencode --version
```

## 3. Rules Before You Use Them | 使用前的规矩

AI assistance is allowed in this org, but every AI-assisted contribution must be **disclosed, verified, and understood** — the operational version is in [AI-assisted workflow](../04-ai-assisted/workflow.md), and the binding policy lives in governance-public.

组织内允许使用 AI 辅助，但每次 AI 辅助贡献都必须**声明、验证、理解**。操作版见 [AI 辅助工作流](../04-ai-assisted/workflow.md)，正式政策在 governance-public 仓。

## Done When | 完成标志

- [ ] VS Code opens a cloned repo and its Source Control panel shows changes / 能打开仓库并看到改动
- [ ] At least one AI assistant runs and answers a prompt / 至少一个 AI 助手可正常对话
- [ ] You have read the three principles (disclose / verify / understand) / 已读声明、验证、理解三原则
