# Solidity 核心开发与审计实战 (2026 Checklist)

> [!TIP]
> **Indie Hacker Insight**: 2026 年，Solidity 开发已进入“防御性编程”时代。
> - **Gas 优化**：在 L2 时代，Gas 虽然便宜但积少成多，学会使用 `immutable`, `constant` 和位运算能显著降低运营成本。
> - **安全范式**：优先使用 OpenZeppelin 提供的经过数亿美金验证的库，严禁手写复杂的权限校验逻辑。
> - **开发套件**：Foundry 已全面超越 Hardhat，利用其极速测试与 Fuzzing 能力是专业开发者的标志。

---

## 🏗️ 官方核心资源 (Official Base)

- [ ] [**Solidity 官方文档**](https://docs.soliditylang.org/en/latest/) - 权威基准，重点关注 0.8.20+ 的新特性（如自定义错误）。
- [ ] [**官方速查表 (Cheatsheet)**](https://docs.soliditylang.org/en/latest/cheatsheet.html) - 开发时必备，快速查阅关键字与原生变量。
- [ ] [**Ethereum Stack Exchange**](https://ethereum.stackexchange.com/) - 解决 99% 报错问题的社区。

---

## 🚀 开发框架与工具 (Frameworks & Tools)

- [ ] [**Foundry**](https://github.com/foundry-rs/foundry) - **[必选]** 速度极快，使用 Solidity 编写测试用例，支持模糊测试。
- [ ] [**Hardhat**](https://hardhat.org/) - 生态成熟，插件丰富，适合全栈 dApp 集成。
- [ ] [**Remix IDE**](https://remix.ethereum.org/) - 快速验证思路、部署 Demo 合约的首选。
- [ ] [**Forge Std**](https://github.com/foundry-rs/forge-std) - Foundry 开发的标准测试辅助库。

---

## 🛡️ 安全、审计与练习 (Security & Practice)

- [ ] [**Ethernaut (OpenZeppelin)**](https://github.com/OpenZeppelin/ethernaut) - **[必练]** 通过黑客挑战学习常见漏洞。
- [ ] [**Damn Vulnerable DeFi**](https://github.com/OpenZeppelin/damn-vulnerable-defi) - 进阶必练，复现真实的 DeFi 攻击案例（闪贷攻击等）。
- [ ] [**Slither**](https://github.com/crytic/slither) - **[必选]** 静态漏洞扫描工具，自动检测 30+ 种风险。
- [ ] [**OpenZeppelin Contracts**](https://github.com/OpenZeppelin/openzeppelin-contracts) - 行业标准，覆盖代币、治理、安全等所有核心组件。

---

## 📖 深度进阶资源 (Advanced Learning)

- [ ] [**Solidity By Example**](https://solidity-by-example.org/) - 最直观的代码段展示，适合快速“抄作业”。
- [ ] [**L2 开发适配指南**](https://github.com/ethereum-optimism/optimism) - 学习 L2 与 L1 在 `block.timestamp` 和 Gas 计费上的差异。
- [ ] [**Mastering Ethereum**](https://github.com/ethereumbook/ethereumbook) - 系统理解 EVM 底层原理的圣经。

---

## 💡 选型建议
1. **构建高性能 DeFi**：首选 **Foundry** 进行极致的 Fuzzing 测试。
2. **构建可升级合约**：强制使用 **OpenZeppelin Upgradeable** 库，并严格检查初始化函数。
3. **安全前置**：在提交审计前，必须通过 **Slither** 和 **Mythril** 的全量扫描。
4. **前端交互**：推荐使用 **Wagmi** + **Viem** (替代 Ethers.js)，体积更小且类型安全。
