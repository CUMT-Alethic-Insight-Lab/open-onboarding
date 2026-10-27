# 经典机器学习：从数据到可信实验

**入口**：PR-00…05；**出口**：ML-08 可复现实验；**状态**：内容完成，待试走。核心材料是 [ISLP](https://www.statlearning.com/)（2023 Python 版）与 [INRIA scikit-learn MOOC](https://inria.github.io/scikit-learn-mooc/)，延伸资源在 [awesome-ai](https://github.com/CUMT-Alethic-Insight-Lab/awesome-ai#classical-machine-learning)。

ML 并未被深度学习淘汰：小样本、表格数据、有限算力和需要审计特征/预测时，它常是更合适且必须保留的基线。这里的“会”是能解释实验证据，不是会调用模型类。

## ML-00 任务与数据

- **前置**：PR-00…02。
- **目标**：区分样本/特征/标签、回归/分类/聚类，以及 train/validation/test 的用途。
- **为什么在这里学**：目标或边界写错，再复杂的模型也只是精确地回答错问题。
- **指定材料**：必学 ISLP 第2章、MOOC [Tabular data exploration](https://inria.github.io/scikit-learn-mooc/python_scripts/01_tabular_data_exploration.html)；推荐 [Cross-validation: time and grouping](https://inria.github.io/scikit-learn-mooc/python_scripts/cross_validation_time.html)。
- **学习动作**：把“预测成绩/识别垃圾邮件/给用户分组”分别写成输入、输出、观测单位；解释数据泄漏、选择偏差和时间穿越。
- **最小实践**：选一个小数据表，先拆分再探索；写一句预测目标与不能使用未来信息的约束。
- **完成标准**：测试集没有参与筛选特征、调参或选模型；同一人/实体的多条记录不会被误当独立样本。
- **卡住时**：回 PR-02 检查数据来源；时间/组相关数据转 DE-05，不强行随机拆。
- **下一步**：ML-01。
- **资源要求**：CPU，合法小数据集。

## ML-01 数学与统计直觉

- **前置**：PR-03…05。
- **目标**：能把向量、梯度、概率、期望/方差连接到模型目标与实验波动。
- **为什么在这里学**：这是读懂损失和评价指标的最小数学集合，不是数学系预修课。
- **指定材料**：必学 MML 第2、5、6章的 PR 指定小节；推荐 ISLP 第2章的 bias-variance 讨论。
- **学习动作**：解释均方误差对应连续残差，交叉熵对应类别概率的负对数似然；说明为何准确率会掩盖类别不平衡。
- **最小实践**：用三个样本手算 MSE 与二分类交叉熵；改变一个高置信错误预测，观察后者变化。
- **完成标准**：能写出任务、输出分布与损失的对应关系，不把 sigmoid 输出默认当已校准概率。
- **卡住时**：回 PR-04 做标量梯度、PR-05 做离散概率；不必先学测度论。
- **下一步**：ML-02。
- **资源要求**：纸笔+NumPy。

## ML-02 线性与广义线性模型

- **前置**：ML-00、ML-01。
- **目标**：理解最小二乘、逻辑回归、正则化和梯度下降。
- **为什么在这里学**：简单模型提供可解释基线，也是 MLP 的直接前身。
- **指定材料**：必学 ISLP 第3、4、6章及对应 Lab；MOOC [手写线性回归](https://inria.github.io/scikit-learn-mooc/python_scripts/linear_regression_without_sklearn.html)、[逻辑回归](https://inria.github.io/scikit-learn-mooc/python_scripts/logistic_regression.html)、[正则化](https://inria.github.io/scikit-learn-mooc/python_scripts/linear_models_regularization.html)。
- **学习动作**：从残差平方和到闭式解；从 log-odds 到 sigmoid；比较 L1/L2 对系数的影响。
- **最小实践**：NumPy 手写线性或逻辑回归之一，与 sklearn 在同划分上比较系数和指标；数值特征缩放只拟合训练集。
- **完成标准**：能解释优化目标、系数与正则强度，不把分类阈值 0.5 当永远最佳。
- **卡住时**：回 PR-03 检查矩阵形状、PR-04 检查梯度；梯度爆炸先查缩放和学习率。
- **下一步**：ML-03。
- **资源要求**：CPU，NumPy/sklearn。

## ML-03 泛化与评估

- **前置**：ML-00、ML-02。
- **目标**：理解欠拟合/过拟合、bias-variance、交叉验证、PR/ROC、校准与类别不平衡。
- **为什么在这里学**：模型名字不能替代对泛化证据的审查。
- **指定材料**：必学 ISLP 第5章；MOOC [train/test 与交叉验证](https://inria.github.io/scikit-learn-mooc/python_scripts/cross_validation_train_test.html)、[bias vs variance](https://inria.github.io/scikit-learn-mooc/overfit/bias_vs_variance_slides.html)、[分类指标](https://inria.github.io/scikit-learn-mooc/python_scripts/metrics_classification.html)；推荐 [sklearn calibration](https://scikit-learn.org/stable/modules/calibration.html)。
- **学习动作**：区分模型偏差、估计方差与不可约误差；画训练/验证曲线；从混淆矩阵推 precision、recall、PR-AUC、ROC-AUC。
- **最小实践**：做分层 K 折交叉验证，报告每折和均值/离散程度；在偏斜数据上比较 accuracy、PR 与 ROC，并画可靠性图。
- **完成标准**：能按漏报/误报成本选指标；调参时使用验证或嵌套 CV，测试集只作最后评估。
- **卡住时**：回 ML-00 查泄漏与拆分；小数据高波动时增加重复/置信说明，不挑最好的一折。
- **下一步**：ML-04。
- **资源要求**：CPU。注意经典 bias-variance 图不是所有深网现象的充分解释。

## ML-04 决策树

- **前置**：ML-02、ML-03。
- **目标**：理解 CART 的递归划分、分类/回归准则、树深与剪枝。
- **为什么在这里学**：树揭示非线性边界与模型容量，是随机森林和 Boosting 的基学习器。
- **指定材料**：必学 ISLP 第8章8.1；MOOC [树分类](https://inria.github.io/scikit-learn-mooc/python_scripts/trees_classification.html)、[树超参数](https://inria.github.io/scikit-learn-mooc/python_scripts/trees_hyperparameters.html)；推荐 [sklearn tree guide](https://scikit-learn.org/stable/modules/tree.html)。
- **学习动作**：手算一个划分的基尼/熵或平方误差下降；解释 axis-aligned 边界和可解释性的局限。
- **最小实践**：同数据比较 max_depth=1,2,3,5,None 的训练/验证曲线，保存一棵小树文本图。
- **完成标准**：能根据曲线选受约束树，解释高方差与叶节点样本过少。
- **卡住时**：回 ML-03 判断过拟合；特征尺度通常不是树的重点，先查划分与叶子数。
- **下一步**：ML-05。
- **资源要求**：CPU。

## ML-05 集成学习

- **前置**：ML-03、ML-04。
- **目标**：区分 Bagging、随机森林、AdaBoost、Gradient Boosting 的训练机制与误差来源。
- **为什么在这里学**：它们都是“多个模型”，却不是同一种重采样、重加权或残差拟合。
- **指定材料**：必学 ISLP 第8章8.2；MOOC [Bagging/随机森林](https://inria.github.io/scikit-learn-mooc/python_scripts/ensemble_random_forest.html)、[AdaBoost](https://inria.github.io/scikit-learn-mooc/python_scripts/ensemble_adaboost.html)、[Gradient Boosting](https://inria.github.io/scikit-learn-mooc/python_scripts/ensemble_gradient_boosting.html)。
- **学习动作**：Bagging 对有放同样本并行拟合后平均/投票以降方差；随机森林另在划分时随机选特征子集去相关；AdaBoost 顺序提高错分样本权重并给基学习器定权；GBDT 以加法模型顺序拟合当前损失的负梯度（平方损失时可对应残差）。
- **最小实践**：运行 `python examples/ml_tree_ensemble.py`，同一 fit/validation 对比四类模型；解读 ROC-AUC 与 accuracy 不一致，保留未触碰的 holdout。
- **完成标准**：能解释样本/特征随机性、基学习器、损失与串并行关系；不会把 AdaBoost 与 GBDT 都描述成“拟合残差”。
- **卡住时**：回 ML-04 检查单树；结果异常先打印划分尺寸/类别，再查随机种子，不调 holdout。
- **下一步**：ML-06；可转高效 AI 的紧凑模型对照。
- **资源要求**：CPU。XGBoost/LightGBM/CatBoost 属工程深入，不要求新手同时学三套 API。

## ML-06 其他监督模型

- **前置**：ML-02…04。
- **目标**：理解 kNN、朴素贝叶斯、SVM/核技巧与特征工程的适用条件。
- **为什么在这里学**：不同归纳偏置决定何时简单模型胜过树或神经网络。
- **指定材料**：必学 ISLP 第9章、MOOC [非线性特征工程](https://inria.github.io/scikit-learn-mooc/python_scripts/linear_regression_non_linear_link.html)；推荐 sklearn [neighbors](https://scikit-learn.org/stable/modules/neighbors.html)、[naive Bayes](https://scikit-learn.org/stable/modules/naive_bayes.html)、[SVM](https://scikit-learn.org/stable/modules/svm.html)。
- **学习动作**：比较距离/条件独立/最大间隔假设；解释核如何把内积换成非线性相似度。
- **最小实践**：在同一小数据集上比较 kNN 与 RBF-SVM（或朴素贝叶斯），把缩放放进 Pipeline；说明为何选这两类。
- **完成标准**：能按样本规模、维度、特征类型和解释需求选模型，并说明比较局限。
- **卡住时**：回 ML-02 查缩放/特征，回 ML-03 查指标；不要仅靠增加 C 和 gamma 追分。
- **下一步**：ML-07。
- **资源要求**：CPU；大型核 SVM 不作为低资源必做。

## ML-07 无监督与降维

- **前置**：ML-01、ML-03。
- **目标**：理解 K-Means、层次聚类、GMM、PCA 和异常检测的任务边界。
- **为什么在这里学**：没有标签时仍可做结构探索，但“分成几类”不等于发现真实类别。
- **指定材料**：必学 ISLP 第12章；MOOC [K-Means](https://inria.github.io/scikit-learn-mooc/python_scripts/clustering_kmeans.html)、[聚类监督指标](https://inria.github.io/scikit-learn-mooc/python_scripts/clustering_supervised_metrics.html)、[PCA 预处理](https://inria.github.io/scikit-learn-mooc/python_scripts/dimred_preprocessing.html)。
- **学习动作**：解释距离/尺度、初始化和 k；比较硬分配与混合模型的软分配；解释 PCA 方差投影。
- **最小实践**：二维数据聚类可视化，改变尺度与 k；用标签只做事后外部评估，不能用标签训练聚类。
- **完成标准**：明确聚类编号可置换、结构可能来自缩放/异常点；PCA 不保证保留类别可分性。
- **卡住时**：回 PR-03 的 SVD 与 ML-06 的距离；先可视化再调算法。
- **下一步**：ML-08。
- **资源要求**：CPU。

## ML-08 稳健实验与毕业任务

- **前置**：ML-00…07。
- **目标**：交付防泄漏 Pipeline，含基线、消融、多种子与不确定度说明。
- **为什么在这里学**：一次高分不是可复现能力，稳健流程才可迁移到 DL 和专题。
- **指定材料**：必学 MOOC [数值 Pipeline](https://inria.github.io/scikit-learn-mooc/python_scripts/02_numerical_pipeline_hands_on.html)、[ColumnTransformer](https://inria.github.io/scikit-learn-mooc/python_scripts/03_categorical_pipeline_column_transformer.html)、[嵌套 CV](https://inria.github.io/scikit-learn-mooc/python_scripts/cross_validation_nested.html)；推荐 sklearn [Pipeline](https://scikit-learn.org/stable/modules/compose.html)。
- **学习动作**：先 Majority/线性基线，再只改一个因素；预处理在每折内拟合；记录代码版本、数据 hash、配置与指标分布。
- **最小实践**：提交一个脚本或 notebook：合理拆分 → Pipeline → CV → 最终一次测试 → 误差分析；至少三个 seed 或重复 CV，并解释随机性来源。
- **完成标准**：从干净环境一条命令复现；能指出主要失败样例、一个消融结果与结果不可信的可能原因。
- **卡住时**：逐项回 ML-00 数据、ML-03 评估、PR-00 环境；先缩成最小失败样例，不靠增加模型复杂度逃避。
- **下一步**：[DL-00](neural-networks.md#dl-00-由线性分类器到感知机)，或按[方向路径](../paths/README.md)转数据工程/评测。
- **资源要求**：CPU；完整任务不得依赖付费服务或 GPU。

## 易错诊断表

| 现象 | 优先检查 | 不要先做什么 |
| --- | --- | --- |
| 训练与验证都差 | 目标、特征、基线、欠拟合 | 盲目加深树/网络 |
| 训练好验证差 | 泄漏、分布差异、容量、样本量 | 继续看测试集调参 |
| CV 分数忽高忽低 | 小样本、分组、时间、类别偏斜 | 只报最好一次 |
| 指标高但业务无用 | 阈值、成本、校准、选择偏差 | 只换更复杂模型 |
| 集成不如单树 | 数据划分、预算、参数与实现差异 | 宣称某算法永远更强 |
