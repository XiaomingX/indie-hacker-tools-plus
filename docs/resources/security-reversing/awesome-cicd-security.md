# 2026 CI/CD 管道安全加固指南 (Checklist)

> [!TIP]
> **Indie Hacker Insight**: 2026 年，CI/CD 管道已成为黑客攻击的第一目标。
> - **安全左移**：在代码提交的那一刻就开始安全扫描，而非等部署到生产环境才发现。
> - **零信任管道**：流水线中的每一个 Step 都应该只有其完成任务所需的最小权限。
> - **供应链溯源**：使用 SLSA 框架对你的构建产物进行签名，确保从源码到镜像的每一步都可信。

---

## 🏗️ 权威指南与框架 (Frameworks)

- [ ] [**SLSA (Supply-chain Levels for Software Artifacts)**](https://slsa.dev/) - **[行业标准]** 确保软件供应链端到端的完整性。
- [ ] [**OWASP CI/CD Security Top 10**](https://owasp.org/www-project-top-10-ci-cd-security-risks/) - 了解管道中最常见的 10 大安全风险。
- [ ] [**NIST SP 800-204D**](https://csrc.nist.gov/pubs/sp/800/204/d/final) - 云原生应用的 CI/CD 安全部署标准。
- [ ] [**CISA Defending CI/CD Environments**](https://media.defense.gov/2023/Jun/28/2003249466/-1/-1/0/CSI_DEFENDING_CI_CD_ENVIRONMENTS.PDF) - CISA 与 NSA 联合发布的管道硬化指南。

---

## 🛠️ 自动化扫描与审计工具 (Security Tools)

- [ ] [**Snyk**](https://snyk.io/) - **[首选]** 扫描第三方依赖漏洞与 IaC 配置错误。
- [ ] [**Trivy**](https://github.com/aquasecurity/trivy) - 多功能的容器镜像、文件系统与 Git 仓库漏洞扫描器。
- [ ] [**Gitleaks**](https://github.com/gitleaks/gitleaks) - 极其高效的本地/流水线秘密（Secrets）扫描工具。
- [ ] [**Semgrep**](https://semgrep.dev/) - 静态代码审计 (SAST)，支持极简的自定义规则编写。
- [ ] [**Cosign**](https://github.com/sigstore/cosign) - 对容器镜像进行签名与验证的行业标准。

---

## 🗝️ 秘密管理与权限控制 (Secrets & Auth)

- [ ] [**HashiCorp Vault**](https://www.vaultproject.io/) - 动态密钥管理，支持短效令牌与自动轮换。
- [ ] [**GitHub Actions Permissions**](https://docs.github.com/en/actions/security-guides/automatic-token-authentication#modifying-the-permissions-for-the-github_token) - 严格限制 `GITHUB_TOKEN` 的 scope，默认应为 `read-only`。
- [ ] [**AWS Secrets Manager**](https://aws.amazon.com/secrets-manager/) - 为 AWS 环境下的流水线提供原生的凭证轮换服务。

---

## 🧪 攻防演练场 (Practice)

- [ ] [**CI/CD Goat**](https://github.com/cider-security-research/cicd-goat) - **[必练]** 模拟了 10+ 种真实管道漏洞的靶场。
- [ ] [**OWASP CI/CD Security Lab**](https://owasp.org/www-project-ci-cd-security-lab/) - 侧重于供应链攻击场景的实战演练。

---

## 💡 选型建议
1. **构建全新的 GitHub 项目**：强制启用 **GitHub Advanced Security (Secret Scanning + CodeQL)**。
2. **需要分发容器镜像**：流水线中必须集成 **Trivy** 扫描与 **Cosign** 签名。
3. **管理跨云凭证**：选 **HashiCorp Vault** 作为唯一的真理来源。
4. **针对初创公司的低成本方案**：集成 **Gitleaks** 到 Pre-commit Hook。
