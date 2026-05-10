# Kotlin & Android 全栈开发资源精选 (2026 Checklist)

> [!TIP]
> **Indie Hacker Insight**: 2026 年，Kotlin 已经通过 **Compose Multiplatform (CMP)** 实现了真正的“写一次，处处运行”。
> - **跨平台分发**：不再局限于 Android，利用 CMP 可以同时发布到 iOS、Web 和桌面端，极大降低独立开发的维护成本。
> - **架构选型**：无脑选择 **MVI (Model-View-Intent)** 架构配合 **Kotlin Flow**，这是目前处理复杂 UI 状态最稳定、最可预测的方案。
> - **构建工具**：全面拥抱 **Kotlin DSL** 和 **Version Catalogs**，保持 Gradle 配置的优雅与一致性。

---

## 🏗️ 核心框架与基础 (Core & Multplatform)

- [ ] [**Kotlin 官方文档**](https://kotlinlang.org/docs/home.html) - **[权威]** 包含从基础语法到协程、多平台开发的完整指南。
- [ ] [**Compose Multiplatform**](https://www.jetbrains.com/lp/compose-multiplatform/) - **[2026 推荐]** JetBrains 出品的 UI 框架，支持一套代码搞定 Android, iOS, Desktop 和 Web。
- [ ] [**Ktor**](https://ktor.io/) - 极轻量级的异步网络框架，既能写高性能后端服务器，也能作为跨平台 HTTP 客户端。
- [ ] [**kotlinx.coroutines**](https://github.com/Kotlin/kotlinx.coroutines) - Kotlin 并发编程的核心，掌握 Flow 和 Channel 是进阶必备。

---

## ⚡ Android 现代开发组件 (Android Modern Stack)

- [ ] [**Jetpack Compose**](https://developer.android.com/jetpack/compose) - Android 原生 UI 开发的唯一标准，声明式编程极大提升了 UI 构建速度。
- [ ] [**Coil**](https://github.com/coil-kt/coil) - 基于协程的图片加载库，轻量且完美适配 Compose。
- [ ] [**Hilt**](https://developer.android.com/training/dependency-injection/hilt-android) - Google 推荐的依赖注入方案，基于 Dagger 但上手更简单。
- [ ] [**LeakCanary**](https://github.com/square/leakcanary) - 内存泄漏检测的神器，独立开发者保障 App 稳定性的底线。

---

## 🛠️ 工程化与效率工具 (Tooling & Quality)

- [ ] [**ktlint**](https://github.com/pinterest/ktlint) - 自动纠正代码风格，让你的 Kotlin 代码符合行业标准。
- [ ] [**detekt**](https://github.com/detekt/detekt) - 静态代码分析工具，自动揪出代码里的“坏味道”和潜在 Bug。
- [ ] [**SQLDelight**](https://github.com/cashapp/sqldelight) - 从 SQL 语句生成类型安全的代码，跨平台本地存储的首选。

---

## 📂 样例项目与实战 (Sample Projects)

- [ ] [**Sunflower**](https://github.com/android/sunflower) - Google 官方出品，学习 Jetpack 各种组件协作的最佳案例。
- [ ] [**Tivi**](https://github.com/chrisbanes/tivi) - 一个完整的开源项目，展示了如何在大型应用中优雅地使用 Compose、Retrofit 和 Room。
- [ ] [**Compose Samples**](https://github.com/android/compose-samples) - 涵盖从简单布局到复杂动效的所有 Compose 官方示例。

---

## 💡 选型建议
1. **构建全新的跨平台 MVP**：选 **Compose Multiplatform** + **Koin (DI)** + **Ktor (Network)**。
2. **重构老旧的 Android 应用**：分步引入 **Jetpack Compose**，使用 **Hilt** 进行依赖注入。
3. **追求极致的本地数据性能**：选 **SQLDelight** 配合 **Kotlin Flow**。
4. **提升团队开发效率**：强制集成 **ktlint** 和 **detekt** 到 CI 流水线。
