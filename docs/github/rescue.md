# Rescue | 事故自救

Mistakes in Git are almost always recoverable. Find your situation below.

Git 里的失误几乎都能挽回。按症状查表。

## Common Accidents | 常见事故

| Symptom | 症状 | Fix |
| --- | --- | --- |
| Wrong commit message | 提交信息写错 | `git commit --amend` (last commit only, before push) / 仅未推送的最后一条 |
| Committed to the wrong branch | 提交到了错误分支 | `git checkout -b right-branch` then switch back and `git reset --hard origin/main` / 先开新分支保住提交，再回退原分支 |
| Undo last commit, keep the changes | 撤销提交但保留改动 | `git reset --soft HEAD~1` |
| Discard all local changes | 丢弃所有本地改动 | `git restore .` (uncommitted only — irreversible) / 仅未提交部分，不可恢复 |

## Rebase Conflict | rebase 冲突

```bash
git rebase main
# CONFLICT (content): Merge conflict in README.md
git status                      # lists conflicted files / 列出冲突文件
```

Open each file, find the markers, keep the correct content, delete the markers:

打开冲突文件，找到标记，保留正确内容并删掉标记：

```text
<<<<<<< HEAD
their version / 对方版本
=======
your version / 你的版本
>>>>>>> your-branch
```

Then continue — or bail out entirely:

然后继续，或干脆放弃这次 rebase：

```bash
git add README.md
git rebase --continue    # repeat until done / 冲突解决完为止
git rebase --abort       # give up, back to pre-rebase state / 回到 rebase 前
```

## Force-push Boundaries | force-push 边界

| Allowed | 允许 | Forbidden | 禁止 |
| --- | --- | --- | --- |
| Your own PR branch, after rebase/amend | 自己的 PR 分支（rebase/amend 之后） | `main` or any shared branch | `main` 及任何共享分支 |

Always use the safer form:

永远用更安全的写法：

```bash
git push --force-with-lease
```

`--force-with-lease` refuses to overwrite if someone else pushed in the meantime. If you are not sure whether a branch is "yours only", do not force-push — ask first.

`--force-with-lease` 会在别人也推送过时拒绝覆盖。不确定分支是否只有自己用时，不要 force-push，先问。

## Done When | 完成标志

- [ ] You know how to amend a message, undo a commit, and abort a rebase / 会改提交信息、撤销提交、中止 rebase
- [ ] You can resolve a conflict by editing the markers / 会手工解冲突标记
- [ ] You only ever force-push your own branch, with `--force-with-lease` / 只对自己的分支用 `--force-with-lease`
