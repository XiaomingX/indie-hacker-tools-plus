# 向量数据库 (Vector Database) 核心指南 (2026 Checklist)

> [!TIP]
> **Indie Hacker Insight**: 2026 年的向量数据库不仅是存储，更是 **"Knowledge Engine"**。
> - **混合检索 (Hybrid Search)**：不要只依赖向量搜索，结合传统的**全文搜索 (BM25)** 能显著提升 RAG 的准确度。
> - **GraphRAG**：关注支持图结构的数据库（如 **Neo4j** 或 **Milvus 3.0**），它们能处理比单纯相似度更复杂的逻辑关联。

---

## 🚀 托管服务与云原生 (Managed Services)

- [ ] [**Pinecone**](https://www.pinecone.io/) - 2026 年依然是 SaaS 首选，支持 Serverless 架构，极低成本起步。
- [ ] [**Zilliz (Cloud Milvus)**](https://zilliz.com/) - 针对超大规模数据的企业级托管服务。
- [ ] [**Weaviate Cloud**](https://weaviate.io/) - 支持多模态（图像、音频、视频）的一体化 AI 数据库。
- [ ] [**MongoDB Atlas Vector Search**](https://www.mongodb.com/products/platform/atlas-vector-search) - 如果你已经在用 MongoDB，这是最丝滑的集成方案。

---

## 🏗️ 开源与本地部署 (Open Source & Self-Hosted)

- [ ] [**Milvus**](https://milvus.io/) - 高性能开源标杆，支持大规模分布式扩展。
- [ ] [**Qdrant**](https://qdrant.tech/) - 采用 Rust 编写，内存效率极高，支持复杂的过滤逻辑。
- [ ] [**Chroma**](https://github.com/chroma-core/chroma) - 2026 年最适合快速原型与本地 Agent 的轻量级数据库。
- [ ] [**pgvector (PostgreSQL)**](https://github.com/pgvector/pgvector) - 将向量搜索带入 SQL 世界，独立开发者最稳健的选型。
- [ ] [**Lantern**](https://lantern.dev/) - 另一个高性能的 PostgreSQL 向量搜索插件。

---

## 📊 性能基准与评估 (Benchmarks)

- [ ] [**VectorDBBench**](https://github.com/zilliztech/VectorDBBench) - 专注于真实生产负载下的向量数据库评测。
- [ ] [**ANN Benchmarks**](http://ann-benchmarks.com/) - 经典的近似最近邻（ANN）算法性能对比。

---

## 📚 核心库与实战教程 (Libraries & Tutorials)

- [ ] [**Faiss (Meta)**](https://faiss.ai/) - 高性能向量相似度搜索的底层库。
- [ ] [**Annoy (Spotify)**](https://github.com/spotify/annoy) - 极简的近似最近邻搜索库。
- [x] **Pinecone Learning Center**: 深入浅出地讲解向量搜索的基本原理。
- [x] **RAG Application Tutorial**: 结合 LLM 与向量搜索的端到端实战。

---

## 💡 选型建议
1. **MVP 快速验证**：选 **Chroma** 或 **Pinecone (Free Tier)**。
2. **已有关系型业务数据**：首选 **PostgreSQL (pgvector)**。
3. **处理千万级以上海量数据**：选 **Milvus** 或 **Qdrant**。
4. **构建复杂 GraphRAG 系统**：关注 **Neo4j Vector** 或 **Memgraph**。
