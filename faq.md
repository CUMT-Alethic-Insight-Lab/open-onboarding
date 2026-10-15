# FAQ | 新人高频问题

## 1. I can't push to an org repository / 推不动 org 仓库

Most members work on branches inside the repo; if you lack write access, **fork** the repo, push to your fork, and open the PR from there. If you believe you should have access, ask a maintainer.

多数成员直接在仓内开分支；没有写权限就先 **fork**，推到自己的 fork 再发 PR。认为应该有权限就找维护者确认。

## 2. Review asked for changes — do I open a new PR? / 被要求修改，要重开 PR 吗

No. Commit the fixes and push to the **same branch**; the PR updates automatically. A new PR loses the whole review history.

不用。修改后推送到**同一分支**，PR 会自动更新。重开 PR 会丢掉全部评审记录。

## 3. My commit message is wrong / 提交信息写错了

Before pushing: `git commit --amend`. After pushing to your own PR branch: amend, then `git push --force-with-lease`. Never amend commits on shared branches. Details: [rescue](docs/github/rescue.md).

未推送用 `git commit --amend`；已推送到自己的 PR 分支则 amend 后 `git push --force-with-lease`。共享分支上的提交不改。详见[自救指南](docs/github/rescue.md)。

## 4. Can I let AI write everything? / 可以全让 AI 写吗

AI assistance is allowed; blind submission is not. You must disclose the tool, verify the output, and be able to explain every line. See the [AI-assisted workflow](docs/ai-assisted/workflow.md).

允许 AI 辅助，不允许不加理解的直接提交。必须声明工具、验证输出、讲清每一行。见 [AI 辅助工作流](docs/ai-assisted/workflow.md)。

## 5. `LF will be replaced by CRLF` warnings on Windows / Windows 上的换行符警告

Normal and safe to ignore — Git converts line endings between your working copy and the repository automatically. Do not "fix" it by reformatting whole files.

属正常现象，可忽略——Git 会自动处理工作区与仓库间的换行符转换。不要为此重排整个文件。

## 6. I can't get through English papers / 英文论文读不动怎么办

Normal. Read abstract, introduction, and figures first; skip proofs on the first pass. Use AI to summarize and translate paragraph by paragraph, but re-check key claims against the original text. Chinese companion readings (e.g. the video courses in the [tree's Foundations branch](docs/ai-tree.md)) cover most prerequisite ideas.

很正常。先读摘要、导言和图表，第一遍跳过证明。可以用 AI 逐段总结与翻译，但关键结论要回到原文核对。多数前置概念在中文课程里都有讲解（见[导论树地基一枝](docs/ai-tree.md)的中文社区资源）。

## 7. Too many resources — where do I start? / 资源太多不知道从哪开始

Start from the tree, not the flat list: pick one direction in [How to Walk the Tree](README.md#how-to-walk-the-tree--怎么用这棵树) and follow that single path. Ignore everything off the path until you finish it; depth on one line beats sampling ten branches.

从树入手而不是从平面清单入手：在[怎么用这棵树](README.md#how-to-walk-the-tree--怎么用这棵树)里选一个方向，只走那一条路径。走完之前不理会路径外的资源——一条线走深胜过十条枝各看一眼。

## 8. Finished the intro tree — how do I move to contribution-playground? / 学完导论后怎么接 contribution-playground

Walk the [first-contribution walkthrough](docs/github/walkthrough.md): fork or branch contribution-playground, make one small commit, and open a PR. Then pick one leaf you liked in the tree and turn it into a small issue-sized contribution (fix a doc, reproduce a demo) as your second PR.

按[首次贡献实操](docs/github/walkthrough.md)走一遍：在 contribution-playground 开分支、做一次小提交、发一个 PR。然后挑导论树里最喜欢的一个叶子节点，把它变成一个 issue 量级的小贡献（修文档、复现 demo），作为你的第二个 PR。

---

Not answered here? Open an issue in this repository. / 没覆盖到？在本仓开 issue 提问。
