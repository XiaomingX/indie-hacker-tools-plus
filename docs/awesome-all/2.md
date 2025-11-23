# 精选软件与架构设计模式指南
## 什么是设计模式？
设计模式不是现成的代码，而是**解决特定场景下重复问题的通用“模板”** ——它总结了前辈开发者的实践经验，告诉我们“在什么情况下用什么思路组织代码/架构”，能帮我们写出更易维护、可扩展、低耦合的系统。


## 一、设计模式学习方法论（先搞懂怎么学）
很多人学模式会陷入“背公式”误区，其实核心是“**先懂问题，再记模式**”：
1.  **从痛点切入**：比如“频繁new对象导致代码冗余”→对应“创建型模式”；“模块间依赖太多改不动”→对应“结构型模式”。
2.  **结合重构练习**：先写“能用但臃肿”的代码，再用模式重构，感受优化过程。
3.  **区分“模式”与“反模式”**：知道“该怎么做”的同时，也要避开“不能踩的坑”（比如SQL的N+1查询、微服务的过度拆分）。

优质学习入口：
- [Refactoring Guru](https://refactoring.guru/design-patterns) - 最适合新手的指南，有图示、代码实例、适用场景对比，支持多语言。
- [Martin Fowler的设计模式文章](https://martinfowler.com/articles/) - 从实战角度解读模式的“为什么用”而非“怎么写”。


## 二、按编程语言分的核心设计模式
不同语言的特性决定了模式的“实现风格”，比如Rust的“所有权模式”、Go的“并发模式”都是语言特有的最优解。

### **Java**
Java是设计模式的“经典实践语言”，核心覆盖创建型、结构型、行为型全类别：
- [iluwatar/java-design-patterns](https://github.com/iluwatar/java-design-patterns) - 业界标杆，包含60+模式的完整代码+场景说明，支持Java 17+。
- [Java企业架构模式](https://martinfowler.com/eaaCatalog) - Martin Fowler的经典，聚焦“企业级系统”（如事务管理、数据访问）。
- **核心必学模式**：单例（线程安全版）、工厂方法、策略、观察者、依赖注入（Spring的核心）。

### **Python**
Python的“动态特性”让部分模式简化，更侧重“实用主义”：
- [faif/python-patterns](https://github.com/faif/python-patterns) - 最流行的Python模式库，含简洁实现（如用装饰器实现单例）。
- [Django设计模式与最佳实践](https://arunrocks.com/static/book/django-design-patterns-best-practices-2-ed/) - 聚焦Web开发，比如“MTV架构”“中间件模式”。
- **核心必学模式**：工厂模式（替代复杂`__init__`）、装饰器、迭代器、观察者（Django信号）。

### **Go**
Go的设计模式紧密结合“并发”和“简洁性”，无类继承特性催生了独特实现：
- [tmrts/go-patterns](https://github.com/tmrts/go-patterns) - 覆盖“并发模式”（如Worker Pool）、“结构模式”（如Composition）。
- [Effective Go](https://go.dev/doc/effective_go) - 官方指南，暗藏“错误处理模式”“接口隔离模式”等最佳实践。
- **核心必学模式**：Worker Pool（并发任务调度）、Option（可选参数）、Interface Segregation（小接口设计）。

### **JavaScript/TypeScript**
前端场景（如组件通信、状态管理）催生了大量特化模式：
- [sohamkamani/javascript-design-patterns-for-humans](https://github.com/sohamkamani/javascript-design-patterns-for-humans) - 通俗讲解，含ES6+实现（如用class写单例）。
- [React设计模式](https://reactpatterns.com) - 前端必备：HOC（高阶组件）、自定义Hook、Context（状态共享）。
- [TypeScript设计模式](https://github.com/torokmark/design_patterns_in_typescript) - 结合类型系统的模式优化（如用泛型实现工厂模式）。

### **Rust**
Rust的“所有权”“生命周期”特性让模式更侧重“内存安全”和“并发安全”：
- [Rust非官方设计模式](https://rust-unofficial.github.io/patterns/) - 核心是“零成本抽象”模式，如Builder（安全构造复杂对象）、State（状态机）。
- **核心必学模式**：Builder、Iterator（迭代器）、Arc+Mutex（线程安全共享）、Error Handling（错误链）。

### **其他主流语言**
| 语言       | 核心资源与必学模式                          |
|------------|---------------------------------------------|
| C#/.NET    | [.NET架构设计模式](https://learn.microsoft.com/en-us/dotnet/architecture/)，必学：依赖注入、仓储模式、中介者 |
| C++        | [cpp-patterns](https://github.com/daniel-hain/cpp-patterns)，必学：RAII（资源管理）、智能指针、观察者 |
| Kotlin     | [Design-Patterns-In-Kotlin](https://github.com/dbacinski/Design-Patterns-In-Kotlin)，必学：委托、单例（object关键字） |
| Angular/Vue | Angular：[官方架构指南](https://angular.io/guide/architecture)（依赖注入、服务模式）；Vue：[vue-patterns](https://learn-vuejs.github.io/vue-patterns/)（组件通信、混入模式） |


## 三、通用架构设计模式（跨语言/场景）
架构模式解决“系统级”问题，比如“如何拆分系统”“如何应对高并发”，是架构师的核心知识。

### 1. 基础架构模式（中小系统必备）
| 模式         | 核心解决问题                          | 适用场景                  |
|--------------|---------------------------------------|---------------------------|
| 分层架构     | 按“职责”拆分（如Controller→Service→DAO），解耦关注点 | 绝大多数Web应用、后台系统  |
| 微内核架构   | 核心逻辑与扩展功能分离（内核+插件）    | IDE（如VS Code）、中间件  |
| 事件驱动架构 | 模块间通过“事件”通信，避免直接依赖    | 实时系统（如消息通知、监控）|
| 管道-过滤器  | 数据按“管道”流转，经多步“过滤”处理    | ETL工具、日志处理系统      |

### 2. 大规模系统架构模式
- [系统设计入门](https://github.com/donnemartin/system-design-primer) - 涵盖高并发、高可用场景的核心模式（必看）。
- **关键模式详解**：
  - **负载均衡模式**：通过代理分发请求（如Nginx、云负载均衡），解决“单点压力过大”。
  - **缓存架构模式**：多级缓存（本地缓存+Redis），解决“数据库读瓶颈”（注意缓存一致性问题）。
  - **限流熔断模式**：限流（控制请求量）、熔断（服务故障时断开），防止“级联失败”（如Sentinel、Hystrix）。


## 四、垂直领域架构模式
### 1. 云架构设计模式
云原生场景的核心是“弹性”“可扩展”“低成本”，三大云厂商的官方指南最权威：
- **AWS**：[AWS架构设计模式](https://docs.aws.amazon.com/whitepapers/latest/aws-architecture-design/aws-architecture-design.html)，核心学“无服务器架构（Serverless）”“多可用区部署”“SaaS多租户隔离”。
- **Azure**：[Azure云架构模式](https://learn.microsoft.com/en-us/azure/architecture/patterns/)，重点看“服务网格（Istio）”“容器编排（AKS）”模式。
- **GCP**：[GCP解决方案库](https://cloud.google.com/solutions/)，推荐“数据湖架构”“微服务部署模板”。

### 2. 微服务与分布式系统
微服务的核心是“拆分”与“协同”，模式围绕这两个点展开：
- [微服务架构模式](http://microservices.io/patterns) - Sam Newman的“模式语言”，覆盖从“拆分策略”到“运维监控”全流程。
- [分布式系统模式](https://martinfowler.com/articles/patterns-of-distributed-systems/) - 解决分布式核心痛点：
  - 服务发现模式：自动找到可用服务（如Consul、Eureka）。
  - API网关模式：统一入口，处理认证、路由（如Kong、Gateway）。
  - 分布式事务模式：解决跨服务数据一致性（如SAGA模式）。

### 3. 数据库设计模式
分SQL和NoSQL两类，核心是“高效存储+低耦合访问”：
- **SQL数据库**：
  - 核心模式：读写分离（读库分担压力）、分库分表（解决数据量过大）、仓储模式（隔离业务与数据访问）。
  - 避坑指南：[SQL反模式](https://github.com/jarulraj/sqlcheck) - 自动检测“N+1查询”“大表无索引”等问题。
- **NoSQL数据库**：
  - MongoDB：[官方数据建模](https://www.mongodb.com/developer/learn/data-modeling/) - 重点学“嵌入文档”vs“引用文档”选择。
  - Redis：[最佳实践](https://redislabs.com/redis-best-practices/) - 缓存穿透/击穿/雪崩的防护模式。

### 4. DevOps与容器设计
容器化部署的核心是“标准化”“可移植”，K8s是绝对核心：
- [Kubernetes设计模式](https://k8spatterns.io/) - 生产级必学：
  - Sidecar模式：给主容器加“辅助容器”（如日志收集、监控）。
  - StatefulSet模式：管理有状态服务（如数据库）。
- 容器化基础：[多阶段构建模式](https://docs.docker.com/build/building/multi-stage/) - 减小镜像体积；镜像分层优化（频繁变动文件放上层）。

### 5. 移动开发设计模式
聚焦“UI与业务解耦”“性能优化”：
- **iOS**：MVVM（数据与UI分离）、Coordinator（页面跳转解耦）、Repository（数据来源隔离）。
  - 资源：[Apple官方架构指南](https://developer.apple.com/documentation/uikit/app_and_environment/scenes_and_lifecycle)。
- **Android**：MVVM+Jetpack（ViewModel+Room）、依赖注入（Hilt）、单Activity多Fragment。
  - 资源：[Android设计模式实战](https://www.raywenderlich.com/109843/common-design-patterns-for-android)。

### 6. 机器学习（ML）设计模式
解决“ML系统落地”的工程问题：
- [分布式机器学习设计模式](https://github.com/terrytangyuan/distributed-ml-patterns) - 核心：模型并行、数据并行、特征工程流水线、模型服务化（如TensorFlow Serving）。


## 最后：设计模式的“避坑提醒”
1.  **不要过度设计**：小项目用“简单代码”比“套模式”更高效（如单文件脚本不用分层架构）。
2.  **模式不是银弹**：同个问题可能有多种模式可选（如“对象创建”可选工厂/Builder），需结合场景选。
3.  **关注“模式演进”**：比如微服务从“单体拆分”到“服务网格”，云模式从“虚拟机”到“Serverless”，要跟进技术趋势。

建议收藏本文，按“先语言特有→再通用架构→最后垂直领域”的顺序学习，结合实际项目练习，才能真正掌握设计模式的价值。
