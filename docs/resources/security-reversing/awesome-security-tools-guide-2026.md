# 2026 安全工具与防御实战指南 (Checklist)

> [!TIP]
> **Indie Hacker Insight**: 2026 年，网络安全已经演变为 AI 攻防战。
> - **零信任架构**：不要信任任何内部网络，所有服务调用必须经过严格的身份验证与令牌校验。
> - **静态代码审计 (SAST)**：在 CI/CD 流水线中强制集成扫描工具，拒绝任何带漏洞的代码合并。
> - **主动防御**：定期进行渗透测试，或者在 Bug Bounty 平台（如 HackerOne）上悬赏，让全球白帽帮你找茬。

---

## 🛡️ 网络扫描与信息收集 (Scanning & Recon)

- [ ] [**Nmap**](https://nmap.org/) - 行业标准的端口扫描与网络发现工具。
- [ ] [**Burp Suite**](https://portswigger.net/burp) - **[必选]** Web 应用安全测试的瑞士军刀。
- [ ] [**Amass (OWASP)**](https://github.com/OWASP/Amass) - 深度子域名挖掘与资产发现。
- [ ] [**Masscan**](https://github.com/robertdavidgraham/masscan) - 极速端口扫描，可在几分钟内扫描完整个互联网。

---

## 🧪 静态与动态漏洞分析 (Analysis)

- [ ] [**SonarQube**](https://www.sonarsource.com/products/sonarqube/) - 企业级静态代码质量与安全审计。
- [ ] [**Snyk**](https://snyk.io/) - **[推荐]** 自动检测第三方依赖（npm, pip, cargo）中的已知漏洞。
- [ ] [**Semgrep**](https://semgrep.dev/) - 轻量级且极速的静态扫描工具，支持自定义规则。
- [ ] [**ZAP (OWASP)**](https://www.zaproxy.org/) - 免费开源的 Web 动态扫描替代方案。

---

## 🗝️ 密码学与身份鉴权 (Auth & Crypto)

- [ ] [**Hashcat**](https://hashcat.net/hashcat/) - 全球最快的密码破解与恢复工具。
- [ ] [**John the Ripper**](https://www.openwall.com/john/) - 经典的离线密码破解器。
- [ ] [**Vault (HashiCorp)**](https://www.vaultproject.io/) - **[必选]** 集中管理 Secret、API Key 与动态证书。
- [ ] [**Auth0 / Clerk**](https://clerk.com/) - 现代化的用户身份认证服务，支持 Passkeys 与多因子认证。

---

## 🚀 运维安全与应急响应 (SecOps)

- [ ] [**Wazuh**](https://wazuh.com/) - 开源的安全监控、端点检测 (EDR) 与合规管理平台。
- [ ] [**Metasploit**](https://www.metasploit.com/) - 渗透测试框架，包含海量溢出攻击载荷。
- [ ] [**Cloudflare WAF**](https://www.cloudflare.com/waf/) - 边缘侧的防御屏障，有效阻挡 DDoS 与 SQL 注入。

---

## 💡 选型建议
1. **构建生产级 SaaS**：必须集成 **Snyk** 监控依赖风险，并使用 **Vault** 管理密钥。
2. **需要进行合规性检查 (SOC2/ISO27001)**：首选 **Wazuh** 进行日志审计。
3. **针对个人开发者的轻量级加固**：配置好 **Cloudflare** 的免费安全套餐即可阻挡 90% 的脚本小子。
4. **进行逆向工程研究**：配合使用 **Ghidra** 和 **Radare2**。
