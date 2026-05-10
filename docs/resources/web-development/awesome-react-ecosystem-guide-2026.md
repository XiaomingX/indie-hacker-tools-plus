# 2026 React 全栈开发生态指南 (Checklist)

> [!TIP]
> **Indie Hacker Insight**: 2026 年，React 的开发重心已从单纯的客户端渲染 (CSR) 彻底转向 **服务器端组件 (RSC)** 与 **Streaming**。
> - **全栈框架**：Next.js 已成为构建生产级 React 应用的事实标准，单纯的 Vite + React 仅适用于内网工具。
> - **状态管理**：随着 RSC 的普及，传统的 Redux 正在边缘化，取而代之的是更加轻量的 **Zustand** 或高度集成的 **React Query (TanStack)**。
> - **性能优化**：关注 React 19+ 的 **Compiler (Forget)** 带来的自动记忆化，不再需要手写 `useMemo` 和 `useCallback`。

---

## 🏗️ 全栈框架与渲染 (Frameworks)

- [ ] [**Next.js (App Router)**](https://nextjs.org/) - **[行业标准]** 深度集成 RSC、Streaming 与 Server Actions。
- [ ] [**Remix**](https://remix.run/) - 专注 Web 标准与极致的并行加载性能。
- [ ] [**TanStack Start**](https://tanstack.com/start) - 基于 TanStack Router 的新兴全栈方案，类型安全度极高。
- [ ] [**Vite**](https://vitejs.dev/) - 依然是构建快速原型与客户端渲染应用的最佳工具。

---

## 🛠️ 数据流与状态管理 (State Management)

- [ ] [**TanStack Query (React Query)**](https://tanstack.com/query) - 处理服务端状态同步、缓存与乐观更新的必备库。
- [ ] [**Zustand**](https://github.com/pmndrs/zustand) - 极致简单、无样板代码的客户端状态管理方案。
- [ ] [**Jotai**](https://jotai.org/) - 基于原子（Atoms）的状态管理，非常适合复杂的交互界面。
- [ ] [**Valtio**](https://valtio.pmndrs.org/) - 利用代理（Proxy）实现的响应式状态管理，体验极佳。

---

## 🎨 UI 组件库与样式 (UI & Styling)

- [ ] [**Tailwind CSS**](https://tailwindcss.com/) - **[必选]** 现代 Web 开发的样式底座。
- [ ] [**Shadcn/UI**](https://ui.shadcn.com/) - 基于 Radix UI 的可直接复制代码的组件库。
- [ ] [**Framer Motion**](https://www.framer.com/motion/) - React 动画的首选，支持极佳的声明式交互。
- [ ] [**Lucide React**](https://lucide.dev/) - 清爽、一致且高性能的图标库。

---

## 🧪 测试、质量与工具 (Testing & Quality)

- [ ] [**Playwright**](https://playwright.dev/) - 现代化的 E2E 测试框架，支持自动录制。
- [ ] [**Vitest**](https://vitest.dev/) - 基于 Vite 的极速单元测试框架，完全兼容 Jest。
- [ ] [**ESLint + Prettier**](https://eslint.org/) - 保持代码质量与风格统一的基石。
- [ ] [**React DevTools**](https://react.dev/learn/react-developer-tools) - 调试组件渲染性能的必备插件。

---

## 💡 选型建议
1. **构建 SEO 敏感的应用 (SaaS/博客)**：强制选 **Next.js 15+**。
2. **构建高交互、纯客户端应用**：选 **Vite + React + Zustand**。
3. **极高性能要求的管理后台**：选 **TanStack Router + TanStack Table**。
4. **移动优先项目**：考虑使用 **Expo (React Native)** 实现跨端代码复用。
