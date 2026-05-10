# Red Teaming Toolkit (2026 Checklist)

> [!IMPORTANT]
> **法律合规提示**：本仓库包含的工具仅用于合规的安全研究、漏洞模拟及防御验证。严禁将以下工具用于任何非法活动。

---

## 🔍 侦察与情报搜集 (Reconnaissance)

- [ ] [**RustScan**](https://github.com/RustScan/RustScan) - 现代端口扫描器，极速发现开放端口。
- [ ] [**Amass**](https://github.com/OWASP/Amass) - 深度攻击面映射与资产发现。
- [ ] [**Gitleaks**](https://github.com/zricethezav/gitleaks) - 扫描代码库中的密钥、令牌和敏感信息。
- [ ] [**BBOT**](https://github.com/blacklanternsecurity/bbot) - 递归式互联网扫描框架，适合大规模 OSINT。
- [ ] [**Cloud Enum**](https://github.com/initstring/cloud_enum) - 多云环境资源探测工具 (AWS, Azure, GCP)。
- [ ] [**SpiderFoot**](https://github.com/smicallef/spiderfoot) - 自动化的 OSINT 集成平台。

---

## 🚪 初始访问与载荷 (Initial Access & Payload)

- [ ] [**Evilginx2**](https://github.com/kgretzky/evilginx2) - 针对多因子认证 (MFA) 的高级钓鱼框架。
- [ ] [**Gophish**](https://github.com/gophish/gophish) - 企业级钓鱼模拟平台。
- [ ] [**Donut**](https://github.com/TheWover/donut) - 将 VBScript, JScript, EXE, DLL 转化为位置无关代码 (PIC)。
- [ ] [**ScareCrow**](https://github.com/optiv/ScareCrow) - 针对 EDR 绕过的载荷生成框架。
- [ ] [**Inceptor**](https://github.com/klezVirus/inceptor) - 模板驱动的 AV/EDR 规避框架。

---

## 📡 指挥与控制 (Command & Control)

- [ ] [**Sliver**](https://github.com/BishopFox/sliver) - 通用跨平台植入框架，支持 mTLS, WireGuard, HTTP(S) 和 DNS。
- [ ] [**Havoc**](https://github.com/HavocFramework/Havoc) - 现代、灵活且极具扩展性的 C2 框架。
- [ ] [**Empire**](https://github.com/BC-SECURITY/Empire) - 经典的 PowerShell/Python 后渗透框架。
- [ ] [**Mythic**](https://github.com/its-a-feature/Mythic) - 基于 Docker 的协作式 C2 平台，支持多种 Agent 开发。
- [ ] [**Cobalt Strike**](https://cobaltstrike.com/) - 行业标准的商业化红队模拟软件。

---

## 🛡️ 防御规避与提权 (Defense Evasion & Privesc)

- [ ] [**EDRSilencer**](https://github.com/netero1010/EDRSilencer) - 利用 WFP 阻止 EDR 向服务器报告安全事件。
- [ ] [**PEASS-ng**](https://github.com/carlospolop/PEASS-ng) - 经典的权限提升自动化脚本 (Win/Linux)。
- [ ] [**Mimikatz**](https://github.com/gentilkiwi/mimikatz) - 核心凭据提取工具（注意：在 2026 年通常需要配合复杂的混淆/加载技术）。
- [ ] [**Rubeus**](https://github.com/GhostPack/Rubeus) - Kerberos 协议交互与攻击工具。
- [ ] [**BloodHound**](https://github.com/BloodHoundAD/BloodHound) - 域环境攻击路径可视化分析。

---

## ☁️ 云环境安全 (Cloud Security)

- [ ] [**Pacu**](https://github.com/RhinoSecurityLabs/pacu) - AWS 漏洞利用与模拟框架。
- [ ] [**Roadtools**](https://github.com/dirkjanm/ROADtools) - Azure AD 勘探与分析框架。
- [ ] [**Stratus Red Team**](https://github.com/DataDog/stratus-red-team) - 云原生环境的“原子红队”测试工具。

---

## 💡 红队实战策略
1. **优先使用云原生工具**：在 2026 年，利用合法云服务的（如 Azure Function, Cloudflare Workers）作为重定向器比自建基础设施更难被封禁。
2. **注重全模态隐藏**：不仅要绕过文件特征扫描，更要关注行为检测（Behavioral AI）和内存扫描。
3. **自动化重构**：定期使用 **Mangle** 或 **ProtectMyTooling** 对常用工具进行重签名和代码混淆。
