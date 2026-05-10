# NestJS 企业级开发资源精选 (2026 Checklist)

> [!TIP]
> **Indie Hacker Insight**: 2026 年，NestJS 依然是构建复杂、可扩展后端的 **"第一选择"**。
> - **性能飞跃**：全面转向 **SWC** 编译器和 **Fastify** 适配器，冷启动与请求处理速度已不再是 Node.js 的瓶颈。
> - **现代 ORM**：优先选择 **Drizzle ORM** 或 **Prisma**，彻底告别沉重且难以维护的传统 TypeORM 架构。
> - **工程化**：利用 **Nestia** 可以自动生成极其精准的 OpenAPI 文档和客户端 SDK，效率提升 2x 以上。

---

## 🏗️ 官方资源与核心教程 (Official & Tutorials)

- [ ] [**NestJS 官方文档**](https://docs.nestjs.com) - **[权威]** 包含从核心模块到微服务、WebSockets 的全方位指南。
- [ ] [**Nest CLI**](https://docs.nestjs.com/cli/overview) - 掌握 `nest new` 和 `nest generate` 自动生成模块、控制器与服务的标准方式。
- [ ] [**NestJS 实战指南 (中文)**](https://nestjs.nodejs.cn/) - 国内开发者社区维护的翻译文档与实战博客，更符合国情。
- [ ] [**NestJS 30 天学习计划**](https://github.com/m24927605/Nestjs30Days) - 循序渐进的学习路径，适合快速上手。

---

## ⚡ 现代 ORM 与数据库集成 (Modern ORM & Data)

- [ ] [**Prisma for NestJS**](https://www.prisma.io/nestjs) - 提供极佳的类型安全感与数据库迁移体验。
- [ ] [**Drizzle for NestJS**](https://github.com/knaadh/nestjs-drizzle) - **[2026 推荐]** 极轻量、极快，且符合 SQL 直觉的现代 ORM 集成方案。
- [ ] [**Mongoose for NestJS**](https://docs.nestjs.com/techniques/mongodb) - 处理 NoSQL 数据的官方标准选型。
- [ ] [**Redis for NestJS**](https://github.com/liaoliaots/nestjs-redis) - 实现缓存、限流与分布式锁的高效集成。

---

## 🚀 性能优化与效能库 (Performance & Efficiency)

- [ ] [**Nestia**](https://github.com/samchon/nestia) - **[效率王者]** 利用编译器宏实现 200x 倍速的验证与序列化，自动生成 SDK。
- [ ] [**NestJS Fastify**](https://docs.nestjs.com/techniques/performance) - 如果追求极致 QPS，请用 Fastify 替换默认的 Express。
- [ ] [**nestjs-pino**](https://github.com/iamolegga/nestjs-pino) - 高性能、零开销的日志框架，支持请求追踪。
- [ ] [**nestjs-cls**](https://github.com/Papooch/nestjs-cls) - 实现请求级别的上下文共享（类似 ThreadLocal）。

---

## 🛡️ 测试与代码质量 (Testing & Quality)

- [ ] [**Automock**](https://github.com/omermorad/automock) - 自动生成类依赖的 Mock，极大减少单元测试的模板代码量。
- [ ] [**ts-jest for NestJS**](https://github.com/kulshekhar/ts-jest) - 官方默认的测试套件，确保类型安全。
- [ ] [**Testcontainers Node**](https://github.com/testcontainers/testcontainers-node) - 在 E2E 测试中自动拉起真实的数据库容器。

---

## 📂 优秀开源项目参考 (Open Source Gems)

- [ ] [**Novu**](https://github.com/novuhq/novu) - 基于 NestJS 构建的开源通知基础设施，学习复杂微服务架构。
- [ ] [**Twenty**](https://github.com/twentyhq/twenty) - 现代化的开源 CRM，展示了 NestJS 在大型企业应用中的落地。
- [ ] [**APITable**](https://github.com/apitable/apitable) - 开源低代码平台，学习高性能表格引擎的后端实现。

---

## 💡 选型建议
1. **构建高性能企业 API**：选 **NestJS** + **Fastify** + **Drizzle ORM** + **Nestia**。
2. **构建全栈个人项目**：选 **NestJS** + **Prisma** + **Next.js** (Turborepo)。
3. **需要极高的安全性与审计**：集成 **nestjs-cls** (请求追踪) 和 **Passport (JWT)**。
4. **提升测试覆盖率**：必装 **Automock**。