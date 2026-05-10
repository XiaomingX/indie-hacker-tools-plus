# 2026 软件架构模式与分布式设计指南 (Checklist)

> [!TIP]
> **Indie Hacker Insight**: 2026 年，架构设计的核心不再是“大而全”，而是“可观测性”与“解耦”。
> - **微服务 vs 单体**：对于初创公司，优先选择 **Modular Monolith (模块化单体)**。只有当团队规模超过 50 人或业务负载极其不均衡时，才考虑拆分为微服务。
> - **事件驱动**：利用消息队列（如 Redis Stream, RabbitMQ）实现服务间解耦，提升系统的容错能力。
> - **Serverless 优先**：将计算逻辑尽可能部署在边缘或按量计费的平台上，降低运维负担。

---

## 🏗️ 经典架构模式 (Classical Patterns)

- [ ] [**分层架构 (Layered Architecture)**](https://github.com/donnemartin/system-design-primer#layered-architecture) - 基础模式，将关注点分离为展示层、业务层、数据层。
- [ ] [**微内核架构 (Microkernel / Plug-in)**](https://github.com/donnemartin/system-design-primer#microkernel-architecture) - 适用于需要高度插件化、动态扩展的系统（如 IDE）。
- [ ] [**微服务架构 (Microservices)**](https://microservices.io/) - 通过独立部署的小服务解决复杂性与团队协作。
- [ ] [**事件驱动架构 (Event-Driven)**](https://aws.amazon.com/event-driven-architecture/) - 异步解耦的核心，通过 Event Bus 进行通信。
- [ ] [**空间驱动架构 (Space-Based)**](https://en.wikipedia.org/wiki/Space-based_architecture) - 解决极端高并发与数据一致性的利器。

---

## 🚀 分布式系统核心概念 (Distributed Systems)

- [ ] [**CAP 定理**](https://github.com/donnemartin/system-design-primer#cap-theorem) - 理解一致性 (C)、可用性 (A) 与分区容错性 (P) 之间的权衡。
- [ ] [**负载均衡 (Load Balancing)**](https://github.com/donnemartin/system-design-primer#load-balancer) - 掌握 L4 (TCP) 与 L7 (HTTP) 负载均衡的区别。
- [ ] [**缓存策略 (Caching)**](https://github.com/donnemartin/system-design-primer#cache) - Write-through, Write-around, Write-back 以及缓存失效策略。
- [ ] [**数据库分片与分区 (Sharding & Partitioning)**](https://github.com/donnemartin/system-design-primer#database) - 解决海量数据存储瓶颈的关键。

---

## 🛠️ 设计原则与最佳实践 (Principles)

- [ ] [**SOLID 原则**](https://en.wikipedia.org/wiki/SOLID) - 面向对象设计的黄金法则。
- [ ] [**十二要素应用 (The Twelve-Factor App)**](https://12factor.net/zh_cn/) - 构建现代化、可移植云原生应用的指导方针。
- [ ] [**领域驱动设计 (DDD)**](https://martinfowler.com/tags/domain%20driven%20design.html) - 处理复杂业务逻辑、划分限界上下文的有力工具。

---

## 💡 选型建议
1. **构建全新的初创 SaaS**：选 **Modular Monolith** 配合 **Next.js + Postgres**。
2. **高频交易或即时通讯系统**：优先考虑 **Event-Driven** 与 **WebSocket** 优化。
3. **海量图片/视频社交应用**：必须引入 **CDN + 分布式对象存储**。
4. **全球化低延迟服务**：选 **Edge Computing (Serverless)** 配合 **Global Replicated DB (如 Neon/PlanetScale)**。
