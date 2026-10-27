# 学习体系缺口审计

> 审计日期：2026-10-27。状态：实施中的证据记录，不是新人试走报告。
> 基线：open-onboarding `77a219c6194f328d3f55093e03f50339201adcff`；awesome-ai `c44ddaaa26ade8c5ad8aba2f6aa659ac4c1fd9b8`。

## 1. 真实范围与分工

open-onboarding 当前只有 README、`docs/ai-tree.md`、`docs/github/`、`docs/project-launch/`、`docs/ai-assisted/`、`faq.md`、LICENSE；awesome-ai 当前是 README 单文件资源索引，另有 CONTRIBUTING、CC0 LICENSE 和 lychee 工作流。任务书建议的 foundations、maps、history、paths、scripts 均尚不存在。

| 仓库 | 保留的职责 | 不搬入的内容 |
| --- | --- | --- |
| open-onboarding | 先修、顺序、学习动作、练习、补救、出口 | 大段资源清单、内部成员/招新资料 |
| awesome-ai | 稳定资源、简介、分类、旧锚点 | 课程节点、学习进度、私有数据 |

## 2. 已有内容与缺口

| 区域 | 已有且保留 | 缺失或学习断点 | 处置 |
| --- | --- | --- | --- |
| 公共起点 | 环境前提与 GitHub 教程 | 未装招新包者的 Python/NumPy、数学、数据与环境自检入口 | P0-A 建 `start-here` 与 prerequisites |
| 经典 ML | CS229、李宏毅课程等单条资源 | 没有 ML-00…08；评估、泄漏、树与集成没有连续实践 | P0-B 建课程主线 |
| 神经网络 | D2L、PyTorch、CS231n/CS224n | 从课程主页直接到 nanoGPT/Transformers；反传、训练循环、CNN/RNN/Attention 无中间节点 | P0-C 建 DL-00…09 |
| 历史 | 模型演进的资源型年表 | 神经/LLM 单线；2017 Transformer 排在 2015 ResNet 前；历史与教学顺序混合 | P0-D 建四轴地图与多线年表 |
| 视觉/RL/Infra/评测/Agent | 高质量导览和一手资源 | 缺先修桥；若干“起点、事实标准、最强”表述超出证据 | 保留资源，P1-C/P2 修桥并审慎措辞 |
| 数据工程 | awesome-ai 的 Pile/Dolma/FineWeb/DCLM/DataTrove 等 | 没有来源许可到版本化导出的练习链 | P1-A 建 DE-00…08 |
| 小模型/高效 AI | 部署与量化工具条目 | 没有同数据、预算、硬件的质量—成本对照 | P1-B 建 EA-1…3 |
| 其他学科 | 多模态含 Whisper；其余分散 | 图、推荐、时序、传统 AI、因果、机器人等无定位 | P2 仅建诚实导览，不冒充完整课程 |
| 工程质量 | awesome-ai 已有 lychee 周检/PR 检查 | onboarding 无内链、锚点、节点字段/依赖检查；无实跑证据 | P2-B 建最小检查与 CI |

## 3. 重复与边界

- `ai-tree.md` 与 awesome-ai 在 LLM、RL、应用、Infra 有重复条目。旧树的“方向导览”有保留价值，但公共课程不再复制资源表，统一链接 awesome-ai 分类。
- README 已说明环境耦合；对外部读者需要可独立执行的 Python/Git/编辑器入口，而不是假设人人装过内部机试包。
- 两仓许可证不同：onboarding CC-BY-4.0，awesome-ai CC0。只做原创概述与链接，不复制教材章节、题解或图片。

## 4. 已核实的纠错与来源

| 项目 | 审计结论 | 一手来源 |
| --- | --- | --- |
| LoRA | arXiv v1 为 2021-06-17，不能放在“2023”；它是冻结基座、训练低秩增量的参数高效适配，不等同量化 | https://arxiv.org/abs/2106.09685 |
| GRPO / DeepSeek-R1 | DeepSeekMath arXiv v1 为 2024-02-05，摘要明确“introduce GRPO”；DeepSeek-R1 为 2025 工作，不能把 GRPO 首创归给 R1 | https://arxiv.org/abs/2402.03300 与 https://arxiv.org/abs/2501.12948 |
| Qwen3-VL | 官方 News 首批 Qwen3-VL 发布记录是 2025-09-23，不能标 2024；条目描述不使用“最强”等无统一口径断言 | https://github.com/QwenLM/Qwen3-VL |
| RAG | 2020 论文是重要代表，但“检索与生成的首次系统结合/范式起点”过强，应按原文贡献描述 | https://arxiv.org/abs/2005.11401 |
| PagedAttention | PagedAttention 是论文提出的注意力服务机制，vLLM 是实现/系统；工具条目与算法归因分开 | https://arxiv.org/abs/2309.06180 |
| Transformer | 2017 原始论文；“自注意力取代循环结构”应限定为论文中的序列转导架构，不宣称所有领域自此无需循环 | https://arxiv.org/abs/1706.03762 |

## 5. 旧链接保护清单

- `README.md` 原有 `The AI Tree`、`How to Walk the Tree`、GitHub、Project Launch、AI Work Habits、Environment Prerequisite 标题保留。
- `docs/ai-tree.md` URL 永久保留；原 Foundations、Model Evolution、Vision & Multimodal、RL、Alignment & Safety、Engineering Stack、Evaluation & Benchmarks、Application Stack、How to Read This Tree 均保留显式兼容锚点。内容改为学习入口时不能只留下 404。
- `docs/github/**`、`docs/project-launch/**`、`docs/ai-assisted/**`、`faq.md` 不移动。
- awesome-ai 保留 `llm-fundamentals`、`rag-retrieval`、`agents`、`reinforcement-learning`、`multimodal`、`reasoning`、`evaluation-benchmarks`、`data-engineering`、`ai-infrastructure`、`serving-deployment`、`engineering-practice` 显式锚点与目录；新增而非改名。

## 6. 参考资源核验清单

| 用途 | 首选来源 | 上架前必须确认 | 当前状态 |
| --- | --- | --- | --- |
| ML 课程 | statlearning.com、INRIA sklearn MOOC、sklearn User Guide | 章节标题、Lab 对应、当前链接 | 待逐章核验 |
| 数学/编程 | Python/NumPy 官方教程、Mathematics for Machine Learning 官方页 | 章节与公开访问方式 | 待逐章核验 |
| DL 课程 | D2L、PyTorch Basics、micrograd、CS231n | 小节、训练循环、低资源路线 | 待逐章核验 |
| 数据 | HF Datasets/DataTrove、DCLM、FineWeb | 许可边界、schema/去重/版本能力 | 待核验 |
| 高效 AI | torchao、ONNX Runtime、ExecuTorch、Hinton 等蒸馏原文 | 当前 API、硬件与测量限制 | 待核验 |
| 历史 | 原论文首版、作者/机构官方记录 | 首次公开与会议年份不混用、影响不过度归因 | 部分已核实，见上表 |

## 7. 验证证据与成熟度规则

- 文档完成、脚本通过、外部链接可达、新人试走是四种不同证据，不互相替代。
- 实跑记录必须包含 Python/依赖版本、设备、命令、数据/随机种子及结果；失败、跳过、未测逐项列出。
- 本审计不声称已经开展新成员试走。未完成至少一名新人的 ML 与 DL 小实验前，所有核心路径最高标为“内容完成，待试走”。
- 后续 PR 按 P0 基础、P0 地图/历史、P1 数据/高效、P1-C/P2 桥接、QA 顺序累积；每阶段说明变更、兼容、验证与回滚。若审查未合并，不宣称线上已生效。
