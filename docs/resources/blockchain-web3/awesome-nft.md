# NFT 开发与生态资源精选 (2026 Checklist)

> [!TIP]
> **Indie Hacker Insight**: 2026 年，NFT 已从“炒作”回归为**“链上凭证”**。
> - **实用性优先**：目前的 NFT 核心价值在于身份验证 (Auth)、会员权益 (Membership) 和 RWA (真实资产上链)。
> - **多链策略**：虽然以太坊是老家，但 **Polygon** 和 **Solana** 是目前高频、低成本 NFT 交互的首选。
> - **动态化**：关注 **ERC-6551 (Token Bound Accounts)**，让你的 NFT 本身就是一个钱包，能持有其他资产。

---

## 🏗️ NFT 核心标准与协议 (Standards)

- [ ] [**ERC-721**](https://eips.ethereum.org/EIPS/eip-721) - **[基础]** 每一个代币都是唯一的，最通用的 NFT 标准。
- [ ] [**ERC-1155**](https://eips.ethereum.org/EIPS/eip-1155) - **[高效]** 混合标准。在一个合约中支持多种类型的代币（如：1 个金币 NFT 和 100 个银币代币），极大节省 Gas。
- [ ] [**ERC-6551**](https://erc6551.com/) - **[进阶]** 代币绑定账户。赋予 NFT 钱包功能，使其能够拥有资产并与 DApp 交互。
- [ ] [**RMRK (Polkadot)**](https://www.rmrk.app/) - 极具创新的 NFT 标准，支持嵌套（NFT 持有 NFT）、可装备附件和多资源展现。

---

## 🛠️ 开发框架与 API (Developer Tools)

- [ ] [**NFTPort**](https://www.nftport.xyz/) - **2026 推荐**。通过简单的 REST API 即可完成铸造、查询和多链分发，无需编写智能合约。
- [ ] [**Alchemy NFT API**](https://docs.alchemy.com/reference/nft-api-quickstart) - 行业最稳的 NFT 数据接口，支持批量查询持仓、元数据和地板价。
- [ ] [**OpenZeppelin Contracts**](https://docs.openzeppelin.com/contracts/) - 安全合约库的事实标准，提供经过审计的 ERC-721/1155 模板。
- [ ] [**Scaffold-eth**](https://github.com/scaffold-eth/scaffold-eth-2) - 全栈开发套件，内置 NFT 模板，适合快速原型开发。
- [ ] [**Thirdweb**](https://thirdweb.com/) - 提供 SDK 和可视化面板，一键部署 NFT 市场和空投合约。

---

## 📂 存储与验证 (Storage & Verification)

- [ ] [**Pinata (IPFS)**](https://www.pinata.cloud/) - 最流行的 NFT 媒体资源托管平台，确保元数据永久可用。
- [ ] [**Arweave**](https://www.arweave.org/) - 真正意义上的永久存储，适合对去中心化有极致要求的项目。
- [ ] [**Check My NFT**](https://checkmynft.com/) - 验证 NFT 元数据存储的安全性与持久性，避免资产“消失”。

---

## 🎨 市场与灵感 (Marketplaces & Inspo)

- [ ] [**OpenSea**](https://opensea.io/) - 全球最大的交易市场，独立开发者的首选上架地。
- [ ] [**Blur**](https://blur.io/) - 针对专业交易者的聚合平台，流动性极高。
- [ ] [**Magic Eden**](https://magiceden.io/) - Solana 生态的王者，现已扩展至多链，用户体验极佳。

---

## 💡 选型建议
1. **构建会员俱乐部**：选 **Ethereum/Polygon** + **ERC-721** + **Thirdweb SDK**。
2. **开发游戏道具系统**：强制选 **ERC-1155** 以降低批量操作的 Gas 费。
3. **实现 NFT 持有资产的功能**：研究并集成 **ERC-6551** 协议。
4. **追求极速与低费率**：无脑选 **Solana** (使用 Metaplex 协议)。
