# CPU 最小实践

这些脚本是学习动作的可运行起点，不是模型排行榜，也不代表新人试走已通过。数据来自 scikit-learn 自带小数据集或本地合成数据，运行不需要下载模型或 GPU。

## 环境与命令

在仓库根目录使用 Python 3.11+：

```bash
python -m venv .venv
# Windows: .venv/Scripts/python -m pip install -r examples/requirements.txt
# Linux/macOS: .venv/bin/python -m pip install -r examples/requirements.txt
```

以下 `python` 指该虚拟环境中的解释器：

```bash
python examples/ml_tree_ensemble.py
python examples/dl_foundations.py gradient
python examples/dl_foundations.py attention
python examples/dl_foundations.py mlp
python examples/dl_foundations.py cnn
```

所有示例默认 seed=42；ML 输出 fit/validation/holdout 数量且不触碰 holdout，DL 训练脚本使用单独的 train/validation。修改后先记录环境、命令和输出，再解释指标；不要通过反复使用测试集选择答案。

## 2026-10-27 维护者实跑

环境：Windows、Python 3.14.0、NumPy 2.3.4、scikit-learn 1.7.2、PyTorch 2.13.0+cpu、单线程 CPU。上述命令均实际执行；`gradient` 的 autograd/有限差分一致，`attention` 与 PyTorch SDPA 一致且未来权重为 0，MLP 从 loss 0.6422 降至 0.2798、验证准确率 0.94。

树/集成验证集结果（未使用 holdout）：tree 0.9386 accuracy / 0.9240 ROC-AUC；RF 0.9561 / 0.9838；AdaBoost 0.9649 / 0.9984；HistGB 0.9474 / 0.9895。一次结果不构成算法普遍排名。

CNN 对照在 sklearn digits 同划分、每个模型 30 个 full-batch epoch：CNN 690 参数、验证准确率 0.8867；MLP 4810 参数、0.9422。此配置下 MLP 更高，恰好说明小数据/小预算不能从架构名字推优劣；不是“CNN 更强”或“MLP 更强”的普遍结论。

首次运行 MLP 曾因训练/验证张量顺序错误失败，已修正并重新运行。脚本通过不等于教学目标完成，更不代表其他版本/操作系统已验证。
