# NestJS 资源汇总（2026 优化版）

## 一、官方资源
- [官方网站](https://nestjs.com) - NestJS 主站，提供框架介绍与生态概览
- [官方文档](https://docs.nestjs.com) - 最新版英文官方指南，含核心概念、API 参考与实战教程
- [GitHub 仓库](https://github.com/nestjs/nest) - 框架源码，可跟踪更新日志与贡献代码
- [YouTube 频道](https://www.youtube.com/@nestframework) - 官方视频教程，含框架作者讲解
- **快速启动模板**
  - [Nest TypeScript  starter](https://github.com/nestjs/typescript-starter) - 官方推荐的 TypeScript 基础模板
  - [Nest JavaScript starter](https://github.com/nestjs/javascript-starter) - 支持 ES6/ES7/ES8 的 JavaScript 模板


## 二、社区交流
优先保留中文社区及全球主流交流渠道，移除小众语言社区：
- ![](https://img.shields.io/discord/520622812742811698?style=flat-square&logo=nestjs&color=a61b3a) [Discord 社区](https://discord.gg/nestjs) - 全球最大的 NestJS 实时交流群
- [Telegram 主社区](https://t.me/nestjs) - 英文社区，覆盖基础问题与生态讨论
- [Reddit 社区](https://www.reddit.com/r/Nestjs_framework) - 技术分享与问题解答论坛
- [NestJS 中文社区](https://nestjs.nodejs.cn/) - 非官方中文社区，含文档翻译与国内开发者交流（新增）
- [NestJS 中文掘金专栏](https://juejin.cn/tag/NestJS) - 国内开发者实战文章与教程集合（新增）


## 三、社区文档
- [NestJS 官方包 API 参考](https://api-references-nestjs.netlify.app/api) - 各官方模块的详细 API 文档
- [NestJS 中文文档](https://docs.nestjs.cn) - 社区维护的简体中文文档，同步官方核心内容
- [NestJS 实战指南（中文）](https://juejin.cn/book/7050083613413816353) - 国内开发者编写的实战教程，含项目架构与最佳实践（新增）


## 四、技术分享与课程
### 1. 核心演讲
- [NestJS 框架底层原理解析（作者 Kamil Myśliwiec）](https://www.youtube.com/watch?v=jo-1EUxMmxc) - 理解框架设计思想的核心演讲
- [用 NestJS 构建响应式 Node.js 流架构](https://www.youtube.com/watch?v=c8hvW14VdkY) - 实战响应式编程与流处理

### 2. 课程推荐
- [Udemy：NestJS 全栈开发实战](https://www.udemy.com/course/nestjs-the-complete-developers-guide/) - 英文付费课程，含 REST API、GraphQL 与数据库集成（更新链接）
- [B站：NestJS 从入门到实战](https://www.bilibili.com/video/BV1sG4y1T759/) - 国内免费视频课程，适合零基础入门（新增）
- [NestJS 30 天学习计划](https://github.com/m24927605/Nestjs30Days) - 社区维护的渐进式学习指南，含每日实战任务

### 3. 实战教程
- [Dev.to 官方团队文章](https://dev.to/nestjs) - 框架核心团队发布的官方教程
- [Trilon 博客](https://trilon.io/blog) - NestJS 作者公司的技术博客，含最新特性解读
- [NestJS 权限控制实战（RBAC/ABAC）](https://www.permit.io/blog/how-to-protect-a-url-inside-a-nestjs-app-using-rbac-authorization) - 基于 Passport 的权限管理实现
- [用 NestJS + Prisma 构建 REST API](https://www.prisma.io/blog/nestjs-prisma-rest-api-7D056s1BmOL0) - 结合现代 ORM 的实战教程（新增）
- [NestJS + Socket.IO 实时聊天系统](https://github.com/mokuteki225/nest-websockets-chat-boilerplate) - 含认证、房间管理的实时应用案例（新增）


## 五、实战示例项目
移除长期未更新的项目，保留高星、活跃维护的实战案例：
- [NestJS 版 RealWorld 后端](https://github.com/lujakob/nestjs-realworld-example-app) - 符合 RealWorld 规范的 REST API 示例，含 TypeORM 集成
- [NestJS + GraphQL + PostgreSQL 全栈示例](https://github.com/kelvin-mai/nest-ideas-api) - 同时支持 REST 与 GraphQL 的后端项目
- [Nodepress：NestJS 博客 CMS](https://github.com/surmon-china/nodepress) - 国内开发者开发的开源博客后端，含权限、评论、搜索功能
- [APITable：开源低代码数据库](https://github.com/apitable/apitable) - 企业级项目，基于 NestJS 构建的 Airtable 替代品（新增）
- [NestJS + Redis + 分布式锁](https://github.com/felanios/murlock) - 分布式场景下的锁机制实现示例（新增）
- [Serverless + NestJS + DynamoDB](https://github.com/International-Slackline-Association/Rankings-Backend) - 无服务器架构的生产级项目示例


## 六、项目模板（Boilerplate）
优先保留支持最新 NestJS 版本、含最佳实践的模板：
- [NestJS 清洁架构模板](https://github.com/VincentJouanne/nest-clean-architecture-ddd-example) - 基于 DDD 设计，含完整测试（单元/集成/E2E）
- [NestJS + Prisma + JWT 认证模板](https://github.com/notiz-dev/nestjs-prisma-starter) - 含 GraphQL、Swagger 与 Docker 配置
- [企业级 NestJS 模板（含 RBAC/日志/监控）](https://github.com/brocoders/nestjs-boilerplate) - 支持 PostgreSQL、邮件发送、文件上传（S3/本地）
- [NestJS + Turborepo 全栈模板](https://github.com/theaungphyo/turborepo) - 后端 NestJS + 前端 Next.js  monorepo 架构，支持 SWC 快速编译（新增）
- [NestJS + Drizzle ORM 模板](https://github.com/innei-template/nest-drizzle-authjs) - 现代轻量 ORM 集成，含 Auth.js 认证（新增）


## 七、常用组件与库
### 1. 工具类
- [`@nestjs/cqrs`](https://github.com/nestjs/cqrs) - 官方 CQRS 模块，分离命令与查询
- [`nestjs-typed-config`](https://github.com/Nikaple/nest-typed-config) - 类型安全的配置管理模块
- [`@nestia/core`](https://github.com/samchon/nestia) - 超高性能的验证与序列化工具（比 class-validator 快 200 倍）
- [`nestjs-cls`](https://github.com/Papooch/nestjs-cls) - 基于 async_hooks 的上下文管理，支持请求级数据共享

### 2. 数据库集成
- [`@nestjs/typeorm`](https://github.com/nestjs/typeorm) - 官方 TypeORM 模块，支持 MySQL/PostgreSQL
- [`@nestjs/mongoose`](https://github.com/nestjs/mongoose) - 官方 MongoDB 模块
- [`nestjs-prisma`](https://github.com/notiz-dev/nestjs-prisma) - Prisma ORM 的 NestJS 集成模块
- [`nestjs-drizzle`](https://github.com/knaadh/nestjs-drizzle) - 轻量 ORM Drizzle 的集成模块（新增）

### 3. 认证与权限
- [`nestjs-session`](https://github.com/iamolegga/nestjs-session) - 基于 express-session 的会话管理
- [`nestjs-rbac`](https://github.com/sergey-telpuk/nestjs-rbac) - 动态 RBAC 权限控制模块
- [`@tfarras/nestjs-firebase-auth`](https://github.com/tfarras/nestjs-firebase-auth) - Firebase 认证集成

### 4. API 与文档
- [`@nestjs/swagger`](https://github.com/nestjs/swagger) - 官方 OpenAPI（Swagger）模块
- [`@nestia/sdk`](https://github.com/samchon/nestia) - 自动生成 TypeScript SDK 与 Mock 服务
- [`nest-problem-details`](https://github.com/Fcmam5/nest-problem-details) - 符合 RFC-7807 标准的错误响应格式

### 5. 日志与监控
- [`nestjs-pino`](https://github.com/iamolegga/nestjs-pino) - 高性能日志模块，支持请求上下文
- [`nestjs-prometheus`](https://github.com/willsoto/nestjs-prometheus) - Prometheus 监控集成，支持自定义指标
- [`apitally`](https://github.com/apitally/apitally-js) - 轻量 API 监控工具，含错误报警（新增）

### 6. 消息队列与微服务
- [`@golevelup/nestjs-rabbitmq`](https://github.com/golevelup/nestjs/tree/master/packages/rabbitmq) - RabbitMQ 集成，支持多种消息模式
- [`nestjs-google-pubsub-microservice`](https://github.com/p-fedyukovich/nestjs-google-pubsub-microservice) - Google Pub/Sub 微服务传输策略


## 八、测试工具
- [Testing NestJS 示例库](https://github.com/jmcdo29/testing-nestjs) - 含单元测试、集成测试、E2E 测试的完整示例
- [`@golevelup/ts-jest`](https://www.npmjs.com/package/@golevelup/ts-jest) - Jest 测试工具集，简化 NestJS 依赖模拟
- [`@automock/jest`](https://github.com/omermorad/automock) - 自动生成类依赖模拟，减少测试代码量


## 九、开发工具与插件
### 1. 编辑器插件
- [VS Code：NestJS Files](https://marketplace.visualstudio.com/items?itemName=AbhijoyBasak.nestjs-files) - 快速创建 Controller/Service/Module 文件
- [VS Code：NestJS Snippets](https://marketplace.visualstudio.com/items?itemName=ashinzekene.vscode-nestjs-snippets) - 常用代码片段（如 `nest-controller`）
- [Vast Studio](https://getvast.app) - 低代码平台，可视化生成 NestJS REST API（新增）

### 2. CLI 工具
- [`@nestjs/cli`](https://github.com/nestjs/nest-cli) - 官方 CLI，支持项目创建、模块生成
- [`nest-commander`](https://github.com/jmcdo29/nest-commander) - 构建 NestJS 命令行应用的模块
- [`nest-sdk-generator`](https://github.com/lonestone/nest-sdk-generator) - 从 NestJS API 自动生成 TypeScript SDK（新增）


## 十、基于 NestJS 的开源项目
- [Novu：开源通知中心](https://github.com/novuhq/novu) - 支持邮件、短信、推送的统一通知系统
- [ToolJet：开源低代码平台](https://github.com/ToolJet/ToolJet) - 快速构建内部工具的平台
- [Vendure：开源电商框架](https://github.com/vendure-ecommerce/vendure) - 基于 GraphQL 的 headless 电商系统
- [Ghostfolio：个人财务分析工具](https://github.com/ghostfolio/ghostfolio) - 隐私优先的资产跟踪平台（新增）
- [Twenty：开源 CRM 系统](https://github.com/twentyhq/twenty) - 替代 Salesforce 的轻量 CRM（新增）