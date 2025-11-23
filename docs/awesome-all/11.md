# 异常检测 (Anomaly Detection)

异常检测 (又名 Outlier Detection) 是一个重要但非常有挑战性的领域，目标是找到数据中偏离主要分布的案例。它在许多领域中有广泛应用，如：

- **信用卡诈骗检测**
- **网络入侵检测**
- **机械故障检测**

## 1. 书籍 & 教程

### 1.1 书籍

- **[Outlier Analysis](https://www.springer.com/gp/book/9781461463955)**  
  作者：Charu Aggarwal  
  经典异常检测教科书，涵盖了大部分相关算法与应用，是异常检测领域人士的必读书籍。

- **[Outlier Ensembles: An Introduction](https://www.springer.com/gp/book/9783319547640)**  
  作者：Charu Aggarwal 和 Saket Sathe  
  权威的集成异常检测教科书，介绍了多种集成方法及其应用。

- **[Data Mining: Concepts and Techniques (3rd Edition)](https://www.elsevier.com/books/data-mining-concepts-and-techniques/han/978-0-12-381479-1)**  
  作者：韩家炜 (Jiawei Han)、Micheline Kamber 和 Jian Pei  
  第十二章专门讨论了异常检测技术，适合数据挖掘学习者阅读。

### 1.2 教程

| Tutorial Title                                | Venue        | Year | Ref                     | Materials                                                                                       |
|-----------------------------------------------|--------------|------|-------------------------|-------------------------------------------------------------------------------------------------|
| Outlier detection techniques                  | ACM SIGKDD   | 2010 | [Kriegel 2010](https://imada.sdu.dk/~zimek/publications/KDD2010/kdd10-outlier-tutorial.pdf)  | [PDF](https://imada.sdu.dk/~zimek/publications/KDD2010/kdd10-outlier-tutorial.pdf)                |
| Anomaly Detection: A Tutorial                 | ICDM         | 2011 | [Chawla 2011](http://webdocs.cs.ualberta.ca/~icdm2011/downloads/ICDM2011_anomaly_detection_tutorial.pdf) | [PDF](http://webdocs.cs.ualberta.ca/~icdm2011/downloads/ICDM2011_anomaly_detection_tutorial.pdf) |
| Data mining for anomaly detection             | PKDD         | 2008 | [Lazarevic 2008](http://videolectures.net/ecmlpkdd08_lazarevic_dmfa/) | [Video](http://videolectures.net/ecmlpkdd08_lazarevic_dmfa/)                                    |

## 2. 课程 & 视频

### Coursera

- **[Introduction to Anomaly Detection by IBM](https://www.coursera.org/learn/ai/lecture/ASPv0/introduction-to-anomaly-detection)**  
  本课程介绍了异常检测的基础知识。

- **[Real-Time Cyber Threat Detection and Mitigation](https://www.coursera.org/learn/real-time-cyber-threat-detection)**  
  涵盖了一部分与实时网络威胁检测和缓解相关的异常检测技术。

- **[Machine Learning by Andrew Ng](https://www.coursera.org/learn/machine-learning)**  
  本课程部分内容涉及异常检测：
  - **[Anomaly Detection vs. Supervised Learning](https://www.coursera.org/learn/machine-learning/lecture/Rkc5x/anomaly-detection-vs-supervised-learning)**
  - **[Developing and Evaluating an Anomaly Detection System](https://www.coursera.org/learn/machine-learning/lecture/Mwrni/developing-and-evaluating-an-anomaly-detection-system)**

### Udemy

- **[Outlier Detection Algorithms in Data Mining and Data Science](https://www.udemy.com/outlier-detection-techniques/)**  
  讲解了数据挖掘和数据科学中的异常值检测算法。

### Stanford

- **[Data Mining for Cyber Security](http://web.stanford.edu/class/cs259d/)**  
  这门课程涵盖了与网络安全相关的异常检测技术。

## 工具箱与数据集

### 3.1 多变量数据异常检测
多变量数据中的异常检测是识别不同于常规模式的异常数据点的技术。以下是几种常用的工具和库：

- **Python**: [PyOD - Python Outlier Detection](https://github.com/yzhao062/PyOD)  
  PyOD 是一个综合且可扩展的 Python 工具包，用于检测多变量数据中的异常。它包括 20 多种检测算法，涵盖了深度学习模型和异常检测集成方法。

- **Python**: [Scikit-learn Novelty and Outlier Detection](http://scikit-learn.org/stable/modules/outlier_detection.html)  
  Scikit-learn 提供了一些常见的算法，如 LOF、Isolation Forest 和 One-class SVM，用于检测异常数据。

- **Java**: [ELKI](https://elki-project.github.io/)  
  ELKI 是一个开源的数据挖掘软件，专注于算法研究，特别是在无监督方法中的聚类分析和异常检测。

- **Java**: [RapidMiner Anomaly Detection Extension](https://github.com/Markus-Go/rapidminer-anomalydetection)  
  这个扩展包含了最著名的无监督异常检测算法，能够为数据集中的每一行分配异常分数，帮助识别与正常数据显著不同的数据。

- **R**: [outliers 包](https://cran.r-project.org/web/packages/outliers/index.html)  
  R 语言的 outliers 包包含了一些常用的异常值检测方法。

- **Matlab**: [Anomaly Detection Toolbox](http://dsmi-lab-ntust.github.io/AnomalyDetectionToolbox/)  
  这是一个 Matlab 平台的工具包，包含了多个流行的异常检测算法。

### 3.2 时间序列异常检测
时间序列数据的异常检测涉及对数据随时间变化的异常值进行检测。以下是一些适用于时间序列的工具：

- **Python**: [datastream.io](https://github.com/MentatInnovations/datastream.io)  
  一个开源框架，用于使用 Python、Elasticsearch 和 Kibana 实现实时异常检测。

- **Python**: [skyline](https://github.com/earthgecko/skyline)  
  一个近实时的异常检测系统，适用于时间序列数据。

- **Python**: [banpei](https://github.com/tsurubee/banpei)  
  一个用于异常检测的 Python 包，支持时间序列数据的检测。

- **Python**: [telemanom](https://github.com/khundman/telemanom)  
  一个基于 LSTM 的框架，用于检测多变量时间序列数据中的异常。

- **Python**: [DeepADoTS](https://github.com/KDD-OpenSource/DeepADoTS)  
  一个基准测试框架，用于评估多种深度学习方法在时间序列异常检测中的表现。

- **R**: [AnomalyDetection](https://github.com/twitter/AnomalyDetection)  
  一个由 Twitter 提供的开源 R 包，能够在季节性和趋势背景下进行强健的异常检测。

### 3.3 数据集
以下是一些常用的异常检测数据集，供研究人员和开发者使用：

- **ELKI Outlier Datasets**: [ELKI数据集](https://elki-project.github.io/datasets/outlier)

- **Outlier Detection DataSets (ODDS)**: [ODDS数据集](http://odds.cs.stonybrook.edu/#table1)

- **Unsupervised Anomaly Detection Dataverse**: [无监督异常检测数据集](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/OPQMVF)

- **Anomaly Detection Meta-Analysis Benchmarks**: [异常检测基准数据集](https://ir.library.oregonstate.edu/concern/datasets/47429f155)

---

通过这些工具和数据集，用户可以实现高效的异常检测和分析，适用于多种数据类型和场景。

以下是更新后的内容，以便更易于理解，并去除了过时和低质量的内容：

# 4. 论文

## 4.1 概述与调查论文
这些论文按出版年份排序：

| 论文标题                                                                                                      | 发表期刊              | 年份  | 引用                  | 资料                                                                                          |
|-----------------------------------------------------------------------------------------------------------|--------------------|------|----------------------|----------------------------------------------------------------------------------------------|
| Outlier Detection Methodologies: A Survey                                                                    | ARTIF INTELL REV     | 2004 | [Hodge2004A]          | [PDF](https://www-users.cs.york.ac.uk/vicky/myPapers/Hodge+Austin_OutlierDetection_AIRE381.pdf) |
| A Survey on Anomaly Detection                                                                                 | CSUR                | 2009 | [Chandola2009Anomaly] | [PDF](https://www.vs.inf.ethz.ch/edu/HS2011/CPS/papers/chandola09_anomaly-detection-survey.pdf) |
| A Comparative Evaluation of Unsupervised Anomaly Detection Algorithms                                          | PLOS ONE            | 2016 | [Goldstein2016A]      | [PDF](http://journals.plos.org/plosone/article/file?id=10.1371/journal.pone.0152173&type=printable) |
| Progress in Outlier Detection Techniques: A Survey                                                           | IEEE Access         | 2019 | [Wang2019Progress]    | [PDF](https://ieeexplore.ieee.org/iel7/6287639/8600701/08786096.pdf)                           |
| Deep Learning for Anomaly Detection: A Review                                                                | CSUR                | 2021 | [Pang2020Deep]        | [PDF](https://arxiv.org/pdf/2007.02500.pdf)                                                    |
| A Unified Survey on Anomaly, Novelty, Open-Set, and Out-of-Distribution Detection: Solutions and Challenges    | Preprint            | 2021 | [Salehi2021A]         | [PDF](https://arxiv.org/pdf/2110.14051.pdf)                                                    |

## 4.2 关键算法
以下是一些常用的异常检测算法，均可以通过 [Python Outlier Detection (PyOD)](https://github.com/yzhao062/pyod) 实现。

| 缩写   | 论文标题                                                                                                  | 发表期刊            | 年份  | 引用                  | 资料                                                                                          |
|------|-------------------------------------------------------------------------------------------------------|------------------|------|----------------------|----------------------------------------------------------------------------------------------|
| kNN  | Efficient algorithms for mining outliers from large data sets                                              | ACM SIGMOD Record  | 2000 | [Ramaswamy2000Efficient] | [PDF](https://webdocs.cs.ualberta.ca/~zaiane/pub/check/ramaswamy.pdf)                            |
| LOF  | LOF: Identifying density-based local outliers                                                            | ACM SIGMOD Record  | 2000 | [Breunig2000LOF]        | [PDF](http://www.dbs.ifi.lmu.de/Publikationen/Papers/LOF.pdf)                                  |
| IForest | Isolation Forest                                                                                         | ICDM               | 2008 | [Liu2008Isolation]     | [PDF](https://cs.nju.edu.cn/zhouzh/zhouzh.files/publication/icdm08b.pdf)                       |
| OCSVM | Estimating the support of a high-dimensional distribution                                                 | Neural Computation  | 2001 | [Scholkopf2001Estimating] | [PDF](http://users.cecs.anu.edu.au/~williams/papers/P132.pdf)                                  |
| AutoEncoder Ensemble | Outlier detection with autoencoder ensembles                                                   | SDM                | 2017 | [Chen2017Outlier]      | [PDF](http://saketsathe.net/downloads/autoencode.pdf)                                          |

## 4.3 图与网络异常检测
以下是与图和网络相关的异常检测研究：

| 论文标题                                                                                                       | 发表期刊              | 年份  | 引用                  | 资料                                                                                          |
|------------------------------------------------------------------------------------------------------------|--------------------|------|----------------------|----------------------------------------------------------------------------------------------|
| Graph-based Anomaly Detection: A Survey                                                                       | DMKD                | 2015 | [Akoglu2015Graph]     | [PDF](https://arxiv.org/pdf/1404.4679.pdf)                                                      |
| Anomaly Detection in Dynamic Networks: A Survey                                                               | WIREs Computational Statistic | 2015 | [Ranshous2015Anomaly] | [PDF](https://onlinelibrary.wiley.com/doi/pdf/10.1002/wics.1347)                               |
| A Comprehensive Survey on Graph Anomaly Detection with Deep Learning                                          | TKDE                | 2021 | [Ma2021A]             | [PDF](https://arxiv.org/pdf/2106.07178.pdf)                                                    |

## 4.4 时间序列异常检测
以下是时间序列数据的异常检测研究：

| 论文标题                                                                                                       | 发表期刊            | 年份  | 引用                  | 资料                                                                                          |
|------------------------------------------------------------------------------------------------------------|--------------------|------|----------------------|----------------------------------------------------------------------------------------------|
| Outlier Detection for Temporal Data: A Survey                                                                  | TKDE                | 2014 | [Gupta2014Outlier]    | [PDF](https://www.microsoft.com/en-us/research/wp-content/uploads/2014/01/gupta14_tkde.pdf)     |
| Detecting Spacecraft Anomalies Using LSTMs and Nonparametric Dynamic Thresholding                               | KDD                 | 2018 | [Hundman2018Detecting] | [PDF](https://arxiv.org/pdf/1802.04431.pdf)                                                    |
| Time-Series Anomaly Detection Service at Microsoft                                                             | KDD                 | 2019 | [Ren2019Time]         | [PDF](https://arxiv.org/pdf/1906.03821.pdf)                                                    |
| Revisiting Time Series Outlier Detection: Definitions and Benchmarks                                          | NeurIPS             | 2021 | [Lai2021Revisiting]   | [PDF](https://openreview.net/pdf?id=r8IvOsnHchr)                                               |

## 4.5 特征选择与异常检测
以下是与异常检测中特征选择相关的研究：

| 论文标题                                                                                                       | 发表期刊            | 年份  | 引用                  | 资料                                                                                          |
|------------------------------------------------------------------------------------------------------------|--------------------|------|----------------------|----------------------------------------------------------------------------------------------|
| Unsupervised Feature Selection for Outlier Detection by Modelling Hierarchical Value-Feature Couplings         | ICDM                | 2016 | [Pang2016Unsupervised] | [PDF](https://opus.lib.uts.edu.au/bitstream/10453/107356/4/DSFS_ICDM2016.pdf)                  |
| Learning Homophily Couplings from Non-IID Data for Joint Feature Selection and Noise-Resilient Outlier Detection | IJCAI               | 2017 | [Pang2017Learning]     | [PDF](https://www.ijcai.org/proceedings/2017/0360.pdf)                                         |


以下是更新后的内容，已删除过时或低质量的条目，保留了有价值的内容，并以易于理解的格式呈现：

## 4.6 高维度与子空间离群点
| 论文标题                                                                                       | 发表期刊                        | 年份 | 参考文献                      | 资源                                                                                   |
| ---------------------------------------------------------------------------------------------- | ------------------------------- | ---- | ---------------------------- | -------------------------------------------------------------------------------------- |
| A survey on unsupervised outlier detection in high-dimensional numerical data                    | Stat Anal Data Min              | 2012 | [#Zimek2012A]                | [HTML](https://onlinelibrary.wiley.com/doi/abs/10.1002/sam.11161)                        |
| Learning Representations of Ultrahigh-dimensional Data for Random Distance-based Outlier Detection | SIGKDD                          | 2018 | [#Pang2018Learning]          | [PDF](https://arxiv.org/pdf/1806.04808.pdf)                                              |
| Reverse Nearest Neighbors in Unsupervised Distance-Based Outlier Detection                       | TKDE                            | 2015 | [#Radovanovic2015Reverse]    | [PDF](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.699.9559&rep=rep1&type=pdf) |

## 4.7 离群点集成
| 论文标题                                                                                        | 发表期刊                      | 年份 | 参考文献                      | 资源                                                                                         |
| ------------------------------------------------------------------------------------------------ | ----------------------------- | ---- | ---------------------------- | -------------------------------------------------------------------------------------------- |
| Outlier ensembles: position paper                                                                  | SIGKDD Explorations           | 2013 | [#Aggarwal2013Outlier]        | [PDF](https://pdfs.semanticscholar.org/841e/ce7c3812bbf799c99c84c064bbf77916ba9.pdf)            |
| Ensembles for unsupervised outlier detection: challenges and research questions                     | SIGKDD Explorations           | 2014 | [#Zimek2014Ensembles]         | [PDF](http://www.kdd.org/exploration_files/V15-01-02-Zimek.pdf)                               |
| An Unsupervised Boosting Strategy for Outlier Detection Ensembles                                  | PAKDD                          | 2018 | [#Campos2018An]              | [HTML](https://link.springer.com/chapter/10.1007/978-3-319-93034-3_45)                        |
| Adaptive Model Pooling for Online Deep Anomaly Detection from a Complex Evolving Data Stream       | KDD                            | 2022 | [#Yoon2022ARCUS]             | [PDF](https://dl.acm.org/doi/pdf/10.1145/3534678.3539348), [GitHub](https://github.com/kaist-dmlab/ARCUS) |

## 4.8 演变数据中的离群点检测
| 论文标题                                                                                        | 发表期刊                      | 年份 | 参考文献                      | 资源                                                                                           |
| ------------------------------------------------------------------------------------------------ | ----------------------------- | ---- | ---------------------------- | ---------------------------------------------------------------------------------------------- |
| A Survey on Anomaly detection in Evolving Data: [with Application to Forest Fire Risk Prediction] | SIGKDD Explorations           | 2018 | [#Salehi2018A]               | [PDF](http://www.kdd.org/exploration_files/20-1-Article2.pdf)                                   |
| Unsupervised real-time anomaly detection for streaming data                                        | Neurocomputing                | 2017 | [#Ahmad2017Unsupervised]     | [PDF](https://www.researchgate.net/publication/317325599_Unsupervised_real-time_anomaly_detection_for_streaming_data) |
| MIDAS: Microcluster-Based Detector of Anomalies in Edge Streams                                   | AAAI                          | 2020 | [#Bhatia2020MIDAS]           | [PDF](https://www.comp.nus.edu.sg/~sbhatia/assets/pdf/midas.pdf), [GitHub](https://github.com/bhatiasiddharth/MIDAS) |

## 4.9 表征学习在离群点检测中的应用
| 论文标题                                                                                        | 发表期刊                      | 年份 | 参考文献                      | 资源                                                                                     |
| ------------------------------------------------------------------------------------------------ | ----------------------------- | ---- | ---------------------------- | ---------------------------------------------------------------------------------------- |
| Learning Representations of Ultrahigh-dimensional Data for Random Distance-based Outlier Detection | SIGKDD                          | 2018 | [#Pang2018Learning]          | [PDF](https://arxiv.org/pdf/1806.04808.pdf)                                                |
| XGBOD: improving supervised outlier detection with unsupervised representation learning            | IJCNN                          | 2018 | [#Zhao2018Xgbod]             | [PDF](http://www.andrew.cmu.edu/user/yuezhao2/papers/18-ijcnn-xgbod.pdf)                  |

## 4.10 可解释性
| 论文标题                                                                                        | 发表期刊                      | 年份 | 参考文献                      | 资源                                                                                         |
| ------------------------------------------------------------------------------------------------ | ----------------------------- | ---- | ---------------------------- | -------------------------------------------------------------------------------------------- |
| Explaining Anomalies in Groups with Characterizing Subspace Rules                                  | DMKD                            | 2018 | [#Macha2018Explaining]       | [PDF](https://www.andrew.cmu.edu/user/lakoglu/pubs/18-pkdd-journal-xpacs.pdf)                 |
| Beyond Outlier Detection: LookOut for Pictorial Explanation                                        | ECML-PKDD                      | 2018 | [#Gupta2018Beyond]           | [PDF](https://www.andrew.cmu.edu/user/lakoglu/pubs/18-pkdd-lookout.pdf)                      |
| Explainable Contextual Anomaly Detection Using Quantile Regression Forests                         | DMKD                            | 2023 | [#Li2023QCAD]                | [HTML](https://link.springer.com/article/10.1007/s10618-023-00967-z)                          |

## 4.11 神经网络中的离群点检测
| 论文标题                                                                                        | 发表期刊                      | 年份 | 参考文献                      | 资源                                                                                           |
| ------------------------------------------------------------------------------------------------ | ----------------------------- | ---- | ---------------------------- | ------------------------------------------------------------------------------------------------ |
| Detecting spacecraft anomalies using lstms and nonparametric dynamic thresholding                   | KDD                            | 2018 | [#Hundman2018Detecting]      | [PDF](https://arxiv.org/pdf/1802.04431.pdf), [Code](https://github.com/khundman/telemanom)       |
| MAD-GAN: Multivariate Anomaly Detection for Time Series Data with Generative Adversarial Networks   | ICANN                          | 2019 | [#Li2019MAD]                 | [PDF](https://arxiv.org/pdf/1901.04997.pdf), [Code](https://github.com/LiDan456/MAD-GANs)        |

## 4.12 主动离群点检测
| 论文标题                                                                                        | 发表期刊                      | 年份 | 参考文献                      | 资源                                                                                           |
| ------------------------------------------------------------------------------------------------ | ----------------------------- | ---- | ---------------------------- | ------------------------------------------------------------------------------------------------ |
| Active learning for anomaly and rare-category detection                                             | NeurIPS                        | 2005 | [#Pelleg2005Active]          | [PDF](http://papers.nips.cc/paper/2554-active-learning-for-anomaly-and-rare-category-detection.pdf) |
| Outlier detection by active learning                                                                | SIGKDD                        | 2006 | [#Abe2006Outlier]            | [PDF](https://www.researchgate.net/profile/Naoki_Abe2/publication/221653343_Outlier_detection_by_active_learning/links/5441464a0cf2e6f0c0f60abb.pdf) |

## 4.13. 交互式离群检测

| 论文标题                                                    | 发表会议/期刊     | 年份  | 参考文献                              | 相关材料                             |
|-----------------------------------------------------------|-----------------|------|-------------------------------------|------------------------------------|
| Learning On-the-Job to Re-rank Anomalies from Top-1 Feedback | SDM             | 2019 | [Lamba2019Learning](https://epubs.siam.org/doi/pdf/10.1137/1.9781611975673.69) | [PDF](https://epubs.siam.org/doi/pdf/10.1137/1.9781611975673.69) |
| Interactive anomaly detection on attributed networks        | WSDM            | 2019 | [Ding2019Interactive](http://www.public.asu.edu/~jundongl/paper/WSDM19_GraphUCB.pdf) | [PDF](http://www.public.asu.edu/~jundongl/paper/WSDM19_GraphUCB.pdf) |
| eX2: a framework for interactive anomaly detection          | IUI Workshop    | 2019 | [Arnaldo2019ex2](http://ceur-ws.org/Vol-2327/IUI19WS-ESIDA-2.pdf) | [PDF](http://ceur-ws.org/Vol-2327/IUI19WS-ESIDA-2.pdf) |
| Tripartite Active Learning for Interactive Anomaly Discovery | IEEE Access     | 2019 | [Zhu2019Tripartite](https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=8707963) | [PDF](https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=8707963) |

## 4.14. 其他领域的离群检测

| 领域      | 论文标题                                                | 发表会议/期刊     | 年份  | 参考文献                              | 相关材料                             |
|-----------|-------------------------------------------------------|-----------------|------|-------------------------------------|------------------------------------|
| 文本      | Outlier detection for text data                        | SDM             | 2017 | [Kannan2017Outlier](https://epubs.siam.org/doi/pdf/10.1137/1.9781611974973.55) | [PDF](https://epubs.siam.org/doi/pdf/10.1137/1.9781611974973.55) |

## 4.15. 离群检测应用

| 领域            | 论文标题                                                   | 发表会议/期刊             | 年份  | 参考文献                                | 相关材料                             |
|-----------------|----------------------------------------------------------|-------------------------|------|-------------------------------------|------------------------------------|
| 安全            | A survey of distance and similarity measures used within network intrusion anomaly detection | IEEE Commun. Surv. Tutor. | 2015 | [WellerFahy2015A](https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=6853338) | [PDF](https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=6853338) |
| 安全            | Anomaly-based network intrusion detection: Techniques, systems and challenges | Computers & Security      | 2009 | [GarciaTeodoro2009Anomaly](http://dtstc.ugr.es/~jedv/descargas/2009_CoSe09-Anomaly-based-network-intrusion-detection-Techniques,-systems-and-challenges.pdf) | [PDF](http://dtstc.ugr.es/~jedv/descargas/2009_CoSe09-Anomaly-based-network-intrusion-detection-Techniques,-systems-and-challenges.pdf) |
| 金融            | A survey of anomaly detection techniques in financial domain | Future Gener Comput Syst  | 2016 | [Ahmed2016A](http://isiarticles.com/bundles/Article/pre/pdf/76882.pdf) | [PDF](http://isiarticles.com/bundles/Article/pre/pdf/76882.pdf) |
| 交通            | Outlier Detection in Urban Traffic Data                  | WIMS                    | 2018 | [Djenouri2018Outlier](http://dss.sdu.dk/assets/fpd-lof/outlier-detection-urban.pdf) | [PDF](http://dss.sdu.dk/assets/fpd-lof/outlier-detection-urban.pdf) |
| 社交媒体        | A survey on social media anomaly detection               | SIGKDD Explorations      | 2016 | [Yu2016A](https://arxiv.org/pdf/1601.01102.pdf) | [PDF](https://arxiv.org/pdf/1601.01102.pdf) |
| 社交媒体        | GLAD: group anomaly detection in social media analysis   | TKDD                    | 2015 | [Yu2015Glad](https://arxiv.org/pdf/1410.1940.pdf) | [PDF](https://arxiv.org/pdf/1410.1940.pdf) |
| 机器故障        | Detecting the Onset of Machine Failure Using Anomaly Detection Methods | DAWAK                    | 2019 | [Riazi2019Detecting](https://webdocs.cs.ualberta.ca/~zaiane/postscript/DAWAK19.pdf) | [PDF](https://webdocs.cs.ualberta.ca/~zaiane/postscript/DAWAK19.pdf) |
| 视频监控        | AnomalyNet: An anomaly detection network for video surveillance | TIFS                    | 2019 | [Zhou2019AnomalyNet](https://ieeexplore.ieee.org/document/8649753) | [IEEE](https://ieeexplore.ieee.org/document/8649753), [Code](https://github.com/joeyzhouty/AnomalyNet) |

## 4.16. 自动化离群检测

| 论文标题                                                   | 发表会议/期刊           | 年份  | 参考文献                                | 相关材料                             |
|----------------------------------------------------------|-----------------------|------|-------------------------------------|------------------------------------|
| AutoML: state of the art with a focus on anomaly detection, challenges, and research directions | Int J Data Sci Anal     | 2022 | [Bahri2022automl](https://www.researchgate.net/publication/358364044_AutoML_state_of_the_art_with_a_focus_on_anomaly_detection_challenges_and_research_directions) | [PDF](https://www.researchgate.net/publication/358364044_AutoML_state_of_the_art_with_a_focus_on_anomaly_detection_challenges_and_research_directions) |
| AutoOD: Automated Outlier Detection via Curiosity-guided Search and Self-imitation Learning | ICDE                    | 2020 | [Li2020AutoOD](https://arxiv.org/pdf/2006.11321.pdf) | [PDF](https://arxiv.org/pdf/2006.11321.pdf) |
| Automatic Unsupervised Outlier Model Selection            | NeurIPS                 | 2021 | [Zhao2020Automating](https://www.andrew.cmu.edu/user/yuezhao2/papers/21-neurips-metaod.pdf) | [PDF](https://www.andrew.cmu.edu/user/yuezhao2/papers/21-neurips-metaod.pdf), [Code](https://github.com/yzhao062/MetaOD) |

## 4.17. 离群检测机器学习系统

| 论文标题                                                   | 发表会议/期刊           | 年份  | 参考文献                                | 相关材料                             |
|----------------------------------------------------------|-----------------------|------|-------------------------------------|------------------------------------|
| PyOD: A Python Toolbox for Scalable Outlier Detection     | JMLR                  | 2019 | [Zhao2019PYOD](https://www.jmlr.org/papers/volume20/19-011/19-011.pdf) | [PDF](https://www.jmlr.org/papers/volume20/19-011/19-011.pdf), [Code](https://github.com/yzhao062/pyod) |
| SUOD: Accelerating Large-Scale Unsupervised Heterogeneous Outlier Detection | MLSys                  | 2021 | [Zhao2021SUOD](https://arxiv.org/pdf/2003.05731.pdf) | [PDF](https://arxiv.org/pdf/2003.05731.pdf), [Code](https://github.com/yzhao062/suod) |
| TOD: Tensor-based Outlier Detection                       | Preprint               | 2021 | [Zhao2021TOD](https://arxiv.org/pdf/2110.14007.pdf) | [PDF](https://arxiv.org/pdf/2110.14007.pdf), [Code](https://github.com/yzhao062/pytod) |

## 4.18. 离群检测中的公平性与偏差问题

| 论文标题                                                   | 发表会议/期刊     | 年份  | 参考文献                              | 相关材料                             |
|----------------------------------------------------------|-----------------|------|-------------------------------------|------------------------------------|
| A Framework for Determining the Fairness of Outlier Detection | ECAI            | 2020 | [Davidson2020A](https://web.cs.ucdavis.edu/~davidson/Publications

/TR.pdf) | [PDF](https://web.cs.ucdavis.edu/~davidson/Publications/TR.pdf) |
| FAIROD: Fairness-aware Outlier Detection                  | AIES            | 2021 | [Shekhar2021FAIROD](https://arxiv.org/pdf/2012.03063.pdf) | [PDF](https://arxiv.org/pdf/2012.03063.pdf) |

## 4.19. 基于隔离的方法

| 论文标题                                                   | 发表会议/期刊      | 年份  | 参考文献                              | 相关材料                             |
|----------------------------------------------------------|------------------|------|-------------------------------------|------------------------------------|
| Isolation forest                                           | ICDM             | 2008 | [Liu2008Isolation](https://cs.nju.edu.cn/zhouzh/zhouzh.files/publication/icdm08b.pdf) | [PDF](https://cs.nju.edu.cn/zhouzh/zhouzh.files/publication/icdm08b.pdf) |
| Isolation‐based anomaly detection using nearest‐neighbor ensembles | Computational Intelligence | 2018 | [Bandaragoda2018Isolation](https://www.researchgate.net/publication/322359651_Isolation-based_anomaly_detection_using_nearest-neighbor_ensembles_iNNE) | [PDF](https://www.researchgate.net/publication/322359651_Isolation-based_anomaly_detection_using_nearest-neighbor_ensembles_iNNE), [Code](https://github.com/zhuye88/iNNE) |
| Extended Isolation Forest                                  | TKDE             | 2019 | [Hariri2019Extended](https://arxiv.org/pdf/1811.02141.pdf) | [PDF](https://arxiv.org/pdf/1811.02141.pdf), [Code](https://github.com/sahandha/eif) |
| Isolation Distributional Kernel: A New Tool for Kernel based Anomaly Detection | KDD              | 2020 | [Ting2020Isolation](https://arxiv.org/pdf/2009.12196.pdf) | [PDF](https://arxiv.org/pdf/2009.12196.pdf), [Code](https://github.com/IsolationKernel/Codes/tree/main/IDK) |
| Deep Isolation Forest for Anomaly Detection               | TKDE             | 2023 | [Xu2023Deep](https://arxiv.org/abs/2206.06602) | [PDF](https://arxiv.org/abs/2206.06602), [Code](https://github.com/xuhongzuo/deep-iforest) |

## 4.20. 新兴和有趣的主题

| 论文标题                                                   | 发表会议/期刊           | 年份  | 参考文献                                | 相关材料                             |
|----------------------------------------------------------|-----------------------|------|-------------------------------------|------------------------------------|
| Clustering with Outlier Removal                           | TKDE                  | 2019 | [Liu2018Clustering](https://arxiv.org/pdf/1801.01899.pdf) | [PDF](https://arxiv.org/pdf/1801.01899.pdf) |
| Real-World Anomaly Detection by using Digital Twin Systems and Weakly-Supervised Learning | IEEE Trans. Ind. Informat. | 2020 | [Castellani2020Siamese](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=9179030) | [PDF](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=9179030) |
| SSD: A Unified Framework for Self-Supervised Outlier Detection | ICLR                   | 2021 | [Sehwag2021SSD](https://openreview.net/pdf?id=v5gjXpmR8J) | [PDF](https://openreview.net/pdf?id=v5gjXpmR8J), [Code](https://github.com/inspire-group/SSD) |

# 5. 重要会议/研讨会/期刊

## 5.1 会议与研讨会

以下是一些主要的数据挖掘与异常检测领域的会议：

- **ACM国际知识发现与数据挖掘会议 (SIGKDD)**  
  网址: [KDD Conference](http://www.kdd.org/conferences)  
  SIGKDD 是数据挖掘领域的顶级会议，常设有与异常检测相关的研讨会，如**Outlier Detection Workshop (ODD)**。

- **ACM国际数据管理会议 (SIGMOD)**  
  网址: [SIGMOD Conference](https://sigmod.org/)

- **IEEE国际数据挖掘大会 (ICDM)**  
  网址: [ICDM Conference](http://icdm2018.org/)

- **SIAM数据挖掘国际会议 (SDM)**  
  网址: [SDM Conference](https://www.siam.org/Conferences/CM/Main/sdm19)

- **IEEE国际数据工程会议 (ICDE)**  
  网址: [ICDE Conference](https://icde2018.org/)

- **ACM国际信息与知识管理大会 (CIKM)**  
  网址: [CIKM Conference](http://www.cikmconference.org/)

- **欧洲机器学习与数据库知识发现大会 (ECML-PKDD)**  
  网址: [ECML-PKDD Conference](http://www.ecmlpkdd2018.org/)

- **亚太知识发现与数据挖掘大会 (PAKDD)**  
  网址: [PAKDD Conference](http://pakdd2019.medmeeting.org)

## 5.2 期刊

以下是一些与数据挖掘和异常检测相关的高影响力期刊：

- **ACM数据知识发现期刊 (TKDD)**  
  网址: [TKDD Journal](https://tkdd.acm.org/)

- **IEEE知识与数据工程期刊 (TKDE)**  
  网址: [TKDE Journal](https://www.computer.org/web/tkde)

- **ACM SIGKDD探索性新闻通讯**  
  网址: [SIGKDD Explorations](http://www.kdd.org/explorations)

- **数据挖掘与知识发现 (DMDK)**  
  网址: [DMDK Journal](https://link.springer.com/journal/10618)

- **知识与信息系统 (KAIS)**  
  网址: [KAIS Journal](https://link.springer.com/journal/10115)

## 5.3 参考文献

以下是部分有影响力的研究文献，涉及异常检测和数据挖掘技术：

- **Chandola, V., Banerjee, A., and Kumar, V. (2009).**  
  Anomaly detection: A survey. *ACM Computing Surveys* 41(3):15.  
  该文献综述了异常检测领域的经典方法与技术。

- **Ahmed, M., Mahmood, A.N., and Islam, M.R. (2016).**  
  A survey of anomaly detection techniques in the financial domain. *Future Generation Computer Systems* 55:278-288.  
  本文介绍了金融领域的异常检测方法。

- **Breunig, M.M., Kriegel, H.P., Ng, R.T., and Sander, J. (2000).**  
  LOF: identifying density-based local outliers. *ACM SIGMOD Record* 29(2):93-104.  
  LOF（局部离群因子）是一种基于密度的异常检测算法，广泛应用于高维数据中。

- **Liu, F.T., Ting, K.M., and Zhou, Z.H. (2008).**  
  Isolation Forest. *International Conference on Data Mining* pp.413-422.  
  本文提出的Isolation Forest算法在大规模数据集中的异常检测中表现出色。

- **Pang, G., Cao, L., Chen, L., and Liu, H. (2021).**  
  Deep Learning for Anomaly Detection: A Review. *ACM Computing Surveys (CSUR)* 54(2):1-38.  
  该综述文章总结了深度学习在异常检测中的应用和挑战。

- **Yoon, S., Lee, Y., Lee, J.G., & Lee, B.S. (2022).** Adaptive Model Pooling for Online Deep Anomaly Detection from a Complex Evolving Data Stream. *Proceedings of the 28th ACM SIGKDD Conference on Knowledge Discovery and Data Mining*, 2347-2357.  
   - 该研究提出了适应性模型池方法，用于在线深度异常检测，能够应对复杂和动态的数据流。

- **Yu, R., He, X., & Liu, Y. (2015).** GLAD: Group Anomaly Detection in Social Media Analysis. *ACM Transactions on Knowledge Discovery from Data (TKDD)*, 10(2), 18.  
   - 本文介绍了GLAD方法，针对社交媒体数据中的群体异常检测。

- **Yu, R., Qiu, H., Wen, Z., Lin, C., & Liu, Y. (2016).** A Survey on Social Media Anomaly Detection. *ACM SIGKDD Explorations Newsletter*, 18(1), 1-14.  
   - 这篇综述文章回顾了社交媒体中的异常检测技术，涵盖了方法和挑战。

-  **Zhao, Y., Nasrullah, Z., Hryniewicki, M.K., & Li, Z. (2019).** LSCP: Locally Selective Combination in Parallel Outlier Ensembles. *Proceedings of the 2019 SIAM International Conference on Data Mining (SDM)*, 585-593.  
   - 提出了LSCP方法，通过局部选择性组合增强了并行异常检测集成模型的效果。

-  **Zhao, Y., Nasrullah, Z., & Li, Z. (2019).** PyOD: A Python Toolbox for Scalable Outlier Detection. *Journal of Machine Learning Research*, 20, 1-7.  
   - 本文介绍了PyOD工具包，提供了扩展性强的异常检测方法，适用于大规模数据集。

-  **Zhao, Y., Hu, X., Cheng, C., Wang, C., Wan, C., Wang, W., Yang, J., Bai, H., Li, Z., Xiao, C., & Wang, Y. (2021).** SUOD: Accelerating Large-scale Unsupervised Heterogeneous Outlier Detection. *Proceedings of Machine Learning and Systems (MLSys)*.  
   - 提出了SUOD方法，旨在加速大规模无监督异构数据集上的异常检测。

- **Zhou, J.T., Du, J., Zhu, H., Peng, X., Liu, Y., & Goh, R.S.M. (2019).** AnomalyNet: An Anomaly Detection Network for Video Surveillance. *IEEE Transactions on Information Forensics and Security*.  
   - AnomalyNet方法应用于视频监控中的异常检测，适应性强，能够识别复杂的监控场景。

- **Zimek, A., Schubert, E., & Kriegel, H.P. (2012).** A Survey on Unsupervised Outlier Detection in High-dimensional Numerical Data. *Statistical Analysis and Data Mining: The ASA Data Science Journal*, 5(5), 363-387.  
   - 这篇综述文章回顾了高维数值数据中的无监督异常检测技术，并讨论了面临的挑战。

-  **Wang, C., Zhuang, Z., Qi, Q., Wang, J., Wang, X., Sun, H., & Liao, J. (2023).** Drift Doesn't Matter: Dynamic Decomposition with Diffusion Reconstruction for Unstable Multivariate Time Series Anomaly Detection. *Advances in Neural Information Processing Systems*, 36.  
   - 该研究提出了一种基于动态分解和扩散重建的时间序列异常检测方法，能够有效应对多变量时间序列中的不稳定性。








