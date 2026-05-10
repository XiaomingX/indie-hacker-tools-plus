# 2026 React Server Components (RSC) 深度实战指南 (Checklist)

> [!TIP]
> **Indie Hacker Insight**: 2026 年，RSC 已成为 Next.js 开发的默认心法。
> - **性能鸿沟**：通过将非交互逻辑移至服务端，你可以减少 70% 以上的客户端 JavaScript 负载。
> - **安全边界**：数据库查询和 API 密钥应仅存在于 Server Components 中，永远不要暴露给浏览器。
> - **组合优于嵌套**：将 Client Components 放在组件树的末端，通过 `children` 属性传递 Server Components，以保持最大的服务端渲染比例。

---

## 🏗️ 核心概念与选型 (Core Concepts)

- [ ] [**React Server Components 官方综述**](https://react.dev/reference/rsc/server-components) - 理解服务端组件与客户端组件的根本区别。
- [ ] [**Next.js RSC 最佳实践**](https://nextjs.org/docs/app/building-your-application/rendering/server-components) - 如何在 App Router 中高效利用渲染流水线。
- [ ] **区分指令**：
    - [ ] `use client`：标记组件及其子树在客户端运行。
    - [ ] `server-only`：**[必备]** 确保敏感逻辑（如 DB 查询）绝不被错误引入客户端。

---

## ⚡ 实战技巧与优化 (Practical Tips)

- [ ] **数据获取 (Data Fetching)**：直接在异步 Server Components 中使用 `await` 获取数据，无需 `useEffect`。
- [ ] **首屏渲染 (LCP) 优化**：将静态部分（如导航、页脚）设为 Server Components，实现接近瞬时的 HTML 呈现。
- [ ] **交互逻辑隔离**：仅在需要 `useState`, `useEffect` 或浏览器 API（如 `window`）时才使用 Client Components。
- [ ] **序列化限制**：确保从 Server 传递到 Client 组件的 Props 是可序列化的（避免传递函数或复杂的 Class 实例）。

---

## 🛡️ 安全与工程化 (Security & Tooling)

- [ ] **环境变量保护**：仅在 Server Components 中访问不带 `NEXT_PUBLIC_` 前缀的环境变量。
- [ ] **Context 桥接**：利用客户端组件作为 `Provider` 包裹服务器组件，实现全局状态共享。
- [ ] **Suspense 颗粒度**：利用 `Suspense` 包裹耗时的数据请求组件，实现流式渲染 (Streaming)。

---

## 💡 选型建议
1. **构建纯展示性页面**：100% 使用 **Server Components**。
2. **构建复杂的交互式表单**：外层容器用 **Server Component**，内部 Form 元素用 **Client Component**。
3. **需要 SEO 且包含动态数据**：使用 **Server Components** 进行服务端预渲染。
4. **性能调优**：利用 `server-only` 库强制执行组件边界，防止 JS 束体积膨胀。