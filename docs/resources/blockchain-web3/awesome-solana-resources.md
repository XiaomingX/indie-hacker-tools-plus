# Solana 开发者与生态资源 (2026 Checklist)

> [!TIP]
> **Indie Hacker Insight**: 2026 年，Solana 凭借其 **"Firedancer"** 升级和极致的低延迟，已成为去中心化支付与 AI 推理代币化的首选链。
> - **性能巅峰**：通过状态压缩 (State Compression) 技术，铸造数百万个 NFT 的成本仅需数美元。
> - **开发选型**：无脑选择 **Anchor 框架**，它是 Solana 上的 "Ruby on Rails"，能帮你规避 90% 的底层 Rust 陷阱。

---

## 🛠️ 开发者核心工具 (Developer Stack)

- [ ] [**Anchor Framework**](https://github.com/coral-xyz/anchor) - Solana 智能合约开发的事实标准，提供强类型检查与自动生成的 IDL。
- [ ] [**Solana Playground (IDE)**](https://beta.solpg.io/) - 浏览器端的合约开发环境，无需配置本地 Rust 即可快速验证想法。
- [ ] [**Solana Cookbook**](https://solanacookbook.com/) - 包含所有常见操作（转账、铸造、权限控制）的代码片段。
- [ ] [**Soldev**](https://soldev.app/) - 全面的 Solana 开发课程与教程集合。
- [ ] [**Helius**](https://helius.dev/) - 最受开发者欢迎的 RPC 与数据解析服务，极大简化了链上数据的读取。

---

## 💰 财务与 DeFi 生态 (DeFi & Finance)

- [ ] [**Jupiter (JUP)**](https://jup.ag/) - 2026 年最强的交易聚合器，支持极速兑换与 DCA (定投) 策略。
- [ ] [**Phantom Wallet**](https://phantom.app/) - 行业标准的钱包，支持多链与极佳的 NFT 展示。
- [ ] [**Jito / Marinade**](https://jito.network/) - 流动性质押协议，获取质押收益的同时保持资产流动性。
- [ ] [**Pyth Network**](https://pyth.network/) - 低延迟、机构级的价格预言机。

---

## 🎨 NFT 与压缩技术 (NFTs & Compression)

- [ ] [**Metaplex**](https://www.metaplex.com/) - Solana NFT 协议的标准制定者，包含 Core 与 Candy Machine。
- [ ] [**Tensor**](https://tensor.trade/) - 专业的 NFT 交易市场，具备强大的图表分析与批量操作功能。
- [ ] [**Bubblegum**](https://developers.metaplex.com/bubblegum) - 用于铸造和管理压缩 NFT (cNFTs) 的程序。

---

## 🛡️ 安全与审计 (Security)

- [ ] [**Soteria**](https://soteria.dev/) - 自动化的 Solana 智能合约漏洞扫描工具。
- [ ] [**Ackee Blockchain**](https://ackeeblockchain.com/blog/solana-security-vulnerabilities-checklist/) - 详细的合约漏洞自查清单。
- [ ] [**Solana Status**](https://status.solana.com/) - 监控主网 Beta 与测试网的实时运行状态。

---

## 💡 选型建议
1. **快速部署代币/NFT**：使用 **Metaplex SDK** 配合 **Helius RPC**。
2. **构建复杂的 DeFi 应用**：利用 **Anchor** 的 Account Context 和 **Jupiter API**。
3. **低成本用户互动**：优先考虑 **Compressed NFTs** 以节省存储租金。
4. **性能监控**：使用 **Solana Beach** 或 **SolScan** 查看账户详情。
