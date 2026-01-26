高价值：否

标题：
Next.js PPR：结合静动态渲染，优化网页性能的实验性功能

### 部分预渲染（PPR）：Next.js 中的优化渲染方案

#### 开篇：主题与背景
部分预渲染（Partial Prerendering，简称 PPR）是 Next.js 框架里一项实验性功能，其背景是为了优化网页的渲染方式，目标是融合静态渲染（Static Site Generation，SSG）和动态渲染（Server-Side Rendering，SSR）的长处。

#### 技术要点详解
##### 1. 静态与动态结合
PPR 能让同一个页面同时有静态和动态组件。Next.js 会尽力多预渲染页面的静态部分。当检测到动态代码，比如读取请求信息时，能用 React 的 `<Suspense>` 组件把动态组件包起来。打个比方，就像你在看一个网页，静态的部分先展现出来，动态的部分用 `<Suspense>` 来处理，在它加载时显示备用内容，优化用户体验。

##### 2. 预渲染与流式传输
构建的时候，Next.js 会预渲染尽可能多的路由。对于动态内容，Next.js 先返回静态 HTML，接着在同一次 HTTP 请求里，通过流式传输动态替换静态内容。这就好比先给你一个大体的框架，然后慢慢把动态的细节填充进去。

##### 3. 单一 HTTP 请求
PPR 想要避免给每个动态组件创建多个 HTTP 请求，而是把静态预渲染的内容和动态组件合并到单个 HTTP 请求中，减少网络请求次数。举个例子，本来可能得发好几个请求，现在一个就行，提高了效率。

##### 4. 增量应用
在 Next.js 15 的 canary 版本中，PPR 作为实验性功能提供。要启用 PPR，得在 `next.config.js` 文件里把 `ppr` 选项设为 `incremental`，还得在页面顶部声明 `experimental_ppr`。像这样：
```typescript
// next.config.js
const nextConfig = {
  experimental: {
    ppr: 'incremental',
  },
};
module.exports = nextConfig;
```
```typescript
// app/page.tsx
import { Suspense } from "react";
import { StaticComponent, DynamicComponent } from "@/app/ui";

export const experimental_ppr = true;

export default function Page() {
  return (
    <>
      <StaticComponent />
      <Suspense fallback={<Fallback />}>
        <DynamicComponent />
      </Suspense>
    </>
  );
}
```

##### 5. Suspense 的使用
动态 API 得用 `<Suspense>` 包裹，还要提供 fallback 内容。要是组件需要读取 cookies 或者 headers 等请求信息，就得用 Suspense。

##### 6. 默认行为
要是没设置 `experimental_ppr`，路由默认不会用 PPR 预渲染，得给每个路由显式启用 PPR。`experimental_ppr` 会应用到路由段的所有子级，包括嵌套的布局和页面。要是想禁用 PPR，能在子路由段把 `experimental_ppr` 设为 `false`。

#### PPR 的优势
- **更快的初始加载速度**：通过预渲染静态内容，服务器能立马发送 HTML，提升初始加载速度。
- **更好的用户体验**：用 Suspense 在动态内容加载时显示备用内容，避免页面空白或一直处于加载状态。
- **减少网络请求**：把静态和动态内容合并到单个 HTTP 请求，减少了请求次数，提升性能。

#### 注意事项
- PPR 还在实验阶段，可能不稳定，生产环境不建议用。
- PPR 主要用于 Node.js 运行时。

#### 总结
总的来说，PPR 是结合静态和动态渲染的优化方案，通过预渲染静态内容和流式传输动态内容，能提升 Next.js 应用的性能和用户体验。