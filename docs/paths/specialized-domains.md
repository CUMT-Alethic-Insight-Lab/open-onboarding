# 专题领域导览

以下均为**导览级**，不是已完成的系统课程，也没有新成员试走记录。用途是定位问题、先修和第一个实践；完成后应沿一手教材/官方文档继续，而不是把两个资源名当作掌握领域。

## 图机器学习

- **解决的问题**：节点分类、链接预测、图分类与关系数据上的归纳偏置。
- **代表方法**：谱图卷积、GCN 的邻居聚合、GAT 的注意力加权、消息传递。
- **先修路径**：PR-03 矩阵/图的基本表示 → ML-03 → DL-01…03；不必先学大语言模型。
- **入门资源**：[Graph Neural Networks: A Review of Methods and Applications](https://arxiv.org/abs/1812.08434) 与 [PyG 官方教程](https://pytorch-geometric.readthedocs.io/en/latest/get_started/introduction.html)。
- **最小实践**：用一个小型无向图写邻接矩阵，手算一层均值邻居聚合；比较无自环/有自环结果。
- **补救/下一步**：形状不清回 PR-01；聚合过平滑或评测泄漏时回 ML-03，再进入 PyG 的 Cora 示例。
- **成熟度**：导览级。

## 推荐系统

- **解决的问题**：大规模候选中的召回、排序与个性化，而非简单“给用户打标签”。
- **代表方法**：协同过滤/矩阵分解、双塔召回、学习排序与深度推荐。
- **先修路径**：ML-02/03/06 → Embedding/DL-01 → 时间与用户拆分。
- **入门资源**：[Matrix Factorization Techniques for Recommender Systems](https://ieeexplore.ieee.org/document/5197422) 与 [Microsoft Recommenders](https://github.com/recommenders-team/recommenders)。
- **最小实践**：构造小型用户—物品矩阵，按时间留一评估；比较 popularity 基线与矩阵分解的 Recall@K/NDCG@K。
- **补救/下一步**：指标异常先查负样本、冷启动和时间泄漏；不要只报随机拆分 RMSE。
- **成熟度**：导览级。

## 时间序列

- **解决的问题**：趋势、季节性、动态依赖与预测，不等同普通 i.i.d. 回归。
- **代表方法**：naive/季节 naive、指数平滑、ARIMA、基于窗口的监督/深度模型。
- **先修路径**：PR-05 → ML-00/03/08 → 时间拆分与滚动验证。
- **入门资源**：[Forecasting: Principles and Practice](https://otexts.com/fpp3/) 的时间序列图形、基准方法与时间交叉验证章节。
- **最小实践**：选公开小型序列，做 naive 与 seasonal naive 基线，滚动起点评估后再比较一个统计模型。
- **补救/下一步**：结果过好消息先查未来信息、归一化与缺失日期；再进入深度时序。
- **成熟度**：导览级。

## 语音与音频

- **解决的问题**：ASR 将语音转文本，TTS 将文本合成语音，通用音频还包括事件/音乐理解与生成。
- **代表方法**：波形/频谱表征、CTC/seq2seq 识别、声学模型+声码器、音频 Transformer。
- **先修路径**：PR-01/03 → DL-05/06/07 → 采样率、窗函数和频谱。
- **入门资源**：[Speech and Language Processing 的公开草稿](https://web.stanford.edu/~jurafsky/slp3/) 与 [Torchaudio 官方文档](https://docs.pytorch.org/audio/stable/)（2.8 起为维护期，编解码转看 TorchCodec）。
- **最小实践**：读取一段合法短音频，画出波形/频谱并比较窗长；ASR/TTS 任务任选其一，明确评价指标。
- **补救/下一步**：先查采样率、声道与归一化；没有 GPU 时用预训小模型观察，不训练大模型。
- **成熟度**：导览级。

## 机器人与 VLA

- **解决的问题**：感知—状态—动作闭环、控制、规划与多模态动作生成。
- **代表方法**：状态估计/控制、模仿学习、强化学习、VLA（vision-language-action）。
- **先修路径**：DL-03 → RL 的 MDP → 模仿/规划 → 多模态表征；硬件实验还需安全规程。
- **入门资源**：[Open X-Embodiment / RT-X](https://arxiv.org/abs/2310.08864) 与 [LeRobot](https://github.com/huggingface/lerobot) 的官方示例。
- **最小实践**：只在模拟器或公开轨迹上做行为克隆，比较训练/未见场景成功率并分析失败。
- **补救/下一步**：先排查坐标系、动作空间、延迟与分布偏移；未经风险评估不得直接驱动真实硬件。
- **成熟度**：导览级；无真实机器人验证。

## 因果学习与科学 AI

- **解决的问题**：干预/反事实与预测的区别，以及物理/生物/化学结构约束下的学习。
- **代表方法**：因果图、do 算子/反事实、潜在结果、物理约束/结构感知模型。
- **先修路径**：PR-05 → ML-00/03 → 因果假设与领域知识；不能从相关模型直接推出因果效应。
- **入门资源**：[Causal Inference: The Mixtape](https://mixtape.scunning.com/) 与 [AlphaFold2](https://www.nature.com/articles/s41586-021-03819-2) 作为两类不同入口。
- **最小实践**：画含 treatment/outcome/confounder 的 DAG，写识别假设；或在一个科学数据集上明确结构、划分与评价。
- **补救/下一步**：先问干预是什么、未观测混杂是否存在；不靠提高预测准确率证明因果。
- **成熟度**：导览级。

## 传统 AI、搜索与规划

- **解决的问题**：离散状态空间、约束、逻辑知识与可验证行动序列。
- **代表方法**：BFS/DFS、A* 与启发式、约束满足、知识表示/推理、MCTS。
- **先修路径**：PR-00…02 → 图/状态表示与复杂度；无需先修深度学习。
- **入门资源**：[AIMA 官方代码与教材入口](https://aima.cs.berkeley.edu/) 与 [AlphaGo](https://www.nature.com/articles/nature16961) 的搜索+学习组合案例。
- **最小实践**：对八数码或网格路径实现 BFS/A*，比较节点扩展数、路径最优性与启发式相容性。
- **补救/下一步**：状态爆炸先检查重复状态与启发式；再接工具 Agent 的搜索、验证与规划。
- **成熟度**：导览级。

## 遥感与地学 CV

- **解决的问题**：多光谱/雷达影像、地理坐标、变化检测、地表分类与时空预测。
- **代表方法**：CNN/ViT、时序变化检测、多模态融合、地理空间评价。
- **先修路径**：ML-03 → DL-05/07 → 坐标/分辨率/波段与空间独立拆分。
- **入门资源**：[TorchGeo](https://github.com/torchgeo/torchgeo) 官方数据集/教程与 [Radiant Earth · Source Cooperative](https://source.coop/radiantearth) 的开放数据入口。
- **最小实践**：在合法小区域样本上做分类/变化检测，按地理块而非随机像素拆分并报告空间泛化。
- **补救/下一步**：先查投影、云/缺失、波段与许可；不要复制自然图像结论而不做领域验证。
- **成熟度**：导览级。
