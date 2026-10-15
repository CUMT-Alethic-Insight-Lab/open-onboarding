# Open Onboarding

Deeper onboarding after joining: practice the full contribution loop, start your own project, and learn the rules for responsible AI-assisted work.

加入之后的深入上手：在练习仓里跑通完整贡献闭环，用模板仓发起自己的项目，并遵守 AI 辅助工作规范。

This repository is safe for public learning materials only. It must not contain real recruitment questions, interview records, candidate evaluations, credentials, or internal notes.

本仓只放公开学习材料，不得包含真实招新题目、面试记录、候选人评价、密钥或内部笔记。

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

The loop is complete only when the PR is merged and the Issue is closed. One round is enough to be ready for real project work.

PR 合并且 Issue 关闭才算完成一次闭环。跑通一轮即可进入正式项目。

## Start Your Own Project | 发起自己的项目

Use [project-template](https://github.com/CUMT-Alethic-Insight-Lab/project-template) as the starting point.

以 [project-template](https://github.com/CUMT-Alethic-Insight-Lab/project-template) 为起点。

| Step | What to do | 操作 |
| --- | --- | --- |
| 1. Use this template | Click **Use this template** on the project-template page, create a new repository under the organization | 在 project-template 页面点击 **Use this template**，在组织下创建新仓 |
| 2. Rewrite the README | State the goal, scope, setup, and current status; keep it bilingual | 改写 README：写清目标、范围、运行方式与当前状态，保持双语 |
| 3. Open suggested issues | Break the first milestone into small Issues so others can join | 把第一个里程碑拆成若干小 Issue，方便他人参与 |

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

AI assistance is allowed. Blind submission is not.

允许使用 AI 辅助，不允许不加理解的直接提交。

| Rule | Detail | 说明 |
| --- | --- | --- |
| Disclose | State the model/tool, assisted parts, and cross-checking method | 声明所用的模型或工具、被辅助的部分、交叉验证方式 |
| Verify | Run the tests you claim to have run | 声称跑过的测试必须真的跑过 |
| Understand | You must be able to explain the final solution yourself | 必须能自己讲清楚最终方案 |

Full policy: [AI Assistance Policy](https://github.com/CUMT-Alethic-Insight-Lab/governance-public/blob/main/docs/en/ai-assistance-policy.md) / [AI 辅助规则](https://github.com/CUMT-Alethic-Insight-Lab/governance-public/blob/main/docs/zh-CN/ai-assistance-policy.md)

## Related | 相关

| Resource | Link |
| --- | --- |
| Contribution rules | [CONTRIBUTING](https://github.com/CUMT-Alethic-Insight-Lab/.github/blob/main/CONTRIBUTING.md) |
| Review policy | [Review Policy](https://github.com/CUMT-Alethic-Insight-Lab/governance-public/blob/main/docs/en/review-policy.md) / [Review 规则](https://github.com/CUMT-Alethic-Insight-Lab/governance-public/blob/main/docs/zh-CN/review-policy.md) |
| Project governance | [Project Governance](https://github.com/CUMT-Alethic-Insight-Lab/governance-public/blob/main/docs/en/project-governance.md) / [项目治理](https://github.com/CUMT-Alethic-Insight-Lab/governance-public/blob/main/docs/zh-CN/project-governance.md) |
