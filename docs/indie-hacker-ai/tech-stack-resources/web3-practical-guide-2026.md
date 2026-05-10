# Web3 实战开发资源 (2026 Checklist)

> [!TIP]
> **Indie Hacker Insight**: 2026 年的 Web3 重点在于 **Account Abstraction (账户抽象)** 和 **DePIN (去中心化物理基础设施)**。
> - **用户体验**：利用 **ERC-4337** 实现社交登录（Social Login）和无 gas 交易，这是 DApp 走向主流的唯一路径。
> - **实战建议**：不要纠结 Layer 1，直接在 **Base** 或 **Arbitrum** 等 Layer 2 上构建，成本更低、速度更快。

---

## 🏗️ 核心开发框架与环境 (Development)

- [ ] [**Foundry**](https://book.getfoundry.sh/) - 2026 年最推荐的合约开发框架，基于 Rust，速度极快，支持 Solidity 写测试。
- [ ] [**Hardhat**](https://hardhat.org/) - 经典的 JS/TS 开发框架，插件生态极其丰富。
- [ ] [**Remix IDE**](https://remix.ethereum.org/) - 浏览器端的合约开发神器，适合快速原型验证。
- [ ] [**OpenZeppelin**](https://www.openzeppelin.com/contracts) - 行业标准的合约零件库（ERC20, ERC721, ERC1155），安全性基石。
- [ ] [**Viem**](https://viem.sh/) - 极其轻量且类型安全的以太坊底层交互库，ethers.js 的现代替代者。

---

## 钱包与用户接入 (Wallets & Auth)

- [ ] [**Privy**](https://www.privy.io/) - 2026 年最流行的入门工具，支持邮箱/手机登录并自动创建嵌入式钱包。
- [ ] [**Dynamic**](https://www.dynamic.xyz/) - 强大的多链认证方案，完美适配账户抽象（AA）场景。
- [ ] [**RainbowKit**](https://www.rainbowkit.com/) - 最美观的钱包连接组件，适配所有主流前端框架。
- [ ] [**WalletConnect**](https://walletconnect.com/) - 钱包与应用连接的行业标准协议。

---

## 🗄️ 基础设施与数据 (Infrastructure)

- [ ] [**The Graph**](https://thegraph.com/) - 区块链数据的“搜索引擎”，通过 GraphQL 快速查询链上历史。
- [ ] [**Alchemy / Infura**](https://www.alchemy.com/) - 顶级节点服务商，支持多链 API 与账户抽象打包服务（Bundler）。
- [ ] [**IPFS / Arweave**](https://www.arweave.org/) - 去中心化存储方案，NFT 图片与 DApp 前端的避风港。
- [ ] [**Pyth Network**](https://pyth.network/) - 2026 年最推荐的预言机，提供极低延迟的实时金融数据。

---

## 📚 实战学习与课程 (Learning)

- [x] **Speed Run Ethereum**: 手把手教你构建 NFT、DeFi 等实战项目。
- [x] **CryptoZombies**: 通过僵尸游戏学习 Solidity 语法的经典入门。
- [x] **Alchemy University**: 免费且系统的 Web3 开发者培训课程。

---

## 💡 选型建议
1. **构建面向大众的 DApp**：必须使用 **Privy** + **Base** + **ERC-4337**。
2. **追求极速合约迭代**：选 **Foundry**。
3. **需要展示海量链上数据**：必须集成 **The Graph**。
4. **DePIN 项目开发**：关注 **Solana** 生态工具链，其高吞吐量更适配物理硬件。
