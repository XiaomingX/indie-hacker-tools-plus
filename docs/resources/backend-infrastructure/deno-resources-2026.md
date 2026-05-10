# Deno 2.x+ 全栈开发资源精选 (2026 Checklist)

> [!TIP]
> **Indie Hacker Insight**: 2026 年，Deno 已进化为 **"无痛版 Node.js"**。
> - **零配置**：内置 Linter、Formatter、Test Runner 和 TypeScript 编译器，你不需要再维护复杂的 `tsconfig.json` 或 `eslint.config.js`。
> - **全面兼容**：通过 `npm:` 协议，Deno 现在可以运行 99% 的 Node.js 库，无需任何适配。
> - **边缘原生**：Deno KV 和 Deno Queues 提供了开箱即用的云端存储与任务队列，是构建 Serverless 应用的终极方案。

---

## 🏗️ 核心框架与基础 (Core & Infrastructure)

- [ ] [**Deno 官方手册**](https://docs.deno.com/runtime/manual/) - **[权威]** 包含从环境安装到高级 API 的所有核心用法指南。
- [ ] [**Fresh (Full-stack)**](https://fresh.deno.dev/) - Deno 官方推荐的全栈框架，主打 Islands 架构，零运行时 JS 负载，极致性能。
- [ ] [**Hono (Edge-first)**](https://hono.dev/) - **[2026 推荐]** 极快、轻量级且类型安全的 Web 框架，完美适配 Deno 运行时。
- [ ] [**Deno Deploy**](https://deno.com/deploy) - 全球分布式的边缘运行平台，支持秒级部署与自动缩放。

---

## ⚡ 存储、数据库与任务 (Data & Tasks)

- [ ] [**Deno KV**](https://deno.com/kv) - 内置的分布式键值存储，支持事务、强一致性，且无需管理数据库实例。
- [ ] [**Deno Queues**](https://docs.deno.com/runtime/manual/runtime/queues) - 开箱即用的异步任务队列，处理邮件发送、后台任务的利器。
- [ ] [**Drizzle ORM**](https://orm.drizzle.team/docs/get-started-deno) - 为 Deno 优化的轻量级 ORM，提供极致的类型安全与极致性能。
- [ ] [**Supabase (Deno Runtime)**](https://supabase.com/docs/guides/functions/quickstart) - Supabase Edge Functions 默认使用 Deno，是构建跨区域后端的黄金组合。

---

## 🛠️ 效率工具与生产力 (Efficiency & Tooling)

- [ ] [**Cliffy**](https://cliffy.io/) - 构建交互式命令行工具 (CLI) 的最佳框架，支持自动补全、色彩输出。
- [ ] [**Deno KV Insights**](https://github.com/denoland/kv-insights) - 可视化管理和监控你的 Deno KV 数据。
- [ ] [**udd (Dependency Updater)**](https://github.com/hayd/deno-udd) - 自动化更新你代码中的 `import` 版本号。

---

## 🛡️ 测试、质量与部署 (Testing & Quality)

- [ ] [**Deno Built-in Test**](https://docs.deno.com/runtime/manual/basics/testing/) - 使用 `Deno.test()` 进行原生单元测试，无需安装外部框架。
- [ ] [**Vitest (Deno Support)**](https://vitest.dev/guide/environments.html#deno) - 如果你需要更复杂的测试套件，Vitest 现已完美支持 Deno 运行。
- [ ] [**GitHub Actions for Deno**](https://github.com/denoland/setup-deno) - 官方维护的 CI/CD 动作，快速实现自动化发布。

---

## 💡 选型建议
1. **快速上线一个 MVP 后端**：选 **Hono** + **Deno KV** + **Deno Deploy**。
2. **构建以内容为主的网站**：选 **Fresh** 或 **Lume** (静态生成)。
3. **编写系统管理工具/脚本**：选 **Cliffy**，直接分发单文件二进制。
4. **需要使用现有的 Node 库**：直接使用 `import { ... } from "npm:pkg-name"`。
