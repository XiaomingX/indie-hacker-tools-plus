# awesome-nft

## **项目亮点**
（精选当前仍具代表性的NFT项目/开发工具，附核心功能说明）
- **Eulerbeats**：[官网](https://eulerbeats.com)，结合生成艺术与音乐的NFT项目，每个NFT对应唯一音频片段，支持版权拆分与流转。
- **Nifty Ink**：[官网](https://nifty.ink/)，主打链上手绘NFT的平台，无需复杂技术即可创作并铸造以太坊NFT，适合创作者入门。
- **Scaffold-eth**：[GitHub](https://github.com/austintgriffith/scaffold-eth)，**NFT与DApp开发全栈工具包**，集成Hardhat（合约开发）、React（前端）、Ethers.js（链交互）等，内置ERC-721/ERC-1155合约模板，新手可快速搭建开发环境。
- **认证非同质化代币（NFT）索引**：[官网](https://nftndx.io/)，聚合合规、真实的NFT资产数据，提供索引、筛选与追踪功能，适合投资者和开发者查询。


## **分布式账本与NFT标准**
（NFT依赖的底层区块链及核心技术标准，解释“不同链的NFT有何区别”）

### **以太坊（Ethereum）**
NFT的“原生主场”，最成熟的NFT标准生态，缺点是Gas费较高（高峰期）。
- **ERC-721**：[EIP链接](https://eips.ethereum.org/EIPS/eip-721)，**基础NFT标准**，定义了非同质化代币的核心规则（如所有权、转账、元数据关联），绝大多数艺术NFT（如CryptoPunks）基于此标准。
- **ERC-1155**：[EIP链接](https://eips.ethereum.org/EIPS/eip-1155)，**多类型代币标准**，同时支持“非同质化（NFT）”和“同质化（如ERC-20）”代币，可批量转账，适合游戏道具（如同时发行“唯一皮肤”和“通用金币”）。
- **EIP-998**：[EIP链接](https://eips.ethereum.org/EIPS/eip-998)，**可组合NFT标准**，允许一个NFT“包含”其他NFT或同质化代币（比如“一个角色NFT”里嵌入“武器NFT”和“代币奖励”）。


### **Polygon（原Matic）**
以太坊的“侧链解决方案”，主打低Gas费、高吞吐量，是当前NFT交易和铸造的热门选择。
- **核心优势**：兼容以太坊NFT标准（ERC-721/ERC-1155），转账成本仅几分钱，速度秒级确认，很多NFT市场（如OpenSea）默认支持Polygon链。
- **官网**：[polygon.technology](https://polygon.technology/)


### **Flow区块链**
专为NFT和游戏优化的公链，采用“分片架构”提升性能，避免拥堵。
- **核心特点**：原生支持复杂NFT交互，知名项目如NBA Top Shot（篮球卡NFT）、UFC Collectibles均基于Flow。
- **资源链接**：[官网](https://www.onflow.org/) | [生态精选列表](https://github.com/gianni-dalerta/awesome-flow)


### **Polkadot与Kusama**
跨链生态，NFT标准更强调“灵活性与互操作性”。
- **RMRK**：[GitHub](https://github.com/rmrk-team/rmrk-spec)，**多功能NFT标准集**，支持“嵌套（NFT里套NFT）、可装备（给NFT加配件）、多资源（NFT关联图片/音频/文本）”，还能链上显示表情符号。
- **学习资源**：[视频解释](https://url.rmrk.app/rmrkccawe) | [图文教程](https://url.rmrk.app/dawnawe)


### **Hedera（哈希图）**
主打“企业级合规”的公链，NFT发行速度快、成本低。
- **HTS（Hedera代币服务）**：[官网](https://hedera.com/token-service)，无需写智能合约即可快速发行NFT，支持合规审计，适合品牌方发行官方NFT。


### **Tezos**
采用“权益证明”机制的环保型公链，NFT生态注重去中心化和创作者权益。
- **核心特点**：支持FA2代币标准（兼容NFT和同质化代币），铸造NFT能耗极低，创作者可设置“二次销售分成”。
- **生态入口**：[Tezos NFT专题](https://github.com/kevinelliott/awesome-tezos#tokens)


## **NFT教程（按学习阶段分类）**
（从入门到进阶，覆盖“理论-代码-实操”，附清晰学习目标）

### 1. 基础入门（零代码/少代码）
- **Cryptozombies Lesson 5**：[链接](https://cryptozombies.io/en/lesson/5)，通过“创建僵尸NFT”学Solidity基础，理解ERC-721核心逻辑，适合编程新手。
- **如何用IPFS铸造ERC-721 NFT**：[Medium文章](https://medium.com/pinata/how-to-build-erc-721-nfts-with-ipfs-e76a21d8f914)，讲解NFT“元数据存储”（IPFS避免链接失效），附分步操作指南。


### 2. 合约开发（进阶）
- **编写ERC-721收藏品合约**：[YouTube视频](https://www.youtube.com/watch?v=YPbgjPPC1d0)，手把手教用Solidity写NFT合约，包含“属性随机生成”功能。
- **OpenZeppelin NFT合约教程**：[官方文档](https://docs.openzeppelin.com/contracts/4.x/erc721)，使用行业公认的安全合约库（OpenZeppelin）开发NFT，避免漏洞。


### 3. 多链与全栈开发
- **构建多链NFT市场**：[博客](https://atila.ca/blog/tomiwa/how-to-build-a-multi-chain-nft-marketplace-on-ethereum-polygon-and-binance-smart-chain-using-solidity-react-hardhat-and-ethersjs)，教用Solidity+React+Hardhat开发支持以太坊/Polygon/BSC的NFT市场，含前端交互和链切换逻辑。


### 4. 特定链实操
- **KodaDot铸造NFT**：[教程1](https://nft.kodadot.xyz/rmrk/collection/10D77F8B699437BB50-KODA) | [教程2](https://stakenode.medium.com/dont-panic-and-mint-your-nft-s-on-kodadot-kusama-polkadot-first-nft-explorer-4273f789e585)，Polkadot/Kusama生态铸造NFT的实操指南，适合玩跨链NFT。
- **Hedera HTS演示**：[YouTube视频](https://www.youtube.com/watch?v=aEFm4bdnsBI)，演示用HTS发行NFT、配置属性、转账的全流程，适合企业级用户。


## **NFT社区（找同好、获资讯的核心渠道）**

### **行业会议（线下/线上大型活动）**
- **NFT NYC**：[官网](https://www.nft.nyc/)，全球最大NFT峰会之一，每年6月举办，聚集创作者、投资者、项目方，有展览和圆桌论坛。
- **Miami NFT Week**：[官网](https://miaminftweek.com/)，聚焦“NFT+艺术+科技”，适合关注NFT落地应用的人。
- **NFT LA**：[官网](https://www.nftla.live/)，洛杉矶本土顶级NFT活动，侧重好莱坞与NFT的结合（如影视IP NFT）。


### **Discord社群（实时交流）**
- **CryptoDevs**：[链接](https://discord.gg/EDA6M3R)，NFT开发者为主的社群，可提问合约开发、工具使用问题。
- **NonFungible.Com**：[链接](https://discord.gg/3WQ5sT4Dpj)，NFT数据平台的官方社群，分享市场动态和数据分析。
- **icy.tools Community**：[链接](https://icy.community)，NFT分析工具icy.tools的社群，投资者常在这里交流持仓和趋势。


### **Telegram群组**
- **LobsterDAO的NFT大道**：[链接](https://t.me/NFT_avenue)，DAO组织（去中心化自治组织）运营的社群，讨论NFT投资和社区治理。


### **NFT权益社区（持有NFT享特权）**
- **VeeFriends**：[官网](https://www.veefriends.com/)，由创业家Gary Vaynerchuk创建，持有NFT可参与线下峰会、获得一对一咨询等权益。


### **X（原Twitter）列表（关注行业动态）**
- **Gianni的NFT X列表**：[链接](https://twitter.com/GianniDalerta/lists/nft)，聚合了NFT行业KOL、项目方和媒体，一键关注获取精选资讯。
- **Rarible**：[X账号](https://x.com/rariblecom)，知名NFT交易平台官方账号，发布平台活动和NFT趋势。


### **行业协会（推动标准与合规）**
- **非同质化联盟（Non-Fungible Alliance）**：[官网](https://nonfungiblealliance.org/)，由Coinbase、OpenSea等发起，旨在制定NFT行业标准、推动合规化发展。


## **出版物（系统学习NFT的内容渠道）**

### **新闻与简报（实时资讯）**
- **Cointelegraph NFT周刊**：[链接](https://cointelegraph.com/magazine/nft-week)，全球知名加密媒体的NFT专栏，涵盖市场数据、项目动态。
- **Dappradar NFT博客**：[链接](https://dappradar.com/blog/tag/nfts)，侧重NFT市场交易量、热门项目排行，数据驱动型内容。
- **NFT评论（NFT Review）**：[链接](https://news.nft.review)，深度解析NFT项目背后的技术和商业逻辑。


### **游戏NFT媒体**
- **Blockchain Gamer**：[官网](https://www.blockchaingamer.biz/)，权威区块链游戏媒体，覆盖“游戏NFT设计、玩法、经济模型”。


### **深度文章（底层逻辑与趋势）**
- **《NFT初学者指南》**：[链接](https://linda.mirror.xyz/df649d61efb92c910464a4e74ae213c4cab150b9cbcc4b7fb6090fc77881a95d)，由加密领域专家Linda Xie撰写，通俗解释NFT的技术原理和应用场景。
- **《新媒体结构：所有权经济》**：[链接](https://darkstar.mirror.xyz/srmoGiN_1pg_toQGzCupkjWFOaf8xi0mM60zYpn_pwI)，解析NFT如何重构“创作者-用户”关系，提出“所有权经济”概念。
- **《理解基于区块链的NFT》**：[链接](https://chuta.medium.com/understanding-blockchain-powered-non-fungible-tokens-nfts-cef88850a133)，从技术、法律、市场三个维度拆解NFT，适合新手全面入门。


### **播客（碎片化学习）**
- **《Lets Talk Bitcoin | E86 - 虚拟世界，真实金钱》**：[链接](https://letstalkbitcoin.com/e86-virtual-worlds-real-money)，早期解析NFT“价值本质”的播客，适合理解NFT的底层逻辑。
- **《Digitally Rare》**：[X账号](https://x.com/digitallyrare)，专注NFT访谈的播客，邀请项目方和创作者分享实战经验。


## **开发与工具资源（提高NFT工作效率）**
（按“开发-铸造-验证-数据”分类，附核心用途）
| 工具名称         | 链接/官网                          | 核心用途                                                                 |
|------------------|------------------------------------|--------------------------------------------------------------------------|
| NFTPort.xyz      | [文档](https://docs.nftport.xyz/)   | 无需写智能合约！通过REST API快速铸造NFT、查询NFT数据（支持多链）。       |
| Scaffold-eth     | [GitHub](https://github.com/austintgriffith/scaffold-eth) | NFT全栈开发工具包，内置合约模板、前端框架，新手可快速搭项目。            |
| OpenZeppelin Contracts | [官网](https://docs.openzeppelin.com/contracts/) | 安全的NFT合约库，提供ERC-721/ERC-1155标准实现，避免重复造轮子和漏洞。   |
| Rarepress        | [官网](https://rarepress.org/)      | IPFS上的NFT工具，支持铸造、存储、分享NFT，确保元数据永久可用。           |
| Check My NFT     | [官网](https://checkmynft.com/)     | 验证NFT的真实性、元数据完整性，避免买到“假NFT”或“元数据失效的NFT”。     |
| minty 🌿         | [GitHub](https://github.com/yusefnapora/minty) | 轻量工具，教你用IPFS和Solidity手动铸造NFT，理解底层流程。                |
| useNft()         | [GitHub](https://github.com/spectrexyz/use-nft) | React钩子库，前端开发者可快速获取任何NFT的元数据（如图片、属性、所有者）。 |
| Alchemy NFT API  | [文档](https://docs.alchemy.com/docs/nft-api) | 高性能NFT数据API，支持查询持仓、交易历史、地板价，适合开发者和投资者。   |
| NFT Multisender  | -                                  | 批量转账NFT的工具（需确认具体版本），适合项目方发放NFT空投。             |
