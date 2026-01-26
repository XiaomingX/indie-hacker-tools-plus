# awesome-RecSys 推荐系统资源精选
整理了一份推荐系统相关的精选资源，适合中国用户快速上手和深入学习，涵盖书籍、会议、论文、开源项目及实用平台，兼顾理论深度与工业实践。

![image](https://github.com/user-attachments/assets/be994c1b-93f3-47bb-841f-c6ff25101aca)

---

## 书籍
以下是推荐系统领域经典且前沿的著作，覆盖从入门到前沿的全学习路径，标注核心价值与适合人群：

- [Recommender Systems: The Textbook (2016)](http://pzs.dstu.dp.ua/DataMining/recom/bibl/1aggarwal_c_c_recommender_systems_the_textbook.pdf) - Charu Aggarwal  
  内容详尽且体系化，涵盖基础算法、上下文感知推荐、鲁棒性防御、跨域推荐等核心模块，理论与工业实践案例结合紧密，**适合进阶研究者与资深工程师**[3]。

- [Recommender Systems Handbook 2nd Edition (2015)](https://edyaaleh.files.wordpress.com/2016/02/recommendersystemshandbook.pdf) - Francesco Ricci  
  领域权威手册，由全球顶尖学者联合撰写，系统梳理推荐系统的数学基础、评估体系、应用场景及开放挑战，**适合作为研究生教材或研究参考工具书**[3]。

- [Recommender Systems An Introduction (2011)](https://github.com/singmiya/recsys/raw/master/Recommender%20Systems%20An%20Introduction.pdf) - Dietmar Jannach  
  入门友好型教材，以“协同过滤→基于内容→知识型推荐”为核心脉络，公式推导通俗，配套案例丰富，**适合零基础初学者构建基础认知**[3]。

- 《推荐系统：前沿与实践》（2026）  
  微软亚洲研究院团队撰写，聚焦深度协同过滤、图神经网络（GNN）推荐、序列推荐、知识图谱融合、强化学习推荐等前沿技术，配套微软开源框架 `Microsoft Recommenders` 的实战教程，**适合想衔接工业界前沿技术的开发者**[3]。

- 《推荐系统：算法、案例与大模型》（2026）  
  国内首部系统解析大模型与推荐系统融合的著作，涵盖LLM驱动的召回/排序、对话式推荐、创作者模拟等新方向，配套MOOC课程与代码仓库，**适合关注大模型+推荐交叉领域的学习者**[7]。

---

## 会议
推荐系统领域的核心学术会议分为“专门领域顶会”“交叉领域顶会”“国内特色会议”三类，以下补充会议定位、侧重方向与核心价值，助力精准追踪研究动态：

### 1. 专门领域顶会（聚焦推荐系统本身）
- [RecSys](https://recsys.acm.org/) - ACM Conference on Recommender Systems  
  全球唯一以推荐系统为核心主题的顶级会议，**定位“理论与实践桥梁”**，每年举办1次。侧重方向包括个性化推荐、可解释推荐、公平性与伦理、工业界落地案例等，特色环节“RecSys Challenge”（如Netflix Prize后续竞赛）常年吸引谷歌、阿里、腾讯等企业参与，是获取“前沿技术+工业需求”的核心渠道。

### 2. 交叉领域顶会（推荐为核心议题之一）
- [KDD](https://www.kdd.org/) - ACM SIGKDD Conference on Knowledge Discovery and Data Mining  
  数据挖掘领域顶会（“数据科学奥斯卡”），每年1次。推荐系统是其**核心议题（占比约20%）**，侧重“真实场景的复杂问题解决”，如大规模冷启动、长尾物品推荐、推荐系统的因果推断等，论文多来自工业界一线（如阿里、字节跳动），实践性极强。

- [SIGIR](https://sigir.org/) - ACM SIGIR International Conference on Research and Development in Information Retrieval  
  信息检索领域顶会，每年1次。推荐与检索深度交叉（如召回、排序、会话式交互），**侧重“检索技术在推荐中的落地”**，2026年重点方向包括生成式推荐、LLM驱动的检索-推荐融合、多模态推荐等，会议同期设“工业界论坛”展示百度、美团等企业的最新实践[4]。

- [ICML](https://icml.cc/) - International Conference on Machine Learning  
  机器学习领域顶会，每年1次。推荐相关论文侧重**“算法理论创新”**，如深度学习推荐模型的收敛性分析、强化学习在序列推荐中的数学建模、大模型推荐的效率优化等，适合追踪纯技术突破。

- [NeurIPS](https://nips.cc/) - Neural Information Processing Systems  
  与ICML齐名的机器学习顶会，每年1次。推荐方向侧重**“前沿技术落地”**，如Transformer在推荐中的改造（如DeepFM→Transformer4Rec）、联邦推荐的隐私保护机制、多智能体推荐系统等，工业界与学术界成果各占半壁江山。

- [WWW](https://www2026.thewebconf.org/) - The Web Conference（原WWW Conference）  
  万维网领域顶会，每年1次。推荐方向侧重**“Web环境下的特殊场景”**，如社交网络推荐、跨境电商推荐、用户行为序列的Web化建模等，论文常结合实际Web数据（如Twitter、淘宝日志）展开，实用性强。

- [WSDM](https://wsdm-conference.org/) - ACM International Conference on Web Search and Data Mining  
  搜索与数据挖掘交叉顶会，每年1次。推荐方向侧重**“高效性与实时性”**，如毫秒级召回算法、流数据推荐、搜索-推荐一体化架构等，百度、微软、Meta等企业的工程化论文集中于此。

### 3. 国内特色会议（贴合本土场景）
- [CCF RecSys](http://recsys.ccf.org.cn/) - CCF 推荐系统学术会议  
  国内推荐领域核心会议（由CCF人工智能专委会主办），每年1次。**侧重“中国本土场景创新”**，如短视频推荐的实时交互优化、直播推荐的用户留存建模、电商“拼团”场景的推荐策略等，设“产学研对接专场”，方便国内学习者链接企业需求。

---

## 论文
精选推荐系统领域“奠基性+前沿性”论文，标注核心贡献与影响力，辅助快速建立知识体系：

### 奠基性经典论文（必读）
- [Matrix Factorization Techniques for Recommender Systems (2009)](https://datajobs.com/data-science-repo/Recommender-Systems-[Netflix].pdf) - Yehuda Koren  
  矩阵分解技术的里程碑之作，系统提出FunkSVD、时间感知MF等方法，直接推动Netflix Prize突破，是传统推荐算法的“入门钥匙”。

- [Neural Collaborative Filtering (2017)](https://www.comp.nus.edu.sg/~xiangnan/papers/ncf.pdf) - Xiangnan He  
  深度学习推荐的“开山之作”，首次将神经网络与协同过滤结合，解决传统MF的线性建模局限，启发了后续DeepFM、Wide&Deep等模型。

- [Wide & Deep Learning for Recommender Systems (2016)](https://arxiv.org/pdf/1606.07792.pdf) - Heng-Tze Cheng  
  谷歌提出的工业级推荐架构，首次融合“记忆（Wide）”与“泛化（Deep）”能力，成为电商、应用商店推荐的标配架构。

- [Deep Learning based Recommender System: A Survey (2018)](https://arxiv.org/pdf/1707.07435.pdf) - Shuai Zhang  
  深度学习推荐领域的权威综述，梳理了DL在CF、CB、序列推荐中的应用脉络，至今仍是该方向的核心参考。

### 前沿重点论文（追踪趋势）
- [Explainable Recommendation: A Survey and New Perspectives (2018)](https://arxiv.org/pdf/1804.11192) - Yongfeng Zhang  
  可解释推荐领域的标杆综述，提出“模型内在可解释”与“事后解释”两大框架，适配监管合规需求。

- SIGIR 2026 最新论文示例（反映大模型+推荐趋势）[4]：  
  - **MGIPF: 多粒度兴趣预测框架**：通过分层注意力机制捕捉用户粗粒度与细粒度偏好，有效缓解长尾物品稀疏性与行为噪声问题。  
  - **基于生成式奖励模型的模拟用户**：针对对话式推荐的“偏好稀疏”痛点，用生成模型模拟用户交互反馈，提升复杂偏好捕捉精度。  
  - **LLM驱动的创作者模拟智能体CreAgent**：通过LLM复现内容创作者的生产逻辑，解决推荐系统长期评估（如用户留存）的“离线-在线鸿沟”问题。

---

## GitHub 项目
精选“工具库+框架+资源集合”三类开源项目，标注核心优势与适用场景，降低工程落地门槛：

- [List_of_Recommender_Systems](https://github.com/grahamjenson/list_of_recommender_systems) - 推荐系统资源总集  
  涵盖传统算法、深度学习、工业实践等方向的项目索引，支持按“技术类型”“应用场景”筛选，适合快速找方向。

- [Deep-Learning-for-Recommendation-Systems](https://github.com/robi56/Deep-Learning-for-Recommendation-Systems) - 深度学习推荐资源库  
  包含论文复现代码（如NCF、Transformer4Rec）、数据集（MovieLens、Amazon）及调参教程，适合初学者练手。

- [NeuRec](https://github.com/wubinzzu/NeuRec) - TensorFlow推荐系统框架  
  模块化设计，支持快速搭建CF、序列推荐、知识图谱推荐模型，自带模型压缩与部署工具，适合研究原型验证。

- [LightFM](https://github.com/lyst/lightfm) - 轻量级推荐工具库  
  支持“协同过滤+基于内容”混合建模，API简洁，无需手动处理特征工程，适合中小规模数据的快速上线。

- [recommenders](https://github.com/microsoft/recommenders) - 微软工业级推荐框架  
  基于PyTorch/TensorFlow，包含Wide&Deep、DeepFM等10+主流模型的端到端实现，配套A/B测试工具与大规模数据处理方案，适合工业界落地。

- [RecBole](https://github.com/RUCAIBox/RecBole) - 国内开源推荐算法库（人大团队）  
  支持80+推荐算法，适配中文数据集（如京东用户行为数据），提供详细的中文文档与教程，对国内开发者友好。

---

## 实用网站
补充“国内平台+垂直工具”，覆盖学习、论文、实战全场景，更贴合中国用户习惯：

- [PapersWithCode](https://paperswithcode.com/task/recommendation-systems) - 论文与代码联动平台  
  实时更新推荐领域SOTA论文，标注代码开源情况与性能指标（如NDCG、MAP），支持按“任务类型”（召回/排序/可解释）筛选。

- [Coursera: Recommender System](https://www.coursera.org/specializations/recommender-systems) - 斯坦福大学专项课程  
  由推荐领域权威Andrew Ng团队打造，涵盖协同过滤、矩阵分解、深度学习推荐，配套编程作业（Python实现）。

- [arXiv: cs.IR](https://arxiv.org/list/cs.IR/recent) - 推荐相关论文预印本平台  
  信息检索（IR）方向包含大量推荐领域预印本，可提前3-6个月获取前沿成果，支持按“提交时间”订阅更新。
