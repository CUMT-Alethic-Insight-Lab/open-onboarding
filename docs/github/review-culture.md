# Review Culture | Review 文化

Review is how the org keeps quality up and spreads knowledge. It is a conversation about the code, never about the person.

Review 是组织保证质量、传递知识的方式。讨论对象是代码，永远不是人。

## Giving Review | 给别人 review

| Principle | 做法 |
| --- | --- |
| Comment on code, not people | Say "this branch swallows the error", not "you wrote this wrong" / 说「这个分支吞掉了异常」，不说「你这里写错了」 |
| Ask before assuming | "Could this break when the file is empty?" beats a demand / 多问「这种情况会不会出问题」，少下结论 |
| Mark severity | Prefix optional suggestions with `nit:`; state clearly when something must change before merge / 可选建议加 `nit:` 前缀；必须改的地方明说 |
| Approve explicitly | When it looks good, hit **Approve** — silence is not approval / 没问题就点 Approve，沉默不算通过 |

## Receiving Review | 接受 review

| Principle | 做法 |
| --- | --- |
| It is not personal | A requested change is about the patch, not your ability / 要求修改针对的是代码，不是你的水平 |
| Respond to every comment | Fix it, explain why not, or ask for clarification — never ignore / 每条意见都要回应：改、解释或追问，不无视 |
| Push to the same branch | Updates appear in the same PR automatically; never open a new PR for review fixes / 修改推到同一分支即可，不要为 review 重开 PR |
| Resolve what you fixed | Mark threads resolved after pushing the fix / 修复后把对应对话标记为 resolved |

The binding rules are in the org [Review Policy](https://github.com/CUMT-Alethic-Insight-Lab/governance-public/blob/main/docs/en/review-policy.md) / [Review 规则](https://github.com/CUMT-Alethic-Insight-Lab/governance-public/blob/main/docs/zh-CN/review-policy.md).

正式规则见 org 的 Review Policy（上方链接）。

## Done When | 完成标志

- [ ] You have left at least one review comment on someone else's PR / 给别人 PR 留过至少一条评论
- [ ] You have responded to review on your own PR and pushed a fix to the same branch / 在自己 PR 上回应过意见并推送到同一分支
- [ ] You know the difference between `nit:` and a blocking comment / 分得清 `nit:` 与必须修改的意见
