# AI-Assisted Workflow | AI 辅助工作流

The three principles — **disclose, verify, understand** — as concrete actions. The binding policy is in governance-public: [English](https://github.com/CUMT-Alethic-Insight-Lab/governance-public/blob/main/docs/en/ai-assistance-policy.md) / [简体中文](https://github.com/CUMT-Alethic-Insight-Lab/governance-public/blob/main/docs/zh-CN/ai-assistance-policy.md).

把**声明、验证、理解**三原则落成具体动作。正式政策见 governance-public（上方链接），此处不复制条文。

## 1. Disclose | 声明

Every AI-assisted PR states, in its description:

每个 AI 辅助的 PR 在描述中写明：

| Item | 说明 | Example |
| --- | --- | --- |
| Tool/model | Which assistant and model / 工具与模型 | Kimi Code (k2) |
| Assisted parts | What it generated or changed / 辅助了哪部分 | Drafted the parser; tests are mine |
| Cross-check | How you checked its output / 交叉验证方式 | Compared against the reference docs |

## 2. Verify | 验证

- Run every test you claim to have run, and paste the real command/output when asked. / 声称跑过的测试必须真的跑过，需要时贴出真实命令与输出。
- Never commit AI output you have not read end to end. / 没通读过的 AI 输出不提交。
- If the AI touches commands that delete, push, or publish, re-check them yourself before running. / 涉及删除、推送、发布的命令，运行前自己再查一遍。

## 3. Understand | 理解

In review you must be able to explain any line of your PR. If you cannot, either learn it or remove it — "the AI wrote it" is never an acceptable answer.

review 时必须能讲清 PR 里的任何一行。讲不清就搞懂或删掉——「AI 写的」永远不是可接受的回答。

## Decision Archive | 决策存档

Keep one habit: when context is nearly exhausted or a phase wraps up, have the AI distill the current progress, key decisions, and trial-and-error into a Markdown document, and commit it into the repository.

保持一个习惯：上下文快用完或阶段性收尾时，让 AI 把当前进展、关键决策与试错过程落成一篇 Markdown 文档，提交进仓库。

From then on, a single `grep` recovers the decision chain and the trial-and-error chain — no need to archive every chat session, and no risk of credentials or private paths leaking into the repo.

之后一个 `grep` 就能找回当时的决策链和试错链——无需频繁导出整段会话，也避免把密钥或私人路径带进仓库。

## Done When | 完成标志

- [ ] Your PRs disclose tool, assisted parts, and cross-check / PR 里声明工具、辅助部分、验证方式
- [ ] You only claim tests you actually ran / 只声称真实跑过的测试
- [ ] Your progress and decisions are committed as repo documents / 进展与决策已落成仓库内的文档
