# Firebase 全栈开发资源精选 (2026 Checklist)

> [!TIP]
> **Indie Hacker Insight**: 2026 年，Firebase 依然是独立开发者实现 **"一人公司"** 的顶级利器。
> - **无服务器化**：利用 **Genkit** 快速将 AI 模型集成到你的 Firebase 工作流中。
> - **数据分析**：务必开启 **BigQuery** 导出，AI 时代的竞争本质上是数据颗粒度的竞争。
> - **成本控制**：关注 **App Check**，防止 API 被盗刷导致天价账单。

---

## 🏗️ 核心框架与入门 (Core & Getting Started)

- [ ] [**Firebase 官方文档**](https://firebase.google.com/docs) - **[权威]** 包含从身份验证到高性能数据库的所有模块指南。
- [ ] [**Firebase CLI**](https://github.com/firebase/firebase-tools) - **[工具]** 管理、部署及运行模拟器 (Emulators) 的核心命令行工具。
- [ ] [**Firebase 模拟器套件**](https://firebase.google.com/docs/emulator-suite) - **[推荐]** 在本地完成开发与测试，节省云端配额且响应极快。
- [ ] [**Firebase Genkit**](https://firebase.google.com/docs/genkit) - **2026 重点**。Google 推出的 AI 开发框架，支持在 Firebase 中快速编排 Agent。

---

## ⚡ 前端集成与 SDK (Frontend Integrations)

- [ ] [**ReactFire**](https://github.com/FirebaseExtended/reactfire) - 官方出品，为 React 提供 Suspense 支持和极致的 Hooks 体验。
- [ ] [**React Native Firebase**](https://rnfirebase.io/) - 移动端全栈开发的金标准，完美适配 iOS 与 Android 的各种系统能力。
- [ ] [**VueFire**](https://vuefire.vuejs.org/) - 为 Vue 3 提供实时响应式绑定。
- [ ] [**AngularFire**](https://github.com/angular/angularfire) - 针对 Angular 的官方封装。

---

## 🚀 云函数与扩展 (Functions & Extensions)

- [ ] [**Firebase Extensions**](https://firebase.google.com/products/extensions) - **[提效]** 一键部署 Stripe 支付、Algolia 搜索、图片缩略图生成等功能。
- [ ] [**Firebase Functions 示例**](https://github.com/firebase/functions-samples) - 涵盖从触发器到自定义 API 的各种实战场景。
- [ ] [**Firebase App Distribution**](https://firebase.google.com/products/app-distribution) - 极速分发 iOS/Android 测试包给种子用户。

---

## 🎓 学习与社区 (Learning)

- [ ] [**Fireship (YouTube)**](https://www.youtube.com/@Fireship) - 全网公认最好的 Firebase 教程频道，风格极简高效。
- [ ] [**Firebase 官方 YouTube**](https://www.youtube.com/user/Firebase) - 了解产品路线图与底层技术的最佳窗口。

---

## 💡 选型建议
1. **快速上线个人 SaaS**：选 **Next.js** + **ReactFire** + **Firestore** + **Stripe Extension**。
2. **需要处理海量社交数据**：选 **Realtime Database** (极低延迟)。
3. **构建 AI 驱动的应用**：重点参考 **Genkit** 教程。
4. **节省预算**：在开发阶段全程使用 **Emulator Suite**。
