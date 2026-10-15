# Open Onboarding

Deeper onboarding after joining: set up your environment, practice the full contribution loop, start your own project, and learn responsible AI-assisted work.

加入之后的深入上手教程：配置环境、在练习仓跑通完整贡献闭环、用模板仓发起自己的项目，并遵守 AI 辅助工作规范。

This repository is safe for public learning materials only. It must not contain real recruitment questions, interview records, candidate evaluations, credentials, or internal notes.

本仓只放公开学习材料，不得包含真实招新题目、面试记录、候选人评价、密钥或内部笔记。

## Learning Path | 学习路径

Follow the stages in order. Each doc ends with a checklist — you are done with a stage when every box is checked.

按顺序推进。每篇文档结尾都有「完成标志」清单，全部打勾即完成该阶段。

| Stage | 阶段 | Docs | Done when | 完成标志 |
| --- | --- | --- | --- | --- |
| 0. Setup | 环境准备 | [Git & GitHub](docs/00-setup/git-and-github.md) · [Editor & AI tools](docs/00-setup/editor-and-ai-tools.md) | You can clone a repo and push a branch | 能 clone 仓库并推送分支 |
| 1. Git flow | 协作流程 | [Branch, commit, PR](docs/01-git-flow/branch-commit-pr.md) · [Review culture](docs/01-git-flow/review-culture.md) · [Rescue](docs/01-git-flow/rescue.md) | You know the branch-commit-PR loop and basic recovery commands | 掌握分支-提交-PR 流程与基本自救命令 |
| 2. First contribution | 首次贡献 | [Walkthrough](docs/02-first-contribution/walkthrough.md) | Your first PR in contribution-playground is merged | 练习仓第一个 PR 已合并 |
| 3. Project launch | 发起项目 | [From template](docs/03-project-launch/from-template.md) · [Milestones & issues](docs/03-project-launch/milestones-and-issues.md) | Your repo is created from the template with its first milestone broken into issues | 用模板建仓并把首个里程碑拆成 issue |
| 4. AI-assisted work | AI 辅助 | [Workflow](docs/04-ai-assisted/workflow.md) | You can disclose, verify, and explain every AI-assisted contribution | 每次 AI 辅助贡献都能声明、验证、讲清 |
| — | 常见问题 | [FAQ](faq.md) | — | — |

## The Contribution Loop | 贡献闭环

Practice in [contribution-playground](https://github.com/CUMT-Alethic-Insight-Lab/contribution-playground). All tasks there are non-sensitive and designed for practice.

在 [contribution-playground](https://github.com/CUMT-Alethic-Insight-Lab/contribution-playground) 练手，其中任务均为非敏感的练习任务。

| Step | What to do | 操作 |
| --- | --- | --- |
| 1. Pick a task | Browse the Issues list, choose one you understand, comment to claim it | 浏览 Issues，挑一个看得懂的任务，留言认领 |
| 2. Create a branch | `git checkout -b <topic-name>` from the latest `main` | 基于最新 `main` 开分支：`git checkout -b <主题名>` |
| 3. Commit | Small commits, conventional messages (e.g. `docs: ...`, `fix: ...`) | 小步提交，使用 conventional commit（如 `docs: ...`、`fix: ...`） |
| 4. Open a PR | Push the branch, open a Pull Request, fill in the template, link the Issue | 推送分支，发起 Pull Request，填写模板并关联 Issue |
| 5. Accept review | Read every comment, discuss or revise, push updates to the same branch | 逐条回应 review 意见，讨论或修改，推送到同一分支 |
| 6. Merge and close | Merge after approval, close the Issue, delete the branch | 通过后合并，关闭 Issue，删除分支 |

The loop is complete only when the PR is merged and the Issue is closed. One round is enough to be ready for real project work. The full step-by-step version with expected output is in the [walkthrough](docs/02-first-contribution/walkthrough.md).

PR 合并且 Issue 关闭才算完成一次闭环，跑通一轮即可进入正式项目。带预期输出的逐步实操见 [walkthrough](docs/02-first-contribution/walkthrough.md)。

## Start Your Own Project | 发起自己的项目

Use [project-template](https://github.com/CUMT-Alethic-Insight-Lab/project-template) as the starting point, then split the first milestone into issues. Details: [From template](docs/03-project-launch/from-template.md) and [Milestones & issues](docs/03-project-launch/milestones-and-issues.md).

以 [project-template](https://github.com/CUMT-Alethic-Insight-Lab/project-template) 为起点建仓，再把第一个里程碑拆成 issue。详见 [用模板建仓](docs/03-project-launch/from-template.md) 与 [里程碑与 issue](docs/03-project-launch/milestones-and-issues.md)。

Suggested topics | 建议题：

| Topic | Idea | 说明 |
| --- | --- | --- |
| Small tool | A script or CLI that solves a real annoyance in your coursework | 解决课程学习中真实痛点的小脚本或命令行工具 |
| Reproduction | Reproduce one figure or table from a paper you care about | 复现一篇你在意的论文中的一张图或一张表 |
| Evaluation | Build a small benchmark for a model you use often | 为你常用的模型搭一个小型评测集 |
| Documentation | Turn your learning notes on one topic into a readable guide | 把某一主题的学习笔记整理成可读的指南 |

Repository-specific rules may override organization defaults, but deviations should be stated clearly in the project README.

仓库级规则可以覆盖组织默认规则，但差异必须在项目 README 中写清楚。

## AI-Assisted Work | AI 辅助工作规范

AI assistance is allowed. Blind submission is not. Operational version: [AI-assisted workflow](docs/04-ai-assisted/workflow.md).

允许使用 AI 辅助，不允许不加理解的直接提交。操作版见 [AI 辅助工作流](docs/04-ai-assisted/workflow.md)。

Full policy: [AI Assistance Policy](https://github.com/CUMT-Alethic-Insight-Lab/governance-public/blob/main/docs/en/ai-assistance-policy.md) / [AI 辅助规则](https://github.com/CUMT-Alethic-Insight-Lab/governance-public/blob/main/docs/zh-CN/ai-assistance-policy.md)

## Related | 相关

| Resource | Link |
| --- | --- |
| Contribution rules | [CONTRIBUTING](https://github.com/CUMT-Alethic-Insight-Lab/.github/blob/main/CONTRIBUTING.md) |
| Review policy | [Review Policy](https://github.com/CUMT-Alethic-Insight-Lab/governance-public/blob/main/docs/en/review-policy.md) / [Review 规则](https://github.com/CUMT-Alethic-Insight-Lab/governance-public/blob/main/docs/zh-CN/review-policy.md) |
| Project governance | [Project Governance](https://github.com/CUMT-Alethic-Insight-Lab/governance-public/blob/main/docs/en/project-governance.md) / [项目治理](https://github.com/CUMT-Alethic-Insight-Lab/governance-public/blob/main/docs/zh-CN/project-governance.md) |
