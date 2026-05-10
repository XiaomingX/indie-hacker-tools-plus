# 2026 Next.js 中间件 (Middleware) 实战指南 (Checklist)

> [!TIP]
> **Indie Hacker Insight**: 2026 年，Next.js 中间件已成为处理 **"全球化流量"** 与 **"边缘端逻辑"** 的利器。
> - **性能至上**：中间件运行在边缘节点 (Edge Runtime)，代码必须极其轻量且执行迅速。
> - **安全网关**：利用中间件实现 Auth 拦截、Bot 检测和 A/B 测试，能有效降低后端的无效计算。
> - **谨慎使用**：不要在中间件中执行复杂的数据库操作或繁重的计算任务，这会显著增加首字节时间 (TTFB)。

---

## 🏗️ 核心职责与约定 (Core & Convention)

- [ ] [**Next.js 中间件官方文档**](https://nextjs.org/docs/app/building-your-application/routing/middleware) - 理解执行顺序与生命周期。
- [ ] **文件位置**：必须在项目根目录（或 `src` 下）创建 `middleware.ts`。
- [ ] **运行环境**：强制在 **Edge Runtime** 下运行，仅支持有限的 Node.js API。
- [ ] **执行顺序**：中间件在缓存匹配和路由匹配 **之前** 执行。

---

## ⚡ 典型使用场景 (Use Cases)

- [ ] **身份验证与授权**：校验会话 Cookie，拦截未授权的受保护路径。
- [ ] **服务器端重定向**：根据地理位置、用户语言或角色进行 Instant Redirect。
- [ ] **路径重写 (Rewriting)**：支持 A/B 测试、功能灰度发布或旧路径兼容。
- [ ] **Bot 拦截**：基于 User-Agent 或 IP 频率限制恶意爬虫。
- [ ] **安全头注入**：统一为所有响应添加 `Content-Security-Policy` 等安全头。

---

## 🛡️ 限制与禁忌 (Limitations)

- [ ] **避免复杂数据处理**：中间件不适合获取海量数据或进行大规模计算。
- [ ] **避免直接数据库操作**：建议通过 API 或轻量级的 Edge 驱动进行极简查询。
- [ ] **包体积控制**：避免引入巨大的第三方依赖，否则会导致边缘节点部署失败。

---

## 🛠️ 进阶 API 指南 (Advanced API)

- [ ] **Matcher 匹配器**：利用正则表达式精准过滤无需中间件处理的静态资源（如 `_next/static`, `favicon.ico`）。
- [ ] **NextResponse**：利用 `NextResponse.next()`, `redirect()` 和 `rewrite()` 控制流量。
- [ ] **NextFetchEvent (waitUntil)**：在后台执行非阻塞任务（如发送审计日志），不延迟响应返回。
- [ ] **单元测试**：使用 `next/experimental/testing/server` 对中间件逻辑进行自动化测试。

---

## 💡 选型建议
1. **构建全球化应用**：利用中间件根据 `x-vercel-ip-country` 自动切换语言。
2. **快速原型开发**：在中间件中简单实现 **RBAC** 逻辑进行路由拦截。
3. **提升 SEO 效果**：利用 `rewrite` 实现动态子域名或多租户架构。
4. **性能监控**：在中间件中注入 Trace ID，实现端到端的可观测性。