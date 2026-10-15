# Branch, Commit, PR | 分支、提交与 PR

The smallest complete unit of collaboration: one branch, a few small commits, one PR.

协作的最小完整单元：一个分支、几个小提交、一个 PR。

## 1. Branch | 分支

Always branch from the latest `main`. Name it `<type>/<short-topic>`:

永远从最新 `main` 开分支，命名为 `<类型>/<简短主题>`：

```bash
git checkout main && git pull
git checkout -b docs/fix-onboarding-typo
```

| Prefix | 用途 | Example |
| --- | --- | --- |
| `fix/` | Bug or typo fixes / 修 bug、错字 | `fix/login-redirect` |
| `feat/` | New features / 新功能 | `feat/export-csv` |
| `docs/` | Documentation only / 纯文档 | `docs/setup-guide` |

## 2. Commit | 提交

Use [Conventional Commits](https://www.conventionalcommits.org): `<type>: <what changed>`. Keep commits small — one logical change per commit.

提交信息遵循 [Conventional Commits](https://www.conventionalcommits.org/zh-hans/)：`<类型>: <改动说明>`。小步提交，一次提交只做一件事。

| Type | 场景 |
| --- | --- |
| `feat` | New feature / 新功能 |
| `fix` | Bug fix / 修复 |
| `docs` | Documentation / 文档 |
| `refactor` | Restructure without behavior change / 不改变行为的重构 |
| `test` | Tests only / 只动测试 |
| `chore` | Tooling, deps, config / 工具、依赖、配置 |

## 3. Pull Request | 发起 PR

Push and open a PR against `main`:

推送并向 `main` 发起 PR：

```bash
git push -u origin docs/fix-onboarding-typo
```

A good PR description answers three questions — the org PR template already asks for them:

好的 PR 描述回答三个问题（org 的 PR 模板已包含）：

| Question | 说明 |
| --- | --- |
| What changed | What the diff does, in one or two sentences / 一句话说清改了什么 |
| Why | Link the Issue (`Closes #12`) or state the motivation / 关联 Issue 或说明动机 |
| How verified | Commands you ran and their result / 实际跑过的验证命令与结果 |

Keep the PR small. If the description needs more than a short paragraph, split it into two PRs.

PR 保持小。描述需要写一大段时，拆成两个 PR。

## Done When | 完成标志

- [ ] You can create a branch with a conventional name / 能开出规范命名的分支
- [ ] Your commits use `<type>: ...` messages / 提交信息符合 conventional 格式
- [ ] Your PR description covers what / why / how verified / PR 描述覆盖三点
