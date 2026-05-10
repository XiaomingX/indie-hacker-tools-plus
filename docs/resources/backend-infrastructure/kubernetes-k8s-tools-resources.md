# Kubernetes (K8s) 云原生架构资源精选 (2026 Checklist)

> [!TIP]
> **Indie Hacker Insight**: 2026 年，对于独立开发者而言，**“不去管理 K8s”** 往往是最好的策略。
> - **Serverless 优先**：如果可能，优先选择 **Google Cloud Run** 或 **AWS Fargate** 等无服务器容器服务。
> - **轻量化选择**：如果必须自建，**K3s** 是唯一的省心选择，它极大地降低了运维的心智负担。
> - **AI 运维**：利用 **K8s GPT** 可以自动分析集群报错，节省大量排障时间。

---

## 🏗️ 核心控制与效率工具 (Efficiency & CLI)

- [ ] [**K9s**](https://github.com/derailed/k9s) - **[必备]** 终端里的可视化控制台，实时监控 Pod 状态、查看日志、甚至直接修改配置。
- [ ] [**Helm**](https://github.com/helm/helm) - K8s 的“应用包管理器”，通过 Chart 快速部署 Redis、PostgreSQL 等基础组件。
- [ ] [**kubectx + kubens**](https://github.com/ahmetb/kubectx) - 极速切换集群上下文 (Context) 和命名空间 (Namespace)，运维防错利器。
- [ ] [**stern**](https://github.com/stern/stern) - 支持按正则匹配多个 Pod 日志，颜色区分流输出，微服务排障必装。

---

## ⚡ 集群部署与本地环境 (Deployment & Local)

- [ ] [**K3s**](https://github.com/rancher/k3s) - **[2026 推荐]** 极轻量级发行版，内存占用极低，单机即可跑全套 K8s 功能，适合边缘计算与 VPS 部署。
- [ ] [**kind (Kubernetes in Docker)**](https://github.com/kubernetes-sigs/kind) - 适合本地 CI 测试，在 Docker 容器里运行 K8s 节点，启动极快。
- [ ] [**Skaffold**](https://github.com/GoogleContainerTools/skaffold) - 自动化“构建-推送-部署”循环，让 K8s 上的开发体验像本地实时热更新一样丝滑。

---

## 🚀 自动化治理与 GitOps (Automation & GitOps)

- [ ] [**Argo CD**](https://github.com/argoproj/argo-cd) - GitOps 的事实标准，Git 里的 YAML 一变，集群自动同步，支持可视化回滚。
- [ ] [**KEDA**](https://github.com/kedacore/keda) - 事件驱动的自动扩缩容，支持根据消息队列堆积量、指标自动将 Pod 从 0 扩容。
- [ ] [**Velero**](https://github.com/vmware-tanzu/velero) - 集群资源与 PV 持久化数据的备份与迁移工具。

---

## 🛡️ 可观测性与安全 (Observability & Security)

- [ ] [**Prometheus + Grafana**](https://github.com/prometheus-operator/kube-prometheus) - 监控全家桶，kube-prometheus-stack 是一键部署的最佳选择。
- [ ] [**Loki**](https://github.com/grafana/loki) - 像 Prometheus 一样管理日志，轻量高效。
- [ ] [**Trivy**](https://github.com/aquasecurity/trivy) - 全能安全扫描器，自动检查镜像漏洞、配置不当及敏感信息泄露。

---

## 💡 选型建议
1. **个人项目/原型验证**：用 **K3s** 或托管的 **Google Cloud Run**。
2. **需要管理多个集群**：必装 **K9s** 和 **kubectx**。
3. **实现自动化部署**：选 **GitHub Actions** + **Argo CD (GitOps)**。
4. **追求集群安全性**：在 CI 阶段集成 **Trivy** 扫描。
