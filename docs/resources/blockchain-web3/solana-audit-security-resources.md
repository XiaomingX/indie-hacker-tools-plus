# Solana 审计与安全资源合集（易懂版）

这份资源清单整理了 Solana 智能合约安全学习、审计方法和漏洞案例，帮你快速掌握核心信息，避开常见风险。


## 一、基础学习资料 📚
适合入门 Solana 安全，覆盖基础概念、开发规范和审计思路，部分资源虽以 ETH 为主，但核心逻辑可迁移。

- [Armani Sealevel 攻击与 Anchor 防御](https://github.com/project-serum/sealevel-attacks)  
  配套 [总结推文](https://twitter.com/pencilflip/status/1483880018858201090)（pencilflip）：核心提醒——用 Anchor 的属性、约束和类型，能大幅降低风险。
- [Armani Solana 安全开发建议](https://twitter.com/armaniferrante/status/1411589629384355840)  
  核心提醒——警惕 `UncheckedAccount` 和 `AccountInfo`，必须做好校验！
- [CMichel 如何成为智能合约审计师](https://cmichel.io/how-to-become-a-smart-contract-auditor/)  
  虽面向 ETH 从业者，但包含通用审计建议，适合新手建立思路。
- [DeFi MOOC 实用智能合约安全（视频）](https://www.youtube.com/watch?v=pJKy5HWuFK8)（samczsun）  
  核心价值——入门级安全 overview，覆盖大量攻击类型；虽以 ETH 为主，但含跨链漏洞案例，概念可迁移到 Solana。
- [Kudelski Solana 程序安全](https://research.kudelskisecurity.com/2021/09/15/solana-program-security-part1/)  
  核心内容——高屋建瓴讲解账户所有权和数据验证逻辑。
- [Neodyme 常见陷阱](https://blog.neodyme.io/posts/solana_common_pitfalls)  
  核心提醒——检查账户所有者、签名者、账户数据；警惕整数溢出/下溢；验证 `invoke_signed()`；优先用 Anchor（除非有充分理由），Anchor 会给 `#[account]` 自动分配 8 字节标识符，避免账户混淆。
- [Neodyme Solana 安全实验与答案](https://workshop.neodyme.io/)  
  配套上述“常见陷阱”博客，提供实操练习，帮你巩固知识点。
- [Neodyme 攻击者思维工作坊（视频）](https://www.youtube.com/watch?v=vbkhhgeP30I)  
  核心内容——快速讲解 PoC（漏洞验证）框架，演示如何破解“Level 0”挑战。
- [OtterSec 审计视角看 Solana](https://osec.io/blog/tutorials/2022-03-14-solana-security-intro/)  
  核心价值——从安全角度拆解 Solana 的执行和编程模型，适合零基础建立认知。
- [Sec3 整数溢出与下溢](https://www.sec3.dev/blog/understanding-arithmetic-overflow-underflows-in-rust-and-solana-smart-contracts)  
  核心提醒——别直接用 `+, -, /, *`，必须校验算术操作是否溢出/下溢！
- [Sec3 审计指南（共 4 篇）](https://www.sec3.dev/blog/how-to-audit-solana-smart-contracts-part-1-a-systematic-approach)  
  1. 系统方法：常见攻击面和审计关键问题；  
  2. 自动化工具：用工具扫描代码漏洞、不安全 Rust 语法和拼写错误（目前这类工具还需补充）；  
  3. 渗透测试：用 Neodyme 的 PoC 框架验证攻击思路；  
  4. Anchor 框架：拆解 `#[program]`、`#[derive(Accounts)]`、`#[account]` 的底层逻辑。
- [Sec3 所有者与签名者校验](https://www.sec3.dev/blog/from-ethereum-smart-contracts-to-solana-programs-two-common-security-pitfalls-and-beyond)  
  核心提醒——必须检查账户所有者和签名者！用 `#[account]` 和 `Signer<'info>` 可避免漏洞。
- [Solend 审计工作坊](https://docs.google.com/presentation/d/1jZ9kVo6hnhBsz3D2sywqpMojqLE5VTZtaXna7OHL1Uk/edit?pli=1#slide=id.ge15c343642_0_51)  
  核心内容——ETH 常见攻击如何迁移到 Solana，附审计方法论。
- [Trail of Bits DeFi 安全案例（视频）](https://www.youtube.com/watch?v=jGrtK5k0CK0)  
  虽以 ETH 为主，但 DeFi 系统安全的通用建议可复用。
- [Zellic Anchor 常见漏洞](https://www.zellic.io/blog/the-vulnerabilities-youll-write-with-anchor/)  
  核心价值——专门讲 Anchor 程序中容易出现的漏洞类型，审计 Anchor 必看。


## 二、漏洞案例分析 🪦
通过真实黑客事件，理解 Solana 智能合约的高频漏洞点和防御思路。

- [CASH 黑客事件总结](https://twitter.com/samczsun/status/1506578902331768832)（samczsun）  
  核心教训——必须建立“信任根”，确保核心逻辑的可信度。
- [CASH 漏洞拆解](https://www.sec3.dev/blog/cashioapp-attack-whats-the-vulnerability-and-how-soteria-detects-it)（Sec3）  
  核心教训——仔细检查所有输入账户，不能遗漏校验。
- [Cope Roulette 漏洞](https://github.com/Arrowana/cope-roulette-pro)（Arrowana）  
  核心特点——利用“交易回滚”实现攻击的典型案例。
- [Solana 交易模拟检测](https://opcodes.fr/en/publications/2022-01/detecting-transaction-simulation/)（Opcodes）  
  核心内容——讲解交易模拟原理和“Bank”模块作用；Sec3 有篇 [Bank 模块详解](https://www.sec3.dev/blog/solana-internals-part-4-the-bank-a-key-component) 可搭配看。
- [Jet Protocol 无限借贷漏洞](https://medium.com/@0xjayne/how-to-freely-borrow-all-the-tvl-from-the-jet-protocol-25d40e35920e)（Jayne）  
  核心漏洞——因 `break` 语句使用不当导致的逻辑漏洞，较为少见但危害极大。
- [借贷协议 rounding 漏洞](https://blog.neodyme.io/posts/lending_disclosure)（Neodyme）  
  核心教训——看似无害的“四舍五入”错误，曾导致 26 亿美元资产面临风险；不确定时优先用 `floor`（向下取整）或 `ceil`（向上取整），而非 `round`。  
  配套 [Solend 对该漏洞的回应](https://blog.solend.fi/bug-bounty-and-response-to-spl-lending-vulnerability-f4c8874342d0)。
- [Solana rBPF 整数溢出漏洞](https://blocksecteam.medium.com/new-integer-overflow-bug-discovered-in-solana-rbpf-7729717159ee)（BlockSec）  
  核心防御——用 `checked_add()`/`checked_div()` 等带校验的算术方法，或 `saturating_add()` 等溢出安全方法；可参考 Sec3 上述“整数溢出”博客。
- [多漏洞链式攻击（薛定谔的 NFT）](https://medium.com/@solens_io/schrodingers-nft-an-incinerator-spl-token-program-and-the-royal-flush-attack-58e4ce4e63dc)（Solens）  
  核心思路——将多个小漏洞组合，形成致命攻击；建议看 samczsun 的 [漏洞链式攻击讲解（视频）](https://www.youtube.com/watch?v=oA6Td5ujGrM)。
- [Candy Machine 漏洞](https://medium.com/@solens_io/smashing-the-candy-machine-for-fun-and-profit-a3bcc58d6c30)（Solens）  
  核心教训——未校验的账户会引发大问题；Anchor 要求 `UncheckedAccount` 必须加 `/// CHECK` 注释，就是为了强制开发者注意校验；修复仅需 1 行 Anchor 代码：正确使用 `#[account(zero)]`。
- [Solana 质押池语义不一致漏洞](https://www.sec3.dev/blog/solana-stake-pool-a-semantic-inconsistency-vulnerability-discovered-by-x-ray)（Sec3）  
  核心价值——演示如何用 Neodyme 的 PoC 框架验证漏洞；同时说明：即使是已审计过的代码，也可能存在漏洞。
- [Solend 恶意借贷市场事件报告](https://docs.google.com/document/d/1-WoQwT1QrPEX-r4N-fDamRQ50LM8DsdsOyq1iTabS3Q/edit#)（Rooter）  
  配套学习——结合 Kudelski 的“Solana 程序安全”博客，能更清晰理解漏洞原理。
- [SPL Token 授权撤销漏洞](https://2501babe.github.io/tools/revoken.html)（Hana）  
  核心特点——一种隐蔽的“撤销 Solana 代币授权”的方法，需警惕。
- [2 亿美元预言机操纵攻击](https://osec.io/blog/reports/2022-02-16-lp-token-oracle-manipulation/)（OtterSec）  
  核心教训——通过操控 AMM 价格影响预言机，进而攻击借贷协议；防御建议：对 LP 代币用“公允定价”，优先用 TWAP（时间加权平均价）；Drift 协议有 [预言机防护示例](https://github.com/drift-labs/protocol-v1/blob/4c2d447a677693da506e4de9596a07e4b9ba4d5d/tests/admin.ts#L212) 可参考。
- [Wormhole 黑客事件（3 篇分析）](https://twitter.com/samczsun/status/1489044939732406275)  
  1. samczsun 总结：必须校验输入账户；  
  2. Halborn 拆解：签名验证链要确保“每一步都有效”；  
  3. Kudelski 分析：需验证“未修改的参考账户”（参考 [Solana 官方文档](https://docs.solana.com/developing/programming-model/accounts#verifying-validity-of-unmodified-reference-only-accounts)）；  
  4. Entropy 事后分析：通过伪造 `SignatureSet` 输入账户实现攻击。


## 三、漏洞验证代码（PoC） 💡
可直接参考的漏洞验证示例，帮你掌握“如何证明漏洞存在”。

- [Cashio 漏洞 PoC](https://github.com/PwnedNoMore/cashio-exploit-workshop/tree/poc)（PNM）
- [Jet Governance 漏洞 PoC](https://github.com/otter-sec/jet-governance-pocs)（OtterSec）
- [Port 最大提取量漏洞 PoC](https://github.com/port-finance/variable-rate-lending/blob/master/token-lending/program/tests/max_withdraw_bug_poc.rs)（nojob）
- [SPL Token-Lending 漏洞 PoC](https://blog.neodyme.io/posts/lending_disclosure)（Neodyme）


## 四、审计报告与代码审查 🔒
整理主流 Solana 项目的公开审计报告，按“项目名-审计机构”分类，方便查阅对标。

| 项目名（Project） | 审计机构（Auditor） | 报告链接（Link） |
|--------------------|---------------------|------------------|
| Aldrin             | Kudelski            | [PDF](https://dex.aldrin.com/877f900320eec44c13409814fe473fb7.pdf) |
| Audius             | Kudelski            | [PDF](https://assets.website-files.com/6024b69839b1b755528798ea/6201872afb297b3955e303aa_Audius%20-%20Security%20Assessment%20for%20Audius%20Protocol%20v1.1.0.pdf) |
| Cashmere           | OtterSec            | [GitHub](https://github.com/cashmere-inc/multisig-audit-report/blob/main/cashmere-audit-public.pdf) |
| Cega               | OtterSec            | [GitHub](https://github.com/otter-sec/cega-vault-report) |
| Crema              | Bramah              | [PDF](https://www.bramah.systems/audits/Crema_Finance_Audit_Bramah.pdf) |
| Cropper            | Halborn             | [GitHub](https://github.com/HalbornSecurity/PublicReports/blob/master/Solana%20Program%20Audit/Cropper_Finance_AMM_Program_Security_Audit_Report_Halborn_Final.pdf) |
| Debridge           | Neodyme             | [Docs](https://docs.debridge.finance/the-core-protocol/security#has-debridge-been-audited) |
| Drift              | Zellic              | [GitHub](https://github.com/Zellic/publications/blob/master/Drift%20Protocol%20Audit%20Report.pdf) |
| Francium           | Certik              | [Certik 页面](https://www.certik.com/projects/francium) |
| Friktion           | Kudelski            | [Docs](https://docs.friktion.fi/protocol/security) |
| Genopets           | MadShield           | [Whitepaper](https://whitepaper.genopets.me/tokenomics/gene-staking/staking-program-audit) |
| GooseFx            | Halborn             | [GitHub](https://github.com/HalbornSecurity/PublicReports/blob/master/Solana%20Program%20Audit/GooseFX_Swap_Program_Security_Audit_Report_Halborn_Final.pdf) |
| Hedge              | Kudelski、OtterSec、Sec3 | [Docs](https://docs.hedge.so/protocol-overview/security) |
| Hubble             | Kudelski            | [Docs](https://docs.hubbleprotocol.io/documentation/security-audits) |
| Invariant          | Sec3                | [PDF](https://invariant.app/audit.pdf) |
| Jet Governance     | OtterSec            | [GitHub](https://github.com/jet-lab/jet-governance/blob/master/reports/jet-governance-audit-public.pdf) |
| Juiced             | OtterSec            | [PDF](https://juiced.fi/audit-report.pdf) |
| Larix              | SlowMist            | [Docs](https://docs.projectlarix.com/how-to-prove/audit) |
| Light Protocol     | HashCloak           | [GitHub](https://github.com/Lightprotocol/light-protocol-program/blob/main/Audit/Light%20Protocol%20Audit%20Report.pdf) |
| Mango              | Neodyme             | [Docs](https://docs.mango.markets/audit) |
| Maple              | Bramah              | [PDF](https://uploads-ssl.webflow.com/6247b0423c35b87bbaaf6d4c/62617902491def721f481ecb_Maple_Finance_Audit_Bramah.pdf) |
| Marinade（V1）     | Kudelski、Ackee（审计）；Neodyme（代码审查） | [Docs](https://docs.marinade.finance/marinade-protocol/security/audits)；[代码审查](https://marinade.finance/docs/Neodyme.pdf) |
| Marinade（V2）     | Neodyme、Sec3       | [GitHub](https://github.com/marinade-finance/liquid-staking-program) |
| Mean               | Sec3                | [Docs](https://docs.meanfi.com/products/safety-and-security) |
| Orca Whirlpools    | Kudelski、Neodyme   | [Docs](https://docs.orca.so/#has-orca-been-audited) |
| Parrot             | Halborn             | [PDF](https://doc.parrot.fi/Party_Parrot_Solana_Smart_Contract_Security_Audit_Report_Halborn_v1_1.pdf) |
| Phantasia          | Halborn             | [GitHub](https://github.com/HalbornSecurity/PublicReports/blob/master/Solana%20Program%20Audit/Phantasia_Sports_NFT_Store_SPA_Solana_Program_Security_Audit_Report_Halborn_Final.pdf) |
| Phoenix            | MadShield、OtterSec | [GitHub](https://github.com/Ellipsis-Labs/phoenix-v1/tree/master/audits) |
| Port Lending       | Kudelski、SlowMist  | [Immunefi](https://immunefi.com/bounty/portfinance/) |
| Port Sundial       | OtterSec            | [GitHub](https://github.com/port-finance/sundial/blob/master/audits/port-finance-sundial-audit-public.pdf) |
| Pyth               | Zellic              | [GitHub](https://github.com/Zellic/publications) |
| Quarry             | Quantstamp          | [GitHub](https://github.com/QuarryProtocol/quarry/blob/master/audit/quantstamp.pdf) |
| Saber              | Bramah              | [GitHub](https://github.com/saber-hq/stable-swap/blob/master/audit/bramah-systems.pdf) |
| Shared Memory & Token Swap | Kudelski | [PDF](https://orca-dev-12345.s3-ap-southeast-1.amazonaws.com/Kudelski-audit.pdf) |
| Soda               | Certik              | [PDF](https://certik-public-assets.s3.amazonaws.com/REP-Soda-Protocol-2021-10-26.pdf) |
| Solana 核心协议（2019） | Kudelski | [PDF](https://solana.com/solana-security-audit-2019.pdf) |
| Solana Stake Pool  | Kudelski、Neodyme、Quantstamp | [Kudelski](https://solana.com/SolanaKudelskiStakePoolAudit.pdf)；[Neodyme](https://solana.com/SolanaNeodymeStakePoolAudit.pdf)；[Quantstamp](https://solana.com/SolanaQuantstampStakePoolAudit.pdf) |
| Solend             | Kudelski            | [Docs](https://docs.solend.fi/protocol/audit) |
| Solido             | Bramah、Neodyme     | [GitHub](https://github.com/ChorusOne/solido/tree/163b26aee08958fbdc0f3909ccb6ef606a1ea0f2/audit) |
| Solvent            | OtterSec            | [Google Drive](https://drive.google.com/file/d/1tVe-0EQhslQxr56nOQmxqaB8BSDwJ1s1/view) |
| Squads             | OtterSec            | [GitHub](https://github.com/Squads-Protocol/squads-mpl/blob/main/Squads%20V3%20-%20OtterSec%20Audit.pdf) |
| Streamflow         | Opcodes             | [GitHub](https://github.com/streamflow-finance/rust-sdk/blob/main/protocol_audit.pdf) |
| Swim               | Kudelski            | [PDF](https://swim.io/audits/kudelski.pdf) |
| Synthetify         | Kudelski            | [PDF](https://synthetify.io/resources/audit.pdf) |
| UXD                | Sec3                | [Docs](https://docs.uxd.fi/uxdprotocol/resources/audits) |
| Wormhole           | Neodyme             | [GitHub](https://github.com/certusone/wormhole/blob/dev.v2/audits/2021-01-10_neodyme.pdf) |


## 五、安全工具 🔧
按“工具名-功能”整理，覆盖模糊测试、漏洞扫描、代码校验等场景，直接复制链接即可使用。

- [Ackee Trident](https://github.com/Ackee-Blockchain/trident)：Solana 模糊测试框架，帮你自动生成测试用例，发现潜在漏洞。
- [Anchor Test UI](https://github.com/0xPratik/anchor-UI)：可视化 Anchor 测试工具，降低手动测试门槛。
- [APR（Anchor Program Registry）](https://www.apr.dev/)：Anchor 程序注册表，可查公开的 Anchor 项目和代码。
- [Blockworks Checked Math](https://github.com/blockworks-foundation/checked-math)：算术校验宏，简化“溢出/下溢”校验代码。
- [cargo-audit](https://docs.rs/cargo-audit/latest/cargo_audit)：检查 Cargo.lock 文件，识别依赖库中的已知漏洞。
- [cargo-geiger](https://crates.io/crates/cargo-geiger)：检测代码中“不安全的 Rust 语法（unsafe）”，降低潜在风险。
- [Kudelski Semgrep](https://twitter.com/cryptographadam/status/1425163382982811650?s=20&t=5rNeZ11MMw0N1e-_SmU5Tw)：静态分析工具，用规则匹配检测代码漏洞。
- [Neodyme Solana PoC Framework](https://github.com/neodyme-labs/solana-poc-framework)：Solana 渗透测试框架，用于编写漏洞验证代码。
- [OtterSec Solana CTF Framework](https://github.com/otter-sec/sol-ctf-framework)：CTF 竞赛专用框架，适合练习漏洞挖掘思路。
- [Saber Vipers](https://github.com/saber-hq/vipers)：封装好的校验工具，简化账户、权限等常见校验逻辑。
- [Sec3 Auto Auditor](https://twitter.com/aeyakovenko/status/1529138221094883333)：自动化漏洞扫描工具，快速排查基础漏洞。
- [L3X](https://github.com/VulnPlanet/l3x)：AI 驱动的智能合约静态分析工具，辅助发现漏洞。
- [Rug Checker Solana](https://rugcheckersolana.com/)：Solana 项目“跑路风险”检测工具，帮普通用户规避诈骗项目。


## 六、漏洞赏金计划 🏆
整理高额赏金项目，按“项目名-最高赏金”分类，适合安全研究者参与。

- Drift：最高 50 万美元 → [链接](https://immunefi.com/bounty/driftprotocol/)
- Friktion：最高 10 万美元 → [链接](https://docs.friktion.fi/protocol/security)
- Hubble：最高 50 万美元 → [链接](https://github.com/hubbleprotocol/audits/blob/master/docs/SECURITY.md)
- Jet：最高 7.5 万美元 → [链接](https://immunefi.com/bounty/jetprotocol/)
- Larix：最高 15 万美元 → [链接](https://docs.projectlarix.com/how-to-prove/bug-bounty-reward)
- Lido（Solana 版）：最高 200 万美元 → [链接](https://immunefi.com/bounty/lidoforsolana/)
- Mango：最高 100 万美元 → [链接](https://docs.mango.markets/mango/bug-bounty)
- Marinade：最高 25 万美元 → [链接](https://immunefi.com/bounty/marinade/)
- Metaplex：最高 20 万美元 → [链接](https://www.metaplex.com/bounty-program)
- Orca：最高 50 万美元 → [链接](https://immunefi.com/bounty/orca/)
- Port：最高 50 万美元 → [链接](https://immunefi.com/bounty/portfinance/)
- Phoenix：最高 10 万美元 → [链接](https://github.com/Ellipsis-Labs/phoenix-v1/security)
- Saber：最高 100 万美元 → [链接](https://blog.saber.so/the-cashio-vulnerability-against-saber-and-our-users-what-happened-and-what-we-are-doing-about-it-d0ee188e8346)
- Serum：最高 100 万美元 → [链接](https://forum.projectserum.com/t/formalizing-a-bug-bounty-program/410)
- Solana Labs：最高 200 万美元 → [链接](https://github.com/solana-labs/solana/security/policy)
- Solend：最高 100 万美元 → [链接](https://docs.solend.fi/protocol/bug-bounty)
- Solvent：最高 25 万美元 → [链接](https://solvent-protocol.gitbook.io/solvent-protocol/developers/bug-bounty)
- Swim：最高 10 万美元 → [链接](https://immunefi.com/bounty/swimprotocol/)
- Synthetify：最高 10 万美元 → [链接](https://synthetify.io/blog/bug-bounty)
- UXD：最高 250 万美元 → [链接](https://docs.uxd.fi/uxdprotocol/resources/bug-bounty)
- Wormhole：最高 250 万美元 → [链接](https://immunefi.com/bounty/wormhole/)


## 七、待解问题 ？
行业内尚未形成共识的问题，适合深入讨论和研究。

- 漏洞赏金的“合理奖励标准”是什么？→ [讨论链接](https://twitter.com/wireless_anon/status/1501025792565915657)
- 项目何时需要进行审计？→ [讨论 1](https://twitter.com/ChenWainuo/status/1499871348696379393)；[“未审计上主网”的讨论](https://twitter.com/cronos_so/status/1500131620606681088)
- 谁会为 Anchor 框架本身的漏洞支付赏金？→ [讨论链接](https://twitter.com/armaniferrante/status/1506691213394694152)


## 八、贡献与许可 🤝
- **贡献方式**：欢迎提交 Pull Request 补充资源；重大修改建议先开 Issue 讨论。
- **许可协议**：可自由使用所有材料，但建议作为“白帽黑客”（保护生态）使用，而非攻击他人项目。


要不要我帮你整理一份 **可打印的 PDF 版资源清单**？会按模块标注核心提醒和链接，方便你离线查阅或分享给团队。