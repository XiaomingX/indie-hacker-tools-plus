# Awesome-Streaming （ 主流流处理引擎与工具精选 ）
以下是为中国开发者优化的**主流、高实用性**流处理相关工具列表，剔除了小众、社区活跃度低的内容，重点补充工具的「核心优势」和「实际适用场景」，帮你快速匹配业务需求。


## 一、核心流处理引擎
流处理引擎是实时数据处理的「核心大脑」，负责对持续产生的数据流进行计算、分析和转换。

### 1. Apache Flink [Java/Scala]
- **核心优势**：真正的「实时流处理」（而非微批），兼具**高吞吐**（每秒处理百万级数据）和**低延迟**（毫秒级响应）；支持「有状态计算」（能留存中间结果，比如累计用户全天行为）、窗口计算（按时间/数量聚合数据），且容错性极强。
- **适用场景**：实时风控（比如秒级识别异常交易）、实时日志分析（监控系统故障）、实时数据大屏（电商实时销量统计）。
- 👉 [GitHub 地址](https://github.com/apache/flink)

### 2. Apache Spark Streaming [Scala/Java/Python]
- **核心优势**：基于 Spark 生态的「微批流处理」（把数据流切成小批次计算），上手门槛低，能无缝对接 Spark 的批处理、SQL 等能力，适合「批流一体」的场景（同一套代码处理实时和离线数据）。
- **适用场景**：实时数据ETL（比如将日志实时清洗后写入数据库）、准实时分析（对延迟要求不极致的场景，如每5分钟更新一次的用户画像）。
- 👉 [GitHub 地址](https://github.com/apache/spark)

### 3. Apache Kafka Streams [Java/Scala]
- **核心优势**：轻量级流处理库，**与 Kafka 消息中间件无缝集成**（无需额外部署独立集群），开发成本低，适合基于 Kafka 数据流的简单实时计算。
- **适用场景**：实时数据过滤（比如从全量日志中筛选出报错日志）、数据格式转换（比如将 JSON 转为 Parquet）、简单聚合（比如统计某类消息的每秒数量）。
- 👉 [GitHub 地址](https://github.com/apache/kafka)

### 4. Bytewax [Python]
- **核心优势**：少数原生支持 Python 的分布式流处理框架，语法简洁，对数据科学家和 Python 开发者极其友好；支持有状态计算和动态扩缩容。
- **适用场景**：快速验证实时算法原型（比如实时推荐模型的初步测试）、Python 生态下的实时数据处理（比如用 Pandas 实时分析数据流）。
- 👉 [GitHub 地址](https://github.com/bytewax/bytewax)

### 5. RisingWave [Rust]
- **核心优势**：「流数据库」的代表，支持 **PostgreSQL 兼容的 SQL**（熟悉 SQL 就能开发，无需学新语法）；能将实时计算结果以表的形式暴露，可直接用 SQL 查询。
- **适用场景**：实时报表生成（用 SQL 写持续查询，结果实时更新）、实时ETL（通过 SQL 完成数据清洗和同步）、事件驱动应用（比如订单状态实时追踪）。
- 👉 [GitHub 地址](https://github.com/risingwavelabs/risingwave)

### 6. Materialize [Rust]
- **核心优势**：专注「持续 SQL 查询」的流处理数据库，查询性能极强，支持复杂的 JOIN 和聚合操作；能自动感知数据源变化并更新结果。
- **适用场景**：实时监控仪表盘（比如监控各服务的接口调用成功率）、实时数据分析（业务人员用 SQL 实时查询最新数据）。
- 👉 [官网地址](https://materialize.com)


## 二、数据管道与消息中间件
相当于实时数据的「高速公路」，负责在数据源（比如日志、数据库）和处理引擎之间传输数据，解决「数据怎么传、传得稳」的问题。

### 1. Apache Kafka [Scala/Java]
- **核心优势**：分布式消息中间件的「事实标准」，支持**高吞吐**（百万级/秒）、高持久化（数据落地磁盘不丢失）、分区扩展（可通过加分区提升容量）。
- **适用场景**：日志集中收集（比如全公司服务的日志都发送到 Kafka）、数据流解耦（数据源和处理引擎不直接依赖，通过 Kafka 对接）、事件溯源（记录系统所有操作事件）。
- 👉 [GitHub 地址](https://github.com/apache/kafka)

### 2. Apache Pulsar [Java]
- **核心优势**：云原生架构（存储和计算分离），支持「多租户」（不同团队隔离使用）、「延迟队列」（消息定时投递）、「消息回溯」（重新消费历史数据），比 Kafka 更灵活。
- **适用场景**：云环境下的多团队数据共享、需要定时处理的任务（比如订单超时未支付提醒）、需要回溯数据的场景（比如算法迭代后重新计算历史指标）。
- 👉 [GitHub 地址](https://github.com/apache/pulsar)

### 3. Redpanda [C++]
- **核心优势**：100% 兼容 Kafka API（可直接替换 Kafka 无需改代码），但**去掉了 Kafka 对 ZooKeeper 和 JVM 的依赖**，部署更简单、性能更高（延迟比 Kafka 低30%+）。
- **适用场景**：想简化架构的 Kafka 现有用户、对性能要求极致的场景（比如高频交易数据传输）。
- 👉 [GitHub 地址](https://github.com/redpanda-data/redpanda)

### 4. Apache RocketMQ [Java]
- **核心优势**：阿里开源的消息中间件，对「事务消息」支持极佳（比如分布式事务中的消息一致性），稳定性经过双11等高并发场景验证。
- **适用场景**：金融级业务（比如银行转账通知）、电商高并发场景（比如秒杀订单消息）、分布式系统通信（服务间异步调用）。
- 👉 [GitHub 地址](https://github.com/apache/rocketmq)


## 三、实时机器学习工具
针对「数据流实时训练模型」或「用训练好的模型实时预测」的场景，解决「AI 模型怎么实时用」的问题。

### 1. River [Python]
- **核心优势**：轻量级「在线机器学习库」，支持**增量学习**（数据来了就更新模型，不用重新训练全量数据）；兼容 Scikit-learn 接口，上手快。
- **适用场景**：实时异常检测（比如实时识别网络攻击流量）、实时推荐（根据用户最新行为更新推荐模型）、流数据分类（比如实时过滤垃圾评论）。
- 👉 [GitHub 地址](https://github.com/online-ml/river)

### 2. Flink MLlib [Java/Scala/Python]
- **核心优势**：Flink 生态的机器学习库，能将训练好的模型直接嵌入 Flink 流处理任务，实现「实时训练 + 实时预测」一体化；支持分类、回归、聚类等常见算法。
- **适用场景**：基于 Flink 的端到端实时 AI 场景（比如实时风控模型的训练和预测在同一 Flink 集群完成）。
- 👉 [GitHub 地址](https://github.com/apache/flink-ml)


## 四、流处理 SQL 引擎
让非开发人员（比如数据分析师）也能用 SQL 操作数据流，降低实时处理的使用门槛。

### 1. ksqlDB [Java]
- **核心优势**：Confluent 公司推出的 SQL 引擎，**与 Kafka 深度绑定**（数据来源/输出都是 Kafka 主题）；支持创建流（对应 Kafka 主题）、表（对应聚合结果），语法贴近标准 SQL。
- **适用场景**：Kafka 生态下的 SQL 实时分析（比如用 SQL 统计 Kafka 中某商品的实时销量）、快速构建实时数据管道（用 SQL 完成数据清洗和转发）。
- 👉 [GitHub 地址](https://github.com/confluentinc/ksql)

### 2. Siddhi [Java]
- **核心优势**：专注「复杂事件处理（CEP）」的 SQL 引擎，能识别数据流中的「事件模式」（比如「5分钟内连续3次登录失败」）。
- **适用场景**：实时监控告警（比如服务器 CPU 连续10秒超过90%则触发告警）、业务规则引擎（比如识别刷单行为的序列事件）。
- 👉 [GitHub 地址](https://github.com/siddhi-io/siddhi)


## 五、边缘流处理引擎
针对「边缘设备（比如工业传感器、物联网网关）」的流处理需求，解决「设备端数据怎么本地实时处理」的问题。

### 1. Kuiper [Go]
- **核心优势**：轻量级引擎（内存占用仅几十 MB），专为资源受限的边缘设备设计；支持 SQL 语法，能对接 MQTT 等边缘常用协议，数据本地处理后再上传云端（减少带宽消耗）。
- **适用场景**：工业物联网（比如车间传感器数据本地过滤和聚合）、边缘网关（比如智能家居设备数据本地分析）。
- 👉 [GitHub 地址](https://github.com/emqx/kuiper)


## 六、实用工具与学习资源
### 1. 必备工具
#### （1）Flink CDC [Java]
- **核心作用**：基于 Flink 的「变更数据捕获」工具，能实时捕获 MySQL、PostgreSQL 等数据库的增删改查（CDC）数据，无需侵入业务系统（不用改代码加日志）。
- **适用场景**：实时数据同步（比如将业务库数据实时同步到数据仓库）、数据库变更实时监控（比如实时追踪订单状态变更）。
- 👉 [GitHub 地址](https://github.com/ververica/flink-cdc-connectors)

#### （2）Benthos [Go]
- **核心作用**：高性能「数据流转工具」，支持 50+ 数据源（Kafka、MQTT、S3 等）和接收器（数据库、 Elasticsearch 等），能通过配置完成数据过滤、转换、路由（无需写代码）。
- **适用场景**：多源数据整合（比如将 Kafka 和 MQTT 的数据合并后写入 Elasticsearch）、数据格式转换（比如将 CSV 转为 JSON）。
- 👉 [GitHub 地址](https://github.com/Jeffail/benthos)

### 2. 推荐学习资源
#### （1）官方文档
- **Apache Flink 官方文档**：最权威的 Flink 入门指南，包含核心概念（流/批、状态、窗口）和实战教程。  
  👉 [中文地址](https://nightlies.apache.org/flink/flink-docs-release-1.18/zh/)

- **Kafka 中文文档**：详细讲解 Kafka 的架构、使用场景和最佳实践。  
  👉 [地址](https://kafka.apache.org/documentation/)

#### （2）经典书籍
- 《Streaming Systems》：流处理领域的「圣经」，由 Google 和 Cloudera 工程师撰写，深入讲解流处理的核心理论（比如水位线、Exactly-Once 语义）。
- 《Flink 原理与实践》：国内 Flink 专家编写，结合实战案例讲解 Flink 的架构和调优技巧，适合国内开发者。

#### （3）实战教程
- **Confluent Kafka Streams 教程**：通过实际案例（比如实时单词计数、用户行为分析）讲解 Kafka Streams 的使用。  
  👉 [地址](https://docs.confluent.io/platform/current/streams/tutorial.html)
