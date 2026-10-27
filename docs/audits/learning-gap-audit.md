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
| ML 课程 | statlearning.com、INRIA sklearn MOOC、sklearn User Guide | 章节标题、Lab 对应、当前链接 | 已按官方目录与具体 notebook 上架；可达性见第8节 |
| 数学/编程 | Python/NumPy 官方教程、Mathematics for Machine Learning 官方页 | 章节与公开访问方式 | 已核对目录；采用第2/3/5/6/7章指定小节 |
| DL 课程 | D2L、PyTorch Basics、micrograd、CS231n | 小节、训练循环、低资源路线 | 已按实际小节上架；Autoencoder 不再使用未确认 D2L 专章 |
| 数据 | HF Datasets/DataTrove、DCLM、FineWeb | 许可边界、schema/去重/版本能力 | 已建原创小样本与 Parquet 实跑；生产规模未验证 |
| 高效 AI | torchao、ONNX Runtime、ExecuTorch、Hinton 等蒸馏原文 | 当前 API、硬件与测量限制 | 已核对官方文档；生产部署未验证，教学 PTQ 已实跑 |
| 历史 | 原论文首版、作者/机构官方记录 | 首次公开与会议年份不混用、影响不过度归因 | 38节点；arXiv 官方 API 抽检/批量核对，纠错见第4节 |

## 7. 验证证据与成熟度规则

- 文档完成、脚本通过、外部链接可达、新人试走是四种不同证据，不互相替代。
- 实跑记录必须包含 Python/依赖版本、设备、命令、数据/随机种子及结果；失败、跳过、未测逐项列出。
- 本审计不声称已经开展新成员试走。未完成至少一名新人的 ML 与 DL 小实验前，所有核心路径最高标为“内容完成，待试走”。
- 后续 PR 按 P0 基础、P0 地图/历史、P1 数据/高效、P1-C/P2 桥接、QA 顺序累积；每阶段说明变更、兼容、验证与回滚。若审查未合并，不宣称线上已生效。

## 8. 实施后的验证记录

### 文档与结构

2026-10-27 在完整分支执行 `python scripts/check_docs.py`：23 份 Markdown 的内链/相对路径/锚点通过；37 个核心节点（PR 6、ML 9、DL 10、DE 9、EA 3）字段齐全，节点引用存在且无强制循环；发展史 38 个节点在 25–40 范围内；README 与 Start Here 的课程入口存在。另执行 `python -m py_compile examples/*.py scripts/check_docs.py` 和 `git diff --check`，均通过。

检查曾发现 README 到 DE/EA 层级过深及 Start Here 缺直接入口，已修正；检查器的 `docs/` 相对路径断言也随之修正。Torchaudio 旧教程 URL 返回确定 404，已换官方文档根页并注明维护期；LeNet 作者 PDF 网关错误后改用 DOI；Sutton & Barto 的证书链问题改用已核实的 MIT Press 官方出版页；失效的 MLHub 入口改用 Radiant Earth 的 Source Cooperative；云端检出的 Arrow 概览 404 改用 PyArrow `read_table` API 页，跳回首页的 D2L 中文旧章节改用已核实的英文官网对应小节。

### 实跑环境、命令与结果

环境：Windows、Python 3.14.0、NumPy 2.3.4、scikit-learn 1.7.2、PyTorch 2.13.0+cpu、pandas 2.3.3、pyarrow 25.0.0、单线程 CPU。完整命令与数值见[示例验证记录](../../examples/README.md)。实际依次执行：

```bash
python examples/ml_tree_ensemble.py
python examples/dl_foundations.py gradient
python examples/dl_foundations.py attention
python examples/dl_foundations.py mlp
python examples/dl_foundations.py cnn
python examples/data_pipeline.py
python examples/efficient_ai.py
```

全部通过。ML 同划分树/集成对照未触碰 holdout；梯度数值校验和 Attention/SDPA 一致；MLP loss 0.6422→0.2798、验证准确率 0.94；CNN/MLP 同预算对照完成。DE 12→6 条，Parquet 读回、组/近重复泄漏断言与版本 hash 通过。EA 的 INT8 weight-only 文件变小但本机未提速，保留反例，未改写成“量化必然加速”。这些只证明示例可运行，不证明学习目标或新人试走完成。

### 外链与史实

- 使用 lychee v0.24.2 做两轮全检。onboarding 首轮 337 项中 303 OK、21 errors、13 timeouts；第二轮网络较差，245 OK、68 errors、24 timeouts。awesome-ai 首轮 192 项中 175 OK、6 errors、11 timeouts；第二轮 148 OK、36 errors、8 timeouts。
- 两仓确定的 Torchaudio 404 已修，第二轮未再出现该 404；LeNet 改用 DOI。awesome-ai 云端 CI 随后检出 MLHub 404 和 Sutton 证书链错误，分别改到 Source Cooperative 与 MIT Press。其余连接重置、超时、502/限流列为**网络未确认**，不断言死链，也不宣称全外链通过。
- arXiv 官方 API 首轮实际核对 28 个条目标题与首次提交日期，另核对 seq2seq 和 PagedAttention；由此避免把 1207.0580（Dropout）误当 AlexNet。LoRA、GRPO、Qwen3-VL 另经原始页面核实。最后一次批量复核遇到 HTTP 429，未把该次标记为完成。

### 仍未验证与回滚

- 未组织新成员试走；所有核心课程最高为“内容完成，待试走”，专题为“导览级”。
- 未在其他 OS/Python 版本、GPU、多卡、移动端或真实机器人上运行；生产 DataTrove、torchao、ONNX Runtime、ExecuTorch、大型语料/模型训练未验证。
- PR-5 新增结构检查与 CPU 示例 CI；外链沿用 awesome-ai 的 lychee 思路，非硬拦合并，红色结果需 reviewer 结合网络证据判断。
- 每阶段都在独立 PR 分支。回滚由 reviewer 关闭对应 PR 或在合并后 revert 该阶段提交；不直接覆盖 main。
