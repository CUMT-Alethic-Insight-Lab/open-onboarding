# AI Development Tree | AI 发展导论树

A tree-shaped index of classic open-source repositories, projects, tech stacks, and papers, ordered by how the field developed — read the branches as a narrative, not a checklist.

对开源经典仓库、项目、技术栈与论文的树状索引，按发展脉络组织——把树枝当作故事线读，而不是待办清单。

Sibling repo [awesome-ai](https://github.com/CUMT-Alethic-Insight-Lab/awesome-ai) is the flat curated list (breadth); this tree is the development path (order). Leaves here link out to primary sources; category-level breadth stays in awesome-ai.

与同 org 的 [awesome-ai](https://github.com/CUMT-Alethic-Insight-Lab/awesome-ai) 分工：awesome-ai 求全（平面精选清单），本树求序（发展脉络），树末梢只指一手来源。

Difficulty tags | 难度标注：`[入门]` 零基础可读 · `[进阶]` 需要地基章节的数学与代码基础 · `[深入]` 面向想做研究或硬核工程的同学。前置依赖以「前置：」标注。

## 1. Foundations | 地基

入门顺序：

1. 先用《动手学深度学习》或李宏毅课程建立直觉，边学边把 PyTorch 跑起来。
2. 按兴趣补一门 Stanford 课（CV 选 CS231n，NLP 选 CS224n，想做理论补 CS229）。
3. 跟着 nanoGPT 手写一遍 GPT 训练，把「课上学过」变成「亲手实现」。
4. 装熟 Hugging Face Transformers，跑通一个预训练模型的推理与微调 demo。

- [入门] [d2l-zh](https://github.com/d2l-ai/d2l-zh) — 《动手学深度学习》，中文可运行教材，从零实现到工程用法。
- [入门] [李宏毅机器学习课程](https://speech.ee.ntu.edu.tw/~hylee/ml/2023-spring.php) — 台大李宏毅的中文课程主页，配 B 站搬运视频，最友好的中文入门路线之一。
- [入门] [李沐 B 站频道](https://space.bilibili.com/1567748478) — 《动手学深度学习》作者亲授视频课，论文精读系列适合进阶跟读。
- [入门] [PyTorch](https://github.com/pytorch/pytorch) — 研究与工业界事实标准的深度学习框架。
- [入门] [The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/) — 图文详解 Transformer 内部机制，读论文前的最佳热身。
- [进阶] [CS229](https://cs229.stanford.edu/) — Stanford 机器学习课，补统计学习基础的默认起点。
- [进阶] [CS231n](https://cs231n.github.io/) — Stanford 视觉课，CNN 时代的标准入门。
- [进阶] [CS224n](https://web.stanford.edu/class/cs224n/) — Stanford NLP 课，理解词向量到 Transformer 的过渡。
- [进阶] [CS285](https://rail.eecs.berkeley.edu/deeprlcourse/) — Berkeley 深度强化学习课，读懂 RLHF 的前置。
- [进阶] [nanoGPT](https://github.com/karpathy/nanoGPT) — 约千行代码训练 GPT，把 Transformer 从「看懂」变「写得出」。前置：PyTorch。
- [进阶] [Hugging Face Transformers](https://github.com/huggingface/transformers) — 预训练模型的统一入口，跑通它等于拿到整个生态的钥匙。

延伸阅读 → [awesome-ai · 工程实践](https://github.com/CUMT-Alethic-Insight-Lab/awesome-ai#engineering-practice--工程实践)

## 2. Model Evolution | 模型演进主线

入门顺序：

1. 按年份顺着读，每条只先读摘要与导言，弄清「它解决了上一代的什么痛点」。
2. 在 Transformer、BERT、GPT-3 三个节点放慢，它们是后续一切分叉的原点。
3. 读到 Scaling Laws / Chinchilla 时回到「为什么变大有效」这条暗线。
4. 读到 RLHF 与 R1/o1 后，跳到对齐与强化学习两枝补机制细节。

- [入门] 2012 · [AlexNet](https://proceedings.neurips.cc/paper/2012/hash/c399862d3b9d6b76c8436e924a68c45b-Abstract.html) — GPU + 深度卷积点燃本轮浪潮的引爆点。
- [入门] 2017 · [Attention Is All You Need](https://arxiv.org/abs/1706.03762) — Transformer 诞生，自注意力取代循环结构。
- [进阶] 2015 · [ResNet](https://arxiv.org/abs/1512.03385) — 残差连接让百层网络可训练，深度不再是瓶颈。
- [进阶] 2018 · [BERT](https://arxiv.org/abs/1810.04805) — 双向预训练 + 微调范式横扫 NLP 榜单。
- [进阶] 2019 · [GPT-2](https://github.com/openai/gpt-2) — 自回归生成路线跑通，「大即涌现」初见端倪。
- [进阶] 2020 · [GPT-3](https://arxiv.org/abs/2005.14165) — 175B 参数与 in-context learning，规模带来质变。
- [进阶] 2020 · [ViT](https://arxiv.org/abs/2010.11929) — 纯 Transformer 杀入视觉，统一架构的开端。
- [进阶] 2020 · [Scaling Laws](https://arxiv.org/abs/2001.08361) — 损失随算力/数据/参数幂律下降，扩展成为可计算的科学。
- [进阶] 2021 · [CLIP](https://arxiv.org/abs/2103.00020) — 图文对比学习打通视觉与语言，多模态的起点。
- [进阶] 2022 · [Chinchilla](https://arxiv.org/abs/2203.15556) — 修正扩展律：数据与参数需等比增长，小模型喂足数据更优。
- [进阶] 2022 · [InstructGPT / RLHF](https://arxiv.org/abs/2203.02155) — 人类反馈强化学习对齐意图，ChatGPT 的技术内核（机制细节见对齐与安全一枝）。
- [进阶] 2023 · [LLaMA](https://arxiv.org/abs/2302.13971) — 高效开源基座发布，社区微调生态由此爆发。
- [进阶] 2023 · [LoRA](https://arxiv.org/abs/2106.09685) — 低秩适配让消费级显卡也能微调大模型。
- [深入] 2024– · [DeepSeek-R1](https://arxiv.org/abs/2501.12948) 与 [OpenAI o1](https://openai.com/index/learning-to-reason-with-llms/) — 推理时计算与强化学习驱动的新范式。前置：RL 一枝的 PPO/GRPO。

延伸阅读 → [awesome-ai · LLM 基础](https://github.com/CUMT-Alethic-Insight-Lab/awesome-ai#llm-foundations--llm-基础)

## 3. Vision & Multimodal | 视觉与多模态（CV / VLM）

入门顺序：

1. 先回地基补 CS231n，再从 ViT 与 CLIP（见模型演进主线）理解「视觉如何 Transformer 化」。
2. VLM 线按 BLIP → LLaVA → Qwen2-VL 读，看图文对齐如何进化成视觉指令微调。
3. 生成线按 DDPM → Stable Diffusion → ControlNet 读，再用 diffusers 亲手跑一遍文生图。
4. 需要分割等感知任务时补 SAM，理解「提示式视觉」范式。

- 表征与 VLM
  - [进阶] 2022 · [BLIP](https://arxiv.org/abs/2201.12086) — 视觉语言预训练代表作，统一理解与生成任务的框架。前置：CLIP。
  - [进阶] 2023 · [LLaVA](https://github.com/haotian-liu/LLaVA) — 开源视觉指令微调标杆，VLM 复现与改造的首选起点。
  - [进阶] 2023 · [Segment Anything (SAM)](https://arxiv.org/abs/2304.02643) — 通用图像分割基础模型，提示式视觉范式的标志。
  - [进阶] 2024 · [Qwen3-VL](https://github.com/QwenLM/Qwen3-VL) — 中文生态最强的开源 VLM 系列之一，文档与权重齐全，适合上手实战。
- 生成式视觉
  - [进阶] 2020 · [DDPM](https://arxiv.org/abs/2006.11239) — 去噪扩散概率模型，扩散生成路线的奠基论文。
  - [入门] 2022 · [Stable Diffusion](https://github.com/CompVis/stable-diffusion) — 潜空间扩散开源模型，把文生图带进大众。
  - [进阶] 2023 · [ControlNet](https://arxiv.org/abs/2302.05543) — 给扩散模型加结构控制，可控生成的标准方案。
  - [入门] [diffusers](https://github.com/huggingface/diffusers) — Hugging Face 扩散模型标准库，几行代码跑通文生图的最佳实践入口。

延伸阅读 → [awesome-ai · 多模态](https://github.com/CUMT-Alethic-Insight-Lab/awesome-ai#multimodal--多模态)

## 4. Reinforcement Learning | 强化学习（RL）

入门顺序：

1. 先用 Sutton & Barto 前几章建立 MDP、价值函数的语言，不必全啃。
2. 跟 OpenAI Spinning Up 把策略梯度讲透，代码用 stable-baselines3 在 Gymnasium 环境里跑实验。
3. 读 DQN 与 PPO 两篇原论文，理解深度 RL 的两个里程碑。
4. 带着 PPO 去读模型演进主线的 InstructGPT，再看 GRPO，接上 LLM 对齐的最新实践。

- [入门] [Sutton & Barto: Reinforcement Learning (2nd ed.)](http://incompleteideas.net/book/the-book-2nd.html) — RL 标准教材，作者官方公开电子版。
- [入门] [OpenAI Spinning Up](https://spinningup.openai.com/) — OpenAI 官方 RL 教程，理论与代码兼顾的入门路线。
- [进阶] 2013 · [DQN](https://arxiv.org/abs/1312.5602) — 深度强化学习开山之作，Atari 游戏超越人类水平。
- [进阶] 2017 · [PPO](https://arxiv.org/abs/1707.06347) — 最广泛使用的策略梯度算法，后来成为 RLHF 的核心组件。
- [入门] [Gymnasium](https://github.com/Farama-Foundation/Gymnasium) — RL 环境标准接口，OpenAI Gym 的社区继任者。
- [进阶] [stable-baselines3](https://github.com/DLR-RM/stable-baselines3) — PyTorch 版主流 RL 算法可靠实现，实验复现利器。前置：PyTorch。
- [深入] 2024 · [DeepSeekMath / GRPO](https://arxiv.org/abs/2402.03300) — 去掉 critic 的分组相对策略优化，R1 推理范式的训练核心。

延伸阅读 → [awesome-ai · 强化学习](https://github.com/CUMT-Alethic-Insight-Lab/awesome-ai#reinforcement-learning--强化学习)

## 5. Alignment & Safety | 对齐与安全

入门顺序：

1. 先读模型演进主线的 InstructGPT，建立「预训练 → SFT → RLHF」的后训练全景。
2. 读 DPO 看「不用 RL 也能对齐」的简化路线，理解 RLHF 的代价与替代方案。
3. 读 Constitutional AI 了解用 AI 反馈替代部分人类标注的对齐思路。
4. 用 RLHF Book 把细节串成体系，再视兴趣深入安全评测话题。

- [进阶] 2022 · [InstructGPT / RLHF](https://arxiv.org/abs/2203.02155) — 奖励模型 + PPO 的经典三段式对齐流程，本枝的总纲（同模型演进主线节点）。
- [进阶] 2023 · [DPO](https://arxiv.org/abs/2305.18290) — 直接偏好优化，跳过奖励模型与 RL 的轻量对齐路线。前置：InstructGPT。
- [进阶] 2022 · [Constitutional AI](https://arxiv.org/abs/2212.08073) — Anthropic 的「宪法式」对齐：用原则清单与 AI 反馈减少人工有害性标注。
- [进阶] [RLHF Book](https://rlhfbook.com/) — Nathan Lambert 的在线专著，把 RLHF 的奖励模型、优化与评测细节系统讲透。
- [深入] [PurpleLlama / Llama Guard](https://github.com/meta-llama/PurpleLlama) — Meta 的开源安全组件，输入输出内容审核的工程化参考。

延伸阅读 → [awesome-ai · 强化学习（含 RLHF 条目）](https://github.com/CUMT-Alethic-Insight-Lab/awesome-ai#reinforcement-learning--强化学习)

## 6. Engineering Stack | 工程栈（Infra）

入门顺序：

1. 先在地基章跑熟 Transformers，再用 llama.cpp 在本地把模型跑起来，建立推理直觉。
2. 读 vLLM 的 PagedAttention 思路，理解高吞吐服务的核心问题。
3. 需要训练时按 DeepSpeed → Megatron-LM 的顺序看显存优化与并行策略。
4. 做后训练实验用 TRL 跑通 SFT/DPO 流水线，再按需深入 FlashAttention 这类算子层优化。

- 训练 Training
  - [深入] [Megatron-LM](https://github.com/NVIDIA/Megatron-LM) — NVIDIA 的张量/流水线并行，超大模型训练的工业模板。
  - [进阶] [DeepSpeed](https://github.com/deepspeedai/DeepSpeed) — ZeRO 显存优化体系，把训练门槛拉低一个数量级。
  - [进阶] [TRL](https://github.com/huggingface/trl) — Hugging Face 的对齐训练库，SFT/DPO/RLHF 一条流水线。
  - [深入] [FlashAttention](https://github.com/Dao-AILab/flash-attention) — IO 感知的精确注意力算子，现代训练推理提速的底层基石。
- 推理 Inference
  - [进阶] [vLLM](https://github.com/vllm-project/vllm) — PagedAttention 高吞吐服务框架，生产部署的主流选择。
  - [入门] [llama.cpp](https://github.com/ggml-org/llama.cpp) — 纯 C/C++ 本地推理，让大模型跑在笔记本上。
  - [进阶] [SGLang](https://github.com/sgl-project/sglang) — RadixAttention 与结构化生成，复杂推理负载的后起之秀。
  - [深入] [TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM) — NVIDIA 官方推理优化库，把 GPU 性能榨到极限的部署方案。

延伸阅读 → [awesome-ai · AI Infra](https://github.com/CUMT-Alethic-Insight-Lab/awesome-ai#ai-infrastructure--ai-infra)

## 7. Evaluation & Benchmarks | 评测与基准

入门顺序：

1. 先读 MMLU 了解「多任务知识问答」这一最通用的度量方式。
2. 用 lm-evaluation-harness 对一个开源模型跑一次标准评测，把论文数字变成亲手结果。
3. 按关心的能力补专项基准：代码看 HumanEval，数学看 GSM8K，工程修 bug 看 SWE-bench。
4. 最后看 Chatbot Arena，理解人类偏好投票这种「非学术」评测为何影响力巨大。

- 学术基准
  - [入门] 2020 · [MMLU](https://arxiv.org/abs/2009.03300) — 57 学科多任务问答，使用最广的 LLM 综合能力基准。
  - [进阶] 2021 · [HumanEval](https://arxiv.org/abs/2107.03374) — 手写编程题测代码生成，Codex 论文提出的经典基准。
  - [进阶] 2021 · [GSM8K](https://arxiv.org/abs/2110.14168) — 小学数学应用题集，思维链与推理能力研究的标准试金石。
  - [进阶] 2022 · [BIG-bench](https://arxiv.org/abs/2206.04615) — 200+ 任务的众包基准，「能力随规模涌现」研究的依托。
- 人类偏好与工程能力
  - [进阶] 2024 · [Chatbot Arena](https://arxiv.org/abs/2403.04132) — LMSYS 的众包对战投票榜单，人类偏好评测的事实标杆。
  - [进阶] [SWE-bench](https://github.com/SWE-bench/SWE-bench) — 用真实 GitHub issue 考「修 bug」能力，Agent 评测标杆。
- 评测框架
  - [进阶] [lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness) — EleutherAI 的统一评测框架，多数开源榜单的事实后端。
  - [进阶] [OpenCompass](https://github.com/open-compass/opencompass) — 中文场景覆盖较全的大模型评测体系。
  - [深入] [HELM](https://github.com/stanford-crfm/helm) — Stanford 的整体性评测框架，强调透明度与多维指标。

延伸阅读 → [awesome-ai · 推理与评测](https://github.com/CUMT-Alethic-Insight-Lab/awesome-ai#reasoning--evaluation--推理与评测)

## 8. Application Stack | 应用栈（Agent / Memory）

入门顺序：

1. 先读 RAG 论文，用 LangChain 或 LlamaIndex 搭一个「文档问答」demo，获得端到端手感。
2. 读 ReAct 理解「推理-行动」循环，再用 MCP 给模型接上真实工具。
3. 看 AutoGPT 与 Generative Agents 两个出圈案例，理解自主 Agent 的能力与局限。
4. 最后进入 Memory 子枝，读 MemGPT、用 Mem0 给应用加长期记忆，补全 Agent 的最后一块拼图。

- RAG 检索增强
  - [进阶] 2020 · [RAG 论文](https://arxiv.org/abs/2005.11401) — 检索与生成的首次系统结合，范式起点。
  - [入门] [LangChain](https://github.com/langchain-ai/langchain) — LLM 应用编排框架，RAG 管线的事实入门。
  - [入门] [LlamaIndex](https://github.com/run-llama/llama_index) — 以数据索引为中心的 RAG 框架，与 LangChain 互补。
- Agent 智能体
  - [进阶] 2022 · [ReAct](https://arxiv.org/abs/2210.03629) — 推理与行动交替的提示范式，现代 Agent 的思想源头。
  - [入门] [AutoGPT](https://github.com/Significant-Gravitas/AutoGPT) — 自主任务分解的早期爆款，引爆 Agent 应用想象。
  - [进阶] 2023 · [Generative Agents](https://arxiv.org/abs/2304.03442) — 记忆-反思-规划的多智能体小镇实验，Agent 行为研究经典。
  - [深入] 2023 · [Voyager](https://arxiv.org/abs/2305.16291) — Minecraft 中的终身学习 Agent，技能库式长程规划的代表作。
- 工具使用 Tool Use
  - [进阶] 2023 · [Toolformer](https://arxiv.org/abs/2302.04761) — 模型自学调用外部 API 的开山之作。
  - [入门] [Model Context Protocol](https://github.com/modelcontextprotocol/modelcontextprotocol) — 工具与数据源接入的开放协议，生态正快速收敛于此。
- Memory 记忆
  - [深入] 2023 · [MemGPT](https://arxiv.org/abs/2310.08560) — 把操作系统式分层内存引入 LLM，长期记忆研究的开山之作。
  - [进阶] [Mem0](https://github.com/mem0ai/mem0) — 面向 LLM 应用的开源记忆层，给 Agent 加可落地的长期记忆。前置：RAG。

延伸阅读 → [awesome-ai · RAG 与检索](https://github.com/CUMT-Alethic-Insight-Lab/awesome-ai#rag--retrieval--rag-与检索) · [awesome-ai · Agent 智能体](https://github.com/CUMT-Alethic-Insight-Lab/awesome-ai#agents--agent-智能体)

## How to Read This Tree | 怎么读这棵树

| Goal | 目标 | Path | 走法 |
| --- | --- | --- | --- |
| New to the field | 零基础入门 | Foundations top to bottom, then Model Evolution | 地基自上而下，再沿演进主线 |
| Building systems | 做工程 / Infra | Engineering Stack, then backfill papers as needed | 先看工程栈，按需回补论文 |
| Building products | 做应用 / Agent | Application Stack, then pick leaves to go deep | 先看应用栈，挑叶子深入 |
| Doing research | 做研究 / 对齐 | Model Evolution, then RL and Alignment branches | 沿演进主线，接 RL 与对齐两枝 |
| Evaluating models | 做评测 | Evaluation & Benchmarks, with Model Evolution as context | 评测一枝为主，演进主线作背景 |

更多按方向的行走路径见 [README · 怎么用这棵树](../README.md#how-to-walk-the-tree--怎么用这棵树)。
