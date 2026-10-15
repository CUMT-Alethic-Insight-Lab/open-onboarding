# AI Development Tree | AI 发展导论树

A tree-shaped index of classic open-source repositories, projects, tech stacks, and papers, ordered by how the field developed — read the branches as a narrative, not a checklist.

对开源经典仓库、项目、技术栈与论文的树状索引，按发展脉络组织——把树枝当作故事线读，而不是待办清单。

Sibling repo [awesome-ai](https://github.com/CUMT-Alethic-Insight-Lab/awesome-ai) is the flat curated list (breadth); this tree is the development path (order). Leaves here link out to primary sources; category-level breadth stays in awesome-ai.

与同 org 的 [awesome-ai](https://github.com/CUMT-Alethic-Insight-Lab/awesome-ai) 分工：awesome-ai 求全（平面精选清单），本树求序（发展脉络），树末梢只指一手来源。

## Foundations | 地基

- [d2l-zh](https://github.com/d2l-ai/d2l-zh) — 《动手学深度学习》，中文可运行教材，从零实现到工程用法。
- [CS229](https://cs229.stanford.edu/) — Stanford 机器学习课，补统计学习基础的默认起点。
- [CS231n](https://cs231n.github.io/) — Stanford 视觉课，CNN 时代的标准入门。
- [CS224n](https://web.stanford.edu/class/cs224n/) — Stanford NLP 课，理解词向量到 Transformer 的过渡。
- [CS285](https://rail.eecs.berkeley.edu/deeprlcourse/) — Berkeley 深度强化学习课，读懂 RLHF 的前置。
- [PyTorch](https://github.com/pytorch/pytorch) — 研究与工业界事实标准的深度学习框架。
- [Hugging Face Transformers](https://github.com/huggingface/transformers) — 预训练模型的统一入口，跑通它等于拿到整个生态的钥匙。

延伸阅读 → [awesome-ai 对应分类](https://github.com/CUMT-Alethic-Insight-Lab/awesome-ai)

## Model Evolution | 模型演进主线

- 2012 · [AlexNet](https://proceedings.neurips.cc/paper/2012/hash/c399862d3b9d6b76c8436e924a68c45b-Abstract.html) — GPU + 深度卷积点燃本轮浪潮的引爆点。
- 2015 · [ResNet](https://arxiv.org/abs/1512.03385) — 残差连接让百层网络可训练，深度不再是瓶颈。
- 2017 · [Attention Is All You Need](https://arxiv.org/abs/1706.03762) — Transformer 诞生，自注意力取代循环结构。
- 2018 · [BERT](https://arxiv.org/abs/1810.04805) — 双向预训练 + 微调范式横扫 NLP 榜单。
- 2019 · [GPT-2](https://github.com/openai/gpt-2) — 自回归生成路线跑通，「大即涌现」初见端倪。
- 2020 · [GPT-3](https://arxiv.org/abs/2005.14165) — 175B 参数与 in-context learning，规模带来质变。
- 2020 · [ViT](https://arxiv.org/abs/2010.11929) — 纯 Transformer 杀入视觉，统一架构的开端。
- 2020 · [Scaling Laws](https://arxiv.org/abs/2001.08361) — 损失随算力/数据/参数幂律下降，扩展成为可计算的科学。
- 2021 · [CLIP](https://arxiv.org/abs/2103.00020) — 图文对比学习打通视觉与语言，多模态的起点。
- 2022 · [Chinchilla](https://arxiv.org/abs/2203.15556) — 修正扩展律：数据与参数需等比增长，小模型喂足数据更优。
- 2022 · [InstructGPT / RLHF](https://arxiv.org/abs/2203.02155) — 人类反馈强化学习对齐意图，ChatGPT 的技术内核。
- 2023 · [LLaMA](https://arxiv.org/abs/2302.13971) — 高效开源基座发布，社区微调生态由此爆发。
- 2023 · [LoRA](https://arxiv.org/abs/2106.09685) — 低秩适配让消费级显卡也能微调大模型。
- 2024– · [DeepSeek-R1](https://arxiv.org/abs/2501.12948) 与 [OpenAI o1](https://openai.com/index/learning-to-reason-with-llms/) — 推理时计算与强化学习驱动的新范式。

延伸阅读 → [awesome-ai 对应分类](https://github.com/CUMT-Alethic-Insight-Lab/awesome-ai)

## Engineering Stack | 工程栈

- 训练 Training
  - [Megatron-LM](https://github.com/NVIDIA/Megatron-LM) — NVIDIA 的张量/流水线并行，超大模型训练的工业模板。
  - [DeepSpeed](https://github.com/deepspeedai/DeepSpeed) — ZeRO 显存优化体系，把训练门槛拉低一个数量级。
  - [TRL](https://github.com/huggingface/trl) — Hugging Face 的对齐训练库，SFT/DPO/RLHF 一条流水线。
- 推理 Inference
  - [vLLM](https://github.com/vllm-project/vllm) — PagedAttention 高吞吐服务框架，生产部署的主流选择。
  - [llama.cpp](https://github.com/ggml-org/llama.cpp) — 纯 C/C++ 本地推理，让大模型跑在笔记本上。
  - [SGLang](https://github.com/sgl-project/sglang) — RadixAttention 与结构化生成，复杂推理负载的后起之秀。
- 评测 Evaluation
  - [lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness) — EleutherAI 的统一评测框架，多数开源榜单的事实后端。
  - [OpenCompass](https://github.com/open-compass/opencompass) — 中文场景覆盖较全的大模型评测体系。
  - [HELM](https://github.com/stanford-crfm/helm) — Stanford 的整体性评测框架，强调透明度与多维指标。
  - [SWE-bench](https://github.com/SWE-bench/SWE-bench) — 用真实 GitHub issue 考「修 bug」能力，Agent 评测标杆。

延伸阅读 → [awesome-ai 对应分类](https://github.com/CUMT-Alethic-Insight-Lab/awesome-ai)

## Application Stack | 应用栈

- RAG 检索增强
  - 2020 · [RAG 论文](https://arxiv.org/abs/2005.11401) — 检索与生成的首次系统结合，范式起点。
  - [LangChain](https://github.com/langchain-ai/langchain) — LLM 应用编排框架，RAG 管线的事实入门。
  - [LlamaIndex](https://github.com/run-llama/llama_index) — 以数据索引为中心的 RAG 框架，与 LangChain 互补。
- Agent 智能体
  - 2022 · [ReAct](https://arxiv.org/abs/2210.03629) — 推理与行动交替的提示范式，现代 Agent 的思想源头。
  - [AutoGPT](https://github.com/Significant-Gravitas/AutoGPT) — 自主任务分解的早期爆款，引爆 Agent 应用想象。
  - 2023 · [Generative Agents](https://arxiv.org/abs/2304.03442) — 记忆-反思-规划的多智能体小镇实验，Agent 行为研究经典。
- 工具使用 Tool Use
  - 2023 · [Toolformer](https://arxiv.org/abs/2302.04761) — 模型自学调用外部 API 的开山之作。
  - [Model Context Protocol](https://github.com/modelcontextprotocol/modelcontextprotocol) — 工具与数据源接入的开放协议，生态正快速收敛于此。

延伸阅读 → [awesome-ai 对应分类](https://github.com/CUMT-Alethic-Insight-Lab/awesome-ai)

## Generative Vision | 生成式视觉支线

- 2020 · [DDPM](https://arxiv.org/abs/2006.11239) — 去噪扩散概率模型，扩散生成路线的奠基论文。
- 2022 · [Stable Diffusion](https://github.com/CompVis/stable-diffusion) — 潜空间扩散开源模型，把文生图带进大众。
- 2023 · [ControlNet](https://arxiv.org/abs/2302.05543) — 给扩散模型加结构控制，可控生成的标准方案。

延伸阅读 → [awesome-ai 对应分类](https://github.com/CUMT-Alethic-Insight-Lab/awesome-ai)

## How to Read This Tree | 怎么读这棵树

| Goal | 目标 | Path | 走法 |
| --- | --- | --- | --- |
| New to the field | 零基础入门 | Foundations top to bottom, then Model Evolution | 地基自上而下，再沿演进主线 |
| Building systems | 做工程 | Engineering Stack, then backfill papers as needed | 先看工程栈，按需回补论文 |
| Building products | 做应用 | Application Stack, then pick leaves to go deep | 先看应用栈，挑叶子深入 |
