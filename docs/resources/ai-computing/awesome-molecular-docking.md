# 分子对接 (Molecular Docking) 与 AI 辅助药物研发精选 (2026 Checklist)

> [!TIP]
> **Indie Hacker Insight**: 2026 年，分子对接已从“实验室专供”演变为 **"云端算力竞赛"**。
> - **AI 时代**：**AlphaFold 3** 已经重新定义了多链蛋白与配体的对接精度，传统工具（如 Vina）更多用于初步的大规模筛选。
> - **扩散模型**：**DiffDock** 等基于扩散模型的工具不仅快，而且在处理“柔性配体”时表现惊人。
> - **算力优化**：利用 **GPU 加速的 GROMACS** 进行对接后的分子动力学（MD）验证，是判断结合稳定性的金标准。

---

## 🏗️ 领域核心综述与基准 (Foundations & Benchmarks)

- [ ] [**Diffusion Models in Molecular Docking (2023)**](https://arxiv.org/abs/2210.01776) - 掌握 2026 年最前沿的扩散模型对接原理。
- [ ] [**PDBBind 数据集**](http://www.pdbbind.org.cn/) - **[必备]** 全球最权威的配体-蛋白复合物结构及亲和力数据库。
- [ ] [**CrossDocked2020**](https://github.com/gnina/resources) - 用于训练和测试 AI 对接模型的大规模基准数据集。

---

## 🛠️ 核心对接工具选型 (Docking Tools)

### 1. 经典工具 (Stable & Trusted)
- [ ] [**AutoDock Vina**](https://vina.scripps.edu/) - 免费开源、速度极快，依然是小分子虚拟筛选的首选入门工具。
- [ ] [**HDOCK**](http://hdock.phys.hust.edu.cn/) - 支持蛋白-蛋白对接的在线平台，适合快速验证。
- [ ] [**CLUSPRO**](https://cluspro.org/) - 蛋白-蛋白对接的“行业标杆”，结果聚类非常成熟。

### 2. AI 驱动工具 (State-of-the-Art)
- [ ] [**AlphaFold 3**](https://alphafold.ebi.ac.uk/) - **[2026 巅峰]** 能够同时预测蛋白、核酸、配体和离子的复合物结构。
- [ ] [**DiffDock**](https://github.com/gcorso/DiffDock) - 首个大规模应用的扩散模型对接工具，精度优势显著。
- [ ] [**EquiBind**](https://github.com/HannesStark/EquiBind) - 速度极快（比传统 AI 工具快 10x），适合海量分子筛选。

---

## 🧬 抗体设计与专项工具 (Antibody & Special)

- [ ] [**SAbDab**](https://opig.stats.ox.ac.uk/webapps/newsabdab/sabdab/) - 专门针对抗体-抗原结构的数据库。
- [ ] [**DiffAb**](https://github.com/luost26/diffab) - 基于扩散模型的抗体序列与结构协同设计工具。
- [ ] [**AntibodyX**](https://antibodyx.ai/) - AI 驱动的抗体亲和力成熟与优化平台。

---

## 🚀 分子动力学与验证 (MD & Validation)

- [ ] [**GROMACS**](https://www.gromacs.org/) - 开源、GPU 加速的 MD 模拟利器，用于验证对接结果的动态稳定性。
- [ ] [**OpenMM**](https://openmm.org/) - 灵活性极高，支持 Python 脚本定制复杂的模拟流程。
- [ ] [**MASIF**](https://github.com/LPDI-EPFL/masif) - 通过“相互作用指纹”从几何表面识别蛋白结合位点。

---

## 💡 选型建议
1. **进行常规小分子药物筛选**：选 **AutoDock Vina** + **PDBBind**。
2. **需要极致精度的多链复合物预测**：选 **AlphaFold 3**。
3. **处理大规模柔性分子对接**：选 **DiffDock**。
4. **进行抗体药物设计**：必看 **SAbDab** 并尝试 **DiffAb**。
