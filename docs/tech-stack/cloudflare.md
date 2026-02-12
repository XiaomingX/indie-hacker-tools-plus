# Cloudflare 基础设施选型指南 (2026)

Cloudflare 已从单纯的 CDN 服务商演变为全球领先的边缘计算与基础设施平台。其核心优势在于“全球分布”、“极低延迟”以及对开发者极其友好的“零出站流量费”策略。

---

## 核心边缘计算 (Edge Compute)

- **Cloudflare Workers**
  - **点评：** 基于 V8 Isolates 的 Serverless 平台。与传统容器相比，启动速度几乎为零，且冷启动损耗极小。它是构建高性能、低延迟边缘逻辑的工业级标准。
- **Cloudflare Pages**
  - **点评：** 极速前端托管平台。完美集成 Git 工作流，提供自动预览链路和无限扩展能力。

---

## 存储与数据服务 (Storage & Data)

- **Cloudflare R2 (Object Storage)**
  - **点评：** **S3 的强力竞争者**。最大的杀手锏是**零出站流量费 (Zero Egress Fees)**。非常适合存储大容量静态资源、AI 模型文件或用户生成的媒体内容，能显著降低云端运营成本。
- **Cloudflare D1 (SQL Database)**
  - **点评：** 基于 SQLite 的全托管关系型数据库。虽然不如 RDS 强大，但在分布式边缘场景下，其简单性和与 Workers 的深度集成使其成为轻量级应用的首选。
- **Cloudflare KV (Key-Value Storage)**
  - **点评：** 最终一致性的高并发键值对存储。适合读取极其频繁、对延迟敏感的配置信息或用户会话数据。

---

## AI 与进阶能力 (AI & Messaging)

- **Cloudflare Vectorize**
  - **点评：** 全球分布的向量数据库。专为 AI 推理和语义检索（RAG）设计，配合 Cloudflare Workers AI，可以实现全栈式的边缘 AI 应用落地。
- **Cloudflare Queues**
  - **点评：** 异步消息队列。确保消息的可靠交付，适合处理后台任务、削峰填谷以及微服务间的解耦。

---

## 选型逻辑建议

1. **追求极致性价比与免流量费：** 核心静态资源和媒体库应重仓 **R2**。
2. **构建全球低延迟应用：** 逻辑层首选 **Workers**，配合 **KV** 或 **D1**。
3. **AI 原生边缘应用：** 利用 **Vectorize** 构建高效的 RAG 检索链路。

👉 [返回云服务全球配置策略](../../README.md#云服务全球配置策略)
