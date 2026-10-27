# AI Development Tree | AI 发展导论树

> 本页保留原 URL 和章节锚点，现为学习总入口。完整公共课程不再塞在一页；[awesome-ai](https://github.com/CUMT-Alethic-Insight-Lab/awesome-ai) 继续承担平面精选资源索引。
>
> **第一次学习请走 [Start Here](start-here.md)**。想理解学科分类读[四轴地图](maps/field-map.md)，想理解技术背景读[多线发展史](history/ai-history.md)，想做项目从[公共先修](foundations/prerequisites.md)开始。

Difficulty tags | 难度标注：`[入门]` 可先修后读 · `[进阶]` 需要数学/代码地基 · `[深入]` 面向研究或硬核工程。历史与教学分离：先修不足时，先回基础而不是硬读最新论文。

<a id="1-foundations--地基"></a>
<a id="foundations"></a>
## 1. Foundations | 地基

**新主线（优先）**：[公共先修](foundations/prerequisites.md) → [经典机器学习 ML-00…08](foundations/classical-ml.md) → [神经网络 DL-00…09](foundations/neural-networks.md) → [CPU 最小实践](../examples/README.md)。

不再采用“先看一门课，再直接写 nanoGPT”的隐式跳跃。必须依次掌握数据边界、评估、张量形状、反向传播和训练循环；数学不足沿节点补救，不必先修完整个数学专业。

原导览中的 D2L、李宏毅、CS229/CS231n/CS224n、PyTorch、micrograd 等仍保留在两仓：学习顺序在[基础课程](foundations/neural-networks.md)，资源索引在 [awesome-ai · ML](https://github.com/CUMT-Alethic-Insight-Lab/awesome-ai#classical-machine-learning) 与 [DL](https://github.com/CUMT-Alethic-Insight-Lab/awesome-ai#deep-learning-foundations)。

<a id="2-model-evolution--模型演进主线"></a>
<a id="model-evolution"></a>
## 2. Model Evolution | 模型演进主线

阅读入口：[AI 多线发展史](history/ai-history.md)。旧页把 2017 Transformer 排在 2015 ResNet 前、LoRA 放在 2023；新表按首次公开/发表口径排列，并区分：

- LoRA：2021 低秩适配，不是量化；
- GRPO：2024 DeepSeekMath 提出；DeepSeek-R1：2025 后训练路线报告；
- Qwen3-VL：官方首批发布记录为 2025，不标 2024；
- Transformer、BERT、GPT 不是“后续一切分叉的唯一原点”，符号、统计、视觉、RL、生成和系统各有独立谱系。

建议先完成 ML/DL 基础，再沿[学科地图](maps/field-map.md)选分支；读历史不能替代做实验。

<a id="3-vision--multimodal--视觉与多模态cv--vlm"></a>
<a id="vision-multimodal"></a>
## 3. Vision & Multimodal | 视觉与多模态（CV / VLM）

**桥接**：ML-03 评估 → DL-05 CNN 与图像分类 → DL-07 Attention → ViT/CLIP → 视觉指令或扩散专题。

- 视觉理解：先能解释卷积、patch、图像分类与迁移，再读 [CS231n](https://cs231n.stanford.edu/)、[ViT](https://arxiv.org/abs/2010.11929)、[CLIP](https://arxiv.org/abs/2103.00020)。
- VLM：BLIP/LLaVA/Qwen3-VL 属于后续方向，不能代替 CNN/Transformer 基础；模型年份与能力描述以官方来源为准。
- 生成：DL-08 → DDPM → Latent Diffusion/ControlNet；大模型生成可选，低资源先理解单步加噪与去噪目标。

资源 → [awesome-ai · 多模态](https://github.com/CUMT-Alethic-Insight-Lab/awesome-ai#multimodal)。

<a id="4-reinforcement-learning--强化学习rl"></a>
<a id="reinforcement-learning-path"></a>
## 4. Reinforcement Learning | 强化学习（RL）

**桥接**：ML/DL 基础 → MDP、回报/折扣与价值函数 → Q-learning → 策略梯度/PPO → DQN/Deep RL → 偏好与后训练。不要用“先读 Sutton 前几章，再直接读 GRPO”跳过中间机制。

[Sutton & Barto](http://incompleteideas.net/book/the-book-2nd.html) 提供理论教材，[Spinning Up](https://spinningup.openai.com/) 提供策略梯度与实现，[Gymnasium](https://github.com/Farama-Foundation/Gymnasium) 提供环境接口；最小任务先在 CPU 小环境上比较回报与稳定性。

资源 → [awesome-ai · 强化学习](https://github.com/CUMT-Alethic-Insight-Lab/awesome-ai#reinforcement-learning)。

<a id="5-alignment--safety--对齐与安全"></a>
<a id="alignment-safety"></a>
## 5. Alignment & Safety | 对齐与安全

**桥接**：DL-09 训练范式 → RL 的 MDP/PPO → InstructGPT 的 SFT/奖励模型/PPO → DPO 的偏好优化 → 安全评测。先分清“奖励来自环境、标注偏好还是模型反馈”，再比较机制与成本。

原有 [InstructGPT](https://arxiv.org/abs/2203.02155)、[DPO](https://arxiv.org/abs/2305.18290)、[Constitutional AI](https://arxiv.org/abs/2212.08073)、[RLHF Book](https://rlhfbook.com/) 可继续作为深入阅读；入门不直接以实现 TRL 代替理解。

<a id="6-engineering-stack--工程栈infra"></a>
<a id="engineering-stack"></a>
## 6. Engineering Stack | 工程栈（Infra）

**桥接**：DL-03 训练循环 → batch/显存与激活分析 → DL-07 注意力 → KV Cache、吞吐/单请求延迟 → EA 同口径测量 → 并行或服务框架。

- 先理解权重、梯度、优化器状态和激活占用，再学 DeepSpeed/Megatron-LM。
- PagedAttention 是 [2023 论文提出的服务机制](https://arxiv.org/abs/2309.06180)，vLLM 是实现系统；不把项目与算法混为同一归因。
- llama.cpp/ONNX Runtime/ExecuTorch 面向不同模型和硬件，不能用理论 FLOPs 或量化位宽直接承诺速度。

资源 → [awesome-ai · AI Infra](https://github.com/CUMT-Alethic-Insight-Lab/awesome-ai#ai-infrastructure) 与 [部署](https://github.com/CUMT-Alethic-Insight-Lab/awesome-ai#serving-deployment)。

<a id="7-evaluation--benchmarks--评测与基准"></a>
<a id="evaluation-benchmarks-path"></a>
## 7. Evaluation & Benchmarks | 评测与基准

**桥接**：ML-00 数据边界 → ML-03 指标/校准 → ML-08 基线/多次运行 → 任务数据污染与统计不确定 → LLM/Agent 评测。

先建立 Majority/简单模型基线和误差分析，再用 [lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness) 或 [HELM](https://github.com/stanford-crfm/helm)。MMLU/HumanEval/GSM8K/SWE-bench 测的是特定任务集合，排行榜不能替代真实使用评价；人类偏好投票也有抽样与偏差约束。

资源 → [awesome-ai · 评估与基准](https://github.com/CUMT-Alethic-Insight-Lab/awesome-ai#evaluation-benchmarks)。

<a id="8-application-stack--应用栈agent--memory"></a>
<a id="application-stack"></a>
## 8. Application Stack | 应用栈（Agent / Memory）

**桥接**：PR-00 Python → HTTP/JSON/API → Embedding 与基础检索 → 检索质量 → RAG → 工具 Schema/权限/错误处理 → Agent 规划与 Memory。

先用少量自有文档验证“检索不到会怎样”，再学 LangChain/LlamaIndex；先能让单个工具超时、重试、校验参数，再学 AutoGPT 等多步 Agent。RAG 是重要代表工作而非所有检索生成的绝对起点，Memory 也不是“最后一块拼图”——权限、评测与失败恢复同样必要。

原有深入资源：[ReAct](https://arxiv.org/abs/2210.03629)、[Generative Agents](https://arxiv.org/abs/2304.03442)、[MemGPT](https://arxiv.org/abs/2310.08560)、[Mem0](https://github.com/mem0ai/mem0)。资源索引 → [awesome-ai · RAG](https://github.com/CUMT-Alethic-Insight-Lab/awesome-ai#rag-retrieval) 与 [Agents](https://github.com/CUMT-Alethic-Insight-Lab/awesome-ai#agents)。

<a id="how-to-read-this-tree--怎么读这棵树"></a>
## How to Read This Tree | 怎么读这棵树

| Goal | 目标 | 推荐走法 |
| --- | --- | --- |
| New to the field | 零基础 | Start Here → 公共先修 → ML → DL → 学科地图 |
| Building systems | 工程 / Infra | ML/DL 训练闭环 → EA 测量 → Engineering Stack |
| Building products | 应用 / Agent | Python/HTTP → 检索与工具错误处理 → RAG/Agent → Evaluation |
| Doing research | 研究 / 对齐 | ML/DL → RL → Alignment；历史用于定位问题而非代替课程 |
| Evaluating models | 评测 | ML-03/08 → 数据污染/统计/基线 → Evaluation |
| Understanding the field | 学科全景 | 四轴地图 → 多线发展史 → 按兴趣回公共基础 |

所有路径与成熟度见 [paths/README.md](paths/README.md)。保留原[环境前提](../README.md#environment-prerequisite--环境前提)，但社外读者可直接使用公共先修的独立环境入口。
