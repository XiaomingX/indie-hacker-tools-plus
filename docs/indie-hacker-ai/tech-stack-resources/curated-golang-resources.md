# Golang 生态资源 (2026 Checklist)

> [!TIP]
> **Indie Hacker Insight**: 2026 年的 Go 语言是**高性能后端与边缘计算**的首选。
> - **AI 集成**：利用 **LangChainGo** 快速接入 LLM。
> - **全栈选型**：利用 **Wails** 使用 Go + 前端技术构建极轻量的跨平台桌面应用。
> - **微服务首选**：Go 的天然并发优势使其在处理高并发 AI 推理请求时表现卓越。

---

## 🧠 AI、大模型与分布式 (AI & Distributed)

- [ ] [**LangChainGo**](https://github.com/tmc/langchaingo) - 在 Go 中构建 LLM 应用的首选框架。
- [ ] [**LocalAI**](https://github.com/mudler/LocalAI) - 本地 AI 模型的 Go 语言封装，OpenAI API 的完美替代。
- [ ] [**Ergo**](https://github.com/ergo-services/ergo) - 灵感来自 Erlang 的 Actor 模型框架，构建高可靠分布式系统。
- [ ] [**Go-Kit**](https://github.com/go-kit/kit) - 微服务开发的工具集，适合大型工程。

---

## 🌐 Web 框架与认证 (Web & Auth)

- [ ] [**Gin**](https://github.com/gin-gonic/gin) - 依然是社区最活跃、生态最全的 Web 框架。
- [ ] [**Fiber**](https://github.com/gofiber/fiber) - 基于 fasthttp，追求极致性能的 Web 框架。
- [ ] [**Casbin**](https://github.com/casbin/casbin) - 强大且灵活的访问控制（RBAC, ABAC）库。
- [ ] [**Goth**](https://github.com/markbates/goth) - 一站式多平台 OAuth 登录库。

---

## 🗄️ 数据库与持久化 (Database & ORM)

- [ ] [**GORM**](https://github.com/go-gorm/gorm) - 功能最全、使用最广的 Go ORM 库。
- [ ] [**Ent**](https://entgo.io/) - Facebook 出品的基于图结构的实体框架，类型安全且易于维护。
- [ ] [**Bbolt**](https://github.com/etcd-io/bbolt) - 经典的嵌入式键值数据库，etcd 的底层支撑。
- [ ] [**Badger**](https://github.com/dgraph-io/badger) - 高性能、事务型的嵌入式存储引擎。

---

## 🖥️ 桌面应用与 GUI (Desktop & GUI)

- [ ] [**Wails**](https://wails.io) - 2026 年最火的 Go 桌面方案，前端技术 + Go 后端。
- [ ] [**Fyne**](https://github.com/fyne-io/fyne) - 原生的跨平台 GUI 库，适合工具类应用开发。

---

## 🛠️ 开发提效与命令行 (Productivity)

- [ ] [**Cobra**](https://github.com/spf13/cobra) - 构建现代 CLI 应用的事实标准（Docker, Kubernetes 都在用）。
- [ ] [**Viper**](https://github.com/spf13/viper) - 功能极其强大的配置管理工具。
- [ ] [**Air**](https://github.com/cosmtrek/air) - 开发时的代码热重载神器。
- [ ] [**Zap**](https://github.com/uber-go/zap) - Uber 出品的极速结构化日志库。

---

## 💡 选型建议
1. **构建高性能 API 服务**：选 **Gin** 或 **Fiber**。
2. **快速开发全栈桌面应用**：选 **Wails**。
3. **需要复杂的权限管理系统**：集成 **Casbin**。
4. **开发 AI 代理 (Agent)**：首选 **LangChainGo**。
