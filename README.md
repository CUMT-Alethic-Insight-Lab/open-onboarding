# Open Onboarding

An index-style introduction to AI development: a tree-shaped guide to classic open-source repositories, projects, tech stacks, and papers, plus the community conventions for working on GitHub.

索引式「AI 发展导论」：对开源经典仓库、项目、技术栈与论文的树状导览，外加 GitHub 社区通用规范。

This repository is safe for public learning materials only. It must not contain real recruitment questions, interview records, candidate evaluations, credentials, or internal notes.

本仓只放公开学习材料，不得包含真实招新题目、面试记录、候选人评价、密钥或内部笔记。

> Note for external readers: this guide assumes the lab's exam kit (Git, editor, AI tools) as the environment baseline — see [Environment Prerequisite](#environment-prerequisite--环境前提). If you are not a lab member, install Git and an editor first.
>
> 社外读者注意：本导论以招新机试包（Git、编辑器、AI 工具）为环境前提，见[环境前提](#environment-prerequisite--环境前提)；非社团成员请先自行安装 Git 与编辑器。

## The AI Tree | 导论树

**学习从这里开始：[Start Here](docs/start-here.md)**——先自检，再进入[公共先修](docs/foundations/prerequisites.md)、[经典机器学习](docs/foundations/classical-ml.md)与[神经网络基础](docs/foundations/neural-networks.md)。后续可选[数据工程](docs/paths/data-engineering.md)或[小模型与高效 AI](docs/paths/efficient-ai.md)，[全部方向见路径目录](docs/paths/README.md)。[CPU 示例](examples/README.md)提供最小实践。

Start here: [docs/ai-tree.md](docs/ai-tree.md) — the development path from foundations to model evolution, engineering, and applications.

从这里开始：[docs/ai-tree.md](docs/ai-tree.md)——从地基到模型演进、工程栈、应用栈的发展脉络。

Sibling repo [awesome-ai](https://github.com/CUMT-Alethic-Insight-Lab/awesome-ai) is the flat curated list (breadth, 求全); this tree is the development path (order, 求序). Tree leaves link to awesome-ai categories instead of duplicating them.

与同 org 的 [awesome-ai](https://github.com/CUMT-Alethic-Insight-Lab/awesome-ai) 分工：awesome-ai 是平面精选清单（求全），本树是发展脉络（求序）；树末梢链接到 awesome-ai 对应分类，不重复搬运。

## How to Walk the Tree | 怎么用这棵树

Pick your direction, then walk from trunk to branch in this order. Each branch of the tree opens with its own numbered reading order.

按你的方向选一行，从树根走到树枝；每一枝开头还有自己的编号入门顺序。

| Direction | 方向 | Walk path | 行走路径 |
| --- | --- | --- | --- |
| LLM apps | 想做 LLM 应用 | Foundations → Model Evolution → Application Stack (RAG) → Evaluation | 地基 → 模型演进 → 应用栈 RAG 子枝 → 评测 |
| Agents | 想做 Agent | Foundations → Model Evolution → Application Stack (Agent + Tool Use + Memory) | 地基 → 模型演进 → 应用栈 Agent/工具/Memory 子枝 |
| Infra | 想做 Infra | Foundations (PyTorch/Transformers) → Engineering Stack → Evaluation frameworks | 地基 PyTorch 与 Transformers → 工程栈 → 评测框架 |
| Vision / VLM | 想做视觉多模态 | Foundations (CS231n) → Model Evolution (ViT/CLIP) → Vision & Multimodal | 地基 CS231n → 演进主线 ViT/CLIP → 视觉多模态枝 |
| Alignment / RL | 想做对齐与强化学习 | Foundations (CS285) → RL → Model Evolution (RLHF/R1) → Alignment & Safety | 地基 CS285 → RL 枝 → 演进主线 RLHF 段 → 对齐枝 |

## GitHub Conventions | GitHub 规范

| Doc | 文档 | What it covers | 内容 |
| --- | --- | --- | --- |
| [Branch, commit, PR](docs/github/branch-commit-pr.md) | 分支、提交、PR | The branch-commit-PR loop | 分支-提交-PR 闭环 |
| [Review culture](docs/github/review-culture.md) | 评审文化 | How to give and take review | 如何给出与接受评审 |
| [Rescue](docs/github/rescue.md) | 自救指南 | Recovering from common Git mistakes | 常见 Git 事故的恢复 |
| [Walkthrough](docs/github/walkthrough.md) | 首次贡献实操 | Step-by-step first PR in contribution-playground | 在练习仓跑通首个 PR |
| [FAQ](faq.md) | 常见问题 | High-frequency newcomer questions | 新人高频问题 |

## Project Launch | 项目发起

| Doc | 文档 | What it covers | 内容 |
| --- | --- | --- | --- |
| [From template](docs/project-launch/from-template.md) | 用模板建仓 | Creating a repo from project-template | 以 project-template 为起点建仓 |
| [Milestones & issues](docs/project-launch/milestones-and-issues.md) | 里程碑与 issue | Splitting the first milestone into issues | 把首个里程碑拆成 issue |

## AI Work Habits | AI 工作习惯

| Doc | 文档 | What it covers | 内容 |
| --- | --- | --- | --- |
| [Workflow](docs/ai-assisted/workflow.md) | AI 辅助工作流 | Disclose, verify, understand; archiving decisions as repo docs | 声明、验证、理解；把决策落成仓库文档 |

Full policy: [AI Assistance Policy](https://github.com/CUMT-Alethic-Insight-Lab/governance-public/blob/main/docs/en/ai-assistance-policy.md) / [AI 辅助规则](https://github.com/CUMT-Alethic-Insight-Lab/governance-public/blob/main/docs/zh-CN/ai-assistance-policy.md)

## Environment Prerequisite | 环境前提

Anyone who has installed the lab's recruitment exam package already has the development environment (Git, editor, AI tools) — so this repo intentionally contains no setup tutorials.

装过实验室招新机试包即已具备开发环境（Git、编辑器、AI 工具），故本仓不含环境安装教程。

## Related | 相关

| Resource | Link |
| --- | --- |
| Contribution rules | [CONTRIBUTING](https://github.com/CUMT-Alethic-Insight-Lab/.github/blob/main/CONTRIBUTING.md) |
| Review policy | [Review Policy](https://github.com/CUMT-Alethic-Insight-Lab/governance-public/blob/main/docs/en/review-policy.md) / [Review 规则](https://github.com/CUMT-Alethic-Insight-Lab/governance-public/blob/main/docs/zh-CN/review-policy.md) |
| Project governance | [Project Governance](https://github.com/CUMT-Alethic-Insight-Lab/governance-public/blob/main/docs/en/project-governance.md) / [项目治理](https://github.com/CUMT-Alethic-Insight-Lab/governance-public/blob/main/docs/zh-CN/project-governance.md) |
