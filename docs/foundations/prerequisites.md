# 公共先修：只补后续真正用到的地基

入口：能使用命令行，或愿意按教程学习基本命令。出口：完成下面的环境自检，并能进入 ML-00。无需先修完整门数学课；遇到具体概念再回补。

资源索引见 [awesome-ai · Classical ML](https://github.com/CUMT-Alethic-Insight-Lab/awesome-ai#classical-machine-learning) 与 [Deep Learning Foundations](https://github.com/CUMT-Alethic-Insight-Lab/awesome-ai#deep-learning-foundations)。

## PR-00 命令行、Python 与可隔离环境

- **前置**：会创建文件夹、解压文件；社外读者不需要安装招新机试包。
- **目标**：能创建虚拟环境、安装锁定范围依赖、运行脚本并看到版本。
- **为什么在这里学**：后续所有结果都要能复现，不能依赖“我电脑上刚好装过”。
- **指定材料**：必学 [Python Tutorial 1–5](https://docs.python.org/3/tutorial/)；推荐 [venv](https://docs.python.org/3/library/venv.html)。
- **学习动作**：解释解释器、模块、函数、列表/字典、异常；在终端运行而非只粘贴到聊天窗口。
- **最小实践**：创建环境后执行 `python -m pip install -r examples/requirements.txt`，再运行 `python -c "import sys,numpy,sklearn,torch; print(sys.version); print(numpy.__version__,sklearn.__version__,torch.__version__)"`。
- **完成标准**：能说明当前 `python` 属于哪个环境，重新打开终端后仍能复现。
- **卡住时**：Windows 用 `py -m venv .venv`，激活脚本执行受阻时直接调用 `.venv/Scripts/python`；不要关闭系统安全策略。
- **下一步**：PR-01。
- **资源要求**：普通电脑；无需 GPU。安装包需联网，运行本地示例不需下载模型。

## PR-01 NumPy、形状与最小数据操作

- **前置**：PR-00。
- **目标**：能区分数组、矩阵乘法、逐元素运算、广播和视图/副本。
- **为什么在这里学**：ML 特征矩阵、DL 张量和 Attention 都以形状为核心。
- **指定材料**：必学 [NumPy absolute beginners 的 array、shape、indexing、broadcasting 小节](https://numpy.org/doc/stable/user/absolute_beginners.html)；推荐 [NumPy quickstart](https://numpy.org/doc/stable/user/quickstart.html)。
- **学习动作**：手算 `(2,3)@(3,4)` 的形状；对 `(batch,features)` 做按行归一化；打印每步形状。
- **最小实践**：取一个 `(6,2)` 数组，算每行均值、两两欧氏距离；故意触发一次维度不匹配并读错误。
- **完成标准**：不靠猜广播规则；能解释 `X @ w`、`X * w`、`keepdims=True`。
- **卡住时**：回 PR-00 检查数组嵌套与 dtype；用 `assert X.shape == (6,2)` 尽早暴露问题。
- **下一步**：PR-02 可并行 PR-03…05。
- **资源要求**：CPU，NumPy。

## PR-02 Git、文件与实验记录

- **前置**：PR-00。
- **目标**：能保存脚本、输入说明、依赖、命令与结果，不覆盖原始数据。
- **为什么在这里学**：可复现不是最后补 README，而是实验过程的一部分。
- **指定材料**：必学本仓 [分支、提交与 PR](../github/branch-commit-pr.md)、[首次贡献实操](../github/walkthrough.md)；推荐 [Pro Git 2.1–2.3](https://git-scm.com/book/en/v2/Git-Basics-Getting-a-Git-Repository)。
- **学习动作**：新建分支，写一次有意义的提交；用 diff 检查没有数据/密钥。
- **最小实践**：建立 `data/raw`、`data/processed`、`reports` 三目录约定，原始输入只读；结果记录 seed 与命令。
- **完成标准**：另一人按 README 能找到入口、运行同一条命令。
- **卡住时**：按[自救指南](../github/rescue.md)处理，不在公共主分支强制推送。
- **下一步**：ML-00。
- **资源要求**：Git 与文本编辑器。

## PR-03 线性代数：表示与变换

- **前置**：PR-01。
- **目标**：理解向量、矩阵、内积、范数、线性独立和投影的直观意义。
- **为什么在这里学**：线性回归、PCA、Embedding、Attention 都复用这些对象。
- **指定材料**：必学 [Mathematics for Machine Learning 第2章 Linear Algebra、3.1–3.4 与3.6](https://mml-book.github.io/)；深入第4章 Matrix Decompositions。
- **学习动作**：手算二维向量内积和投影；把一次仿射变换写成 `XW+b`；解释奇异矩阵为何不能求逆。
- **最小实践**：对一个二维数据集做去均值，再用 NumPy SVD 验证第一主方向。
- **完成标准**：能把矩阵运算翻译成“样本×特征”，而非只会调用 `inv`。
- **卡住时**：回 PR-01 画形状；先掌握第2、3章再进第4章。
- **下一步**：ML-01、ML-02。
- **资源要求**：纸笔+CPU。

## PR-04 微积分与优化：局部变化

- **前置**：PR-01；PR-03 的向量基础。
- **目标**：理解导数、偏导、梯度、链式法则和梯度下降的学习率。
- **为什么在这里学**：反向传播不是框架魔法，是链式法则的系统应用。
- **指定材料**：必学 MML 第5章 Vector Calculus（尤其5.1–5.5）、第7章7.1；深入7.2–7.3。
- **学习动作**：手算 `f(x)=(x^T w-y)^2` 对 `w` 的梯度；比较过大/过小学习率。
- **最小实践**：对一元二次函数运行20步梯度下降并记录轨迹。
- **完成标准**：能解释梯度方向、局部最小值与数值梯度校验。
- **卡住时**：先标量再向量；在 DL-02 用有限差分验证，不靠背矩阵公式。
- **下一步**：ML-01、DL-02。
- **资源要求**：纸笔+NumPy。

## PR-05 概率统计：不确定性与样本

- **前置**：PR-01。
- **目标**：理解条件概率、期望、方差、常用分布、抽样与置信不确定性的基本含义。
- **为什么在这里学**：损失、交叉熵、指标方差与数据偏差都来自这里。
- **指定材料**：必学 MML 第6章6.1–6.4；推荐 [ISLP 第2章](https://www.statlearning.com/)关于统计学习与评估的引言。
- **学习动作**：区分 `P(y|x)` 与 `P(x|y)`；用抽样实验观察均值随样本量波动。
- **最小实践**：同一总体的不同种子抽样，比较均值/分类指标并记录分散程度。
- **完成标准**：不把一次小样本指标当稳定事实；能解释期望与方差。
- **卡住时**：先离散随机变量，再连续密度；不要把概率密度当概率。
- **下一步**：ML-01、ML-03。
- **资源要求**：纸笔+NumPy。

## 公共出口

完成 PR-00…02，且能通过 PR-03…05 的基础自检后进入 [ML-00](classical-ml.md#ml-00-任务与数据)。数学仍是薄弱环节可同步回补，但不要跳过 ML-01 与 ML-03 的解释任务。
