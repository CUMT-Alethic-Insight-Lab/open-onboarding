# Walkthrough: Your First PR | 逐步实操：第一个 PR

Complete [task 01](https://github.com/CUMT-Alethic-Insight-Lab/contribution-playground/blob/main/tasks/01-first-pr.md) in contribution-playground: fix a typo and open a PR. Expected output shown after each command.

完成 contribution-playground 的 [task 01](https://github.com/CUMT-Alethic-Insight-Lab/contribution-playground/blob/main/tasks/01-first-pr.md)：修一个错字并发 PR。每条命令后附预期输出。

## 1. Clone and branch | clone 并开分支

```bash
git clone git@github.com:CUMT-Alethic-Insight-Lab/contribution-playground.git
cd contribution-playground
git checkout -b fix/typo-<your-github-id>
# Switched to a new branch 'fix/typo-<your-github-id>'
```

## 2. Fix and check | 修改并检查

Edit `tasks/01-first-pr.md` in VS Code: change `excersise` to `exercise`. If it is already fixed, pick any other wording issue. Then:

用 VS Code 打开 `tasks/01-first-pr.md`，把 `excersise` 改成 `exercise`（若已被修，另找一处措辞问题）。然后：

```bash
git status
# Changes not staged for commit:
#   modified:   tasks/01-first-pr.md
git diff
# -This excersise is intentionally seeded here for practice.
# +This exercise is intentionally seeded here for practice.
```

The diff must contain **only** your intended fix.

diff 里必须只有你的目标修改。

## 3. Commit and push | 提交并推送

```bash
git add tasks/01-first-pr.md
git commit -m "docs: fix typo in task 01"
# [fix/typo-<id> a1b2c3d] docs: fix typo in task 01
#  1 file changed, 1 insertion(+), 1 deletion(-)
git push -u origin fix/typo-<your-github-id>
# remote: Create a pull request for 'fix/typo-<id>' on GitHub by visiting:
# remote:      https://github.com/.../pull/new/fix/typo-<id>
```

## 4. Open the PR | 发起 PR

Open the URL from the push output (or the repo's Pull Requests page). Fill in the template:

打开 push 输出里的链接（或仓库 Pull Requests 页面），按模板填写：

| Field | 内容 |
| --- | --- |
| What changed | Fixed the misspelled word "excersise" in task 01 / 修正 task 01 中的拼写错误 |
| Why | Task 01 asks for it; links the task issue if one exists / 任务要求，有关联 Issue 就写 `Closes #n` |
| How verified | `git diff` shows only the one-word change / diff 仅包含该单词修改 |

## 5. Review and merge | 评审与合并

Wait for review, respond to every comment, push fixes to the **same** branch. After approval, merge, then delete the branch.

等待评审，逐条回应，修改推到同一分支。通过后合并并删除分支。

## Done When | 完成标志

- [ ] PR opened from your own branch / PR 从自己的分支发起
- [ ] Diff contains only the intended fix / diff 只含目标修改
- [ ] PR description covers what / why / how verified / 描述覆盖三点
- [ ] PR merged after review / 评审通过后已合并
