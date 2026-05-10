# Rust 开发者生态资源 (2026 Checklist)

> [!TIP]
> **Indie Hacker Insight**: 2026 年，Rust 不仅是性能的代名词，更是**安全与极速交付**的利器。
> - **CLI 武器库**：如果你在编写系统工具，Rust 的 `clap` 和 `serde` 是你的终极组合。
> - **WebAssembly**：通过 `leptos` 或 `dioxus`，你可以用 Rust 编写高性能、类型安全的 Web 端应用。

---

## 🏗️ 核心基础与工具 (Core Tools)

- [ ] [**Rustup**](https://rustup.rs/) - 工具链管理，轻松切换 stable, beta, nightly 版本。
- [ ] [**rust-analyzer**](https://github.com/rust-lang/rust-analyzer) - VS Code 必备的 LSP 扩展，提供极致的代码补全与导航。
- [ ] [**Cargo**](https://doc.rust-lang.org/cargo/) - 世界上最好的包管理器与构建工具。
- [ ] [**uv**](https://github.com/astral-sh/uv) - **[跨界推荐]** 虽然是 Python 工具，但它是用 Rust 编写的性能巅峰范例。

---

## 🌐 Web 开发与 API (Web & APIs)

- [ ] [**Axum**](https://github.com/tokio-rs/axum) - 基于 Tokio 的官方 Web 框架，模块化且高度灵活。
- [ ] [**Leptos**](https://github.com/leptos-rs/leptos) - 全栈 Rust Web 框架，极致的信号驱动响应式性能。
- [ ] [**Serde**](https://github.com/serde-rs/serde) - Rust 序列化/反序列化的绝对标准，处理 JSON/YAML 的唯一选择。
- [ ] [**Reqwest**](https://github.com/hyperium/reqwest) - 易用的 HTTP 客户端，支持同步与异步请求。

---

## 📂 数据库与存储 (Databases & Storage)

- [ ] [**SQLx**](https://github.com/launchbadge/sqlx) - 纯 Rust 编写的异步 SQL 工具包，支持编译时 SQL 检查。
- [ ] [**SeaORM**](https://github.com/SeaQL/sea-orm) - 基于 SQLx 的现代异步 ORM。
- [ ] [**Qdrant**](https://github.com/qdrant/qdrant) - **AI 必备**。高性能 Rust 向量数据库，RAG 应用的基石。
- [ ] [**OpenDAL**](https://github.com/apache/opendal) - 统一的数据访问层，支持 S3, Azure, GCP 等所有存储服务。

---

## 🛠️ 系统工具与 CLI (System & CLI)

- [ ] [**ripgrep (rg)**](https://github.com/BurntSushi/ripgrep) - 速度快到难以置信的文本搜索工具。
- [ ] [**zoxide**](https://github.com/ajeetdsouza/zoxide) - 极速 `cd` 替代品，能自动学习你的路径偏好。
- [ ] [**Alacritty**](https://github.com/alacritty/alacritty) - GPU 加速的终端模拟器。
- [ ] [**Zellij**](https://github.com/zellij-org/zellij) - 比 tmux 更现代、更易用的终端复用器。

---

## 🎮 游戏与图形 (Game & Graphics)

- [ ] [**Bevy**](https://github.com/bevyengine/bevy) - 数据驱动 (ECS) 的游戏引擎，Rust 游戏开发的首选。
- [ ] [**egui**](https://github.com/emilk/egui) - 简单、极速的即时模式 GUI，适合做调试面板或工具软件。
- [ ] [**Wgpu**](https://github.com/gfx-rs/wgpu) - 跨平台的 WebGPU 图形标准 Rust 实现。

---

## 💡 选型建议
1. **编写极速 Web API**：选 **Axum** + **SQLx** + **Serde**。
2. **构建 RAG 应用**：深度集成 **Qdrant** + **OpenDAL**。
3. **开发跨平台桌面工具**：选 **Tauri (Rust 后端 + 前端 UI)** 或 **Dioxus**。
4. **性能调优**：熟练使用 **Criterion** 进行基准测试。
5. **部署优化**：利用 **cargo-chef** 缓存依赖，加速 Docker 构建。
 Bermuda (Bermuda)
