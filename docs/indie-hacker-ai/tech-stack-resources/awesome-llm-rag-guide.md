# 高级检索增强生成 (RAG) 实战指南 (2026 Checklist)

> [!TIP]
> **Indie Hacker Insight**: 2026 年的 RAG 已进化为 **GraphRAG (图 RAG)** 和 **Agentic RAG**。
> - **消除幻觉**：简单的向量检索已不够，必须引入知识图谱（KG）来处理复杂的关系查询。
> - **长文本优势**：利用 Gemini 1.5 Pro 或 Claude 4 的长上下文能力，部分场景下可直接取代传统 RAG。

---

## 🏗️ 核心开发框架 (Frameworks)

- [ ] [**LangChain**](https://www.langchain.com/) - 企业级 AI 代理开发标配，支持复杂的 RAG 流水线集成。
- [ ] [**LlamaIndex**](https://www.llamaindex.ai/) - 专注数据连接与高级索引，是构建私有知识库的最强引擎。
- [ ] [**GraphRAG (Microsoft)**](https://github.com/microsoft/graphrag) - 利用图机器学习提取文档结构，极大提升复杂问题的回答质量。
- [ ] [**Haystack**](https://haystack.deepset.ai/) - 模块化 RAG 框架，适合追求极致工程化与性能的项目。
- [ ] [**Dify**](https://dify.ai/) - 可视化 RAG 编排平台，支持从 PDF 导入到 API 发布的完整闭环。

---

## 🗄️ 向量数据库与检索 (Vector DB & Retrieval)

- [ ] [**Pinecone**](https://www.pinecone.io/) - 托管式向量数据库首选，支持海量数据的高并发检索。
- [ ] [**Milvus / Zilliz**](https://milvus.io/) - 企业级开源向量数据库，适配分布式架构。
- [ ] [**Qdrant**](https://qdrant.tech/) - 高性能 Rust 编写，支持地理位置向量与多模态检索。
- [ ] [**Chroma**](https://www.trychroma.com/) - 极致轻量，适合原型开发与本地部署。
- [ ] [**Weaviate**](https://weaviate.io/) - 原生支持 GraphQL 的向量数据库，Schema 定义灵活。

---

## 🛠️ 优化与评估工具 (Optimization & Eval)

- [ ] [**RAGAS**](https://github.com/explodinggradients/ragas) - 专注于 RAG 评估的框架，涵盖忠实度、答案相关性等指标。
- [ ] [**Arize Phoenix**](https://phoenix.arize.com/) - 开源的可观测性工具，支持 RAG 过程的可视化追踪。
- [ ] [**DeepEval**](https://github.com/confident-ai/deepeval) - 将 RAG 测试集成到 CI/CD 流程中。
- [ ] [**Jina Reader**](https://r.jina.ai/) - 将网页转为精简 Markdown，极大提升 Web 检索的准确率。

---

## 📚 2026 核心研究与趋势 (Research)

- [x] **Hybrid RAG**: 结合稀疏检索（BM25）与稠密检索（Embedding）的混合模式已成标配。
- [x] **Self-RAG**: 赋予模型“自我批判”能力，自主决定何时检索、何时生成。
- [x] **Long-Context vs RAG**: 针对 1M+ Token 的长文本，研究如何平衡检索成本与推理质量。

---

## 💡 选型建议
1. **快速上线产品**：使用 **Dify** + **OpenRouter**。
2. **处理海量私有文档**：首选 **LlamaIndex** + **Pinecone**。
3. **金融/医疗高精度需求**：必须引入 **GraphRAG** 和 **RAGAS** 评估。
4. **极致性能与低延迟**：推荐 **Qdrant** + **Hono** (Edge Runtime)。
