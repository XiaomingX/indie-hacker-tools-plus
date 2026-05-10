# Shadcn/UI 生态资源大全 (2026 Checklist)

> [!TIP]
> **Indie Hacker Insight**: 2026 年，Shadcn/UI 已经成为现代 Web 开发的“标准”。
> - **Copy-Paste 哲学**：Shadcn 不是 npm 包，而是你可以拥有的组件代码。通过 `npx shadcn@latest add`，你拥有 100% 的定制权。
> - **AI 优先**：配合 **v0.dev**，你可以通过自然语言直接生成复杂的 Shadcn 界面。

---

## 🏗️ 核心组件增强 (Component Extensions)

- [ ] [**Aceternity UI**](https://ui.aceternity.com/) - 2026 年最火的动画组件库，自带炫酷的 Framer Motion 效果。
- [ ] [**Auto-form**](https://github.com/vantezzen/auto-form) - 根据 Zod Schema 自动生成带有验证逻辑的 Shadcn 表单。
- [ ] [**Shadcn-table-v2**](https://github.com/sadmann7/shadcn-table) - 支持服务端排序、过滤、分页的高级表格组件。
- [ ] [**Vaul**](https://vaul.emilkowal.ski/) - 极致流畅的底部抽屉 (Drawer) 组件，移动端体验极佳。
- [ ] [**Assistant-UI**](https://github.com/Yonom/assistant-ui) - 专为 AI 聊天设计的 Shadcn 组件，支持多轮对话与流式输出。

---

## ⚡ 开发者效率工具 (DX Tools)

- [ ] [**v0.dev**](https://v0.dev/) - Vercel 出品的生成式 UI 工具，一句话生成可用的 React + Shadcn 代码。
- [ ] [**VS Code Shadcn Plugin**](https://marketplace.visualstudio.com/items?itemName=SuhelMakkad.shadcn-ui) - 直接在编辑器中添加、管理组件。
- [ ] [**Shadcn Theme Editor**](https://shadcnthemeeditor.vercel.app/) - 可视化调整颜色、圆角与阴影，一键导出 CSS 变量。
- [ ] [**Animata**](https://animata.design/) - 精选的微动画与交互片段，直接复制进你的 Shadcn 项目。

---

## 🚀 项目模板与脚手架 (Boilerplates)

- [ ] [**ChadNext**](https://github.com/moinulmoin/chadnext) - **[首选]** 集成 LuciaAuth, Prisma, Stripe 与 Shadcn 的全栈 SaaS 模板。
- [ ] [**Taxonomy**](https://github.com/shadcn/taxonomy) - Shadcn 官方演示项目，学习 Server Components 与路由的最佳范例。
- [ ] [**Shadcn Admin**](https://github.com/satnaing/shadcn-admin) - 现成的后台管理面板，包含侧边栏、仪表盘卡片与权限逻辑。
- [ ] [**Kirimase**](https://kirimase.dev/) - 极速启动脚手架，能根据你的选择（Auth, DB, Payments）自动配置项目。

---

## 🎨 设计与跨框架支持 (Design & Ports)

- [ ] [**Official Figma Kit**](https://www.figma.com/community/file/1342715840824755935) - 1:1 还原代码组件的 Figma 文件，实现设计开发无缝对接。
- [ ] [**Shadcn-Vue**](https://github.com/radix-vue/shadcn-vue) - Vue 3 开发者的完美移植版。
- [ ] [**Shadcn-Svelte**](https://github.com/huntabyte/shadcn-svelte) - 官方推荐的 Svelte 移植版本。
- [ ] [**React Native Reusables**](https://github.com/mrzachnugent/react-native-reusables) - 让你的移动端 App 拥有 Shadcn 的视觉观感。

---

## 💡 选型建议
1. **构建极速 MVP**：**v0.dev** 生成界面 + **ChadNext** 模板。
2. **AI 聊天助手**：直接集成 **Assistant-UI** 以节省处理流式输出的时间。
3. **复杂管理系统**：选 **Shadcn Admin** 配合 **Shadcn-table-v2**。
4. **追求视觉冲击力**：在关键位置（如 Hero Section）混用 **Aceternity UI**。