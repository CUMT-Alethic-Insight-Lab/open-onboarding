# 学习路径与成熟度

所有路径先过[起点自检](../start-here.md)。成熟度只表示内容与验证证据，不表示学习效果：

- **内容完成，待试走**：节点和实践已写、维护者做过技术核验，但未有新成员完整试走。
- **导览级**：只提供定位、先修、代表资源与一个入门任务，不是完整课程。
- **已试走**：必须有真实学习者的起点、卡点、恢复和完成证据；当前没有任何路径获得此标记。

| 路径 | 入口 | 出口 | 状态 |
| --- | --- | --- | --- |
| [公共先修](../foundations/prerequisites.md) | 基本电脑操作 | Python/NumPy/数学/Git 环境自检 | 内容完成，待试走 |
| [经典 ML](../foundations/classical-ml.md) | 公共先修 | ML-08 可复现 sklearn 实验 | 内容完成，待试走 |
| [神经网络](../foundations/neural-networks.md) | ML-00…03 | MLP、CNN 对照、Attention | 内容完成，待试走 |
| [数据工程](data-engineering.md) | PR-00…02、ML-00/03 | DE-08 可追溯数据集 | 内容完成，待试走 |
| [小模型与高效 AI](efficient-ai.md) | ML-03/08、DL-03/05 | 同口径质量—资源权衡报告 | 内容完成，待试走 |

| [专题领域导览](specialized-domains.md) | 按专题差异 | 定位、先修与一个入门任务 | 导览级 |

## 公共分叉

```text
PR → ML → DL ─┬─ 数据工程 → 小型训练/LLM 数据
              ├─ 高效 AI → Infra/部署
              └─ 方向桥 → LLM / CV / RL / RAG / Infra / Evaluation / Diffusion
```

历史与地图是独立导览：[四轴学科地图](../maps/field-map.md)、[多线发展史](../history/ai-history.md)。原有 [AI Tree](../ai-tree.md) 继续提供方向资源入口；以下为桥接，全部“内容完成，待试走”，不是另开一套完整方向课程。

## LLM / NLP 桥

- **前置**：ML-00/03、DL-03、DL-06/07、DE-01/05。
- **目标**：把文本变成可训练序列，并解释 Tokenizer、Embedding、语言建模与数据/评测的关系。
- **为什么在这里学**：没有 token/批次/训练闭环，直接调大框架只会隐藏错误。
- **指定材料**：必学 D2L [文本预处理](https://d2l.ai/chapter_recurrent-neural-networks/text-preprocessing.html) 与 [Transformer](https://d2l.ai/chapter_attention-mechanisms-and-transformers/transformer.html)；推荐 [Hugging Face LLM Course](https://huggingface.co/learn/llm-course/) 的 Tokenizers 章节。
- **学习动作**：字符/子词切分对照 → vocab/特殊 token → Embedding → next-token → 按文档/时间拆分 → 训练小模型。
- **最小实践**：在合法小文本上训练字符级 next-token 基线，报告 token 数、困惑度与样例，再考虑 nanoGPT；不需大模型。
- **完成标准**：能解释 OOV/词表/上下文窗口、数据污染与 train/validation 边界。
- **卡住时**：回 DL-06/07；文本清洗回 DE-02，指标回 ML-03。
- **下一步**：[awesome-ai · LLM](https://github.com/CUMT-Alethic-Insight-Lab/awesome-ai#llm-fundamentals)，或 RAG/Infra 桥。
- **资源要求**：字符级 CPU；大模型预训练不是入口要求。

## CV / VLM 桥

- **前置**：ML-03、DL-05、DL-07、DL-09。
- **目标**：从图像分类过渡到 ViT/CLIP 与视觉语言对齐。
- **为什么在这里学**：先理解视觉表征和任务评价，再谈通用多模态模型。
- **指定材料**：必学 [CS231n Transfer Learning](https://cs231n.github.io/transfer-learning/)、[ViT](https://arxiv.org/abs/2010.11929)、[CLIP](https://arxiv.org/abs/2103.00020)。
- **学习动作**：图像分类 → patch/token → 预训练/线性 probe → 图文对比 → zero-shot 类别构造与误差分析。
- **最小实践**：小图像数据集做 CNN/线性 probe；或用小 CLIP 检查文本 prompt 改变对检索的影响，记录数据与指标。
- **完成标准**：能区分视觉编码器、文本编码器、对齐目标与生成式 VLM。
- **卡住时**：CNN 回 DL-05，Attention 回 DL-07，训练范式回 DL-09。
- **下一步**：检测/分割、[awesome-ai · Multimodal](https://github.com/CUMT-Alethic-Insight-Lab/awesome-ai#multimodal) 或遥感导览。
- **资源要求**：基础实验 CPU；预训 VLM 推理可用低资源模型但不作为已验证承诺。

## RL / Alignment 桥

- **前置**：ML-01/03、DL-03、PR-05。
- **目标**：掌握 MDP、价值、策略梯度与 PPO，再理解偏好训练。
- **为什么在这里学**：RLHF 不是普通分类，奖励、状态和信用分配不能省略。
- **指定材料**：必学 Sutton & Barto [第3章 MDP、第6章 TD、第13章 Policy Gradient](https://mitpress.mit.edu/9780262039246/reinforcement-learning/)、[Spinning Up 策略梯度](https://spinningup.openai.com/en/latest/spinningup/rl_intro3.html)；推荐 [PPO](https://arxiv.org/abs/1707.06347)。
- **学习动作**：MDP 五元组 → 回报/折扣 → Q 值更新 → 策略梯度 → clipping → 奖励/偏好模型 → PPO/DPO 对照。
- **最小实践**：在 Gymnasium 小环境跑 random 与价值/策略基线，报告多种子回报分布；随后才读 InstructGPT/GRPO。
- **完成标准**：能区分 on/off-policy、价值/策略优化、环境奖励与偏好奖励。
- **卡住时**：回报异常先查 episode/折扣/终止，梯度回 DL-02；不要先调大模型超参。
- **下一步**：[awesome-ai · RL](https://github.com/CUMT-Alethic-Insight-Lab/awesome-ai#reinforcement-learning) 与 AI Tree 的 Alignment。
- **资源要求**：经典小环境 CPU；大模型 RL 训练不要求。

## RAG / Agent 桥

- **前置**：PR-00…02；DL-06 的 Embedding 概念；ML-03 评估。
- **目标**：先建立 HTTP/JSON、检索与工具调用可靠性，再进入多步 Agent。
- **为什么在这里学**：框架不能替代接口、检索质量和失败处理。
- **指定材料**：必学 [Requests Quickstart](https://requests.readthedocs.io/en/latest/user/quickstart/)、[Sentence Transformers semantic search](https://www.sbert.net/examples/applications/semantic-search/README.html)、[MCP Specification](https://modelcontextprotocol.io/specification/latest)；推荐 [RAG](https://arxiv.org/abs/2005.11401)。
- **学习动作**：HTTP 状态/JSON/超时 → 文档切块/Embedding → top-k 检索 → 命中与回答评价 → 工具 Schema/权限/幂等/错误恢复。
- **最小实践**：用少量自有文档做检索，构造“无答案/错误文档/工具超时”三类失败；没有证据时系统应拒答或请求补充。
- **完成标准**：能分别评检索和生成，工具输入有校验、超时与权限边界，不把长上下文当必然优于检索。
- **卡住时**：HTTP/JSON 回 PR-00；检索差先查切块与召回，不先换 Agent 框架。
- **下一步**：[awesome-ai · RAG](https://github.com/CUMT-Alethic-Insight-Lab/awesome-ai#rag-retrieval) / [Agents](https://github.com/CUMT-Alethic-Insight-Lab/awesome-ai#agents)。
- **资源要求**：本地小文档 CPU；不需要付费 API。

## Infra 桥

- **前置**：DL-03/07、EA-1…3。
- **目标**：从训练/推理公式定位显存、KV Cache、吞吐和延迟，再读并行与服务框架。
- **为什么在这里学**：大框架配置不能替代资源模型与同口径测量。
- **指定材料**：必学 [PyTorch Profiler](https://docs.pytorch.org/tutorials/recipes/recipes/profiler_recipe.html)、[PagedAttention/vLLM](https://arxiv.org/abs/2309.06180)；推荐 [FlashAttention](https://arxiv.org/abs/2205.14135)。
- **学习动作**：权重/梯度/优化器/激活 → batch 与峰值显存 → 自回归 KV Cache → prefill/decode → P50/P95/吞吐 → profile。
- **最小实践**：在小 Transformer 上改变 batch 或序列长度，记录内存/延迟，画出成本曲线；不要求分布式集群。
- **完成标准**：能区分计算/内存带宽/IO 瓶颈，说明并发与单请求延迟不是同一指标。
- **卡住时**：回 DL-07 算注意力形状，回 EA-3 检查测量；先单设备再分布式。
- **下一步**：[awesome-ai · AI Infra](https://github.com/CUMT-Alethic-Insight-Lab/awesome-ai#ai-infrastructure) / Serving。
- **资源要求**：小模型 CPU；GPU/多卡结果标待实际测试。

## Evaluation 桥

- **前置**：ML-00/03/08、DE-05。
- **目标**：把经典评估原则迁移到生成、检索和 Agent，而不是只看榜单平均分。
- **为什么在这里学**：数据泄漏、选择偏差与小样本波动在 LLM 上同样存在。
- **指定材料**：必学 MOOC [分类指标](https://inria.github.io/scikit-learn-mooc/python_scripts/metrics_classification.html)、[HELM](https://arxiv.org/abs/2211.09110) 的多维评价；推荐 [lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness)。
- **学习动作**：任务/参考实现 → 简单基线 → 污染检查 → 多种子/bootstrap → 分片误差分析 → 人工评审一致性。
- **最小实践**：选一个小型生成/检索任务，写 20–50 个评价样例，比较两系统并报告绝对数、比例与不确定度。
- **完成标准**：能区分自动指标/人工偏好/任务成功率，不将单次小样本差异写成稳定优劣。
- **卡住时**：回 ML-03 指标与 DE-05 污染；指标无法对应目标时先做误差分类。
- **下一步**：[awesome-ai · Evaluation](https://github.com/CUMT-Alethic-Insight-Lab/awesome-ai#evaluation-benchmarks)。
- **资源要求**：小评价集 CPU。

## Diffusion 桥

- **前置**：DL-03/05/08、PR-05。
- **目标**：理解前向加噪、噪声预测、反向采样、潜空间与条件控制。
- **为什么在这里学**：调用文生图 API 不等于理解扩散目标或采样成本。
- **指定材料**：必学 [DDPM](https://arxiv.org/abs/2006.11239) 与 [Diffusers basic training](https://huggingface.co/docs/diffusers/tutorials/basic_training)；推荐 [Latent Diffusion](https://arxiv.org/abs/2112.10752)。
- **学习动作**：高斯加噪 → 时间步/噪声 schedule → 预测 ε → 反向迭代 → autoencoder 潜空间 → 条件输入。
- **最小实践**：对一张小图执行不同时间步加噪并手算系数；有算力再训练小型 DDPM，记录采样步数与质量/时间。
- **完成标准**：能区分训练一次噪声预测与多步采样、像素与潜空间扩散。
- **卡住时**：回 PR-05 高斯与 DL-08 生成家族；先检查时间步/张量形状，不先换大模型。
- **下一步**：[awesome-ai · Multimodal](https://github.com/CUMT-Alethic-Insight-Lab/awesome-ai#multimodal)。
- **资源要求**：加噪实验 CPU；完整训练可选且未验证。

## 专题地图

[图学习、推荐、时序、语音/音频、机器人/VLA、因果/科学 AI、搜索规划、遥感/地学 CV](specialized-domains.md) 均为导览级，分别给出问题、方法、先修、资源、最小任务与补救，不宣称完整课程或新人已验证。
