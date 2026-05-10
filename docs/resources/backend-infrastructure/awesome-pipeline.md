# 2026 数据流水线与任务调度指南 (Checklist)

> [!TIP]
> **Indie Hacker Insight**: 2026 年，流水线管理已从“脚本堆砌”进化为“资产编排 (Asset Orchestration)”。
> - **Python 优先**：现代流水线（如 Airflow, Dagster）均以 Python 为核心，方便集成 AI 模型与复杂逻辑。
> - **可观察性**：不仅要能跑通，还要能实时监控每一步的耗时与资源消耗，及时发现性能瓶颈。
> - **云原生**：优先考虑支持 Kubernetes 原生运行的方案（如 Argo），实现资源的按需缩放。

---

## 🏗️ 核心任务调度平台 (Orchestration)

- [ ] [**Apache Airflow**](https://airflow.apache.org/) - **[行业标准]** 功能最全，生态最广，适合复杂的企业级调度。
- [ ] [**Dagster**](https://dagster.io/) - **[推荐]** 现代化的资产编排系统，提供极其强大的开发与调试体验。
- [ ] [**Argo Workflows**](https://argoproj.github.io/argo-workflows/) - Kubernetes 原生流，适合容器化程度高的生产环境。
- [ ] [**Prefect**](https://www.prefect.io/) - “调度即代码”的典范，配置极简，适合快速原型与中型项目。
- [ ] [**Temporal**](https://temporal.io/) - 保证工作流的耐用性与容错性，适合支付、订单等关键业务流。

---

## 🚀 大数据与并行计算 (Parallel Computing)

- [ ] [**Apache Beam**](https://beam.apache.org/) - 统一批处理与流处理的编程模型。
- [ ] [**Dask**](https://www.dask.org/) - 为 Python 提供灵活的并行计算能力，与 NumPy/Pandas 无缝集成。
- [ ] [**Ray**](https://www.ray.io/) - 高性能分布式执行框架，2026 年大模型训练与推理的首选底座。

---

## 🧬 科学计算与生物信息 (Scientific Pipelines)

- [ ] [**Nextflow**](https://www.nextflow.io/) - 科学计算领域的标准，支持极佳的可重现性。
- [ ] [**Snakemake**](https://snakemake.readthedocs.io/) - Python 风格的科学流管理，深受生物信息学家喜爱。
- [ ] [**Cromwell**](https://github.com/broadinstitute/cromwell) - 针对 WDL 语言的大规模批处理引擎。

---

## 🛠️ 数据处理与 ETL (Data Processing)

- [ ] [**dbt (Data Build Tool)**](https://www.getdbt.com/) - 让数据分析师能用 SQL 编写生产级的数据转换流。
- [ ] [**Kestra**](https://kestra.io/) - 声明式的全场景编排平台，支持海量插件。
- [ ] [**Mara**](https://github.com/mara/data-integration) - 轻量级的 Python ETL 框架，适合不需要 Airflow 这种重型工具的场景。

---

## 💡 选型建议
1. **企业级数据仓库与复杂 ETL**：首选 **Apache Airflow**。
2. **注重开发体验与数据血缘 (Data Lineage)**：强制选 **Dagster**。
3. **构建高可用的分布式计算应用**：选 **Ray**。
4. **科学研究与高度可重复性实验**：选 **Nextflow** 或 **Snakemake**。
