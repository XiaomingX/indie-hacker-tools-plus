# AWS 服务选型与评估 (2026)

在 2026 年，AWS 的基础设施是云服务的核心标准。我们应优先选择具有高稳定性、高效率和高不可替代性的核心服务。

---

## 核心基础设施 (Core Infrastructure)

这些服务是云上业务的基石。

- **S3 (Simple Storage Service)**
  - **点评：** 极其稳固、耐用且低成本的对象存储。它是数字化世界的底层仓库，无论业务规模大小，S3 都是数据存储的最优选。
- **EC2 (Elastic Compute Cloud)**
  - **点评：** 核心计算资源。特别是基于 **Graviton (ARM 架构)** 的实例，在提升性能的同时显著降低了运行成本，是降本增效的核心手段。
- **RDS (Relational Database Service)**
  - **点评：** 关系型数据库托管首选。将复杂的数据库运维工作抽象化，使团队能专注于业务逻辑，是业务数据的核心托管地。

---

## 高效生产力服务 (Productivity & Serverless)

代表了现代云原生开发的先进生产力。

- **Lambda (Serverless)**
  - **点评：** 精益生产的代表。按需计费，无闲置成本，能显著降低中小型任务或非连续任务的运行开销。
- **DynamoDB**
  - **点评：** 高性能 NoSQL。具备极强的水平扩展能力和极低的访问延迟，适合应对瞬间爆发的业务需求。
- **Amazon Bedrock (Generative AI)**
  - **点评：** 生成式 AI 集成平台。作为模型“渠道商”，通过统一 API 整合多种顶尖模型，避免了单一模型锁定的风险，是构建 AI 应用的高效入口。

---

## 关键辅助组件

- **IAM (Identity and Access Management)**：权限控制的核心，确保资产安全。
- **VPC / PrivateLink**：确保网络流量的安全隔离与私有连接。

---

## 建议剔除/避开项

鉴于 AWS 官方维护计划或市场竞争情况，以下服务建议在 2026 年避开：
- **已停止/减弱支持**：Amazon Pinpoint, CloudWatch Evidently。
- **生态替代方案更强**：CodeCatalyst/CodeGuru (推荐 GitHub/GitLab), Timestream (官方推荐转向 InfluxDB)。
- **被新技术取代**：Elastic Beanstalk (建议转向 EKS 或 Lambda/Cloud Run)。

---

### 选型建议

1. **重仓基础（S3/EC2/RDS）**：确保架构的核心稳固。
2. **拥抱效率（Lambda/Bedrock）**：利用 Serverless 和 AI 提升产品竞争力。
3. **规避风险**：停止在已被边缘化或官方宣布即将停止支持的服务上进行投入。
