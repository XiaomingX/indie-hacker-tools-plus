# awesome-serverless(🚀 零基础也能懂的Serverless精选指南)


## 什么是“无服务器”（Serverless）计算？

**Serverless（无服务器）绝非“没有服务器”**，而是把服务器的管理工作完全交给了云厂商。开发者不用再操心“买多大配置的服务器”“怎么部署代码”“用户多了怎么扩容”“服务器系统要不要更新”这些运维琐事，只需专注写核心业务代码——代码会像“待命的工人”，有请求/事件触发时才启动运行，结束后自动“下班”，资源按需分配。

### 举两个直观例子：
- 国外场景：你写了一段处理用户上传图片的代码，部署到 **AWS Lambda** 上。当用户在你的App上传图片时，Lambda会自动启动代码压缩图片，处理完就释放资源，你只按“运行时长+调用次数”付费。
- 国内场景：你为小程序写了一个“查询天气”的接口，部署到 **阿里云函数计算** 上。没人用的时候不花钱，高峰期用户突然变多，云厂商会自动加“工人”（扩容），不用你手动操作。


## Serverless的核心优势与适用场景

这部分能帮你快速判断：自己的项目该不该用Serverless？

### 核心优势（为什么开发者爱用）
1.  **零运维负担**：不用管服务器、操作系统、扩容容错，省出时间写业务。
2.  **成本更可控**：按“实际使用”付费（比如调用1次收0.0001元，闲置时0成本），适合流量波动大的场景（比如电商促销突然爆单、工具类产品低频使用）。
3.  **迭代速度快**：写完代码直接部署，不用等服务器配置，小功能几小时就能上线。

### 适用与不适用场景
| 适用场景                  | 不适用场景                          |
|---------------------------|-----------------------------------|
| API接口（如小程序后端、前端接口） | 长耗时任务（如视频渲染超过15分钟）  |
| 定时任务（如每日数据统计、推送） | 高并发低延迟核心场景（如高频交易）  |
| 数据处理（如日志分析、文件转换） | 需要持久化连接的服务（如即时通讯服务器） |
| 个人项目/中小型团队快速试错      | 依赖复杂本地环境的应用（如传统ERP）  |


## 常用Serverless平台和工具（按场景分类，附适用人群）

### 一、一体化解决方案（“一站式配齐”，适合快速搭全栈项目）
这类平台集成了“数据存储+用户认证+部署”等功能，不用自己拼多个工具。
- **[Firebase](https://firebase.google.com/)**：谷歌旗下，强项是“实时数据库”（比如聊天App的消息同步）和用户认证，适合做海外的Web/移动端项目，免费额度足够个人开发。
- **[LeanCloud](https://leancloud.app/)**：国内老牌平台，自带数据存储、短信验证、推送功能，支持小程序/APP/Web，国内访问速度快，适合国内开发者快速搭后端。
- **[Vercel](https://vercel.com/)**：前端开发者的“神器”，支持React、Vue等框架，推送代码就自动部署前端，内置的“Serverless Functions”能快速写API接口，适合个人博客、中小型前端项目。
- **[Netlify](https://netlify.com/)**：和Vercel类似，侧重静态网站部署，集成的Lambda函数能对接前端，适合需要“前端+简单后端”的团队（比如营销页的表单提交）。


### 二、托管与代码执行平台（只负责“运行代码”，灵活度高）
核心功能是“按事件触发代码”，需自己搭配数据库等其他工具，适合有一定经验的开发者。
- **[AWS Lambda](https://aws.amazon.com/lambda)**：全球最早的Serverless服务，生态最完善（能对接AWS的所有云服务），适合做海外企业级项目，但国内访问速度一般。
- **[阿里云函数计算](https://www.aliyun.com/product/fc)**：国内主流选择，对接阿里云的OSS（存储）、RDS（数据库）很方便，支持Java/Node.js/Python等语言，适合国内企业或小程序项目。
- **[Google Cloud Functions](https://cloud.google.com/functions/docs)**：轻量灵活，和谷歌的云存储、AI服务集成紧密，适合做海外的轻量API或数据处理任务。
- **[Cloudflare Workers](https://workers.cloudflare.com/)**：全球分布式部署（边缘计算），代码运行在离用户最近的节点，适合需要“低延迟”的场景（比如海外用户的接口加速、CDN+函数结合）。


### 三、开发框架（帮你高效管理多环境/多函数，适合复杂项目）
当你有十几个函数要部署、要对接多个云厂商时，框架能简化流程。
- **[Serverless Framework](https://serverless.com/)**：最流行的开源框架，支持AWS、阿里云、腾讯云等几乎所有平台，用YAML配置文件就能管理函数部署，适合多云项目或函数数量多的场景。
- **[Pulumi](https://www.pulumi.com/)**：不用写YAML，直接用JavaScript/Python等代码定义部署逻辑，适合熟悉编程语言、讨厌配置文件的开发者。
- **[OpenFaaS](https://www.openfaas.com/)**：基于Docker和Kubernetes，适合本身在用K8s的团队，能在自己的集群里跑Serverless函数，兼顾灵活度和可控性。


### 四、安全工具（解决“用户登录”“权限控制”问题）
- **[Auth0](https://auth0.com/)**：支持谷歌、苹果、微信等多种登录方式（单点登录），自带安全防护，适合需要多端统一登录的海外项目。
- **[Amazon Cognito](https://aws.amazon.com/cognito/)**：和AWS Lambda无缝对接，快速给App加“注册/登录/忘记密码”功能，不用自己写认证逻辑。
- **[Supabase Auth](https://supabase.com/auth)**：开源工具，和Supabase的数据库绑定，支持邮箱、OAuth登录，适合中小型项目或开源项目。


### 五、Serverless数据库（专为无服务器场景设计，按需扩容）
传统数据库需要固定配置，Serverless数据库能随请求量自动扩缩容，闲置时低成本。
- **[Amazon DynamoDB](https://aws.amazon.com/dynamodb/)**：NoSQL数据库，读写速度快，和Lambda搭配是经典组合，适合存储用户数据、订单信息等。
- **[Upstash](https://upstash.com/)**：Serverless版Redis，支持缓存、消息队列，按请求次数付费，适合需要高频读写的场景（比如计数器、会话存储）。
- **[Neon](https://neon.tech)**：Serverless版PostgreSQL（关系型数据库），支持按需扩容，免费额度足够个人开发，适合习惯SQL的开发者。
- **[PlanetScale](https://planetscale.com/)**：Serverless版MySQL，支持分支管理（像Git一样管理数据库版本），适合团队协作开发。


### 六、CI/CD与观察性工具（部署、监控、排错必备）
- **CI/CD（自动部署代码）**
  - **[GitHub Actions](https://github.com/features/actions)**：免费且易用，推送代码到GitHub后自动部署到Lambda/Vercel，适合个人或小团队。
  - **[Serverless Framework Pro](https://www.serverless.com/pro/)**：自带CI/CD、环境管理，还能集成监控工具，适合中大型Serverless项目。

- **观察性工具（查日志、监控性能）**
  - **[AWS CloudWatch](https://aws.amazon.com/cloudwatch/)**：和Lambda/DynamoDB深度集成，能看函数运行日志、调用成功率，出问题会发告警。
  - **[Lumigo](https://www.lumigo.io/)**：可视化监控，能清晰看到“一个请求经过了哪些函数/数据库”，排错效率高，适合分布式Serverless项目。
  - **[Datadog](https://www.datadoghq.com/)**：企业级工具，支持多云监控（同时看AWS和阿里云的函数），适合大型团队。


### 七、其他常用工具（按场景补全）
| 场景          | 工具推荐                                  | 核心优势与适用场景                          |
|---------------|-------------------------------------------|-------------------------------------------|
| 文件/媒体管理 | [Cloudinary](https://cloudinary.com/)     | 图片/视频的上传、压缩、裁剪，CDN分发，适合内容型App |
| 实时功能      | [Supabase Realtime](https://supabase.com/realtime) | 开源实时数据库，能做聊天、实时榜单，比Pusher成本低 |
| 表单处理      | [Formspree](https://formspree.io/)        | 几行代码给静态页加表单，提交后发邮件/存数据库，适合个人博客 |
| 电商          | [Medusa](https://medusajs.com/)           | 开源Serverless电商，可自定义支付、物流，适合中小电商团队 |
| 邮件发送      | [SendGrid](https://sendgrid.com/)         | 批量发送验证邮件、营销邮件，有免费额度，支持Serverless集成 |
| 邮件发送（国内） | [腾讯云邮件推送](https://cloud.tencent.com/product/ses) | 国内送达率高，对接腾讯云函数方便，适合小程序/App的验证邮件 |


## 精选学习资源（从入门到进阶，附难度标注）

### 1. 入门实战（0基础能上手，跟着做就会）
- **[Serverless Stack (SST)](https://sst.dev/)**：用TypeScript从零搭“前端+Lambda+DynamoDB”全栈项目，每步有代码示例，适合前端转全栈的开发者。
- **[阿里云函数计算快速入门](https://help.aliyun.com/document_detail/52831.html)**：国内文档，30分钟部署第一个Node.js接口，适合国内开发者入门。
- **[Serverless Framework Examples](https://www.serverless.com/examples/)**：上千个现成模板（比如“定时发邮件”“图片压缩”），直接复制修改就能用。

### 2. 系统教程（理解原理与架构）
- **《Serverless Architectures on AWS》**：公认的经典书，讲清楚Serverless的设计原则和最佳实践，适合想做架构设计的开发者。
- **[AWS Serverless官方课程](https://aws.amazon.com/training/learn-about/serverless/)**：免费视频课，覆盖Lambda、DynamoDB的核心用法，带实验操作。

### 3. 行业洞察（了解趋势与坑）
- **[Martin Fowler：Serverless架构](https://martinfowler.com/articles/serverless.html)**：技术大神的经典解读，讲透Serverless的本质和局限性。
- **[InfoQ 2026 Serverless技术趋势报告](https://www.infoq.cn/article/xxxxxxx)**：分析国内企业的落地案例（如电商、金融），帮你避坑。


## 总结：怎么快速开始用Serverless？

1.  **选对平台**：国内项目优先用「阿里云函数计算」+「Vercel」；海外项目用「AWS Lambda」+「Firebase」；纯前端项目直接用「Vercel/Netlify」。
2.  **从小事做起**：别一开始就搭复杂项目，先写一个“查询天气的API”或“表单提交接口”，熟悉部署流程。
3.  **善用模板**：用「Serverless Framework Examples」或云厂商的“快速启动模板”，少写重复代码。

Serverless的核心是“解放开发者”——不用被运维绑住，能更快把想法变成产品。跟着上面的资源试手，1-2天就能完成第一个无服务器项目！
