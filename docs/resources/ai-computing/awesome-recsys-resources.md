# 推荐系统 (RecSys) 技术与实践资源精选 (2026 Checklist)

> [!TIP]
> **Indie Hacker Insight**: 2026 年，推荐系统已全面进入 **"生成式"** 与 **"全向量化"** 时代。
> - **大模型驱动**：传统的协同过滤正在被 **LLM-as-a-Ranker** 取代，利用大语言模型的语义理解能力可以极大地提升推荐的“惊喜感”。
> - **实时向量召回**：无脑选择 **Milvus** 或 **Pinecone** 作为你的召回底座，配合 **HuggingFace** 的 Embedding 模型，数行代码即可搭建起百万级召回系统。
> - **长短期兴趣平衡**：利用 **Transformer** 架构捕捉用户的即时行为流，是提升点击率 (CTR) 的核心利器。

---

## 🏗️ 核心算法与理论 (Algorithms & Theory)

- [ ] [**Neural Collaborative Filtering (NCF)**](https://arxiv.org/abs/1708.05031) - **[必读]** 深度学习推荐系统的开山之作，理解神经网络如何替代矩阵分解。
- [ ] [**Wide & Deep Learning**](https://arxiv.org/abs/1606.07792) - 谷歌提出的经典架构，平衡了“记忆”与“泛化”的工业级标准。
- [ ] [**DeepFM**](https://arxiv.org/abs/1703.04247) - 华为提出，自动提取高阶特征组合，是目前工业界排序阶段的高频选型。
- [ ] [**Generating Next Item Recommendation (LLM-Rec)**](https://arxiv.org/abs/2306.05814) - 学习如何将推荐任务建模为生成任务，利用 LLM 进行序列预测。

---

## ⚡ 工业级框架与工具 (Frameworks & Tooling)

- [ ] [**RecBole (伯乐)**](https://github.com/RUCAIBox/RecBole) - **[推荐]** 人大出品，集成 80+ 种推荐算法，支持一键复现 SOTA 结果，文档非常友好。
- [ ] [**Microsoft Recommenders**](https://github.com/recommenders-team/recommenders) - 微软开源的生产级工具箱，包含大量端到端的实战案例（从数据处理到部署）。
- [ ] [**DeepMatch**](https://github.com/shenweichen/DeepMatch) - 专注于推荐系统“召回阶段”的深度学习模型库。
- [ ] [**TensorFlow Recommenders (TFRS)**](https://github.com/tensorflow/recommenders) - 谷歌出品，与 TF 生态深度集成，适合大规模分布式训练。

---

## 🚀 向量数据库与召回 (Vector DBs & Retrieval)

- [ ] [**Milvus**](https://github.com/milvus-io/milvus) - 开源向量数据库领头羊，支持毫秒级、十亿级规模的向量检索。
- [ ] [**Pinecone**](https://www.pinecone.io/) - **[Serverless 首选]** 无需维护基础设施，直接通过 API 实现向量搜索。
- [ ] [**Faiss**](https://github.com/facebookresearch/faiss) - Meta 出品的极速向量相似度搜索库，适合本地大规模离线索引构建。

---

## 📂 学习资源与前沿会议 (Learning & Conferences)

- [ ] [**RecSys (ACM Conference)**](https://recsys.acm.org/) - 推荐系统领域最高水平的年度盛会，关注每年的 Best Paper。
- [ ] [**Papers with Code (RecSys)**](https://paperswithcode.com/task/recommendation-systems) - 实时查看各细分任务（召回、排序、冷启动）的 SOTA 排行榜。
- [ ] [**Baeldung for Java/Spring (RecSys context)**](https://www.baeldung.com/java-recommender-systems) - 如果你的后端是 Java，这里有实用的集成案例。

---

## 💡 选型建议
1. **构建全新的内容/电商推荐系统**：选 **Milvus** (召回) + **DeepFM** (排序) + **RecBole** (模型原型)。
2. **利用 AI 提升推荐语义理解**：集成 **LLM** 进行特征增强或直接作为排序器。
3. **处理极度稀疏的冷启动数据**：引入 **知识图谱 (KG)** 或 **多模态特征**。
4. **追求开发效率与快速上线**：选 **Pinecone** + **Microsoft Recommenders**。
