# Java (JDK 21+) 全栈开发资源精选 (2026 Checklist)

> [!TIP]
> **Indie Hacker Insight**: 2026 年，Java 已经通过 **Virtual Threads (Project Loom)** 彻底重塑了高并发编程模型。
> - **性能飞跃**：抛弃复杂的 WebFlux 响应式架构，回归简单的阻塞式编程，利用虚拟线程轻松处理百万级并发。
> - **云原生**：**GraalVM Native Image** 已成为标配，Java 应用的启动速度和内存占用现已可与 Go/Rust 媲美。
> - **工程化**：Spring Boot 3.x + JDK 21 是目前稳定性与开发效率的最佳平衡点。

---

## 🏗️ 核心框架与基础 (Core Frameworks)

- [ ] [**JDK 21 (LTS)**](https://adoptium.net/) - **[底座]** 必须使用 JDK 21+ 以获得虚拟线程和结构化并发支持。
- [ ] [**Spring Boot 3.3+**](https://spring.io/projects/spring-boot) - 行业标准，深度集成 GraalVM 原生镜像和虚拟线程。
- [ ] [**Quarkus**](https://quarkus.io/) - **[云原生首选]** 为 K8s 优化的超轻量级框架，启动极快。
- [ ] [**SDKMAN!**](https://sdkman.io/) - 命令行下的 Java 版本管理神器，一键切换不同供应商的 JDK。

---

## ⚡ 高并发与底层优化 (High Concurrency & Low Level)

- [ ] [**Virtual Threads**](https://docs.oracle.com/en/java/javase/21/core/virtual-threads.html) - 掌握 `Executors.newVirtualThreadPerTaskExecutor()`，这是 2026 年 Java 处理并发的标准方式。
- [ ] [**GraalVM**](https://www.graalvm.org/) - 将 Java 应用编译为原生二进制文件，适合 Serverless 和资源受限环境。
- [ ] [**Arthas**](https://github.com/alibaba/arthas) - **[排障神器]** 阿里开源的 Java 诊断工具，无需重启应用即可在线排查问题。

---

## 🛠️ 生产力工具库 (Productivity Libraries)

- [ ] [**MapStruct**](https://mapstruct.org/) - 编译时生成的对象转换器，性能远超反射，是 DTO 转换的首选。
- [ ] [**Caffeine**](https://github.com/ben-manes/caffeine) - 目前最强本地内存缓存，性能接近理论最优。
- [ ] [**Jackson**](https://github.com/FasterXML/jackson) - 依然是 JSON 处理的事实标准，但在高吞吐场景可考虑 **FastJSON2**。
- [ ] [**Resilience4j**](https://github.com/resilience4j/resilience4j) - 轻量级熔断限流库，完美替代已停更的 Hystrix。

---

## 📂 数据库与持久化 (Database & Persistence)

- [ ] [**HikariCP**](https://github.com/brettwooldridge/HikariCP) - 极其纯粹、高性能的数据库连接池。
- [ ] [**Flyway**](https://flywaydb.org/) - 数据库版本管理工具，让数据库变更像代码 Git 提交一样可追溯。
- [ ] [**Testcontainers**](https://www.testcontainers.org/) - 在测试中自动通过 Docker 启动真实的 MySQL/Redis，解决“测试环境不一致”的问题。

---

## 💡 选型建议
1. **构建传统企业级 Web 服务**：选 **Spring Boot 3** + **JDK 21 (Virtual Threads)** + **HikariCP**。
2. **构建极致冷启动的云函数**：选 **Quarkus** + **GraalVM Native Image**。
3. **处理超大规模并发流量**：选 **Project Reactor (WebFlux)** 或最新的 **Virtual Threads**。
4. **快速定位线上 Bug**：必装 **Arthas**。
