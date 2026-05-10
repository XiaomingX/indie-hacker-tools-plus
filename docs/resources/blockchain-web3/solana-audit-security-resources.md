# Solana 安全审计与智能合约最佳实践 (2026 Checklist)

> [!TIP]
> **Indie Hacker Insight**: Solana 的高性能伴随着极高的安全复杂性。
> - **Rust 驱动**：不同于 Solidity，Solana 使用 Rust，开发者必须处理 Account 持有权、所有权验证与指令数据反序列化。
> - **Anchor 框架**：强烈建议使用 Anchor，它能自动生成大量安全检查代码，极大降低漏洞风险。
> - **安全重于速度**：Solana 生态中因漏洞损失的资金通常难以挽回，发布前必须经过多轮静态扫描与审计。

---

## 🛡️ 核心安全原则 (Security Principles)

- [ ] [**Solana 账户所有权验证**](https://docs.solana.com/developing/programming-model/accounts#ownership-and-assignment) - **[必修]** 理解为什么必须始终验证 `account.owner == program_id`。
- [ ] [**跨程序调用 (CPI) 安全**](https://docs.solana.com/developing/programming-model/cpi) - 确保在调用外部程序时正确签署指令并验证权限。
- [ ] [**指令数据反序列化防御**](https://github.com/solana-labs/solana-program-library) - 学习如何通过 Borsh 及其安全扩展防止恶意指令注入。
- [ ] [**PDA (程序派生地址) 的安全使用**](https://docs.solana.com/developing/programming-model/calling-between-programs#program-derived-addresses) - 理解 PDA 如何充当程序的“私钥”并防止伪造签名。

---

## 🛠️ 自动化审计工具 (Audit & Analysis Tools)

- [ ] [**Anchor Framework**](https://github.com/coral-xyz/anchor) - **[必选]** 内置大量宏用于账户验证和重入防护。
- [ ] [**Soteria**](https://github.com/soteria-dac/soteria) - 专门针对 Solana Rust 代码的静态分析工具，可发现常见的“账号注入”漏洞。
- [ ] [**Solana Program Library (SPL) Audits**](https://github.com/solana-labs/solana-program-library/tree/master/audits) - 官方库的审计报告，是学习高标准代码的最佳范本。
- [ ] [**Trident**](https://github.com/ackee-blockchain/trident) - 针对 Solana 合约的模糊测试 (Fuzzing) 框架。

---

## 📖 实战学习资源 (Learning Resources)

- [ ] [**Solana CookBook - Security Section**](https://solanacookbook.com/core-concepts/security.html) - 整理了常见的漏洞模式（如 Missing Signer, Account Reloading）。
- [ ] [**Sealevel Attacks**](https://github.com/coral-xyz/sealevel-attacks) - 展示了如何攻击不安全的 Solana 合约，并提供修复方案。
- [ ] [**Awesome-Solana-Security**](https://github.com/analysis-tools-dev/awesome-solana-security) - 动态更新的 Solana 安全资源清单。

---

## 💡 选型建议
1. **新项目启动**：强制使用 **Anchor 0.30+** 框架，避免原生 Rust 合约的繁琐验证。
2. **发布前置流程**：必须运行 **Soteria** 静态扫描，并编写覆盖 90% 以上逻辑的 **Trident** 模糊测试。
3. **资金管理**：对于涉及大额资金的项目，参考 **SPL Token** 的账户管理模式。
4. **进阶防御**：使用 **Guardians** 或多签钱包（如 **Squads**）管理合约升级权限。