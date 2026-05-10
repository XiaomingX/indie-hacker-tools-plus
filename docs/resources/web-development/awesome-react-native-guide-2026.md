# 2026 React Native 跨端移动开发指南 (Checklist)

> [!TIP]
> **Indie Hacker Insight**: 2026 年，React Native 已经完全进入了 **New Architecture (Fabric/TurboModules)** 时代。
> - **Expo 优先**：除非你有极其特殊的 Native 模块定制需求，否则 **Expo** 始终是首选，它极大简化了开发、构建（EAS）与分发流程。
> - **性能调优**：利用 **FlashList** 替代 FlatList，使用 **Reanimated 3** 处理 60FPS 的复杂动画。
> - **代码复用**：通过 **Solito** 或 **Tamagui**，可以实现 Web 与 Mobile 之间 80% 以上的 UI 逻辑复用。

---

## 🏗️ 核心框架与工作流 (Core & Workflow)

- [ ] [**Expo SDK (Latest)**](https://expo.dev/) - **[必选]** 提供开箱即用的开发体验与 EAS 构建服务。
- [ ] [**React Native 官方文档**](https://reactnative.dev/) - 重点理解新架构的渲染模型与 JSI。
- [ ] [**Expo Router**](https://docs.expo.dev/router/introduction/) - 基于文件系统的路由，完美支持 Web、iOS 和 Android。
- [ ] [**TypeScript**](https://www.typescriptlang.org/) - 现代移动开发的标准配置，严禁使用 JS。

---

## 🛠️ 核心 UI 与交互 (UI & Interaction)

- [ ] [**Tamagui**](https://tamagui.dev/) - **[推荐]** 支持跨端优化的 UI 套件，拥有极佳的性能与类型提示。
- [ ] [**React Native Reanimated**](https://docs.swmansion.com/react-native-reanimated/) - 处理复杂高性能动画的行业标准。
- [ ] [**FlashList (Shopify)**](https://shopify.github.io/flash-list/) - 极速列表渲染，彻底告别 FlatList 的卡顿感。
- [ ] [**React Native Gesture Handler**](https://docs.swmansion.com/react-native-gesture-handler/) - 提供原生的手势交互体验。

---

## ⚡ 数据持久化与功能扩展 (Persistence & Features)

- [ ] [**WatermelonDB**](https://nozbe.github.io/WatermelonDB/) - 支持大规模数据量的离线优先数据库，响应极快。
- [ ] [**MMKV**](https://github.com/mrousavy/react-native-mmkv) - 目前最快的 Key-Value 存储方案，远超 AsyncStorage。
- [ ] [**TanStack Query (React Query)**](https://tanstack.com/query) - 移动端远程状态管理与网络请求缓存。
- [ ] [**React Native VisionCamera**](https://github.com/mrousavy/react-native-vision-camera) - 功能强大的原生摄像头框架，支持二维码扫描与 AI 实时滤镜。

---

## 💡 选型建议
1. **构建全新的初创项目**：强制选 **Expo + Expo Router + Tamagui**。
2. **需要极高性能的长列表（如电商/社交）**：强制使用 **FlashList**。
3. **注重离线使用的应用**：选 **WatermelonDB**。
4. **全量跨端项目 (Web + Mobile)**：选 **Solito** 配合 Next.js。
