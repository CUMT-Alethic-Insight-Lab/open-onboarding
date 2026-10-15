# Start a Project from the Template | 用模板发起项目

[project-template](https://github.com/CUMT-Alethic-Insight-Lab/project-template) carries the org conventions (license, `.gitignore`, README shape) so your new repo starts consistent.

[project-template](https://github.com/CUMT-Alethic-Insight-Lab/project-template) 内置了组织约定（许可证、`.gitignore`、README 结构），让新仓从一开始就保持一致。

## Steps | 步骤

| Step | What to do | 操作 |
| --- | --- | --- |
| 1 | On the project-template page, click **Use this template** → **Create a new repository** | 在模板仓页面点击 **Use this template** 创建新仓 |
| 2 | Owner: the org (or your account if it is a personal experiment); name it lowercase-with-dashes | Owner 选 org（个人试验可选自己）；仓库名用小写连字符 |
| 3 | Clone the new repo locally | 本地 clone 新仓 |
| 4 | Work through the **New Repository Checklist** in its README, then delete that checklist | 逐项完成 README 里的新仓检查清单，完成后删掉它 |
| 5 | Rewrite the README: goal, scope, setup, current status — keep it bilingual | 改写 README：目标、范围、运行方式、当前状态，保持双语 |

```bash
git clone git@github.com:CUMT-Alethic-Insight-Lab/<your-project>.git
cd <your-project>
git checkout -b docs/init-readme
# edit README.md, remove the checklist section / 改 README，删掉检查清单
git commit -am "docs: rewrite README for <your-project>"
git push -u origin docs/init-readme   # then open a PR / 然后发 PR
```

## After the Repo Exists | 建仓之后

- Add topics in repo settings so it is discoverable in the org. / 在设置里加 Topics，便于检索。
- State any deviation from org defaults in the README. / 与 org 默认规则的差异写进 README。
- Split your first milestone into issues — see [Milestones & issues](milestones-and-issues.md). / 把第一个里程碑拆成 issue，见[里程碑与 issue](milestones-and-issues.md)。

## Done When | 完成标志

- [ ] Repo created from the template under the correct owner / 已在正确 owner 下用模板建仓
- [ ] README rewritten (bilingual, checklist removed) / README 已改写为双语并删掉检查清单
- [ ] Topics and description set / 已设置 Topics 与描述
- [ ] First milestone exists as issues / 首个里程碑已拆成 issue
