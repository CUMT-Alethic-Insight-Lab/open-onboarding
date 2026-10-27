# AI 多线发展史：问题、方法与代价

这是一份 38 个代表节点的导览，不是“AI 全部发明史”。年份采用**所列一手成果的首次公开/发表口径**：arXiv 项按 v1，会议/期刊项按正式出版；同一成果可能有更早前身或更晚版本，不能用后见之明抹掉。每条都给出入口，但**历史顺序不是学习顺序**。

阅读方式：先看[四轴地图](../maps/field-map.md)，再沿符号/统计、神经/生成、RL、系统与应用几条线读。表内“影响”是有边界的代表性联系，不表示唯一原因。

## 1950s–1980s：问题形式化、符号方法与早期学习机器

| 时间与一手来源 | 先前瓶颈 → 核心思路 | 代价/局限与后续 | 学习入口 |
| --- | --- | --- | --- |
| 1950 · [Turing: Computing Machinery and Intelligence](https://doi.org/10.1093/mind/LIX.236.433) | “机器能否思考”难操作 → 用 imitation game 讨论机器行为 | 行为测试不是意识/能力全集；成为机器智能评价的重要思想起点 | 地图的评测轴 |
| 1956 会议 · [Dartmouth Summer Research Project 提案](https://www-formal.stanford.edu/jmc/history/dartmouth/dartmouth.html) | 自动计算分散 → 将学习、推理、语言等聚为共同研究议程 | 提案不等于技术实现；早期乐观预期遭遇能力/算力限制 | 符号 AI |
| 1958 · [Rosenblatt: The Perceptron](https://doi.org/10.1037/h0042519) | 固定规则难适应 → 用可学习权重的阈值单元做分类 | 线性可分限制明显；不等于现代深层 MLP | DL-00 |
| 1986 · [Rumelhart, Hinton & Williams](https://www.nature.com/articles/323533a0) | 多层网络内部表示难训练 → 系统展示反向误差传播学习表示 | 反向传播有更早理论/应用背景，不能称此文明所有首创；深网训练仍受梯度与算力限制 | DL-02 |

## 1990s–2000s：统计学习、集成与序列/价值方法成熟

| 时间与一手来源 | 先前瓶颈 → 核心思路 | 代价/局限与后续 | 学习入口 |
| --- | --- | --- | --- |
| 1992 · [Watkins & Dayan: Q-learning](https://link.springer.com/article/10.1007/BF00992698) | 无模型序贯决策难直接学最优价值 → 离策略时序差分更新动作价值 | 表格表示与探索/稳定性限制；是价值型深度 RL 的基础之一 | RL 桥接 |
| 1995 · [Cortes & Vapnik: Support-Vector Networks](https://link.springer.com/article/10.1007/BF00994018) | 高维小样本分类泛化难 → 最大间隔与核函数 | 大规模核计算/参数选择成本；成为统计学习代表 | ML-06 |
| 1997 · [Freund & Schapire: AdaBoost](https://doi.org/10.1006/jcss.1997.1504) | 弱学习器精度有限 → 顺序重加权样本并加权组合 | 对噪声/异常敏感；不同于 GBDT 的负梯度拟合 | ML-05 |
| 1997 · [Hochreiter & Schmidhuber: LSTM](https://doi.org/10.1162/neco.1997.9.8.1735) | 普通 RNN 长依赖梯度难传 → 门控与持续状态通路 | 顺序计算、训练成本仍在；成为序列建模重要分支 | DL-06 |
| 1998 · [LeCun et al.: Gradient-Based Learning](https://doi.org/10.1109/5.726791) | 手写视觉特征与识别割裂 → 卷积网络端到端文档识别（含 LeNet-5） | 当时数据/算力约束规模；证明局部共享视觉学习的工程价值 | DL-05 |
| 2001 · [Breiman: Random Forests](https://link.springer.com/article/10.1023/A:1010933404324) | 单树高方差且树间相关 → bootstrap 与特征随机性组合多树 | 可解释性/外推有限；至今仍是表格基线 | ML-05 |

## 2010–2016：数据与算力推动的深度表征、多类生成与深度 RL

| 时间与一手来源 | 先前瓶颈 → 核心思路 | 代价/局限与后续 | 学习入口 |
| --- | --- | --- | --- |
| 2012 · [Krizhevsky et al.: AlexNet](https://proceedings.neurips.cc/paper/2012/hash/c399862d3b9d6b76c8436e924a68c45b-Abstract.html) | 大规模图像分类手工特征受限 → GPU 深 CNN、ReLU、数据增强与 dropout | 依赖标注、GPU 与大量训练；推动视觉深度表征，不是神经网络起点 | DL-05 |
| 2013 · [Mikolov et al.: word2vec](https://arxiv.org/abs/1301.3781) | 稠密词表示训练昂贵 → 用浅层预测目标高效学词向量 | 静态向量上下文有限；推动分布式语义表示 | DL-06/09 |
| 2013 · [Mnih et al.: DQN](https://arxiv.org/abs/1312.5602) | 高维像素难接价值方法 → Q-learning + 经验回放/目标网络 | 样本效率与训练稳定性问题；后续 Nature 版完善，不能混写两版结果 | RL 桥接 |
| 2013 · [Kingma & Welling: VAE](https://arxiv.org/abs/1312.6114) | 生成模型后验推断困难 → 变分下界 + 重参数化 | 后验近似与生成质量权衡；不同于普通 autoencoder | DL-08 |
| 2014 · [Goodfellow et al.: GAN](https://arxiv.org/abs/1406.2661) | 难显式定义生成分布似然 → 生成器与判别器对抗 | 训练不稳定、模式坍塌与评测困难 | DL-08 |
| 2014 · [Sutskever et al.: seq2seq](https://arxiv.org/abs/1409.3215) | 变长序列输入输出映射困难 → 编码器—解码器 LSTM 联合学习 | 固定上下文瓶颈、串行成本；为注意力 seq2seq 奠基 | DL-06 |
| 2015 · [He et al.: ResNet](https://arxiv.org/abs/1512.03385) | 网络加深后优化退化 → 残差学习与恒等捷径 | 不表示深度不再有限制；广泛影响视觉与其他深网 | DL-04/05 |
| 2016 · [Silver et al.: AlphaGo](https://www.nature.com/articles/nature16961) | 围棋巨大搜索空间 → 价值/策略网络与 MCTS 结合 | 专用规则/大量训练与搜索成本；混合学习与规划的范例 | 搜索规划 + RL |

## 2017–2020：注意力、预训练与多种生成路线并行

| 时间与一手来源 | 先前瓶颈 → 核心思路 | 代价/局限与后续 | 学习入口 |
| --- | --- | --- | --- |
| 2017 · [Vaswani et al.: Transformer](https://arxiv.org/abs/1706.03762) | 序列转导的循环串行瓶颈 → 以注意力为核心并行建模依赖 | 标准注意力 pairwise 成本、位置需另编码；论文是 seq2seq 架构，不等于所有后续 LLM | DL-07 |
| 2017 · [Schulman et al.: PPO](https://arxiv.org/abs/1707.06347) | 策略梯度更新过大易失稳 → 截断比率等约束的策略优化 | 采样/调参与实现成本；后来成为部分 RLHF 流程组件 | RL 桥接 |
| 2018 · [Peters et al.: ELMo](https://arxiv.org/abs/1802.05365) | 静态词向量缺上下文 → 深层双向语言模型产生上下文化表示 | 任务适配/计算成本；预训练表征路线的重要节点 | DL-09 |
| 2018 · [Devlin et al.: BERT](https://arxiv.org/abs/1810.04805) | 通用文本表征迁移有限 → 掩码语言模型预训练 + 任务微调 | 双向预训练不直接等于自回归生成；数据/算力与评测污染风险 | DL-09 |
| 2020 · [Lewis et al.: RAG](https://arxiv.org/abs/2005.11401) | 参数记忆难更新、知识密集任务受限 → 联合检索非参数记忆与生成 | 检索/语料误差与延迟；是代表工作，不断言史上首次结合检索生成 | RAG 桥接 |
| 2020 · [Brown et al.: GPT-3](https://arxiv.org/abs/2005.14165) | 每任务标注/微调成本高 → 大规模自回归预训练与上下文学习 | 计算/数据成本、事实性与偏差；规模带来新能力也带来新评估问题 | DL-09 |
| 2020 · [Ho et al.: DDPM](https://arxiv.org/abs/2006.11239) | 高质量生成与稳定训练难兼顾 → 学习逐步去噪的扩散过程 | 多步采样成本；成为扩散生成的重要基础 | DL-08 |
| 2020 · [Dosovitskiy et al.: ViT](https://arxiv.org/abs/2010.11929) | 视觉依赖 CNN 归纳结构 → 图像 patch 上直接训练 Transformer | 大规模数据/计算重要；不是“视觉从此无需 CNN” | DL-05/07 |
| 2020 · [Chen et al.: SimCLR](https://arxiv.org/abs/2002.05709) | 视觉标注昂贵 → 数据增强 + 对比表示学习 | batch/增强与训练预算敏感；自监督代表而非唯一路线 | DL-09 |

## 2021–2023：跨模态、效率、科学应用与后训练分化

| 时间与一手来源 | 先前瓶颈 → 核心思路 | 代价/局限与后续 | 学习入口 |
| --- | --- | --- | --- |
| 2021 · [Radford et al.: CLIP](https://arxiv.org/abs/2103.00020) | 固定视觉类别与人工标注限制 → 自然语言监督的图文对比预训练 | 网络数据偏差、细粒度/分布外限制；影响开放词汇视觉与 VLM | CV/VLM 桥接 |
| 2021 · [Hu et al.: LoRA](https://arxiv.org/abs/2106.09685) | 全量微调参数/存储成本高 → 冻结基座、训练低秩增量 | 任务/秩/目标层影响效果；是适配方法，不等同量化 | EA-2 |
| 2021 · [Jumper et al.: AlphaFold2](https://www.nature.com/articles/s41586-021-03819-2) | 蛋白结构预测精度与泛化受限 → 结合序列/结构先验的端到端架构 | 数据、算力与适用边界仍在；科学 AI 代表，不是通用结构预测终点 | 科学 AI |
| 2021 · [Rombach et al.: Latent Diffusion](https://arxiv.org/abs/2112.10752) | 像素空间扩散计算昂贵 → 在感知压缩潜空间扩散并可条件控制 | 自编码器信息损失与采样成本；影响高分辨率生成 | DL-08 |
| 2022 · [Hoffmann et al.: Chinchilla](https://arxiv.org/abs/2203.15556) | 大模型训练数据/参数配置不当 → 在给定计算预算下联合研究规模配置 | 结论依赖数据/训练设置，不能简化成任何场景固定比例 | 数据 + Infra |
| 2022 · [Ouyang et al.: InstructGPT](https://arxiv.org/abs/2203.02155) | 预训练目标与用户指令不一致 → SFT、奖励模型与 PPO 的人类反馈流程 | 标注/奖励偏差与训练复杂度；不是全部对齐方法 | RL/Alignment |
| 2023 · [Touvron et al.: LLaMA](https://arxiv.org/abs/2302.13971) | 开放基座可研究性受限 → 发布一组不同规模的基础语言模型 | 许可/数据与使用边界需单独判断；推动适配与研究生态 | DL-09 |
| 2023 · [Rafailov et al.: DPO](https://arxiv.org/abs/2305.18290) | 显式奖励模型 + RL 流程复杂 → 用偏好数据直接优化策略的闭式关系 | 偏好数据质量/分布约束；不是“无需奖励假设”或所有场景替代 RLHF | RL/Alignment |
| 2023 · [Gu & Dao: Mamba](https://arxiv.org/abs/2312.00752) | 注意力随序列长的计算/缓存压力 → 输入依赖的选择性状态空间模型 | 硬件内核、任务与规模影响收益；不是注意力在所有任务的替代 | DL-08/Infra |

## 2024–2026：推理后训练与系统权衡，暂不作终局判断

| 时间与一手来源 | 先前瓶颈 → 核心思路 | 代价/局限与后续 | 学习入口 |
| --- | --- | --- | --- |
| 2024 · [DeepSeekMath / GRPO](https://arxiv.org/abs/2402.03300) | PPO 的 critic 成本与数学推理优化 → 组内相对优势估计的 GRPO | 采样/奖励设计与方差权衡；GRPO 首归此项，不归 2025 R1 | RL 桥接 |
| 2024 · [OpenAI o1 System Card](https://arxiv.org/abs/2412.16720) | 复杂推理的测试时预算与安全性 → 推理模型及推理时计算的官方安全披露 | 不是完整训练论文；不能把未公开机制当已证实事实 | 评测 + RL |
| 2025 · [DeepSeek-R1](https://arxiv.org/abs/2501.12948) | 推理能力与后训练配方 → 报告纯 RL 探索、冷启动和多阶段训练路线 | 计算/数据/评测条件需核实；2025 发布，GRPO 的前身另见 2024 | RL/Alignment |

## 容易混淆的六条结论

1. 反向传播早于 1986 年有理论和应用背景；1986 工作具有重要推动与展示作用，不写“凭空发明”。
2. CNN、LSTM、随机森林、SVM 在深度学习热潮前已有关键成果；它们今天仍有各自适用场景。
3. Transformer 是架构，预训练/自监督是学习信号，LLM 是模型与任务生态，三者不能互换。
4. VAE、GAN、Diffusion 不是一条“后者全面淘汰前者”的直线，目标、训练与采样代价不同。
5. LoRA 2021、GRPO 2024、DeepSeek-R1 2025；Qwen3-VL 官方首批发布记录为 2025，均按实际口径，不按热门年份归档。
6. 2024–2026 的技术影响仍在形成，本节只记录已公开成果与明确边界，不以流行度写历史结论。
