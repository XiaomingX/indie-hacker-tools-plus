# SwiftUI 现代开发资源精选 (2026 Checklist)

> [!TIP]
> **Indie Hacker Insight**: 2026 年，SwiftUI 已成为苹果全生态（iPhone, Mac, iPad, Vision Pro）的 **"唯一真理"**。
> - **状态管理**：全面转向 **Observation** 框架，抛弃过时的 `@Published` 和 `ObservableObject`，让视图刷新更精准、更高效。
> - **空间计算**：利用 **VisionOS** 的新特性，你的 SwiftUI 应用可以轻松实现“窗口深度”与“体积化”交互。
> - **持久化**：无脑选择 **SwiftData**，它是 Core Data 的现代替代品，与 SwiftUI 声明式风格完美契合。

---

## 🏗️ 官方教程与核心文档 (Core & Official)

- [ ] [**SwiftUI 官方教程**](https://developer.apple.com/tutorials/swiftui) - **[权威]** 包含从基础布局到交互逻辑的动态小案例。
- [ ] [**iOS App 开发实战 (含 SwiftUI)**](https://developer.apple.com/tutorials/app-dev-training/) - 通过构建一个完整应用来掌握数据处理、布局与上架流程。
- [ ] [**SwiftUI 性能优化专题 (WWDC)**](https://developer.apple.com/videos/play/wwdc2023/10164/) - 解决“视图重复刷新”和“布局卡顿”的必读课。
- [ ] [**Observation 框架解析**](https://developer.apple.com/videos/play/wwdc2023/10149/) - 学习 iOS 17+ 引入的下一代数据观察模型。

---

## 🛠️ 必装开源库 (Essential Libraries)

- [ ] [**Kingfisher**](https://github.com/onevcat/Kingfisher) - **[首选]** SwiftUI 图片异步加载与缓存的事实标准。
- [ ] [**TCA (The Composable Architecture)**](https://github.com/pointfreeco/swift-composable-architecture) - 针对复杂大型项目，提供可预测、可测试的状态管理架构。
- [ ] [**Lottie for SwiftUI**](https://github.com/airbnb/lottie-ios) - 轻松集成高质量的矢量动画（AE 导出）。
- [ ] [**AlertToast**](https://github.com/elai950/AlertToast) - 仿苹果原生样式的极简提示框（Toast）。

---

## 🎨 动效与 UI 增强 (UI & Animation)

- [ ] [**SwiftUI-Animations**](https://github.com/Shubham0812/SwiftUI-Animations) - 收集了 100+ 实战动画案例，可直接复制使用。
- [ ] [**WaterfallGrid**](https://github.com/paololeonardi/WaterfallGrid) - 快速实现“瀑布流”布局，补齐 SwiftUI 原生网格的短板。
- [ ] [**SkeletonUI**](https://github.com/CSolanaM/SkeletonUI) - 为数据加载过程提供优雅的“骨架屏”占位效果。

---

## 📂 样例项目与实战 (Sample Projects)

- [ ] [**MovieSwiftUI**](https://github.com/Dimillian/MovieSwiftUI) - 学习网络请求封装、列表懒加载与复杂页面布局的典范。
- [ ] [**ControlRoom**](https://github.com/twostraws/ControlRoom) - 一个由 SwiftUI 开发的 macOS 生产力工具，学习跨端 UI 设计。

---

## 💡 选型建议
1. **构建全新的个人 App**：选 **SwiftUI** + **SwiftData** + **Observation**。
2. **需要处理超复杂状态流**：选 **TCA 架构**。
3. **适配 Vision Pro 空间计算**：关注 **RealityKit** 与 SwiftUI 的混合渲染。
4. **追求极致加载体验**：必装 **Kingfisher** 和 **SkeletonUI**。
