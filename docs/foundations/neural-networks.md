# 神经网络与深度学习基础

**入口**：ML-00…03，PR-01/04；**出口**：MLP 训练闭环、CNN 对照、Attention 前向与毕业解释；**状态**：内容完成，待试走。主线用 [D2L](https://zh.d2l.ai/) 和 [PyTorch Basics](https://docs.pytorch.org/tutorials/beginner/basics/intro.html)，不以论文发布时间替代教学顺序。

先分清三条轴：**架构**（MLP/CNN/RNN/Transformer）处理信息的方式，**学习信号**（监督/自监督/强化等）来自哪里，**任务**（分类/生成/控制等）要预测什么。同属 Transformer 的模型可以用不同学习信号，训练范式不是网络层。

## DL-00 由线性分类器到感知机

- **前置**：ML-01、ML-02。
- **目标**：理解神经元、阈值/激活、线性可分与 XOR 的非线性需求。
- **为什么在这里学**：避免把单层感知机与现代深层 MLP 混为一谈。
- **指定材料**：必学 D2L [多层感知机 4.1.1](https://zh.d2l.ai/chapter_multilayer-perceptrons/mlp.html)；推荐 [CS231n Neural Networks Part 1](https://cs231n.github.io/neural-networks-1/)。
- **学习动作**：手算 AND/OR 的线性边界；尝试 XOR 并说明为什么单层线性分类不行。
- **最小实践**：用 NumPy 写感知机预测函数，分别在 AND 与 XOR 小表上检查预测；不要求把 XOR 训练到不可能的 100%。
- **完成标准**：能区分模型表达能力与优化失败，解释非线性隐藏层的必要。
- **卡住时**：回 ML-02 画决策边界；不要靠增大单层权重解决 XOR。
- **下一步**：DL-01。
- **资源要求**：纸笔+CPU。

## DL-01 MLP 与前向计算

- **前置**：DL-00，PR-01/03。
- **目标**：能把层、参数、激活、损失写成形状正确的张量计算。
- **为什么在这里学**：形状和归纳偏置没弄清，后续反传与 Transformer 都只能靠猜。
- **指定材料**：必学 D2L [MLP 4.1](https://zh.d2l.ai/chapter_multilayer-perceptrons/mlp.html)、[PyTorch Tensors](https://docs.pytorch.org/tutorials/beginner/basics/tensorqs_tutorial.html)；推荐 [Build Model](https://docs.pytorch.org/tutorials/beginner/basics/buildmodel_tutorial.html)。
- **学习动作**：对 `X(n,d)`、`W(d,h)` 写出每层形状；说明两层线性等价于一层，激活为何改变表达。
- **最小实践**：不用框架或只用张量写 `ReLU(XW1+b1)W2+b2`，断言 batch 不变、输出类别数正确、参数量计算一致。
- **完成标准**：能解释 logits 与概率，不用逐样本 Python 循环完成前向。
- **卡住时**：回 PR-01 查矩阵乘/广播；把每层 `shape` 打出来再读报错。
- **下一步**：DL-02。
- **资源要求**：CPU。

## DL-02 计算图、链式法则与反向传播

- **前置**：DL-01，PR-04。
- **目标**：能手算局部梯度、组合计算图，并用数值梯度验证 autograd。
- **为什么在这里学**：理解梯度才能诊断训练，而非把 `backward()` 当黑盒。
- **指定材料**：必学 D2L [前向/反向与计算图 4.7](https://zh.d2l.ai/chapter_multilayer-perceptrons/backprop.html)、[micrograd](https://github.com/karpathy/micrograd) 的 `engine.py`；推荐 [PyTorch Autograd](https://docs.pytorch.org/tutorials/beginner/basics/autogradqs_tutorial.html)。
- **学习动作**：沿图先 forward 缓存中间量，再 reverse-mode 累加梯度；手算二层 MLP 一个权重梯度。
- **最小实践**：运行 `python examples/dl_foundations.py gradient`，再用 centered finite difference 校验自己的标量/小矩阵例子。
- **完成标准**：能解释链式法则、梯度累加、`zero_grad()`，解析/数值梯度误差在明示容差内。
- **卡住时**：回 PR-04 先做标量；数值校验用 float64、小 epsilon，检查非光滑点。
- **下一步**：DL-03。
- **资源要求**：CPU；micrograd 用作最小参考，不要求先读语言模型。

## DL-03 数据、优化器与训练循环

- **前置**：DL-02，ML-00/03。
- **目标**：独立写 Dataset/DataLoader、mini-batch、loss、SGD/Momentum/Adam、验证与 checkpoint 的闭环。
- **为什么在这里学**：模型只是训练系统的一部分，数据与优化决定结果是否可信。
- **指定材料**：必学 PyTorch [Datasets & DataLoaders](https://docs.pytorch.org/tutorials/beginner/basics/data_tutorial.html)、[Optimization Loop](https://docs.pytorch.org/tutorials/beginner/basics/optimization_tutorial.html)；D2L [SGD](https://zh.d2l.ai/chapter_optimization/sgd.html)、[Adam](https://zh.d2l.ai/chapter_optimization/adam.html)。
- **学习动作**：画出一个 epoch 的顺序；区分 SGD、Momentum 的累积方向与 Adam 的一/二阶矩估计；说明学习率与 batch 的耦合。
- **最小实践**：运行 `python examples/dl_foundations.py mlp`（合成二分类），再改成 mini-batch、保存 best-val checkpoint，测试只在选定后使用。
- **完成标准**：loss 下降且验证指标可解释；能复述训练/评估模式、梯度清零、反传、更新的顺序。
- **卡住时**：先过拟合几十条数据；检查标签 dtype、输入形状、学习率、数据混洗；回 DL-02 查梯度是否存在。
- **下一步**：DL-04。
- **资源要求**：CPU；官方 MNIST/Fashion-MNIST 可作为下载后的等价练习，不要求 GPU。

## DL-04 泛化与训练稳定性

- **前置**：DL-03，ML-03。
- **目标**：理解初始化、梯度消失/爆炸、ReLU/GELU、Dropout、归一化和残差。
- **为什么在这里学**：网络能写不等于能稳定训练，技巧必须对应具体故障。
- **指定材料**：必学 D2L [数值稳定性与初始化 5.1](https://zh.d2l.ai/chapter_multilayer-perceptrons/numerical-stability-and-init.html)、[Dropout 5.6](https://zh.d2l.ai/chapter_multilayer-perceptrons/dropout.html)；推荐 [BatchNorm 8.5](https://zh.d2l.ai/chapter_convolutional-modern/batch-norm.html)、[ResNet 8.6](https://zh.d2l.ai/chapter_convolutional-modern/resnet.html)。
- **学习动作**：比较 sigmoid 饱和与 ReLU；解释 BatchNorm 的 batch 统计与 LayerNorm 的单样本特征统计；说明残差提供恒等通路而非“消灭所有梯度问题”。
- **最小实践**：在 DL-03 上一次只改初始化/深度/Dropout 之一，记录训练与验证曲线和梯度范数。
- **完成标准**：能用证据区分优化困难与泛化差，不把正则化当学习率修复。
- **卡住时**：回 DL-03 小数据过拟合测试；NaN 先查学习率/输入/损失，再查梯度裁剪。
- **下一步**：DL-05。
- **资源要求**：CPU 小网络即可。

## DL-05 CNN 视觉主干

- **前置**：DL-01…04。
- **目标**：理解卷积、权重共享、池化、感受野和视觉架构演进。
- **为什么在这里学**：CNN 的局部性/平移归纳偏置不同于把像素摊平的 MLP。
- **指定材料**：必学 D2L [为什么需要卷积 7.1](https://zh.d2l.ai/chapter_convolutional-neural-networks/why-conv.html)、[卷积层 7.2](https://zh.d2l.ai/chapter_convolutional-neural-networks/conv-layer.html)、[LeNet 7.6](https://zh.d2l.ai/chapter_convolutional-neural-networks/lenet.html)；推荐 CS231n [CNN](https://cs231n.github.io/convolutional-networks/)、D2L [ResNet](https://zh.d2l.ai/chapter_convolutional-modern/resnet.html)。
- **学习动作**：手算输出高宽与参数量；沿 LeNet→AlexNet→VGG/Inception→ResNet→轻量 CNN/ViT 说明每站解决的问题和成本，不当作必修论文清单。
- **最小实践**：运行 `python examples/dl_foundations.py cnn`，在 sklearn digits 同划分、同 epoch 预算下比较 MLP/CNN；再训练更久并画曲线，解释小数据结果不证明普遍优劣。
- **完成标准**：能解释局部连接/共享、通道形状、感受野和至少两种架构取舍。
- **卡住时**：回 DL-01 查 `(N,C,H,W)`；小数据过拟合先查数据增强/容量，不直接下载大模型。
- **下一步**：DL-06；视觉可转 CV/VLM 桥接，模型成本可转 EA-1。
- **资源要求**：示例 CPU 已可运行；ImageNet 级训练不是入门要求。

## DL-06 序列网络

- **前置**：DL-01…04。
- **目标**：理解 Embedding、RNN、BPTT、LSTM/GRU、seq2seq 及其长依赖与串行瓶颈。
- **为什么在这里学**：先建立序列状态视角，才能看清 Attention 改变了什么、没有改变什么。
- **指定材料**：必学 D2L [序列模型 9.1](https://zh.d2l.ai/chapter_recurrent-neural-networks/sequence.html)、[RNN 9.4](https://zh.d2l.ai/chapter_recurrent-neural-networks/rnn.html)、[LSTM 10.1](https://zh.d2l.ai/chapter_recurrent-neural-networks/lstm.html)；推荐 [GRU 10.2](https://zh.d2l.ai/chapter_recurrent-neural-networks/gru.html)。
- **学习动作**：写出隐藏状态递推和按时间展开的梯度；解释门控、teacher forcing 与变长 padding；Embedding 是查表表示，不等于语义保证。
- **最小实践**：在字符序列上实现 next-character 小 RNN，比较截断长度对 loss/速度的影响；观察长依赖失败。
- **完成标准**：能说明参数共享发生在时间维、BPTT 的成本与并行瓶颈。
- **卡住时**：回 DL-02 画展开图；梯度异常回 DL-04，先缩小序列和隐藏维。
- **下一步**：DL-07。
- **资源要求**：CPU 小序列；不需下载大语料。

## DL-07 Attention 与 Transformer

- **前置**：DL-01、DL-02、DL-06；PR-03。
- **目标**：理解 Q/K/V、scaled dot-product、位置编码、Mask、残差/Norm 和 Encoder/Decoder。
- **为什么在这里学**：把 Attention 从公式落到可检查的张量计算，再过渡到小 Transformer。
- **指定材料**：必学 [The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/)、D2L [Self-Attention 与位置编码](https://zh.d2l.ai/chapter_attention-mechanisms-and-transformers/self-attention-and-positional-encoding.html)、[Transformer](https://zh.d2l.ai/chapter_attention-mechanisms-and-transformers/transformer.html)；深入 [Attention Is All You Need](https://arxiv.org/abs/1706.03762)。
- **学习动作**：写出 `softmax(QK^T/sqrt(d_k))V` 的形状；区分配对相关性、权重与值聚合；解释 padding mask 与 causal mask，比较 RNN 的路径长度/并行性和注意力 pairwise 成本。
- **最小实践**：运行 `python examples/dl_foundations.py attention`，验证未来权重为 0 且与 PyTorch SDPA 一致；再实现一个带多头和位置编码的小前向模块。
- **完成标准**：能手算 2 token 示例、解释多头/位置/残差作用，并说明标准注意力随序列长的平方项成本。
- **卡住时**：回 PR-01 检查 transpose/softmax 维度，回 DL-02 做数值梯度；mask 用 `-inf` 前检查 dtype。
- **下一步**：DL-08 或 DL-09；随后进入 LLM/NLP、ViT/CLIP、Infra 的 KV Cache 桥接。
- **资源要求**：小实现 CPU；不以训练大语言模型作为完成条件。

## DL-08 其他主要模型家族

- **前置**：DL-01、DL-03；DL-07 仅 Transformer 对照需要。
- **目标**：定位 Autoencoder/VAE、GAN、Diffusion、GNN、SSM/Mamba 的输入、归纳偏置和学习目标。
- **为什么在这里学**：架构世界不止 CNN 与 Transformer，先会定位再决定深入。
- **指定材料**：必学 D2L [Autoencoder 简介可结合第4章网络表示](https://zh.d2l.ai/chapter_multilayer-perceptrons/index.html)与 [GAN](https://zh.d2l.ai/chapter_generative-adversarial-networks/gan.html)；推荐原始 [VAE](https://arxiv.org/abs/1312.6114)、[DDPM](https://arxiv.org/abs/2006.11239)、[GCN](https://arxiv.org/abs/1609.02907)、[Mamba](https://arxiv.org/abs/2312.00752)。Autoencoder 的 D2L 专章定位 **待核验**，不得据此声称存在专章。
- **学习动作**：比较重构/对抗/去噪/消息传递/选择性状态的信号与计算；区分 VAE 概率潜变量与普通 autoencoder。
- **最小实践**：任选一个家族做玩具级前向或图示，例如三节点消息传递、单步加噪/去噪目标；不要求同时实现五种。
- **完成标准**：能指出每族适用问题、训练信号和一个局限，并沿专题路径继续。
- **卡住时**：回 DL-01 写清输入输出；概率建模回 PR-05；图结构回 PR-03。
- **下一步**：DL-09；扩散/GNN/序列架构分别转对应地图专题。
- **资源要求**：默认纸笔+CPU；大生成模型仅作可选观察。

## DL-09 训练范式与公共出口

- **前置**：DL-03、DL-05…08 按所选范式。
- **目标**：区分监督、无监督、自监督、对比、迁移、预训练/微调、多任务和强化学习。
- **为什么在这里学**：避免把“Transformer”“监督”“NLP”误当同一层分类。
- **指定材料**：必学 D2L [Fine-tuning](https://zh.d2l.ai/chapter_computer-vision/fine-tuning.html)；推荐 [SimCLR](https://arxiv.org/abs/2002.05709)、[CLIP](https://arxiv.org/abs/2103.00020) 与 Sutton & Barto [RL 教材](http://incompleteideas.net/book/the-book-2nd.html)前几章。
- **学习动作**：为图像旋转预测、图文对比、指令微调、奖励优化分别写“数据/信号—架构—任务”；对比学习不是无标签数据的唯一自监督形式。
- **最小实践**：用同一预训练小模型做线性 probe 与全量微调二选一，固定划分比较可训练参数和指标。
- **完成标准**：能为新论文画出三轴定位，说明学习信号来源和迁移成本。
- **卡住时**：回 ML-00 任务定义、DL-03 训练闭环；RL 先补 MDP，不直接读 RLHF 框架。
- **下一步**：按[方向路径](../paths/README.md)进入 LLM、CV/VLM、RL、RAG、Infra、评测、数据或高效 AI。
- **资源要求**：概念部分 CPU；预训练复现不是毕业门槛。

## 毕业任务与故障回退

1. 从 DL-03 提交一个能独立运行的 MLP：数据/形状、训练/验证、checkpoint、seed 与结果说明齐全。
2. 从 DL-05 提交 CNN/MLP 对照：同划分与预算，讨论归纳偏置而非只抄准确率。
3. 从 DL-07 提交 Attention：手算小例子 + 代码 + causal mask 检查。
4. 用一页图说明 CNN（局部/共享）、RNN（顺序状态）、Transformer（内容相关全连接）的归纳偏置、并行性与序列成本。

 loss 不降先回 DL-03 小数据闭环；梯度不对回 DL-02；指标异常回 ML-03；部署慢不能凭架构名下结论，转 EA 同口径实测。
