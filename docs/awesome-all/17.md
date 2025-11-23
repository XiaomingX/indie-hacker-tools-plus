# 2024 实用 Web3 资源指南（从入门到开发实战）
Web3 生态迭代迅速，部分工具已停止维护或被更优方案替代。本指南**重构分类逻辑、剔除过时工具、补充核心实战资源**，用“通俗定位+核心价值”的方式拆解每个资源，帮你快速搞懂“是什么、能干嘛、适合谁用”，尤其适配新手入门和开发者实战需求。


## 一、入门核心：Web3 基础概念与资源库
先搞懂核心技术栈的“地基”，这些资源是系统学习的起点。

| 资源名称          | 链接                                                                 | 通俗定位（是什么）                          | 核心价值 / 适合场景                          |
|-------------------|----------------------------------------------------------------------|-------------------------------------------|-------------------------------------------|
| **Solidity 精选库** | [github.com/bkrem/awesome-solidity](https://github.com/bkrem/awesome-solidity) | Solidity 语言的“资源大全”                  | 包含入门教程、安全工具、开源合约模板，新手找资料不用东拼西凑 |
| **以太坊生态库**   | [github.com/bekatom/awesome-ethereum](https://github.com/bekatom/awesome-ethereum) | 以太坊的“百科全书”，覆盖链、DApp、工具       | 想全面了解以太坊生态（Layer2、DeFi、NFT）的人必备 |
| **Web3 安全库**    | [github.com/Anugrahsr/Awesome-web3-Security](https://github.com/Anugrahsr/Awesome-web3-Security) | 区块链安全的“工具箱+案例集”                 | 渗透测试工程师、合约审计师找漏洞工具、攻击案例的核心资源 |
| **区块链总览库**   | [github.com/yjjnls/awesome-blockchain](https://github.com/yjjnls/awesome-blockchain) | 跨公链的“资源地图”（不止以太坊）             | 想对比比特币、Solana、Avalanche 等生态的开发者参考 |
| **零知识证明（ZK）库** | [github.com/ventali/awesome-zk](https://github.com/ventali/awesome-zk) | ZK 技术的“入门到进阶手册”                   | 包含 ZK 算法、开发工具（如 Circom）、落地项目（zkSync），适合研究隐私计算 |


## 二、开发准备：环境与效率工具
写智能合约、测 DApp 必须的“工作台”，按“新手友好→专业实战”排序。

| 工具名称          | 链接                                                                 | 通俗定位（是什么）                          | 核心价值 / 适合场景                          |
|-------------------|----------------------------------------------------------------------|-------------------------------------------|-------------------------------------------|
| **Remix**         | [remix.ethereum.org](https://remix.ethereum.org/)                     | 浏览器端的 Solidity 开发 IDE（不用装软件）  | 新手入门首选：实时编译、一键部署到测试网、在线调试合约，零配置启动 |
| **Hardhat**       | [hardhat.org](https://hardhat.org/)                                   | 本地的智能合约开发/测试/部署框架（基于 JS/TS） | 专业开发者必备：支持自定义脚本、插件生态丰富（如集成 Etherscan 验证）、适合复杂 DApp 开发 |
| **Foundry**       | [book.getfoundry.sh](https://book.getfoundry.sh/)                     | 基于 Rust 的以太坊开发工具（编译/测试速度快） | 追求效率的开发者：支持 Solidity 写测试用例、本地节点模拟，比 Hardhat 更轻量 |
| **OpenZeppelin Contracts** | [github.com/OpenZeppelin/openzeppelin-contracts](https://github.com/OpenZeppelin/openzeppelin-contracts) | 安全的智能合约“标准零件库”                 | 避免重复造轮子：包含 ERC20（代币）、ERC721（NFT）等经过审计的合约模板，减少漏洞风险 |
| **solidity-coverage** | [github.com/sc-forks/solidity-coverage](https://github.com/sc-forks/solidity-coverage) | 合约代码的“测试覆盖率检测器”               | 审计前必备：告诉你哪些代码没测到，降低隐藏漏洞概率 |


## 三、合约开发：核心语言与实战示例
智能合约的“编程语言”，不同语言适配不同需求。

| 语言/资源         | 链接                                                                 | 通俗定位（是什么）                          | 核心价值 / 适合场景                          |
|-------------------|----------------------------------------------------------------------|-------------------------------------------|-------------------------------------------|
| **Solidity**      | [docs.soliditylang.org](https://docs.soliditylang.org/)               | 以太坊生态的“主流合约语言”（面向对象）      | 90% 以上的以太坊 DApp 用它写，新手必学，文档支持多语言 |
| **Vyper**         | [docs.vyperlang.org](https://docs.vyperlang.org/)                     | Python 风格的“安全优先合约语言”             | 语法更简洁，强制规避 Solidity 的部分风险（如重入攻击），适合对安全要求高的场景 |
| **Solidity by Example** | [solidity-by-example.org](https://solidity-by-example.org/)           | Solidity 的“代码示例大全”                   | 边看边抄：包含“发代币”“写 NFT”“做众筹”等实战代码，新手可直接改造成自己的项目 |


## 四、前端对接：SDK 与交互工具
让 Web3 前端（网页/APP）连接区块链、调用合约的“桥梁”。

| SDK/工具          | 链接                                                                 | 通俗定位（是什么）                          | 核心价值 / 适合场景                          |
|-------------------|----------------------------------------------------------------------|-------------------------------------------|-------------------------------------------|
| **ethers.js**     | [github.com/ethers-io/ethers.js](https://github.com/ethers-io/ethers.js) | 以太坊的“JavaScript 开发工具包”             | 功能全、文档清晰，支持钱包连接、合约调用、交易签名，前端开发首选 |
| **viem**          | [viem.sh](https://viem.sh/)                                           | 轻量版的“ethers.js 平替”（新增）            | 体积比 ethers.js 小 70%，启动更快，适合追求性能的前端项目 |
| **wagmi**         | [github.com/tmm/wagmi](https://github.com/tmm/wagmi)                   | 基于 React 的“Web3 组件库”                 | 前端开发者省时间：封装了“连接钱包”“调用合约”等组件，不用重复写逻辑 |
| **WalletConnect** | [walletconnect.com](https://walletconnect.com/)                       | 钱包与 DApp 的“通用连接协议”               | 解决跨端适配：比如手机钱包（Trust Wallet）连接电脑端 DApp，不用局限于浏览器插件 |


## 五、基础设施：核心协议与存储
Web3 应用的“底层服务”——存数据、查数据、做交易都靠它们。

| 协议/存储         | 链接                                                                 | 通俗定位（是什么）                          | 核心价值 / 适合场景                          |
|-------------------|----------------------------------------------------------------------|-------------------------------------------|-------------------------------------------|
| **IPFS**          | [ipfs.io](https://ipfs.io/)                                           | 分布式的“文件存储系统”（替代传统服务器）     | 数据抗审查、不宕机：适合存 NFT 图片、DApp 静态资源，比如 OpenSea 的 NFT 大多存在 IPFS |
| **The Graph**     | [thegraph.com/en/](https://thegraph.com/en/)                           | 区块链的“搜索引擎”                         | 快速查链上数据：比如 DApp 要查“某地址的 NFT 持仓”，不用自己遍历区块，直接调用 The Graph 的接口 |
| **Uniswap**       | [uniswap.org](https://uniswap.org/)                                   | 去中心化的“代币交易协议”                   | 最主流的 DEX（去中心化交易所），支持任意 ERC20 代币兑换，开发者可集成其交易功能 |
| **Aave**          | [aave.com](https://aave.com/)                                         | 去中心化的“借贷平台协议”                   | 支持“存币赚利息”“抵押借币”，开发者可基于它做金融类 DApp |
| **zkSync Era**    | [zksync.io](https://zksync.io/)                                       | 以太坊的“Layer2 扩容协议”（基于 ZK）        | 解决以太坊“贵、慢”问题：交易费比主网低 90%，确认速度快，适合高频交易场景 |
| **Optimism**      | [optimism.io](https://optimism.io/)                                   | 以太坊的“Layer2 扩容协议”（新增）           | 另一种扩容方案：兼容性强，以太坊合约几乎不用改就能部署上去 |
| **OrbitDB**       | [github.com/orbitdb/orbit-db](https://github.com/orbitdb/orbit-db)     | 基于 IPFS 的“分布式数据库”                 | 存结构化数据：比如 DApp 的用户数据，不用依赖中心化数据库 |
| **WeaveDB**       | [github.com/weavedb/weavedb](https://github.com/weavedb/weavedb)       | 基于智能合约的“NoSQL 数据库”               | 链上链下结合：数据存在区块链，查询靠索引，适合需要“数据可信+查询快”的场景 |


## 六、学习实战：教程与课程
从“理论”到“动手”，这些资源能帮你快速做出第一个 Web3 项目。

| 教程/课程         | 链接                                                                 | 通俗定位（是什么）                          | 核心价值 / 适合场景                          |
|-------------------|----------------------------------------------------------------------|-------------------------------------------|-------------------------------------------|
| **CryptoZombies** | [cryptozombies.io](https://cryptozombies.io/)                         | 游戏化的“区块链入门课”                     | 新手不枯燥：通过“写一个区块链僵尸游戏”学 Solidity，边玩边学 |
| **Speed Run Ethereum** | [speedrunethereum.com](https://speedrunethereum.com/)                 | 以太坊开发的“实战任务清单”                 | 进阶必备：包含“做 NFT 铸造 DApp”“写 DeFi 闪电贷”等 10+ 实战任务，做完就能上手项目 |
| **Alchemy University** | [university.alchemy.com](https://university.alchemy.com/)             | 免费的“Web3 系统课程”                     | 从基础到进阶：涵盖区块链原理、合约开发、前端对接，还有老师答疑 |
| **Buildspace**    | [buildspace.so](https://buildspace.so/)                               | 项目驱动的“Web3 实战营”（新增）            | 手把手做项目：比如“2 周做一个 NFT 集合”“3 周做一个链上社交 DApp”，完成还能拿证书 |
| **全栈 DApp 教程** | [dev.to/dabit3/the-complete-guide-to-full-stack-ethereum-development-3j13](https://dev.to/dabit3/the-complete-guide-to-full-stack-ethereum-development-3j13) | 前端+合约的“全流程开发指南”               | 适合想做完整产品的人：从写合约到 React 前端对接，再到部署上线 |


## 七、实用工具：日常开发/使用必备
不管是开发还是用 Web3 产品，这些工具能帮你省大量时间。

| 工具名称          | 链接                                                                 | 通俗定位（是什么）                          | 核心价值 / 适合场景                          |
|-------------------|----------------------------------------------------------------------|-------------------------------------------|-------------------------------------------|
| **Chainlist**     | [chainlist.org](https://chainlist.org/)                               | 以太坊兼容链的“网络配置大全”               | 开发/使用 DApp 必用：一键添加 BSC、Polygon 等测试网/主网到钱包，不用手动填 RPC 地址 |
| **Etherscan**     | [etherscan.io](https://etherscan.io/)                                 | 以太坊的“区块链浏览器”（新增）             | 查交易、查合约：比如看某笔转账是否到账、验证合约源码、查代币持仓 |
| **Rainbow Wallet** | [rainbow.me](https://rainbow.me/)                                     | 高颜值的“多链钱包”（新增）                 | 普通用户友好：支持以太坊、Polygon 等多链，界面比 MetaMask 更简洁 |
| **以太坊生态地图** | [www.ethereum-ecosystem.com](https://www.ethereum-ecosystem.com/)     | 以太坊生态的“工具/DApp 导航”               | 找资源不迷路：按“DeFi、NFT、Layer2”分类，快速找到对应的产品或工具 |


## 八、开源项目：可参考的优质代码
看高手写的代码是最快的学习方式，这些项目是生态标杆。

| 开源项目          | 链接                                                                 | 核心定位                                  | 参考价值                                  |
|-------------------|----------------------------------------------------------------------|-------------------------------------------|-------------------------------------------|
| **MetaMask**      | [github.com/MetaMask/metamask-extension](https://github.com/MetaMask/metamask-extension) | 最流行的“浏览器钱包插件”                   | 学习“钱包签名逻辑”“与区块链交互”的核心代码 |
| **Uniswap V4**    | [github.com/Uniswap/v4-core](https://github.com/Uniswap/v4-core)     | 去中心化交易协议的“最新核心代码”           | 研究 DeFi 协议设计：比如流动性池、手续费机制的实现 |
| **Chainlink**     | [github.com/smartcontractkit/chainlink](https://github.com/smartcontractkit/chainlink) | 区块链的“预言机协议”（连接真实世界数据）   | 学习“链下数据上链”的实现：比如获取比特币价格、体育比赛结果 |
| **Lens Protocol** | [github.com/lens-protocol/core](https://github.com/lens-protocol/core) | 去中心化的“社交协议”（新增）               | 学习 Web3 社交产品设计：比如“关注”“发帖”“点赞”的链上实现 |


## 九、视频学习：可视化教程渠道
适合喜欢“看视频学”的人，内容从入门到进阶全覆盖。

| 视频渠道          | 链接                                                                 | 核心内容方向                              | 适合人群                                  |
|-------------------|----------------------------------------------------------------------|-------------------------------------------|-------------------------------------------|
| **Smart Contract Programmer** | [youtube.com/channel/UCJWh7F3AFyQ_x01VKzr9eyA](https://www.youtube.com/channel/UCJWh7F3AFyQ_x01VKzr9eyA) | Solidity 语法、合约安全、DeFi 开发         | 想深入学合约开发的开发者                   |
| **Dapp University** | [youtube.com/c/DappUniversity](https://youtube.com/c/DappUniversity) | 全栈 DApp 开发、钱包对接、NFT 项目实战     | 零基础想做完整 Web3 项目的人               |
| **Alchemy**       | [youtube.com/c/AlchemyPlatform](https://youtube.com/c/AlchemyPlatform) | Layer2 开发、API 实战、生态最新动态        | 想跟进以太坊生态新功能（如账户抽象）的开发者 |


## 补充说明
1.  **过时资源剔除**：原列表中的 **Brownie**（基于 Python 的开发框架，维护活跃度下降，被 Hardhat/Foundry 替代）已剔除；新增 viem、Optimism 等 2024 年仍活跃的核心工具。
2.  **工具选择建议**：
    - 新手入门：先用 Remix 写简单合约，配合 CryptoZombies 学语法，再用 Speed Run Ethereum 做实战。
    - 专业开发：选 Hardhat（JS/TS 生态）或 Foundry（Rust 生态），配合 OpenZeppelin 写安全合约。
3.  **安全提醒**：智能合约漏洞损失不可逆！开发后务必用 **slither**（静态分析工具）扫漏洞，复杂项目建议找第三方审计（如 CertiK）。
