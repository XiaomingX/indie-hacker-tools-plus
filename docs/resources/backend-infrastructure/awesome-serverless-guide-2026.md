# 2026 Serverless 架构与开发实战指南 (Checklist)

> [!TIP]
> **Indie Hacker Insight**: 2026 年，Serverless 已经从单纯的“函数”演变为全栈“边缘云”。
> - **边缘优先**：利用 Cloudflare Workers 或 Vercel Edge Functions，将逻辑部署在离用户最近的地方，延迟降至 50ms 以下。
> - **冷启动优化**：现代 Serverless 运行在 V8 Isolates 上，冷启动几乎为零，无需再为延迟担忧。
> - **降本增效**：通过按需付费，独立开发者可以用每月不到 $20 的成本支撑起数万日活的应用。

---

## 🏗️ 核心平台与计算 (Platforms & Compute)

- [ ] [**Cloudflare Workers**](https://workers.cloudflare.com/) - **[首选]** 极致的边缘计算能力，带 D1 (SQL)、KV、Durable Objects。
- [ ] [**Vercel**](https://vercel.com/docs/functions) - 极佳的开发体验，与 Next.js 完美集成，支持 Edge 与 Serverless 模式。
- [ ] [**AWS Lambda**](https://aws.amazon.com/lambda/) - 企业级标准，功能最全，通过 Lambda@Edge 支持全球加速。
- [ ] [**Supabase Functions**](https://supabase.com/docs/guides/functions) - Deno 驱动的边缘函数，与 Postgres 数据库无缝集成。

---

## 💾 Serverless 数据库与存储 (Data & Storage)

- [ ] [**Supabase (Postgres)**](https://supabase.com/) - 开源的 Firebase 替代品，内置实时推送、鉴权与存储。
- [ ] [**Neon**](https://neon.tech/) - 无服务器 Postgres 数据库，支持分支功能，极其适合开发流程。
- [ ] [**PlanetScale (MySQL)**](https://planetscale.com/) - 专为 Serverless 设计的分布式 MySQL，支持零停机架构变更。
- [ ] [**Upstash (Redis/Kafka)**](https://upstash.com/) - 按量付费的 Redis 与 Kafka，边缘场景必备。
- [ ] [**Cloudflare R2**](https://www.cloudflare.com/developer-platform/r2/) - 无出口流量费用的 S3 兼容对象存储。

---

## 🛠️ 开发工具与框架 (Tools & Frameworks)

- [ ] [**Serverless Framework**](https://www.serverless.com/) - 支持多云部署的行业标准框架。
- [ ] [**SST (Serverless Stack)**](https://sst.dev/) - **[推荐]** 极佳的开发体验，支持本地实时调试 lambda。
- [ ] [**Hono**](https://hono.dev/) - 极其轻量的边缘 Web 框架，支持几乎所有运行时（Bun, Deno, Workers）。

---

## 💡 选型建议
1. **追求极致性价比与速度**：全量选 **Cloudflare 栈 (Workers + D1 + R2)**。
2. **构建全栈 SaaS 应用**：选 **Next.js + Vercel + Supabase/Neon**。
3. **需要复杂的异步队列与任务处理**：选 **Upstash QStash** 配合 AWS Lambda。
4. **注重数据合规与多云分发**：使用 **Serverless Framework** 配合 Terraform 管理。
