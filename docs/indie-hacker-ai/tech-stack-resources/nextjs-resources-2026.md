# Next.js 资源导航 (2026 Checklist)

> [!TIP]
> **Indie Hacker Insight**: 2026 年的 Next.js 是独立开发的**标准答案**。
> - **起步建议**：直接使用 **App Router**，配合 **Server Actions** 彻底告别繁琐的 API 定义。
> - **效率核心**：利用 **v0.dev** 生成 UI，配合 **Cursor** 进行逻辑注入，1 小时即可完成 MVP。
> - **部署策略**：小规模部署在 **Vercel**，流量起飞后考虑 **Coolify** 自建。

---

## 🏗️ 核心学习资源 (Learning)

- [ ] [**Next.js 官方文档**](https://nextjs.org/docs) - 始终是最权威的参考，优先看 App Router 部分。
- [ ] [**Next.js Learn**](https://nextjs.org/learn) - 官方出的零基础实战教程，适合新手快速上手。
- [ ] [**Vercel 官方博客**](https://nextjs.org/blog) - 关注每年的 Next.js Conf 和版本更新。

---

## 🚀 起步模板与 SaaS 启动器 (Starters)

- [ ] [**T3 Stack**](https://create.t3.gg/) - 集成 Next.js, TypeScript, Prisma, NextAuth 的极致类型安全方案。
- [ ] [**ShipFast**](https://shipfa.st/) - 2026 年最热门的付费 SaaS 模板，内置了所有独立开发需要的 Auth, Stripe, SEO。
- [ ] [**Next.js Enterprise**](https://github.com/Blazity/next-enterprise) - 适用于复杂项目的生产级模板。
- [ ] [**Shadcn/ui Taxonomy**](https://github.com/shadcn/taxonomy) - 展示如何优雅地组合 App Router 与 Server Components。

---

## 🎨 UI 与交互 (UI & Components)

- [ ] [**Shadcn/ui**](https://ui.shadcn.com/) - 2026 年的 UI 标准，不再是安装库，而是直接复制代码块。
- [ ] [**v0.dev**](https://v0.dev/) - Vercel 出品的 AI UI 生成器，支持自然语言生成 React 组件。
- [ ] [**Magic UI**](https://magicui.design/) - 专注于动效和高质感交互的组件库。
- [ ] [**Aceternity UI**](https://ui.aceternity.com/) - 提供极具视觉冲击力的落地页组件。

---

## 🛠️ 扩展工具与生态 (Ecosystem)

- [ ] [**NextAuth.js (Auth.js)**](https://authjs.dev/) - Next.js 的身份验证事实标准。
- [ ] [**Prisma / Drizzle ORM**](https://orm.drizzle.team/) - 数据库操作神器，Drizzle 在边缘侧性能更优。
- [ ] [**Next-Intl**](https://next-intl-docs.vercel.app/) - 2026 年最推荐的 Next.js 国际化方案。
- [ ] [**Next-Sitemap**](https://github.com/iamvishnusankar/next-sitemap) - 自动生成站点地图，SEO 必备。

---

## 💡 选型建议
1. **快速验证想法**：**v0.dev** + **ShipFast**。
2. **构建大型复杂 SaaS**：**T3 Stack** + **Shadcn/ui**。
3. **内容驱动/SEO 站点**：**Next.js (SSG)** + **Cloudflare R2**。
4. **极致性能与边缘部署**：**Hono** + **Drizzle** + **Cloudflare Workers**。