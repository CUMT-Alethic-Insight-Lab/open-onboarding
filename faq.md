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

---

Not answered here? Open an issue in this repository. / 没覆盖到？在本仓开 issue 提问。
