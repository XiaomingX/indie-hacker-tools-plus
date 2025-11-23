# awesome-zkevm：零知识以太坊虚拟机核心资源指南


## 前言
**zkEVM（零知识以太坊虚拟机）** 是解决以太坊“扩容三元悖论”（去中心化、安全性、可扩展性）的关键技术：它既能完整复现EVM（以太坊虚拟机）的计算逻辑，又能通过**零知识证明（ZKP）** 将大量交易打包验证后提交到以太坊主网（Layer1），实现“ Layer2 扩容+原生兼容性+隐私保护”的三重价值。

本文档整理了zkEVM领域的核心知识、主流方案与实用工具，剔除过时内容并补充关键背景，帮你快速入门并深入该领域。


## 一、基础概念：从Rollup到zkEVM
要理解zkEVM，需先掌握其底层支撑技术与核心定义。


### 1. Rollup：zkEVM的“扩容载体”
**Rollup（滚动压缩）** 是以太坊Layer2扩容的核心范式：将Layer2的大量交易打包、计算后，仅把“交易摘要+有效性证明”提交到Layer1验证，大幅降低Layer1的存储与计算压力。  
Rollup分两类：**Optimistic Rollup（乐观rollup，依赖“挑战期”验证）** 和 **ZK-Rollup（零知识rollup，依赖零知识证明验证）**，zkEVM本质是“兼容EVM的ZK-Rollup执行环境”。

| 核心资源 | 说明（核心价值） |
|----------|------------------|
| [Rollup指南（Vitalik）](https://vitalik.ca/general/2021/01/05/rollup.html) | 以太坊创始人Vitalik的经典科普，详解Rollup的工作原理、优势及为何是“以太坊扩容的未来”。 |
| [以Rollup为核心的以太坊路线图](https://ethereum-magicians.org/t/a-rollup-centric-ethereum-roadmap/4698) | Vitalik提出的以太坊长期扩容战略，明确ZK-Rollup将逐步成为Layer2的主导方案（截至2024年已基本落地）。 |
| [Zk-Rollups如何工作（Barry WhiteHat）](https://medium.com/fcats-blockchain-incubator/how-zk-rollups-work-8ac4d7155b0e) | 零知识领域专家的实操向解析，从“数据存储、交易执行、证明生成”三步骤讲清ZK-Rollup的细节。 |


### 2. zkEVM：核心定义与技术解析
**zkEVM的核心目标**：让以太坊生态的DApp（基于Solidity开发）无需修改代码，就能直接部署在ZK-Rollup上运行，同时享受零知识证明的扩容与隐私能力。  
根据“与EVM兼容程度”和“技术实现路径”，Vitalik将zkEVM分为4类（详见下方Vitalik的文章）。

| 核心资源 | 说明（核心价值） |
|----------|------------------|
| [zkEVM的4种类型（Vitalik）](https://vitalik.ca/general/2022/08/04/zkevm.html) | 最权威的zkEVM分类框架：从“完全兼容EVM”到“定制化zk友好虚拟机”，解析各类方案的trade-off（兼容性vs性能）。 |
| [Scroll zkEVM详解](https://hackmd.io/@yezhang/S1_KMMbGt) | 原生zkEVM代表项目Scroll的技术白皮书，讲清如何通过“电路算术化”复现EVM逻辑。 |
| [Scroll与EF zkEVM架构对比](https://twitter.com/LuozhuZhang/status/1538166119785111552?s=20&t=o9hnHeP1na00u6gldaxnCw) | 深入对比“Scroll社区方案”与“以太坊基金会（EF）官方方案”的架构差异，适合技术开发者。 |
| [Polygon zkEVM（原Hermez 2.0）深度解析](https://blog.polygon.technology/zkverse-deep-dive-into-polygon-hermez-2-0/) | 详解Polygon zkEVM的“Prover（证明器）-Verifier（验证器）”架构及主网落地细节。 |
| [zkEVM电路算术化（视频）](https://www.youtube.com/watch?v=DT8g3veR17k&t=910s) | Ye Zhang（Scroll核心开发者）的技术分享，拆解“如何将EVM指令转化为零知识证明可验证的电路”（zkEVM的核心难点）。 |


### 3. 零知识证明（ZKP）：zkEVM的“信任基石”
ZKP是一种“能证明某个陈述为真，但不泄露任何额外信息”的密码技术。zkEVM依赖的主流ZKP协议如下：

#### （1）zk-SNARK：早期主流协议
**zk-SNARK（零知识简洁非交互式知识证明）** 是首个大规模应用的ZKP协议，特点是“证明体积小、验证速度快”，但需“可信初始化”（早期缺陷，已被后续协议优化）。  
- [zk-SNARK简介与示例](https://media.consensys.net/introduction-to-zksnarks-with-examples-3283b554fc3b)：通过“匿名转账”案例，通俗解释zk-SNARK的核心逻辑（适合新手）。  
- [zk-SNARK工作原理深度解析](https://medium.com/@imolfar/why-and-how-zk-snark-works-1-introduction-the-medium-of-a-proof-d946e931160)：从数学层拆解“多项式承诺、椭圆曲线配对”等核心组件。

#### （2）PLONK：通用可更新协议
**PLONK（Permutations over Lagrange-bases for Oecumenical Non-interactive arguments of Knowledge）** 解决了zk-SNARK的“可信初始化”问题，支持“通用设置”（一次初始化可复用给多个应用），是zkEVM电路设计的常用协议。  
- [理解PLONK（Vitalik）](https://vitalik.ca/general/2019/09/22/plonk.html)：用极简语言讲清PLONK的“置换检查、多项式承诺”核心创新。  
- [PLONK与Plookup机制](https://hackmd.io/@arielg/ByFgSDA7D)：解析PLONK中“高效处理查表逻辑”的Plookup技术（zkEVM处理EVM指令的关键）。

#### （3）Halo2：无需配对的新一代协议
**Halo2** 是Zcash团队开发的协议，核心优势是“无需椭圆曲线配对”（降低计算复杂度）和“增量验证”（适合链上持续验证场景），现为Scroll、PSE等项目的核心协议。  
- [Halo2：无配对SNARK探索（Vitalik）](https://vitalik.ca/general/2021/11/05/halo.html)：对比Halo2与传统zk-SNARK的差异，解释“无配对”的技术价值。  


## 二、主流zkEVM解决方案（2024年现状）
根据“兼容EVM的技术路径”，zkEVM主要分为三类，下表整理了各方案的代表项目、核心特点与实用资源：

### 1. 原生zkEVM（Direct zkEVM）
**核心逻辑**：直接在零知识电路中复现EVM的每一条指令，实现“100% EVM兼容”，开发者无需修改任何Solidity代码。  
是目前最受生态欢迎的路线。

| 项目 | 2024年现状 | 核心资源 |
|------|------------|----------|
| **Scroll** | 主网已稳定运行，支持以太坊主网资产跨链，兼容99%+EVM功能 | - [Scroll架构解析](https://scroll.mirror.xyz/nDAbJbSIJdQIWqp9kn8J0MVS4s6pYBwHmK7keidQs-k) <br> - [zkEVM电路代码](https://github.com/privacy-scaling-explorations/zkevm-circuits) |
| **Polygon zkEVM** | 原Hermez 2.0，Polygon生态核心扩容方案，主网支持高TPS | - [主网文档](https://docs.polygon.technology/docs/zkEVM/overview/) <br> - [Prover代码仓库](https://github.com/0xPolygonHermez/zkevm-prover) |
| **PSE（隐私与扩容探索）** | 以太坊基金会支持的开源社区，为Scroll等项目提供底层技术支撑 | - [zkEVM规范文档](https://github.com/privacy-scaling-explorations/zkevm-specs) <br> - [Halo2应用工具](https://github.com/privacy-scaling-explorations/halo2) |
| **Polygon Zero** | 基于Plonky2协议，主打“超快速证明生成”，2024年逐步合并入Polygon zkEVM生态 | - [Plonky2协议库](https://github.com/mir-protocol/plonky2)（zk领域最快的证明库之一） |


### 2. 基于编译器的zkEVM（Compiler-based zkEVM）
**核心逻辑**：不直接复现EVM，而是将Solidity代码编译为“zk友好的中间语言”（如zkSync的Yul+），再生成证明。兼容性略低于原生方案，但性能更高。

| 项目 | 2024年现状 | 核心资源 |
|------|------------|----------|
| **zkSync Era（原zkSync v2+）** | 主网已上线，支持账户抽象、EVM兼容（95%+功能），生态DApp数量领先 | - [开发门户](https://docs.zksync.io/)（含水龙头、教程，已支持Sepolia测试网） <br> - [Solidity编译器](https://github.com/matter-labs/compiler-solidity) |


### 3. 基于转译器的zkEVM（Transpiler-based zkEVM）
**核心逻辑**：将EVM字节码“转译”为目标虚拟机的代码（如StarkNet的Cairo语言），再生成证明。兼容性最低，但可定制化程度高。

| 项目 | 2024年现状 | 核心资源 |
|------|------------|----------|
| **StarkNet** | 基于StarkWare的STARK证明，主网支持以太坊资产跨链，生态以DeFi为主 | - [Warp转译工具](https://github.com/NethermindEth/warp)（将Solidity转Cairo） <br> - [Awesome-StarkNet资源汇总](https://github.com/gakonst/awesome-starknet) |
| **Miden** | 基于“Miden VM”，主打隐私计算，2024年处于测试网阶段 | - [Miden VM代码仓库](https://github.com/0xPolygonMiden/miden-vm) |


### 4. 其他重要方案
- **Consensys zkEVM**：Consensys（以太坊生态核心机构）推出的开源方案，侧重“企业级兼容性”，文档对开发者友好。  
  资源：[Consensys zkEVM 2.0规范](https://ethresear.ch/t/a-zk-evm-specification-part-2/13903)


## 三、实用工具与开发库
### 1. 零知识证明核心库
| 库名称 | 用途 | 特点 |
|--------|------|------|
| [Halo2仓库](https://github.com/zcash/halo2) | 零知识证明协议底层实现 | 无需可信设置，支持自定义电路，Scroll/PSE的核心依赖 |
| [Plonky2](https://github.com/mir-protocol/plonky2) | 快速证明生成库 | 基于PLONK变体，证明速度比传统库快10倍以上 |
| [Awesome-ZKPs](https://github.com/matter-labs/awesome-zero-knowledge-proofs) | ZKP资源汇总 | 涵盖协议、论文、工具，适合系统性学习 |


### 2. zkEVM开发工具
| 工具名称 | 关联项目 | 用途 |
|----------|----------|------|
| [zkEVM文档（PSE）](https://privacy-scaling-explorations.github.io/zkevm-docs/) | PSE/Scroll | 详细说明zkEVM的指令集、电路设计规范 |
| [Hermez文档](https://docs.hermez.io/zkEVM/Overview/Overview/) | Polygon zkEVM | 主网部署、跨链操作、Prover调试指南 |


### 3. ZKP硬件加速
零知识证明生成是“计算密集型任务”，硬件加速可将证明时间从分钟级压缩到秒级。  
- [零知识证明硬件加速（Paradigm）](https://www.paradigm.xyz/2022/04/zk-hardware)：解析“专用ASIC芯片、GPU优化”等硬件加速方案的技术原理。  
- [Supranational sppark](https://github.com/supranational/sppark)：开源的“椭圆曲线配对运算加速库”，大幅提升zk-SNARK的证明生成效率。


## 补充说明
1. **资源时效性**：本文档基于2024年5月的技术现状整理，zkEVM领域迭代极快，建议通过项目官网（如Scroll、zkSync）获取最新动态。  
2. **学习路径建议**：新手可先读Vitalik的《Rollup指南》和《zkEVM的4种类型》，再结合具体项目的文档（如Scroll架构）深入，最后通过代码仓库（如zkEVM-circuits）实操。
