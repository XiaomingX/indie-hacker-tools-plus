# Google Cloud (GCP) 服务选型与评估 (2026)

GCP 以数据处理和标准化容器服务见长。在选型时应注重服务的长期确定性和效率原则，避开高维护成本或实验性质的产品。

---

## 核心标准化服务 (Core & Standard)

GCP 竞争力最强的领域。

- **BigQuery (Serverless Data Warehouse)**
  - **点评：** GCP 皇冠上的明珠。存储与计算分离的架构极大地提升了处理 PB 级数据的效率。其优势在于全托管、免运维及极高的操作门槛优势。
- **Google Kubernetes Engine (GKE)**
  - **点评：** K8s 嫡系方案。自动化程度高、集群管理最成熟。作为事实上的行业标准，拥有极高的人才流动性和生态稳定性。
- **Cloud Run (Serverless Containers)**
  - **点评：** 高效率计算。将 Serverless 理念与容器标准结合，按需付费，闲时归零。极大地降低了开发者对基础设施的关注度。
- **Cloud Storage**
  - **点评：** GCP 所有业务的稳固基石。对象存储是云端业务的必需组件，具备极高的耐用性和退出壁垒。

---

## 特色与未来增量

- **Vertex AI**
  - **点评：** 集成模型开发、部署与 Gemini 模型能力。作为 AI 基建的先驱，控制了进入 AI 门槛的高效路口，是未来增长的核心配置。
- **Cloud Spanner**
  - **点评：** 全球强一致性数据库。虽然成本较高，但在全球化高并发交易场景下，其确定性无与伦比。

---

## 建议剔除/不予考虑

避免投入精力到缺乏长期生命力或已有更优替代品的平庸服务中：
- **过时架构**：App Engine (GAE) —— 臃肿且灵活性差，已被 Cloud Run/GKE 取代。
- **次选存储**：Cloud Datastore / Filestore —— 通用性及性价比通常不如 Firestore/Cloud Storage。
- **低版本服务**：Cloud Functions (1st Gen)。
- **厂商锁定工具**：Cloud Deployment Manager (建议统一使用开源的 Terraform)。

---

### 选型逻辑建议

1. **核心配置：** BigQuery + Cloud Run。
2. **规模支撑：** GKE 负责复杂应用托管，Vertex AI 负责智能化需求。
3. **风险管理：** 避开已过时的 PaaS 方案和非标准的专有部署工具。
