# Milestones & Issues | 里程碑与 Issue

A milestone is a testable state of the project; an issue is one piece of work someone can pick up without asking you questions.

里程碑是项目的一个可检验状态；issue 是一块别人不用问你就能上手的工作。

## How to Split | 怎么拆

| Rule | 说明 |
| --- | --- |
| Milestone = a demo-able checkpoint | "v0.1 can do X end to end", not "make progress" / 里程碑要能演示，不是「有进展」 |
| Issue = half a day to two days of work | Smaller than that, merge it; larger, split it / 小于半天就合并，大于两天就再拆 |
| Every issue has a "done when" | One line stating how the picker verifies completion / 每条 issue 写清一行完成标准 |
| Order by dependency | Setup/scaffolding issues first, polish last / 先搭架子，后打磨 |

## A Real Split Example | 真实拆例

Idea: a CLI that tracks which papers you have read, with notes. Milestone **v0.1 — record and list locally**:

想法：一个记录已读论文和笔记的命令行工具。里程碑 **v0.1——本地记录与列表**：

| Issue | Title | Done when |
| --- | --- | --- |
| #1 | `chore: init project layout and CLI skeleton` | `papers --help` prints usage / 打印用法 |
| #2 | `feat: add a paper entry (title, url, note)` | Entry persists to a local file / 条目落盘 |
| #3 | `feat: list all entries` | Entries print in add order / 按添加顺序输出 |
| #4 | `docs: README with install and usage` | A newcomer can run it from README alone / 新人照 README 能跑起来 |

Create the milestone under Issues → Milestones, file the issues, assign the milestone to each, and label them (`good first issue` for the ones a newcomer can take).

在 Issues → Milestones 下创建里程碑，逐条开 issue 并挂上里程碑；新人可上手的打上 `good first issue` 标签。

## Done When | 完成标志

- [ ] Your repo has a milestone named by a demo-able result / 里程碑以可演示结果命名
- [ ] The milestone contains 3-6 issues, each with a one-line "done when" / 含 3-6 条 issue，各有一行完成标准
- [ ] At least one issue is labeled `good first issue` / 至少一条打了 `good first issue`
