# awesome-java（JDK 17+ 开发者必备资源精选）
本指南整合了 **主流、适配JDK 17+** 的Java工具与框架，剔除小众、过时内容，按「开发场景」分类梳理。每个工具均补充「核心价值」与「适用场景」，帮你快速匹配技术需求。


## 一、基础开发工具（高效开工必备）
### 1. 集成开发环境（IDE）
| 名称 | 链接 | 核心优势 | 适合场景 |
|------|------|----------|----------|
| IntelliJ IDEA | [官网](https://www.jetbrains.com/idea/) | 智能补全、Spring生态深度适配、内置调试/测试工具、重构能力强 | 企业级开发、微服务、复杂多模块项目（首选） |
| Eclipse | [官网](https://www.eclipse.org) | 开源免费、插件生态丰富（如Spring Tools Suite） | 轻量级项目、开源贡献、低成本团队协作 |
| Visual Studio Code | [Java插件](https://code.visualstudio.com/docs/languages/java) | 轻量跨平台、支持多语言、插件轻量化（如Extension Pack for Java） | 小型项目、多语言混合开发、临时快速编码 |

### 2. 构建与依赖管理
#### （1）Apache Maven
- **链接**：[官网](https://maven.apache.org)  
- **核心功能**：基于`pom.xml`的「声明式构建」，标准化编译/测试/打包流程，集成中央仓库管理依赖。  
- **优势**：「约定优于配置」，无需手动定义目录结构，团队协作一致性强。  
- **适合场景**：传统Java项目、遗留系统维护、对标准化要求高的团队。

#### （2）Gradle
- **链接**：[官网](https://gradle.org)  
- **核心功能**：支持Groovy/Kotlin DSL的「编程式构建」，增量构建（比Maven快30%+），兼容Maven仓库。  
- **优势**：灵活度极高，可定制构建逻辑；支持Spring Boot、Android、云原生等多场景。  
- **适合场景**：微服务、Spring Boot 3+项目、需要自定义构建流程（如多环境打包）的场景。

### 3. Java版本管理
#### SDKMan
- **链接**：[官网](https://sdkman.io)  
- **核心功能**：一键安装/切换JDK（支持Oracle JDK、OpenJDK、GraalVM），管理Maven/Gradle等工具版本。  
- **实用命令**：  
  - `sdk list java`：查看可安装的JDK版本  
  - `sdk use java 17.0.10-open`：临时切换到JDK 17  
- **优势**：跨平台（Linux/macOS），避免手动配置环境变量。


## 二、核心功能库（解决具体开发问题）
### 1. 对象映射（Bean转换）
| 名称 | 链接 | 核心功能 | 优势 | 适合场景 |
|------|------|----------|------|----------|
| MapStruct | [GitHub](https://github.com/mapstruct/mapstruct) | 编译时生成映射代码（无反射），支持自定义转换逻辑 | 性能接近手写代码，编译期报错（避免运行时问题） | 企业级项目的DTO与实体类转换（首选） |
| ModelMapper | [GitHub](https://github.com/modelmapper/modelmapper) | 自动推断字段映射关系，无需写接口 | 上手快，零配置 | 简单场景（如字段名完全一致的转换） |

### 2. JSON处理
#### （1）Jackson
- **链接**：[GitHub](https://github.com/FasterXML/jackson)  
- **核心功能**：序列化/反序列化、树模型（动态操作JSON）、多态支持、自定义序列化器。  
- **优势**：Spring生态默认JSON库，性能强、功能最全，支持JDK 17+。  
- **适合场景**：企业级应用、高并发JSON解析、复杂对象处理。

#### （2）Gson
- **链接**：[GitHub](https://github.com/google/gson)  
- **核心功能**：API简洁，支持任意对象序列化，无需额外注解。  
- **优势**：易用性第一，对复杂泛型兼容性好。  
- **适合场景**：轻量级项目、快速原型开发。

#### （3）fastjson2
- **链接**：[GitHub](https://github.com/alibaba/fastjson2)  
- **核心功能**：阿里重构的高性能JSON库，兼容旧版fastjson，支持JDK 17+和GraalVM。  
- **优势**：解析速度比Jackson快20%+，适合大数据量场景。  
- **适合场景**：日志解析、数据同步、高吞吐量服务。

### 3. 日期与时间
#### ThreeTen-Extra
- **链接**：[GitHub](https://github.com/ThreeTen/threeten-extra)  
- **核心功能**：补充JDK 8+ `java.time`包的缺失功能，如`YearWeek`（周处理）、`LocalDateRange`（日期区间）、`Interval`（时间间隔）。  
- **实用示例**：  
  ```java
  // 判断两个时间区间是否重叠
  Interval interval1 = Interval.of(LocalDateTime.now(), LocalDateTime.now().plusHours(2));
  Interval interval2 = Interval.of(LocalDateTime.now().plusHours(1), LocalDateTime.now().plusHours(3));
  boolean isOverlap = interval1.overlaps(interval2); // true
  ```
- **优势**：完全兼容JDK原生API，避免重复造轮子。

### 4. 缓存
#### （1）Caffeine
- **链接**：[GitHub](https://github.com/ben-manes/caffeine)  
- **核心功能**：基于LRU算法的内存缓存，支持过期策略（固定时间/访问后失效）、异步加载、缓存统计。  
- **优势**：性能接近理论最优，Spring Boot 2+默认集成。  
- **适合场景**：高频读取、低频更新的数据（如字典表、用户权限、接口结果缓存）。

#### （2）Ehcache 3
- **链接**：[官网](https://www.ehcache.org)  
- **核心功能**：支持内存+磁盘+分布式缓存，兼容JSR-107缓存规范，可与Spring Cache集成。  
- **优势**：成熟稳定，支持跨服务缓存共享。  
- **适合场景**：分布式系统、需要持久化缓存的场景。

### 5. HTTP客户端
#### （1）Retrofit 2
- **链接**：[官网](https://square.github.io/retrofit/)  
- **核心功能**：「类型安全的REST客户端」——用接口定义API，自动生成请求代码，支持OKHttp拦截器、RxJava/Reactor适配。  
- **实用示例**：  
  ```java
  // 定义API接口
  public interface UserService {
      @GET("/users/{id}")
      Call<User> getUser(@Path("id") Long id);
  }
  // 生成客户端并调用
  Retrofit retrofit = new Retrofit.Builder().baseUrl("https://api.example.com").build();
  UserService service = retrofit.create(UserService.class);
  User user = service.getUser(1L).execute().body();
  ```
- **优势**：代码简洁，易维护，支持多种数据格式。

#### （2）Apache HttpComponents 5
- **链接**：[官网](https://hc.apache.org/)  
- **核心功能**：低级别HTTP工具包，支持HTTPS、连接池、异步请求、自定义请求头/超时。  
- **优势**：控制力极强，适合底层HTTP协议定制。  
- **适合场景**：爬虫开发、需要精细控制请求的场景。

### 6. 数据库工具
| 名称 | 链接 | 核心功能 | 优势 | 适合场景 |
|------|------|----------|------|----------|
| HikariCP | [GitHub](https://github.com/brettwooldridge/HikariCP) | 高性能JDBC连接池，Spring Boot默认集成 | 启动快、内存占用低、并发性能强 | 所有需要数据库连接的Java应用（替代老牌DBCP） |
| Flyway | [官网](https://flywaydb.org) | 数据库版本管理，基于SQL脚本自动迁移 | 简单轻量，遵循「约定优于配置」 | 中小项目、SQL主导的数据库变更 |
| Liquibase | [官网](https://www.liquibase.com) | 支持XML/YAML/SQL多种格式迁移脚本，支持回滚 | 灵活强大，适合复杂变更（如分库分表） | 大型项目、多环境数据库同步 |
| jOOQ | [官网](https://www.jooq.org) | 基于数据库Schema生成类型安全的SQL代码 | 接近原生SQL，编译期校验SQL语法 | 既想写原生SQL又要避免语法错误的场景 |
| H2 | [官网](https://h2database.com) | 轻量级SQL数据库，支持内存模式 | 启动快，无需独立部署 | 单元测试、临时数据存储 |

### 7. 命令行工具
#### （1）picocli
- **链接**：[官网](https://picocli.info)  
- **核心功能**：基于注解的参数解析，支持ANSI颜色、子命令、自动补全、帮助文档生成。  
- **优势**：功能全面，API简洁，替代JCommander成为主流。

#### （2）JLine 3
- **链接**：[GitHub](https://github.com/jline/jline3)  
- **核心功能**：提供命令行交互能力，如历史命令、Tab自动补全、命令提示。  
- **适合场景**：开发交互式命令行工具（如数据库客户端、运维脚本）。

### 8. 图像处理
- **ZXing**  
  [GitHub](https://github.com/zxing/zxing)  
  - 核心功能：生成/解析条形码（EAN-13）、二维码（QR Code）。  
  - 优势：开源成熟，支持多种格式，可集成到Web/桌面应用。

- **Thumbnailator**  
  [GitHub](https://github.com/coobird/thumbnailator)  
  - 核心功能：一行代码生成高质量缩略图，支持裁剪、旋转、加水印。  
  - 示例：`Thumbnails.of("input.jpg").size(200, 200).toFile("output.jpg");`  
  - 优势：简化Java 2D API的复杂操作。


## 三、架构与框架（支撑大型应用）
### 1. 架构验证与设计
#### （1）ArchUnit
- **链接**：[GitHub](https://github.com/TNG/ArchUnit)  
- **核心功能**：用代码定义架构规则（如「控制层不能直接调用DAO层」「禁止使用Thread.sleep()」），并在测试中验证。  
- **优势**：避免团队协作中的「架构腐化」，将架构规则落地为可执行的测试。

#### （2）jMolecules
- **链接**：[GitHub](https://github.com/xmolecules/jmolecules)  
- **核心功能**：用注解表达领域驱动设计（DDD）概念，如`@Aggregate`（聚合根）、`@Entity`（实体）、`@ValueObject`（值对象）。  
- **优势**：让代码「自解释」架构意图，可配合Spring Data等框架自动生成实现。

### 2. 依赖注入（DI）
| 名称 | 链接 | 核心功能 | 优势 | 适合场景 |
|------|------|----------|------|----------|
| Dagger 2 | [官网](https://dagger.dev/) | 编译时生成依赖注入代码（无反射） | 性能极强，启动快 | Android开发、高性能服务 |
| Guice | [GitHub](https://github.com/google/guice) | 轻量级DI框架，支持模块化配置 | API简洁，易集成Google生态 | 后端服务、非Spring项目 |

### 3. Spring生态（企业级开发首选）
| 组件 | 链接 | 核心功能 | 学习重点 |
|------|------|----------|----------|
| Spring Framework | [官网](https://spring.io/projects/spring-framework) | 依赖注入（DI）、面向切面编程（AOP）、事务管理 | IoC容器原理、Bean生命周期、AOP切点表达式 |
| Spring Boot 3+ | [官网](https://spring.io/projects/spring-boot) | 自动配置、嵌入式服务器（Tomcat）、starter依赖 | 自定义自动配置、JDK 17+适配、GraalVM支持 |
| Spring Cloud | [官网](https://spring.io/projects/spring-cloud) | 微服务组件集（注册中心、配置中心、网关等） | Spring Cloud Alibaba（国内主流）、服务治理 |
| Spring Security | [官网](https://spring.io/projects/spring-security) | 认证（登录）、授权（权限控制）、OAuth2.0 | JWT集成、RBAC权限模型、单点登录（SSO） |

### 4. 现代微服务框架
#### （1）Quarkus
- **链接**：[官网](https://quarkus.io)  
- **核心功能**：为云原生优化的微服务框架，支持GraalVM原生编译（启动时间<1秒，内存占用降50%）。  
- **优势**：兼容Spring API，适合K8s/Serverless部署。

#### （2）Micronaut
- **链接**：[官网](https://micronaut.io)  
- **核心功能**：编译时DI，低内存占用，支持多语言（Java/Kotlin/Groovy）。  
- **适合场景**：高性能微服务、IoT设备开发。

### 5. 响应式编程（高并发场景）
#### （1）Project Reactor
- **链接**：[GitHub](https://github.com/reactor/reactor-core)  
- **核心功能**：Spring WebFlux的底层框架，基于Reactive Streams规范，支持背压（避免数据溢出）。  
- **适合场景**：高并发API（如秒杀系统）、非阻塞数据库操作（如R2DBC）。

#### （2）RxJava 3
- **链接**：[GitHub](https://github.com/ReactiveX/RxJava)  
- **核心功能**：老牌响应式库，操作符丰富（如`map`/`flatMap`），生态成熟。  
- **适合场景**：Android开发、跨平台响应式逻辑。

### 6. 分布式与容错
#### （1）resilience4j
- **链接**：[GitHub](https://github.com/resilience4j/resilience4j)  
- **核心功能**：轻量级容错库，支持熔断（Circuit Breaker）、重试（Retry）、限流（RateLimiter）、超时控制。  
- **优势**：函数式API，无依赖，与Spring Cloud无缝集成（替代Hystrix）。

#### （2）Hazelcast
- **链接**：[GitHub](https://github.com/hazelcast/hazelcast)  
- **核心功能**：分布式内存数据网格（IMDG），支持分布式缓存、会话共享、分布式计算。  
- **适合场景**：需要跨服务共享数据的分布式系统。

### 7. 作业调度
#### （1）Quartz
- **链接**：[GitHub](https://github.com/quartz-scheduler/quartz)  
- **核心功能**：支持复杂调度（cron表达式、触发条件）、分布式调度、作业持久化。  
- **适合场景**：定时任务（如凌晨数据同步、定时报表生成）。

#### （2）Spring Scheduler
- **链接**：[Spring文档](https://docs.spring.io/spring-framework/docs/current/reference/html/integration.html#scheduling)  
- **核心功能**：基于注解的简单调度（`@Scheduled`），集成Spring生态。  
- **优势**：零配置，适合简单定时任务（如每5分钟执行一次）。

### 8. GUI与游戏开发
#### （1）JavaFX
- **链接**：[OpenJFX](https://wiki.openjdk.java.net/display/OpenJFX/Main)  
- **核心功能**：Swing的继任者，支持现代UI组件、动画、FXML布局。  
- **适合场景**：桌面应用开发（如管理工具、客户端）。

#### （2）libGDX
- **链接**：[官网](https://libgdx.com)  
- **核心功能**：跨平台游戏开发框架，支持2D/3D游戏，适配Windows/macOS/Android/iOS。  
- **优势**：API简洁，无需掌握多平台技术栈。


## 四、测试与代码质量
### 1. 测试框架
| 名称 | 链接 | 核心功能 | 优势 |
|------|------|----------|------|
| JUnit 5 | [官网](https://junit.org/junit5/) | 单元测试框架，支持参数化测试、动态测试、注解驱动 | 兼容JDK 8+，与IDE/构建工具无缝集成 |
| Mockito 4+ | [GitHub](https://github.com/mockito/mockito) | 模拟依赖对象（如数据库服务、第三方API） | 避免测试依赖外部系统，提高测试稳定性 |
| Testcontainers | [GitHub](https://github.com/testcontainers/testcontainers-java) | 基于Docker启动临时测试环境（MySQL、Redis等） | 测试环境与生产一致，解决「本地测通、线上报错」 |

### 2. 代码质量分析
- **Checkstyle**  
  [GitHub](https://github.com/checkstyle/checkstyle)  
  - 核心：检查代码规范（如变量命名、注释格式、代码长度）。  
  - 集成：支持Maven/Gradle插件、IDE插件，可自定义规则。

- **SpotBugs**  
  [GitHub](https://github.com/spotbugs/spotbugs)  
  - 核心：分析字节码，发现潜在Bug（如空指针、内存泄漏、未关闭流）。

- **PMD**  
  [GitHub](https://github.com/pmd/pmd)  
  - 核心：检查代码「坏味道」（如重复代码、未使用变量、死循环）。

### 3. 代码覆盖率
#### JaCoCo
- **链接**：[官网](https://www.eclemma.org/jacoco/)  
- **核心功能**：通过字节码插桩收集覆盖率数据，生成HTML报告（显示行覆盖、分支覆盖、类覆盖）。  
- **用途**：衡量测试完整性（企业级项目通常要求核心代码覆盖率≥80%）。


## 五、部署与诊断
### 1. 原生编译（云原生优化）
#### GraalVM
- **链接**：[官网](https://www.graalvm.org)  
- **核心功能**：将Java代码编译为原生可执行文件（`native-image`），启动时间从秒级降至毫秒级，内存占用减少60%+。  
- **适配**：支持Spring Boot 3+、Quarkus、Micronaut。  
- **适合场景**：K8s部署、Serverless应用、边缘计算设备。

### 2. 诊断工具
#### Arthas
- **链接**：[GitHub](https://github.com/alibaba/arthas)  
- **核心功能**：阿里开源的Java诊断工具，支持在线排查问题（如查看JVM状态、反编译类、跟踪方法调用）。  
- **实用命令**：  
  - `dashboard`：查看JVM实时状态  
  - `jad com.example.UserService`：反编译类  
- **优势**：无需重启应用，线上问题排查神器。


## 六、常用组件集：Apache Commons 精选
剔除过时组件（如DBCP、FileUpload），保留高频使用工具：
- **Commons Lang 3**：[官网](https://commons.apache.org/proper/commons-lang/)  
  增强`java.lang`包，提供`StringUtils`（空判断、拼接）、`ObjectUtils`（对象比较）等工具。
- **Commons IO**：[官网](https://commons.apache.org/proper/commons-io/)  
  简化I/O操作，如`FileUtils.copyFile()`（文件复制）、`IOUtils.toString()`（流转字符串）。
- **Commons Codec**：[官网](https://commons.apache.org/proper/commons-codec/)  
  编解码工具，支持Base64、MD5、SHA等。
- **Commons CSV**：[官网](https://commons.apache.org/proper/commons-csv/)  
  快速读写CSV文件，避免手动解析的繁琐。
- **Commons Compress**：[官网](https://commons.apache.org/proper/commons-compress/)  
  操作压缩格式（ZIP、TAR、GZIP）的工具集。


## 七、资源推荐
### 1. 书籍
| 书名 | 核心价值 | 适合人群 |
|------|----------|----------|
| 《Effective Java（第3版）》 | Java开发最佳实践，覆盖并发、集合、面向对象等核心领域 | 所有Java开发者（必读） |
| 《Java Concurrency in Practice》 | 深入讲解Java并发编程原理与线程安全实践 | 中高级开发者（解决并发问题） |
| 《Spring实战（第6版）》 | 从基础到实战，掌握Spring Boot 3+与微服务开发 | 后端开发者（Spring生态入门） |
| 《领域驱动设计：软件核心复杂性应对之道》 | 学习DDD思想，设计可扩展的大型系统 | 架构师、高级开发者 |

### 2. 网站与社区
- **Baeldung**：[官网](https://www.baeldung.com)  
  高质量Java教程，覆盖Spring、并发、测试等领域，示例代码可直接复用。
- **JavaGuide**：[GitHub](https://github.com/Snailclimb/JavaGuide)  
  开源Java知识图谱，从基础到面试全覆盖（国内开发者首选）。
- **Oracle Java Tutorials**：[官网](https://docs.oracle.com/javase/tutorial/)  
  官方教程，权威讲解JDK原生API（如`java.time`、集合框架）。
- **Stack Overflow（Java标签）**：[链接](https://stackoverflow.com/questions/tagged/java)  
  解决Java开发中的具体问题，社区响应速度快。
