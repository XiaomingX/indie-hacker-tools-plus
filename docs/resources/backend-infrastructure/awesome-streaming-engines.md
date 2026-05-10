# 流处理引擎与实时数据架构 (2026 Checklist)

> [!TIP]
> **Indie Hacker Insight**: 2026 年，流处理不再是大厂的专利，而是**实时响应业务**的基础。
> - **Serverless 化**：对于独立开发者，优先选择 **Upstash Kafka** 或 **Confluent Cloud**，避免维护复杂的 Kafka 集群。
> - **SQL 驱动**：使用 **RisingWave** 或 **ksqlDB**，让你用熟悉的 SQL 语法就能处理复杂的实时计算任务。
> - **AI 集成**：流处理不仅是为了统计，更是为了给 **AI Agents** 提供实时上下文（RAG 2.0）。

---

## 🏗️ 核心流处理引擎 (Compute Engines)

- [ ] [**Apache Flink**](https://github.com/apache/flink) - **[工业标准]** 真正的实时流处理，毫秒级延迟，支持复杂的“有状态”计算（Exactly-Once）。
- [ ] [**RisingWave**](https://github.com/risingwavelabs/risingwave) - **2026 推荐**。基于 Rust 的流数据库，100% 兼容 PostgreSQL 语法，极大地降低了流处理门槛。
- [ ] [**Bytewax**](https://github.com/bytewax/bytewax) - 专为 Python 开发者设计，适合将 Python 生态（Pandas, ML）无缝引入实时流。
- [ ] [**Apache Spark Streaming**](https://github.com/apache/spark) - 适合“批流一体”场景，如果你的项目已经在用 Spark 进行离线分析，这是最自然的选择。

---

## 🛣️ 数据管道与消息队列 (MQ & Pipelines)

- [ ] [**Redpanda**](https://github.com/redpanda-data/redpanda) - **[高性能]** 100% 兼容 Kafka 协议，但去除了 JVM 和 Zookeeper，性能极高且部署极其简单。
- [ ] [**Upstash Kafka**](https://upstash.com/kafka) - **独立开发者首选**。Serverless 架构，按量付费，0 运维成本。
- [ ] [**Apache Pulsar**](https://github.com/apache/pulsar) - 云原生消息平台，支持多租户和无限存储，适合大规模企业级应用。
- [ ] [**Apache RocketMQ**](https://github.com/apache/rocketmq) - 阿里开源，在分布式事务和金融级消息可靠性方面表现最佳。

---

## 🔍 实时分析与 SQL 引擎 (SQL & Analytics)

- [ ] [**ksqlDB**](https://github.com/confluentinc/ksql) - 与 Kafka 深度绑定的流处理数据库，通过 SQL 即可定义流转表逻辑。
- [ ] [**Flink CDC**](https://github.com/ververica/flink-cdc-connectors) - 实时捕获数据库（MySQL, PG）变更，是构建实时索引（Elasticsearch）的灵魂工具。
- [ ] [**Benthos (Redpanda Connect)**](https://github.com/Jeffail/benthos) - 极简的数据流转工具，通过 YAML 配置即可实现 50+ 数据源之间的清洗与转发。

---

## 🤖 实时机器学习与 AI (Real-time ML/AI)

- [ ] [**River**](https://github.com/online-ml/river) - Python 在线学习库，支持数据“即来即训”，适合实时异常检测。
- [ ] [**Quix**](https://quix.io/) - 专为高性能 AI 应用设计的流处理平台，支持 Python 全栈实时化。

---

## 💡 选型建议
1. **构建极速 MVP**：选 **Upstash Kafka** + **Benthos**。快速打通数据流，无需运维。
2. **需要处理复杂业务逻辑（如金融风控）**：选 **Apache Flink**。
3. **传统 SQL 开发者转实时计算**：无脑选 **RisingWave**。
4. **边缘计算/物联网场景**：使用 **Kuiper**，内存占用极低。
