# 2026 Docker 与容器镜像安全加固指南 (Checklist)

> [!TIP]
> **Indie Hacker Insight**: 2026 年，容器安全的核心在于“最小化基础镜像”与“运行时可见性”。
> - **Distroless 优先**：如果不需要 Shell 调试，优先使用 Distroless 镜像，能减少 90% 以上的攻击面。
> - **Root 禁用**：严禁在容器内使用 Root 用户运行进程，利用 `USER` 指令指定非特权账号。
> - **只读文件系统**：对于无状态服务，启动时加上 `--read-only`，能有效阻断黑客持久化恶意代码。

---

## 🏗️ 基础镜像与构建安全 (Image Security)

- [ ] [**Docker 官方安全最佳实践**](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/) - **[必读]** 掌握多阶段构建与缓存优化。
- [ ] [**Google Distroless Images**](https://github.com/GoogleContainerTools/distroless) - 仅包含运行应用所需的最小二进制文件。
- [ ] [**Chainguard Images**](https://www.chainguard.dev/chainguard-images) - 专为零漏洞（Zero-CVE）设计的生产级加固镜像。
- [ ] [**Hadolint**](https://github.com/hadolint/hadolint) - Dockerfile 静态检查工具，自动纠正不安全指令。

---

## 🛠️ 自动化扫描与审计 (Scanning Tools)

- [ ] [**Trivy**](https://github.com/aquasecurity/trivy) - **[首选]** 支持镜像漏洞、IaC、秘密信息全方位扫描。
- [ ] [**Clair**](https://github.com/quay/clair) - 针对容器层漏洞的静态分析引擎。
- [ ] [**Anchore Engine**](https://github.com/anchore/anchore-engine) - 强大的镜像合规性审计与政策引擎。
- [ ] [**Grype**](https://github.com/anchore/grype) - 极其快速的镜像漏洞扫描器，适配 SBOM。

---

## 🛡️ 运行时防御与加固 (Runtime Security)

- [ ] [**Docker Bench for Security**](https://github.com/docker/docker-bench-security) - 自动检测 Docker 宿主机与配置是否符合 CIS 标准。
- [ ] [**Falco**](https://falco.org/) - 云原生环境下的实时行为审计与威胁监控工具。
- [ ] [**AppArmor / Seccomp**](https://docs.docker.com/engine/security/apparmor/) - 利用内核安全模块限制容器的系统调用权限。
- [ ] [**Cosign**](https://github.com/sigstore/cosign) - 构建环节签署镜像，运行时验证镜像完整性。

---

## 💡 选型建议
1. **构建生产级 Python 应用**：选 **Chainguard Python 镜像**，强制禁用 Root。
2. **在 CI 流水线中集成分钟级扫描**：选 **Trivy**。
3. **需要极高的运行时安全可见性**：部署 **Falco** 监控异常系统调用。
4. **针对初创公司的低成本加固**：使用 **Hadolint** 优化 Dockerfile，并开启 `--read-only`。
