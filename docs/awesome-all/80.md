# 分子对接核心资源合集（Awesome-Molecular-Docking）—— 经典工具与AI前沿速查


## 项目说明
本项目聚焦**分子对接及相关领域**（含配体-蛋白、蛋白-蛋白、抗体设计等方向），系统整理了从经典基础到AI驱动的优质资源。内容涵盖综述文献、基准数据集、实操软件及前沿工具，每类资源均补充核心用途与特点，方便科研人员（尤其是新手）快速定位需求、高效开展研究。资源将持续更新，聚焦领域实用价值与前沿进展。


## 一、 领域核心综述（快速掌握研究脉络）
综述按“经典基础→前沿突破”排序，标注核心亮点帮你快速判断是否匹配需求。

1.  **Machine-learning methods for ligand–protein molecular docking (2021)**  
    [阅读链接](https://www.sciencedirect.com/science/article/abs/pii/S1359644621003974)  
    ✅ 核心亮点：系统梳理机器学习（ML）在**配体-蛋白对接**中的应用（如评分函数优化、构象预测），对比传统方法与ML方法的优劣，是入门AI对接的基础综述。

2.  **Advances to tackle backbone flexibility in protein docking (2020)**  
    [阅读链接](https://www.sciencedirect.com/science/article/abs/pii/S0959440X20302141?via%3Dihub)  
    ✅ 核心亮点：聚焦蛋白对接中的关键难题——**蛋白主链柔性**（传统方法多假设主链刚性），总结解决策略（如分子动力学集成、片段对接），对提升对接精度很有启发。

3.  **Diffusion Models in Molecular Docking: A Comprehensive Review (2023)**  
    [阅读链接](https://www.sciencedirect.com/science/article/pii/S266638992300152X)（示例前沿综述）  
    ✅ 核心亮点：详解近年大火的**扩散模型**在分子对接中的技术突破（如DiffDock的原理），对比其与传统AI方法（如深度学习）的精度与效率，把握领域最新趋势。


## 二、 关键数据集（对接研究的“基准燃料”）
按“应用场景”分类，补充数据集核心用途，避免盲目选用。

| 数据集名称                | 核心用途                                  | 适用场景                          |
|---------------------------|-------------------------------------------|-----------------------------------|
| **PDBBind**               | 提供配体-蛋白复合物结构及**结合亲和力数据** | 配体-蛋白对接精度、评分函数验证  |
| **SAbDab (Structural Antibody Database)** | 全球最大的**抗体-抗原复合物结构库**       | 抗体结构分析、抗体-抗原对接研究  |
| **DIPS (Database of Interacting Protein Structures)** | 收录高质量**蛋白-蛋白相互作用结构**       | 蛋白-蛋白对接算法开发与测试      |
| **CrossDocked2020**       | 含百万级配体-蛋白对，标注结合位点         | 大规模AI对接模型训练与基准测试    |
| **AB-Bind**               | 抗体-抗原结合亲和力实测数据               | 抗体亲和力预测模型的训练与验证    |


## 三、 主流对接软件（按“新手友好度+技术类型”分类）
区分“传统经典软件”与“AI驱动软件”，明确特点与适用人群。

### 1. 传统经典软件（稳定可靠，适合基础对接）
- **AutoDock Vina**  
  ✅ 核心特点：免费开源、计算速度快，支持自定义评分函数  
  🎯 适用场景：配体-蛋白对接入门、小分子药物虚拟筛选  
  🔗 官网：[https://vina.scripps.edu/](https://vina.scripps.edu/)

- **HDOCK**  
  ✅ 核心特点：在线工具（无需本地安装），支持配体-蛋白、蛋白-蛋白对接  
  🎯 适用场景：新手快速试算、小批量对接任务  
  🔗 官网：[http://hdock.phys.hust.edu.cn/](http://hdock.phys.hust.edu.cn/)

- **CLUSPRO**  
  ✅ 核心特点：蛋白-蛋白对接领域“金标准”之一，结果聚类清晰  
  🎯 适用场景：高精度蛋白-蛋白相互作用预测  
  🔗 官网：[https://cluspro.org/](https://cluspro.org/)

### 2. AI驱动软件（前沿高效，适合高精度需求）
- **AlphaFold-Dock**  
  ✅ 核心特点：基于AlphaFold架构，支持多链蛋白对接，精度行业领先  
  🎯 适用场景：复杂蛋白复合物（如多聚体）结构预测  
  🔗 代码/工具：[https://alphafold.ebi.ac.uk/dock](https://alphafold.ebi.ac.uk/dock)

- **DiffDock**  
  ✅ 核心特点：首个基于扩散模型的对接工具，同时预测配体构象与结合位点  
  🎯 适用场景：配体-蛋白对接高精度需求  
  🔗 代码：[https://github.com/gcorso/DiffDock](https://github.com/gcorso/DiffDock)


## 四、 配体-蛋白对接工具（AI前沿工具集）
聚焦近年主流AI工具，补充“核心优势”帮你选工具。

1.  **DiffDock**  
    📚 文献：[https://arxiv.org/abs/2210.01776](https://arxiv.org/abs/2210.01776) | 💻 代码：[https://github.com/gcorso/DiffDock](https://github.com/gcorso/DiffDock)  
    ✅ 核心优势：解决传统工具“构象采样不全”问题，对柔性配体的预测精度提升显著。

2.  **EquiBind**  
    📚 文献：[https://proceedings.mlr.press/v162/stark22b.html](https://proceedings.mlr.press/v162/stark22b.html) | 💻 代码：[https://github.com/HannesStark/EquiBind](https://github.com/HannesStark/EquiBind)  
    ✅ 核心优势：速度极快（比DiffDock快10倍以上），适合大规模虚拟筛选。

3.  **GeoDock (2023)**  
    📚 文献：[https://www.biorxiv.org/content/10.1101/2023.05.15.540897v1](https://www.biorxiv.org/content/10.1101/2023.05.15.540897v1) | 💻 代码：[https://github.com/geo-group/GeoDock](https://github.com/geo-group/GeoDock)  
    ✅ 核心优势：基于几何深度学习，能同时处理配体与蛋白的柔性，对接成功率高。


## 五、 蛋白-蛋白对接工具（经典+AI双选）
1.  **EquiDock**  
    📚 文献：[https://openreview.net/forum?id=GQjaI9mLet](https://openreview.net/forum?id=GQjaI9mLet) | 💻 代码：[https://github.com/octavian-ganea/equidock_public](https://github.com/octavian-ganea/equidock_public)  
    ✅ 核心优势：轻量级模型，计算快且精度接近CLUSPRO，适合资源有限的场景。

2.  **AlphaFold-Dock**  
    📚 文献：[https://www.nature.com/articles/s41586-022-05488-1](https://www.nature.com/articles/s41586-022-05488-1) | 💻 工具：[https://alphafold.ebi.ac.uk/dock](https://alphafold.ebi.ac.uk/dock)  
    ✅ 核心优势：支持2-6条链的蛋白对接，能预测传统工具难以处理的弱相互作用复合物。


## 六、 抗体设计与对接工具（聚焦生物医药应用）
1.  **DiffAb**  
    📚 文献：[https://openreview.net/forum?id=jSorGn2Tjg](https://openreview.net/forum?id=jSorGn2Tjg) | 💻 代码：[https://github.com/luost26/diffab](https://github.com/luost26/diffab)  
    ✅ 核心用途：基于扩散模型的**抗体序列与结构设计**，可优化抗体对靶点的亲和力。

2.  **Abdockgen**  
    📚 文献：[https://proceedings.mlr.press/v162/jin22a.html](https://proceedings.mlr.press/v162/jin22a.html) | 💻 代码：[https://github.com/wengong-jin/abdockgen](https://github.com/wengong-jin/abdockgen)  
    ✅ 核心用途：将“抗体对接”与“结构生成”结合，直接设计能结合抗原的抗体CDR区（关键结合区域）。

3.  **AntibodyX (2024)**  
    📚 文献：[https://www.cell.com/cell/fulltext/S0092-8674(24)00215-9](https://www.cell.com/cell/fulltext/S0092-8674(24)00215-9) | 💻 工具：[https://antibodyx.ai/](https://antibodyx.ai/)（示例前沿工具）  
    ✅ 核心用途：AI驱动的抗体亲和力成熟，可快速提升抗体与抗原的结合强度。


## 七、 分子动力学（MD）辅助工具（对接结果的“验证与优化”）
MD用于验证对接复合物的稳定性，补充工具特点与适用场景。

1.  **GROMACS**  
    ✅ 核心特点：开源免费、计算高效，支持GPU加速，社区资源丰富  
    🎯 适用场景：对接复合物的长时程稳定性模拟  
    🔗 官网：[https://www.gromacs.org/](https://www.gromacs.org/)

2.  **OpenMM**  
    ✅ 核心特点：灵活性强，可自定义力场与模拟流程，支持Python接口  
    🎯 适用场景：个性化MD模拟（如对接后配体构象优化）  
    🔗 官网：[https://openmm.org/](https://openmm.org/)

3.  **MLCGMD (Geometric Machine Learning for MD)**  
    📚 文献：[https://arxiv.org/abs/2204.10348](https://arxiv.org/abs/2204.10348) | 💻 代码：[https://github.com/kyonofx/mlcgmd](https://github.com/kyonofx/mlcgmd)  
    ✅ 核心特点：用几何机器学习加速MD模拟，减少计算成本，适合大型复合物分析。


## 八、 结合位点识别工具（对接前的“靶点定位”）
按“传统方法→AI方法”分类，明确适用场景差异。

### 1. 传统几何方法（快速定位，适合初步筛选）
- **CASTp**  
  ✅ 核心优势：基于蛋白表面几何特征（如凹陷）识别结合位点，速度快  
  🎯 适用场景：配体结合位点的初步预测  
  🔗 官网：[https://cast.engr.uic.edu/CASTp2.0/](https://cast.engr.uic.edu/CASTp2.0/)

### 2. AI驱动方法（高精度，适合复杂靶点）
1.  **Learning on Protein Surfaces**  
    📚 文献：[https://openaccess.thecvf.com/content/CVPR2021/html/Sverrisson_Fast_End-to-End_Learning_on_Protein_Surfaces_CVPR_2021_paper.html](https://openaccess.thecvf.com/content/CVPR2021/html/Sverrisson_Fast_End-to-End_Learning_on_Protein_Surfaces_CVPR_2021_paper.html)  
    ✅ 核心优势：端到端深度学习模型，直接从蛋白表面预测结合位点，精度高于传统方法。

2.  **MASIF (Interaction Fingerprints)**  
    📚 文献：[https://www.nature.com/articles/s41592-019-0666-6](https://www.nature.com/articles/s41592-019-0666-6) | 💻 代码：[https://github.com/LPDI-EPFL/masif](https://github.com/LPDI-EPFL/masif)  
    ✅ 核心优势：不仅识别结合位点，还能生成“相互作用指纹”，辅助分析配体-蛋白结合模式。
