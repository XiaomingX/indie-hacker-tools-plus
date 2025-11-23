# Awesome-Mamba-Papers：Mamba与状态空间模型（SSM）核心论文与学习指南
本合集聚焦 **2023年底至2024年中** 最具影响力的Mamba与SSM相关研究，剔除重复及小众内容，按「理论演进→模型核心→应用场景」梳理。每篇论文均补充「核心突破」「解决的痛点」和「实用价值」，并新增「关键概念速查」，帮新手快速入门、研究者精准定位重点。


## 一、关键概念速查（先懂基础，再看论文）
在看论文前，先理清SSM与Mamba的核心术语，避免理解障碍：
- **状态空间模型（SSM）**：一种通过「状态向量」捕捉序列历史信息的模型，核心是「状态转移方程」，相比RNN能更高效建模长序列，时间复杂度多为 **O(n)**（n为序列长度）。
- **选择性状态空间（Selective SSM）**：Mamba的核心创新，能根据输入内容「动态筛选重要信息」（类似人类阅读时的注意力），过滤冗余数据，兼顾效率与表达力。
- **HiPPO（最优多项式投影）**：SSM的关键记忆机制，解决传统RNN「记不住远期信息」的问题，让模型能高效保留长序列中的早期关键特征。
- **混合专家（MoE）**：将模型拆分为多个「小专家模块」，输入仅激活少数相关专家，在不提升计算成本的前提下扩大模型容量。
- **长程依赖**：序列数据中「早期元素对后期结果的影响」（如文本中前文的代词指代、时间序列中上月销量对下月的影响），是SSM/Mamba的核心优势场景。


## 二、基础理论与SSM演进（Mamba的「前身」与理论根基）
这部分论文是Mamba的技术铺垫，解决了「SSM如何高效建模长序列」「如何适配语言任务」等核心问题。

| 论文标题 | 链接 | 核心突破 | 关键价值 |
|----------|------|----------|----------|
| **HiPPO: Recurrent Memory with Optimal Polynomial Projections** | [Paper](https://arxiv.org/abs/2008.07669) <br> [Code](https://github.com/HazyResearch/hippo-code) | 提出「最优多项式投影」记忆机制，首次让模型用低复杂度（O(n)）记住长序列的远期信息。 | 打破传统RNN的「短期记忆瓶颈」，为后续S4、Mamba等结构化SSM奠定理论基础。 |
| **S4: Efficiently Modeling Long Sequences with Structured State Spaces** | [Paper](https://arxiv.org/abs/2111.00396v3) <br> [Code](https://github.com/state-spaces/s4) | 将SSM参数「结构化」（如使用对角矩阵），实现「线性时间推理+线性空间存储」，解决了早期SSM计算复杂的问题。 | 首次证明SSM能在长序列任务（如文本生成、语音识别）上比肩Transformer，且效率更高。 |
| **H3: Toward Language Modeling with State Space Models** | [Paper](https://arxiv.org/abs/2212.14052) <br> [Code](https://github.com/HazyResearch/H3) | 优化SSM的「语言适配性」：引入分层结构、残差连接，让SSM能处理10万+长度的文本序列。 | 推动SSM从「通用长序列建模」走向「专属语言任务」，是Mamba语言能力的直接前身。 |
| **Transformers are SSMs: Generalized Models and Efficient Algorithms** | [Paper](https://arxiv.org/abs/2405.21060) <br> [Code](https://github.com/state-spaces/mamba) | 从数学上证明「Transformer可被视为一种特殊的SSM」，提出两者的统一框架。 | 打破「Transformer与SSM对立」的认知，为后续跨架构融合（如Samba）提供理论依据。 |


## 三、Mamba核心与变种模型（从基础到优化的演进路线）
这部分是Mamba的核心研究，包括原始模型及针对「效率、任务适配、输入形式」的改进变种。

| 论文标题 | 链接 | 核心突破 | 关键价值 |
|----------|------|----------|----------|
| **Mamba: Linear-Time Sequence Modeling with Selective State Spaces** | [Paper](https://arxiv.org/abs/2312.00752) <br> [Code](https://github.com/state-spaces/mamba) | 1. 提出「选择性状态空间」：根据输入动态调整状态更新（只保留重要信息）；<br>2. 简化SSM结构，推理速度比Transformer快5倍+。 | SSM领域的「里程碑模型」，首次实现「长序列建模+高速度+强性能」三者平衡，引爆SSM研究热潮。 |
| **MoE-Mamba: Efficient Selective State Space Models with Mixture of Experts** | [Paper](https://arxiv.org/abs/2401.04081) | 将「混合专家（MoE）」与Mamba结合，仅激活10%的专家模块处理输入。 | 解决「大模型计算成本高」的问题，在保持Mamba性能的同时，计算量降低90%，适配超大规模任务。 |
| **BlackMamba: Mixture of Experts for State-Space Models** | [Paper](https://arxiv.org/abs/2402.01771) <br> [Code](https://github.com/Zyphra/BlackMamba) | 优化MoE-Mamba的「专家调度机制」：让专家更专注于特定输入类型（如文本中的名词、动词）。 | 进一步提升MoE-Mamba的精度，在语言理解任务（如GLUE基准）上超越原始Mamba 3%-5%。 |
| **MambaByte: Token-free Selective State Space Model** | [Paper](https://arxiv.org/abs/2401.13660) <br> [Code](https://github.com/lucidrains/MEGABYTE-pytorch) | 提出「无Token化建模」：直接处理原始字节（如UTF-8编码），无需先做Token分割。 | 解决传统NLP模型「Tokenizer依赖」的问题，适配小语种、代码等Tokenizer效果差的场景。 |


## 四、核心应用场景（SSM/Mamba落地的实战价值）
这部分论文展示了Mamba/SSM在各领域的落地能力，解决了传统模型（CNN/Transformer/RNN）的场景痛点。

### 1. 语言与序列建模（长文本、专业序列）
| 论文标题 | 链接 | 核心突破 | 应用价值 |
|----------|------|----------|----------|
| **Caduceus: Bi-Directional Equivariant Long-Range DNA Sequence Modeling** | [Paper](https://arxiv.org/abs/2403.03234) <br> [Code](https://github.com/wangtz19/NetMamba) | 用双向SSM建模DNA长序列（可达百万碱基对），引入「等变机制」适配基因序列的结构特性。 | 比传统基因模型（如CNN、Transformer）更精准预测基因功能，加速生物信息学研究。 |
| **Samba: Simple Hybrid State Space Models for Unlimited Context Language Modeling** | [Paper](https://arxiv.org/abs/2406.07522) | 融合SSM与Transformer的优势：用SSM处理长序列（O(n)），用Transformer捕捉局部依赖。 | 首次实现「无限上下文长度」的语言建模，在100万Token的长文本摘要任务上表现最优。 |

### 2. 视觉建模（图像分类、修复、遥感）
视觉任务的核心痛点是「局部细节与全局语义的平衡」，SSM的长程建模能力恰好适配。

| 论文标题 | 链接 | 核心突破 | 应用价值 |
|----------|------|----------|----------|
| **Vision Mamba: Efficient Visual Representation Learning with Bidirectional State Space Model** | [Paper](https://arxiv.org/abs/2401.09417) <br> [Code](https://github.com/hustvl/Vim) | 将图像拆分为「补丁序列」，用双向SSM建模补丁间的长程关系，替代Transformer的自注意力。 | 在ImageNet分类任务上精度比肩ViT，推理速度快2倍，适配移动端等低算力场景。 |
| **MambaIR: A Simple Baseline for Image Restoration with State-Space Model** | [Paper](https://arxiv.org/abs/2402.15648) <br> [Code](https://github.com/csguoh/MambaIR) | 用SSM替换图像修复模型中的CNN骨干，增强对「破损区域与完整区域的长程关联」捕捉。 | 修复模糊、噪声图像的效果超越传统CNN模型，且模型体积缩小30%。 |
| **RSMamba: Remote Sensing Image Classification with State Space Model** | [Paper](https://arxiv.org/abs/2403.19654) <br> [Code](https://github.com/KyanChen/RSMamba) | 针对遥感图像「尺度大、目标分散」的特点，优化SSM的感受野，适配多分辨率图像。 | 遥感图像分类精度提升4%-6%，可用于农业监测、灾害评估等实际场景。 |

### 3. 医学影像（分割、病灶检测）
医学影像对「长程依赖」要求极高（如肿瘤与血管的关联），Mamba的优势显著。

| 论文标题 | 链接 | 核心突破 | 应用价值 |
|----------|------|----------|----------|
| **U-Mamba: Enhancing Long-range Dependency for Biomedical Image Segmentation** | [Paper](https://arxiv.org/abs/2401.04722) <br> [Code](https://github.com/bowang-lab/U-Mamba) | 将Mamba融入UNet架构（医学分割的经典模型），增强对病灶与周围组织的长程关联建模。 | 在肺结节、肝脏肿瘤分割任务上Dice系数提升3%-5%，辅助医生更精准定位病灶。 |
| **LightM-UNet: Mamba Assists in Lightweight UNet for Medical Image Segmentation** | [Paper](https://arxiv.org/abs/2403.05246) <br> [Code](https://github.com/MrBlankness/LightM-UNet) | 用轻量化Mamba模块替代UNet中的部分CNN层，在降低模型体积60%的同时保持精度。 | 适配超声、X光等移动设备采集的影像，可用于基层医院的快速诊断。 |
| **ProMamba: Prompt-Mamba for Polyp Segmentation** | [Paper](https://arxiv.org/abs/2403.13660) | 结合「提示学习（Prompt）」与Mamba，让模型仅用少量标注数据就能精准分割肠道息肉。 | 解决医学数据「标注成本高」的痛点，加速模型在小众疾病场景的落地。 |

### 4. 时间序列预测（长程、多变量）
时间序列的核心需求是「精准预测远期趋势」，SSM的线性复杂度适配性极强。

| 论文标题 | 链接 | 核心突破 | 应用价值 |
|----------|------|----------|----------|
| **TimeMachine: A Time Series is Worth 4 Mambas for Long-term Forecasting** | [Paper](https://arxiv.org/abs/2403.09898) <br> [Code](https://github.com/Atik-Ahamed/TimeMachine) | 设计4个并行Mamba模块，分别处理时间序列的「趋势、周期、噪声、异常」4类特征。 | 在电力负荷、股票价格等长程预测任务上，精度超越Transformer类模型15%+。 |
| **Chimera: Modeling Multivariate Time Series with 2-Dimensional State Space Models** | [Paper](https://arxiv.org/abs/2406.04320) | 提出2D-SSM：同时建模「时间维度的长程依赖」和「变量维度的关联（如温度与湿度）」。 | 解决多变量时间序列（如气象、工业传感器数据）的耦合建模问题，预测误差降低20%。 |

### 5. 推荐系统（序列行为建模）
推荐系统需要捕捉「用户长期行为偏好」，Mamba比RNN/Transformer更高效。

| 论文标题 | 链接 | 核心突破 | 应用价值 |
|----------|------|----------|----------|
| **Mamba4Rec: Towards Efficient Sequential Recommendation** | [Paper](https://arxiv.org/abs/2403.03900) <br> [Code](https://github.com/chengkai-liu/Mamba4Rec) | 用Mamba替代推荐系统中的GRU/Transformer，建模用户的长期点击序列（1000+行为）。 | 推荐准确率提升8%，推理速度比Transformer快3倍，适配电商平台的实时推荐场景。 |


## 五、优质学习资源（从入门到深入）
| 资源名称 | 链接 | 资源类型 | 适合人群 | 核心价值 |
|----------|------|----------|----------|----------|
| Mamba_State_Space_Model_Paper_List | [GitHub](https://github.com/Event-AHU/Mamba_State_Space_Model_Paper_List) | 论文合集 | 研究者 | 按「理论-模型-应用」分类，更新至2024年中，含中文摘要，适合系统性梳理文献。 |
| Awesome-state-space-models | [GitHub](https://github.com/radarFudan/Awesome-state-space-models) | 综合资源库 | 开发者+研究者 | 包含论文、代码、教程、基准测试，甚至有SSM与Transformer的对比实验数据。 |
| A Visual Guide to Mamba and State Space Models | [Blog](https://www.maartengrootendorst.com/blog/mamba/) | 可视化教程 | 新手入门 | 用动画和简化公式解释Mamba的「选择性状态更新」机制，避免复杂数学推导，入门友好。 |
| Mamba Official Codebase | [GitHub](https://github.com/state-spaces/mamba) | 官方代码 | 开发者 | 原始Mamba模型的PyTorch实现，含训练/推理脚本，可直接复现论文实验，学习工程细节。 |
