# zkEVM 零知识以太坊虚拟机资源 (2026 Checklist)

> [!TIP]
> **Indie Hacker Insight**: 2026 年，zkEVM 已成为以太坊 Layer 2 的事实标准。
> - **无缝迁移**：对于开发者而言，zkEVM 的最大价值在于“零改动”部署 Solidity 代码，同时享受极低的手续费。
> - **高性能证明**：关注 **Plonky2** 和 **Halo2** 协议，它们是目前证明生成速度最快的方案。
> - **流动性聚合**：虽然 L2 众多，但通过 **AggLayer (Polygon)** 或类似方案，流动性碎片化问题正在被解决。

---

## 🏗️ 核心概念与架构 (Fundamentals)

- [ ] [**Rollup 极简指南 (Vitalik)**](https://vitalik.ca/general/2021/01/05/rollup.html) - 理解 zkEVM 的扩容载体与安全基石。
- [ ] [**zkEVM 的 4 种类型 (Vitalik)**](https://vitalik.ca/general/2022/08/04/zkevm.html) - **[必读]** 掌握“完全兼容”与“zk 友好”之间的权衡。
- [ ] [**Zk-Rollups 工作原理**](https://medium.com/fcats-blockchain-incubator/how-zk-rollups-work-8ac4d7155b0e) - 深入浅出讲解数据存储、执行与证明生成的闭环。
- [ ] [**电路算术化 (Arithmetization)**](https://www.youtube.com/watch?v=DT8g3veR17k&t=910s) - 核心开发者解析如何将 EVM 指令转化为电路。

---

## 🚀 主流 zkEVM 方案 (Mainstream Solutions)

- [ ] [**Scroll**](https://scroll.io/) - **[原生首选]** 极致追求与以太坊等效的原生 zkEVM。
- [ ] [**Polygon zkEVM**](https://polygon.technology/polygon-zkevm) - 性能卓越、生产环境验证成熟的扩容方案。
- [ ] [**zkSync Era**](https://zksync.io/) - 基于编译器的方案，支持原生账户抽象（AA）与极高性能。
- [ ] [**Lineas (Consensys)**](https://linea.build/) - 由 MetaMask 团队开发，生态集成深度极高。
- [ ] [**StarkNet (Transpiler-based)**](https://starknet.io/) - 虽然不是原生 EVM，但通过 Warp 转译器实现了极高的吞吐量。

---

## 🛠️ 开发库与硬件加速 (Tools & Acceleration)

- [ ] [**Halo2 (Zcash/PSE)**](https://github.com/zcash/halo2) - 现代电路设计的标准协议栈。
- [ ] [**Plonky2**](https://github.com/mir-protocol/plonky2) - 目前已知生成证明速度最快的零知识证明库之一。
- [ ] [**Awesome-ZKP**](https://github.com/matter-labs/awesome-zero-knowledge-proofs) - 涵盖所有主流协议、论文与工具的动态清单。
- [ ] [**sppark (Hardware Acceleration)**](https://github.com/supranational/sppark) - 利用 GPU 加速椭圆曲线运算的必备底层库。

---

## 🛡️ 安全与审计 (Security)

- [ ] [**zkEVM Circuits Audit Reports**](https://github.com/privacy-scaling-explorations/zkevm-specs) - 学习顶级项目是如何对其电路逻辑进行形式化验证的。
- [ ] [**L2Beat**](https://l2beat.com/) - 实时查看各 zkEVM 的“安全逃生舱”状态与去中心化程度。

---

## 💡 选型建议
1. **追求最高兼容性**：选 **Scroll** 或 **Linea**。
2. **追求极致用户体验（账户抽象）**：选 **zkSync Era**。
3. **追求证明生成速度与低延时**：选 **Polygon zkEVM (Plonky2)**。
4. **大型企业级隐私应用**：研究 **Polygon Zero** 或 **Miden**。
