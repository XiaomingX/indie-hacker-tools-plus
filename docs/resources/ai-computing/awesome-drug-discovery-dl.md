# 深度学习辅助药物发现 (AI for Drug Discovery) 精选 (2026 Checklist)

> [!TIP]
> **Indie Hacker Insight**: 2026 年，药物发现已经从“试错”模式转变为 **"计算先行"**。
> - **生成式化学**：利用 **Generative AI** 直接生成符合特定药理特性的新分子（De novo Design），而非仅仅在现有库中筛选。
> - **端到端预测**：从蛋白质折叠（**AlphaFold**）到分子对接（**DiffDock**）再到 ADMET 特性预测，全流程均有成熟的 AI 模型覆盖。
> - **图神经网络**：**Graph Neural Networks (GNN)** 依然是处理分子拓扑结构的最强工具，掌握 **PyTorch Geometric** 是入行的基本功。

---

## 🏗️ 领域综述与基础 (Foundations & Surveys)

- [ ] [**AI in Drug Discovery (Nature 2023 Review)**](https://www.nature.com/articles/s41573-023-00713-z) - 系统掌握 AI 在靶点识别、筛选与优化中的最新应用。
- [ ] [**Deep Learning for Molecules (2026 Guide)**](https://arxiv.org/abs/2301.00001) - 学习从 SMILES 到 3D 坐标的分子表示学习技术。
- [ ] [**PyTorch Geometric (PyG)**](https://pytorch-geometric.readthedocs.io/) - **[必备]** 处理分子图数据的标准库，内置大量 GNN 算子。

---

## ⚡ 核心模型与算法选型 (Models & Algorithms)

- [ ] [**AlphaFold 3**](https://alphafold.ebi.ac.uk/) - **[2026 推荐]** 革命性的复合物预测模型，支持蛋白、小分子、核酸的联合建模。
- [ ] [**AttentiveFP**](https://github.com/OpenDrugAI/AttentiveFP) - 基于注意力机制的图神经网络，在分子特性预测上表现稳健。
- [ ] [**DeepDTA / GraphDTA**](https://github.com/thinng/GraphDTA) - 经典的药物-靶点亲和力（DTA）预测模型。
- [ ] [**REINVENT**](https://github.com/MolecularAI/Reinvent) - 基于强化学习的分子生成框架，支持多目标优化。

---

## 📂 数据集与基准测试 (Datasets & Benchmarks)

- [ ] [**ChEMBL**](https://www.ebi.ac.uk/chembl/) - 全球最大的生物活性分子数据库，包含数百万分子的实验数据。
- [ ] [**MoleculeNet**](https://moleculenet.org/) - 专门为深度学习设计的分子性质预测基准集。
- [ ] [**ZINC 数据库**](http://zinc.docking.org/) - 提供超过 10 亿个可购买化合物的结构，适合虚拟筛选。

---

## 🛠️ 生产力工具与框架 (Tooling & Frameworks)

- [ ] [**RDKit**](https://www.rdkit.org/) - **[行业标准]** 化学信息学的基石库，用于分子清洗、指纹计算与 2D/3D 渲染。
- [ ] [**DeepChem**](https://deepchem.io/) - 提供一站式的药物研发 AI 工作流，集成了大量预训练模型。
- [ ] [**Transformer4Rec for Chemistry**](https://github.com/NVIDIA-Merlin/Transformers4Rec) - 学习如何将 Transformer 架构应用于分子序列（SMILES）分析。

---

## 💡 选型建议
1. **进行分子性质（如溶解度、毒性）预测**：选 **RDKit** + **AttentiveFP**。
2. **需要生成全新的候选药物分子**：选 **REINVENT** + **DeepChem**。
3. **研究大规模药物-靶点相互作用**：选 **GraphDTA** + **ChEMBL**。
4. **处理复杂的生物大分子复合物**：强制使用 **AlphaFold 3**。
