# Flutter 跨平台开发资源精选 (2026 Checklist)

> [!TIP]
> **Indie Hacker Insight**: 2026 年，Flutter 已成为**“全平台分发”**的终极武器。
> - **渲染进化**：**Impeller** 引擎已全面成熟，彻底解决了 iOS 上的着色器编译卡顿问题。
> - **AI 集成**：利用 **Google AI Edge SDK**，可以在 Flutter 应用中直接运行本地推理。
> - **桌面级体验**：Flutter 在 Windows 和 macOS 上的表现已接近原生，适合构建跨平台的生产力工具。

---

## 🏗️ 核心框架与入门 (Core & Getting Started)

- [ ] [**Flutter 官方文档**](https://docs.flutter.dev/) - **[权威]** 包含从环境配置到各平台发布的完整指南。
- [ ] [**Flutter Journey**](https://flutter.dev/learn) - 官方学习路径，适合零基础开发者系统入门。
- [ ] [**Flutter 3.x 新特性解析**](https://medium.com/flutter) - 关注 **Impeller**、**Wasm** 支持以及 **Macros**（宏）带来的开发体验提升。
- [ ] [**Dart 官方文档**](https://dart.dev/) - 掌握 Flutter 的基石语言，重点关注空安全和异步编程。

---

## ⚡ 状态管理与架构 (State & Architecture)

- [ ] [**Riverpod**](https://riverpod.dev/) - **[2026 推荐]** 无需 context、类型安全、且高度可测试，是目前最优雅的状态管理方案。
- [ ] [**Bloc / Cubit**](https://bloclibrary.dev/) - 适合大型复杂项目，逻辑与 UI 彻底分离，状态流转极度严谨。
- [ ] [**GetX**](https://pub.dev/packages/get) - **[极速开发]** 集成了路由、状态管理和依赖注入，适合快速验证 MVP。
- [ ] [**Clean Architecture**](https://github.com/ResoCoder/flutter-tdd-clean-architecture-course) - 学习如何构建可维护、可测试的企业级应用架构。

---

## 🎨 UI 组件与动效 (UI & Animation)

- [ ] [**Shadcn UI (Flutter Port)**](https://github.com/danon/shadcn-ui) - 2026 年最火的 UI 风格，现已完美适配 Flutter。
- [ ] [**Drei (R3F 类似物)**](https://github.com/pmndrs/drei-flutter) - 在 Flutter 中实现高保真 3D 交互的工具库。
- [ ] [**Lottie for Flutter**](https://pub.dev/packages/lottie) - 轻松集成高质量的 AE 动画，提升 App 质感。
- [ ] [**Rive**](https://rive.app/flutter) - 下一代交互式矢量动画工具，完美替代 Flash。

---

## 🛠️ 工程化与效率 (Tooling & DevOps)

- [ ] [**FlutterFlow**](https://flutterflow.io/) - **[低代码首选]** 可视化构建 UI 并直接导出高质量的 Flutter 代码。
- [ ] [**Shorebird**](https://shorebird.dev/) - **[热更新]** 官方团队成员出品，为 Flutter 应用提供极其丝滑的代码热修复能力。
- [ ] [**Appflowy**](https://github.com/AppFlowy-IO/appflowy) - **[参考案例]** 顶级开源项目（Notion 替代品），学习复杂 Flutter 应用架构的典范。
- [ ] [**Cider**](https://github.com/f-pazos/cider) - 自动管理 pubspec.yaml 的版本号和发布流程。

---

## 💡 选型建议
1. **构建高性能商业应用**：选 **Riverpod** + **GoRouter** + **Firebase/Supabase**。
2. **快速交付营销类应用**：选 **FlutterFlow** + **GetX**。
3. **开发跨平台生产力软件**：关注 **Fluent UI** (Windows) 或 **Macos UI** (macOS) 风格库。
4. **极致性能要求的渲染**：强制开启 **Impeller** 引擎并使用 **Wasm** 编译。
