# 异常检测 (Anomaly Detection) 实战资源 (2026 Checklist)

> [!TIP]
> **Indie Hacker Insight**: 在 AI 时代，异常检测已从简单的统计规则进化为深度表征学习。
> - **应用场景**：不仅限于反欺诈，在 RAG 系统中检测“离群请求”、在运维中检测“指标突变”都是刚需。
> - **模型选择**：对于表格数据，**Isolation Forest** 依然强劲；对于时间序列，**LSTM/Transformer** 是主流。
> - **可解释性**：在商业决策中，知道“为什么是异常”比“发现异常”更重要，优先关注带 Explainable AI 能力的工具。

---

## 📚 权威指南与书籍 (Knowledge Base)

- [ ] [**Outlier Analysis (Charu Aggarwal)**](https://link.springer.com/book/9783319475776) - 行业圣经，涵盖了大部分经典算法。
- [ ] [**Deep Learning for Anomaly Detection (Review 2024)**](https://arxiv.org/abs/2007.02500) - **[必读]** 梳理了深度学习在异常检测中的前沿应用。
- [ ] [**Anomaly Detection vs. Supervised Learning**](https://www.coursera.org/learn/machine-learning/lecture/Rkc5x/anomaly-detection-vs-supervised-learning) - 吴恩达讲解两者在样本量级和目标定义上的本质差异。

---

## 🛠️ 核心工具箱与库 (Toolkits)

- [ ] [**PyOD (Python Outlier Detection)**](https://github.com/yzhao062/PyOD) - **[首选]** 最全面的 Python 工具包，包含 40+ 种检测算法。
- [ ] [**Scikit-learn (Novelty Detection)**](https://scikit-learn.org/stable/modules/outlier_detection.html) - 内置了 LOF、Isolation Forest 等开箱即用的经典模型。
- [ ] [**Telemanom**](https://github.com/khundman/telemanom) - 针对多变量时间序列的深度学习（LSTM）检测框架。
- [ ] [**AnomalyDetection (Twitter)**](https://github.com/twitter/AnomalyDetection) - 经典的 R 语言库，擅长在季节性和趋势背景下定位异常。
- [ ] [**DeepADoTS**](https://github.com/KDD-OpenSource/DeepADoTS) - 针对深度异常检测的时间序列基准测试框架。

---

## 🏗️ 关键算法与论文 (Key Algorithms)

- [ ] [**Isolation Forest (IForest)**](https://cs.nju.edu.cn/zhouzh/zhouzh.files/publication/icdm08b.pdf) - 简单高效，适合大规模高维数据。
- [ ] [**Local Outlier Factor (LOF)**](http://www.dbs.ifi.lmu.de/Publikationen/Papers/LOF.pdf) - 经典的基于密度的局部异常检测算法。
- [ ] [**AutoEncoder Ensembles**](http://saketsathe.net/downloads/autoencode.pdf) - 利用深度学习重构误差来识别离群点。
- [ ] [**MIDAS**](https://github.com/bhatiasiddharth/MIDAS) - 针对流式数据和图结构异常的高效检测方案。

---

## 💡 选型建议
1. **构建 B 端风控系统**：首选 **PyOD** 集成多种模型进行投票。
2. **实时运维指标监控**：选 **Telemanom** 或 **Twitter AnomalyDetection**。
3. **极小样本且无标签数据**：优先尝试 **Isolation Forest** 或 **One-Class SVM**。
4. **追求高透明度与合规性**：使用带 **SHAP/LIME** 解释性的线性模型。
