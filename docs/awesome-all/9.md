# Awesome-Security：开源安全工具与资源精选指南
> 一份为**安全从业者、开发者、运维工程师及学习者**整理的开源安全资源清单，涵盖网络安全、终端防护、威胁情报、Web安全等核心领域。清单精选活跃维护的工具，补充实用场景说明，帮你快速选型、系统学习，或提升攻防实战能力。


## 一、网络安全（Network Security）
网络安全是防御与测试的核心，涵盖扫描探测、监控审计、边界防护等方向。以下工具均优先选择**社区活跃、文档完善**的项目。

### 1. 网络架构与规划
| 工具/资源名称                | 核心用途                          | 特点/技术栈                          | 官方链接                                  |
|-----------------------------|-----------------------------------|---------------------------------------|-------------------------------------------|
| Network Segmentation Cheat Sheet | 企业网络分段最佳实践指南          | 覆盖中小型到大型企业场景，含拓扑示例  | https://github.com/sergiomarotco/Network-segmentation-cheat-sheet |
| Zero Trust Cheat Sheet      | 零信任架构设计与落地参考          | 基于NIST标准，含身份认证、权限控制要点 | https://github.com/OWASP/CheatSheetSeries/blob/master/cheatsheets/Zero_Trust_Cheat_Sheet.md |


### 2. 扫描与渗透测试（Scanning / Pentesting）
用于发现网络、设备或应用的漏洞，是渗透测试的核心工具集。
| 工具名称                | 核心用途                          | 特点/技术栈                          | 官方链接                                  |
|-------------------------|-----------------------------------|---------------------------------------|-------------------------------------------|
| Greenbone GVM（原OpenVAS） | 全功能漏洞扫描与管理              | 含30000+漏洞检测规则，支持定期扫描调度 | https://www.greenbone.net/en/gvm/         |
| Metasploit Framework     | 漏洞利用开发与攻击模拟            | 支持10000+ exploit模块，跨平台兼容    | https://github.com/rapid7/metasploit-framework |
| Kali Linux               | 渗透测试专用操作系统              | 预装600+安全工具（nmap、Wireshark等）  | https://www.kali.org/                     |
| Nmap                     | 网络发现与端口扫描                | 支持OS识别、服务版本探测，轻量高效    | https://nmap.org/                         |
| RustScan                 | 高速端口扫描（Nmap替代工具）      | Rust编写，17分钟Nmap扫描缩短至19秒    | https://github.com/RustScan/RustScan      |
| Amass                    | DNS子域名枚举                     | 整合多数据源（搜索引擎、DNS服务器），支持暴力破解 | https://github.com/OWASP/Amass |
| Prowler                  | AWS云环境安全评估                | 基于CIS基准，自动检测权限泄露、配置漏洞 | https://github.com/prowler-cloud/prowler  |
| Grype                    | 容器/镜像漏洞扫描                | 支持OCI镜像、文件系统，集成CI/CD       | https://github.com/anchore/grype          |


### 3. 监控与日志审计（Monitoring / Logging）
实时追踪网络行为、日志分析，及时发现异常（如入侵、数据泄露）。
| 工具名称                | 核心用途                          | 特点/技术栈                          | 官方链接                                  |
|-------------------------|-----------------------------------|---------------------------------------|-------------------------------------------|
| Wazuh                    | 跨平台威胁检测与日志分析          | 支持文件完整性监控、入侵检测，集成ELK  | https://github.com/wazuh/wazuh            |
| Falco                    | 云原生运行时安全监控              | CNCF毕业项目，检测容器异常行为（如权限提升） | https://falco.org/ |
| Matano                   | 服务器less安全数据湖              | 基于Apache Iceberg，支持PB级日志存储与实时检测 | https://github.com/matanolabs/matano |
| OpenSnitch               | Linux应用防火墙（类Little Snitch） | 监控进程网络连接，支持自定义拦截规则   | https://github.com/evilsocket/opensnitch  |
| GitGuardian              | 代码仓库秘钥泄露扫描              | 支持GitLab/GitHub，实时检测API密钥、密码 | https://github.com/GitGuardian/ggshield   |


### 4. 入侵检测/防御（IDS/IPS）
识别并阻断恶意网络流量，分为网络层（NIDS/NIPS）和主机层（HIDS/HIPS）。
| 工具名称                | 核心用途                          | 特点/技术栈                          | 官方链接                                  |
|-------------------------|-----------------------------------|---------------------------------------|-------------------------------------------|
| Snort 3                  | 开源网络入侵检测/防御系统         | 支持规则自定义，处理速度达10Gbps       | https://www.snort.org/                    |
| Suricata                 | 高性能NIDS/IPS（替代Snort）       | 多线程架构，支持HTTP/2、TLS 1.3检测    | https://suricata-ids.org/                 |
| CrowdSec                 | 协同式行为检测引擎                | Go编写（比Fail2Ban快60倍），支持IP信誉共享 | https://github.com/crowdsecurity/crowdsec |
| Security Onion           | 集成化NSM（网络安全监控）平台     | 预装Snort、Suricata、Zeek，适合企业部署 | https://securityonion.net/                |


### 5. 蜜罐与欺骗防御（Honeypot / Honey Net）
模拟脆弱系统诱捕攻击者，收集攻击数据（如恶意样本、攻击手法）。
| 工具名称                | 核心用途                          | 特点/技术栈                          | 官方链接                                  |
|-------------------------|-----------------------------------|---------------------------------------|-------------------------------------------|
| T-Pot Honeypot Distro    | 多容器蜜罐平台                    | 支持10+蜜罐类型（SSH、HTTP、ICS等），Docker化部署 | https://github.com/telekom-security/tpotce |
| Conpot                   | ICS/SCADA工业控制系统蜜罐         | 模拟PLC、SCADA协议，支持自定义HMI界面  | http://conpot.org/                        |
| Glastopf                 | Web应用蜜罐（模拟漏洞）           | 支持数千种Web漏洞模拟，收集攻击Payload | http://glastopf.org/                      |
| Cuckoo Sandbox           | 恶意样本动态分析蜜罐              | 自动运行样本并记录行为（文件操作、网络连接） | http://www.cuckoosandbox.org/             |


### 6. 全流量捕获与取证（Full Packet Capture / Forensic）
捕获网络流量并分析，用于事后溯源或攻击还原。
| 工具名称                | 核心用途                          | 特点/技术栈                          | 官方链接                                  |
|-------------------------|-----------------------------------|---------------------------------------|-------------------------------------------|
| Wireshark                | 图形化网络抓包与分析              | 支持1000+协议，含流量过滤、统计功能    | https://www.wireshark.org/                |
| tcpflow                  | 按TCP流拆分数据包并存储            | 每个连接生成独立文件，便于协议分析      | https://github.com/simsong/tcpflow        |
| Moloch                   | 大规模PCAP存储与检索              | 支持TB级流量索引，Web界面快速查询      | https://github.com/aol/moloch             |
| Xplico                   | 网络流量数据提取（NFAT工具）       | 提取邮件、HTTP内容、VoIP通话等应用数据  | http://www.xplico.org/                    |


### 7. 安全信息与事件管理（SIEM）
整合多源日志，通过关联分析识别安全事件（如暴力破解、数据泄露）。
| 工具名称                | 核心用途                          | 特点/技术栈                          | 官方链接                                  |
|-------------------------|-----------------------------------|---------------------------------------|-------------------------------------------|
| Wazuh SIEM               | 开源SIEM平台（含日志分析+可视化）  | 集成OpenSearch，支持自定义检测规则     | https://github.com/wazuh/wazuh            |
| Elastic Stack（ELK）     | 日志收集、分析与可视化            | 需自行配置安全规则，适合技术团队定制    | https://www.elastic.co/cn/what-is/elk-stack |
| Prelude SIEM             | 跨平台日志归一化与关联分析        | 支持100+日志源，无需代理（agentless）  | https://www.prelude-siem.org/             |


### 8. VPN与边界防护
保障远程访问或跨网络通信的安全性。
| 工具名称                | 核心用途                          | 特点/技术栈                          | 官方链接                                  |
|-------------------------|-----------------------------------|---------------------------------------|-------------------------------------------|
| WireGuard                | 轻量高速VPN协议/工具              | 比OpenVPN快3倍，加密更简洁（仅3000行代码） | https://www.wireguard.com/                |
| Firezone                 | 基于WireGuard的企业VPN服务器       | 支持单点登录（SSO），Web界面管理客户端  | https://github.com/firezone/firezone      |
| OpenVPN                  | 成熟的SSL/TLS VPN解决方案          | 支持路由/桥接模式，跨平台兼容性强      | https://openvpn.net/                      |


### 9. 防火墙（Firewall）
控制网络流量进出，是网络边界的第一道防线。
| 工具名称                | 核心用途                          | 特点/技术栈                          | 官方链接                                  |
|-------------------------|-----------------------------------|---------------------------------------|-------------------------------------------|
| pfSense                  | 企业级防火墙/路由器系统            | 基于FreeBSD，支持VPN、负载均衡、入侵检测 | https://www.pfsense.org/                  |
| OPNsense                 | 开源防火墙（pfSense分支）         | 更易用的Web界面，含应用层过滤功能      | https://opnsense.org/                     |
| nftables                 | Linux内核防火墙（替代iptables）    | 语法更简洁，支持批量规则管理            | https://netfilter.org/projects/nftables/  |


## 二、终端安全（Endpoint Security）
保护服务器、工作站等终端设备，涵盖恶意软件检测、配置加固、身份认证等。

### 1. 反病毒/反恶意软件
| 工具名称                | 核心用途                          | 特点/技术栈                          | 官方链接                                  |
|-------------------------|-----------------------------------|---------------------------------------|-------------------------------------------|
| ClamAV                   | 跨平台开源杀毒引擎                | 支持病毒库更新，集成邮件/文件扫描      | https://www.clamav.net/                   |
| Linux Malware Detect（LMD） | Linux服务器恶意软件扫描            | 针对共享主机场景，支持MD5哈希检测      | https://www.rfxn.com/projects/linux-malware-detect/ |
| Loki                     | IOC（入侵指示器）扫描工具          | 支持YARA规则、文件哈希，适合应急响应    | https://github.com/Neo23x0/Loki           |
| rkhunter                 | Linux rootkit检测工具              | 检查系统文件完整性、隐藏进程与端口      | http://rkhunter.sourceforge.net/          |


### 2. 配置管理与加固
确保终端配置符合安全基准，避免人为失误导致的漏洞。
| 工具名称                | 核心用途                          | 特点/技术栈                          | 官方链接                                  |
|-------------------------|-----------------------------------|---------------------------------------|-------------------------------------------|
| Fleet                   | 跨平台终端管理平台                | 支持macOS/Windows/Linux，收集硬件/软件信息 | https://github.com/fleetdm/fleet |
| Ansible OS Hardening     | 自动化操作系统加固                | 基于CIS基准，支持Linux/Windows         | https://github.com/dev-sec/ansible-os-hardening |
| Rudder                   | IT基础设施自动化与合规检查        | 支持配置漂移检测，自动修复异常配置      | http://www.rudder-project.org/            |


### 3. 身份认证与访问控制
防止未授权访问终端或服务。
| 工具名称                | 核心用途                          | 特点/技术栈                          | 官方链接                                  |
|-------------------------|-----------------------------------|---------------------------------------|-------------------------------------------|
| Google Authenticator    | 双因素认证（2FA）工具             | 支持TOTP/HOTP协议，集成SSH/PAM         | https://github.com/google/google-authenticator |
| Keycloak                | 开源身份管理系统                  | 支持OAuth 2.0/OpenID Connect，单点登录 | https://www.keycloak.org/                 |
| WebAuthn                | 无密码认证工具（替代密码登录）    | 基于公钥加密，支持硬件密钥（如YubiKey） | https://webauthn.io/                      |


### 4. 移动设备安全（Mobile / Android / iOS）
针对移动应用的逆向、漏洞检测与防护。
| 工具名称                | 核心用途                          | 特点/技术栈                          | 官方链接                                  |
|-------------------------|-----------------------------------|---------------------------------------|-------------------------------------------|
| MobSF（Mobile Security Framework） | 移动应用自动化安全测试            | 支持静态/动态分析，覆盖Android/iOS     | https://github.com/MobSF/Mobile-Security-Framework |
| jadx                    | Android APK反编译工具             | 生成可读Java代码，支持GUI/CLI          | https://github.com/skylot/jadx            |
| frida                   | 移动应用动态 instrumentation       | 注入JavaScript代码监控进程行为，适合逆向 | https://github.com/frida/frida            |
| OWASP MSTG              | 移动应用安全测试指南              | 含100+测试用例，覆盖隐私、认证等维度    | https://github.com/OWASP/owasp-mstg        |


### 5. 数字取证（Forensics）
终端被入侵后的证据收集与分析。
| 工具名称                | 核心用途                          | 特点/技术栈                          | 官方链接                                  |
|-------------------------|-----------------------------------|---------------------------------------|-------------------------------------------|
| Volatility 3            | 内存取证分析框架                  | 支持Windows/Linux/macOS，提取进程、密码 | https://github.com/volatilityfoundation/volatility |
| Autopsy                 | 开源数字取证平台                  | 支持磁盘镜像分析、文件恢复，GUI界面友好 | https://www.autopsy.com/                  |
| GRR Rapid Response      | 远程实时取证工具                  | 谷歌开发，支持批量终端证据收集          | https://github.com/google/grr             |


## 三、威胁情报（Threat Intelligence）
收集、分析恶意IP/域名/样本等数据，提前防御威胁。
| 工具名称/资源            | 核心用途                          | 特点/技术栈                          | 官方链接                                  |
|-------------------------|-----------------------------------|---------------------------------------|-------------------------------------------|
| MISP（Malware Information Sharing Platform） | 威胁情报共享平台                | 支持STIX/TAXII标准，集成100+情报源     | https://www.misp-project.org/             |
| IntelMQ                 | 威胁情报自动化处理框架            | 收集→解析→富集→输出，适合CERT团队      | https://github.com/certtools/intelmq       |
| abuse.ch                | 恶意软件C2服务器追踪              | 提供ZeuS、Emotet等家族的IP/域名黑名单  | https://www.abuse.ch/                     |
| PhishTank               | 钓鱼网站数据库                    | 支持API查询，实时更新钓鱼URL           | http://www.phishtank.com/                 |
| MITRE ATT&CK Framework  | 攻击战术与技术知识库              | 覆盖APT攻击全流程，用于威胁建模        | https://attack.mitre.org/                 |


## 四、Web安全（Web Security）
针对Web应用的漏洞检测、防护与开发安全。

### 1. Web应用防火墙（WAF）
阻断SQL注入、XSS等Web攻击。
| 工具名称                | 核心用途                          | 特点/技术栈                          | 官方链接                                  |
|-------------------------|-----------------------------------|---------------------------------------|-------------------------------------------|
| ModSecurity + Coraza    | 开源WAF引擎（Apache/Nginx模块）   | 支持OWASP CRS规则集，自定义拦截逻辑    | https://coraza.io/                        |
| BunkerWeb               | 容器化WAF（含自动HTTPS）          | 集成ModSecurity，支持Docker/K8s部署    | https://github.com/bunkerity/bunkerweb    |
| NAXSI                   | Nginx轻量WAF                      | 低规则维护成本，专注XSS/SQL注入防护    | https://github.com/nbs-system/naxsi       |


### 2. Web扫描与渗透测试
发现Web应用漏洞（如注入、权限绕过）。
| 工具名称                | 核心用途                          | 特点/技术栈                          | 官方链接                                  |
|-------------------------|-----------------------------------|---------------------------------------|-------------------------------------------|
| OWASP ZAP（Zed Attack Proxy） | 入门级Web漏洞扫描器              | GUI界面友好，支持自动化扫描与手动测试  | https://www.zaproxy.org/                  |
| sqlmap                  | SQL注入自动化检测与利用           | 支持30+数据库，自动识别注入点          | http://sqlmap.org/                        |
| Nuclei                  | 基于模板的漏洞扫描框架            | 含10000+漏洞模板，支持HTTP/HTTPS/SSH   | https://github.com/projectdiscovery/nuclei |
| Burp Suite Community Edition | 专业Web渗透测试工具（免费版）    | 支持代理、爬虫、爆破，适合进阶学习      | https://portswigger.net/burp/communityedition |


### 3. 运行时应用自我保护（RASP）
在应用运行中实时阻断攻击（无需修改代码）。
| 工具名称                | 核心用途                          | 特点/技术栈                          | 官方链接                                  |
|-------------------------|-----------------------------------|---------------------------------------|-------------------------------------------|
| OpenRASP                | 百度开源RASP解决方案              | 支持Java/PHP/Python，误报率低          | https://github.com/baidu/openrasp         |
| open-appsec             | 机器学习驱动的RASP                | 自动识别零日攻击，支持云原生部署        | https://github.com/openappsec/openappsec  |


### 4. 开发安全（DevSecOps）
将安全融入开发流程，避免上线后漏洞。
| 工具名称                | 核心用途                          | 特点/技术栈                          | 官方链接                                  |
|-------------------------|-----------------------------------|---------------------------------------|-------------------------------------------|
| OWASP Dependency-Check  | 第三方依赖漏洞扫描                | 支持Maven/Gradle/npm，集成CI/CD        | https://github.com/jeremylong/Dependency-Check |
| Semgrep                 | 静态代码分析（SAST）              | 规则易写，支持10+语言，速度快          | https://semgrep.dev/                      |
| Trivy                   | 容器/代码/配置漏洞扫描            | 支持Docker镜像、Terraform、K8s配置     | https://github.com/aquasecurity/trivy     |
| Sigstore                | 软件供应链安全（签名/验证）       | 自动为构建产物签名，防止篡改            | https://www.sigstore.dev/                 |


## 五、容器与云安全
针对Docker、K8s等云原生环境的安全工具。
| 工具名称                | 核心用途                          | 特点/技术栈                          | 官方链接                                  |
|-------------------------|-----------------------------------|---------------------------------------|-------------------------------------------|
| Trivy                   | 容器镜像漏洞扫描                  | 支持OCI镜像，集成Docker/K8s            | https://github.com/aquasecurity/trivy     |
| Falco                   | K8s运行时安全监控                | 检测容器权限提升、敏感文件访问          | https://falco.org/                        |
| Docker Bench for Security | Docker配置安全检查                | 基于CIS基准，自动检测20+配置风险        | https://github.com/docker/docker-bench-security |
| Prowler                  | AWS云安全评估工具                | 检测S3权限泄露、IAM配置错误等          | https://github.com/prowler-cloud/prowler  |


## 六、秘钥与数据安全（Datastores Security）
保护敏感数据（密码、API密钥）的存储与传输。
| 工具名称                | 核心用途                          | 特点/技术栈                          | 官方链接                                  |
|-------------------------|-----------------------------------|---------------------------------------|-------------------------------------------|
| HashiCorp Vault         | 秘钥管理系统                      | 支持动态秘钥生成，加密存储敏感数据      | https://www.vaultproject.io/              |
| Sops                    | 配置文件加密工具                  | 支持YAML/JSON，集成AWS KMS/PGP         | https://github.com/mozilla/sops           |
| Passbolt                | 团队密码管理器                    | 基于OpenPGP加密，支持Web界面管理        | https://www.passbolt.com/                 |
| Vaultwarden             | Bitwarden开源服务器端             | 轻量部署，支持个人/团队密码同步        | https://github.com/dani-garcia/vaultwarden |


## 七、实用资源补充

### 1. 开源渗透测试Docker镜像
| 工具名称                | Docker镜像                        | 核心用途                          |
|-------------------------|-----------------------------------|-----------------------------------|
| Kali Linux              | `kalilinux/kali-rolling`          | 全功能渗透测试环境                |
| OWASP ZAP               | `owasp/zap2docker-stable`         | Web漏洞扫描                       |
| WPScan                  | `wpscanteam/wpscan`               | WordPress漏洞扫描                 |
| OWASP Juice Shop         | `bkimminich/juice-shop`           | 故意脆弱的Web应用（学习测试用）    |


### 2. 推荐书籍（经典+最新）
- **入门必读**：《Web Application Hacker's Handbook》（Web渗透测试圣经）
- **实战指南**：《Practical Malware Analysis》（恶意软件分析实战）
- **云安全**：《Cloud Security and Privacy》（云安全与隐私保护）
- **DevSecOps**：《Securing DevOps》（DevOps安全最佳实践）
- **免费资源**：《Holistic Info-Sec for Web Developers》（Web开发者安全指南，可免费下载）


### 3. 其他精选Awesome列表
- [Awesome DevSecOps](https://github.com/devsecops/awesome-devsecops)：DevSecOps工具与实践清单
- [Awesome Cloud Security](https://github.com/4nth0ny/awesome-cloud-security)：云安全资源汇总
- [Awesome Threat Detection](https://github.com/0x4D31/awesome-threat-detection)：威胁检测与狩猎工具
- [Awesome Container Security](https://github.com/kai5263499/container-security-awesome)：容器安全工具集
