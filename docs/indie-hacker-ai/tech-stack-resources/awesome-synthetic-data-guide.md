# awesome-synthetic-data（合成数据入门指南与实用资源大全）
## 什么是合成数据？
合成数据是通过算法、模型或仿真生成的**非真实但具备真实数据特征与统计规律**的数据，其核心价值在于：解决隐私敏感场景（如医疗、金融）的数据合规问题、弥补真实数据稀缺性（如罕见病病例、边缘场景自动驾驶数据）、快速扩充训练数据以提升AI模型泛化能力。它已成为AI开发、数据安全与业务仿真领域的关键支撑。


## 一、入门与教程（从基础到实战）
### 1. 博客与文章
- **[RNN 的惊人有效性](http://karpathy.github.io/2015/05/21/rnn-effectiveness/)** - Andrej Karpathy（OpenAI前AI主管）的经典入门文。  
  ✅ 核心内容：用通俗语言解释RNN的“序列记忆”本质，搭配字符生成、翻译等实例，是理解**时序合成数据基础原理**的入门必读。  
  ⚠️ 说明：虽发布于2015年，但RNN是后续时序生成模型（如Temporal GAN）的基础，仍具学习价值。

- **[Annotated Diffusion](https://huggingface.co/blog/annotated-diffusion)** - Hugging Face官方教程（附完整代码）。  
  ✅ 核心内容：逐行拆解Diffusion（扩散）模型原论文，从“加噪-去噪”原理到PyTorch实现，手把手教你理解**当前最主流的高保真合成数据模型**。  
  ✅ 额外价值：配套Colab代码可直接运行，适合零基础动手实践。

- **[合成数据：从原理到企业级应用](https://www.gretel.ai/blog/synthetic-data-principles-to-enterprise)** - Gretel AI官方指南。  
  ✅ 核心内容：结合金融、医疗案例，讲解合成数据的“隐私性验证”“真实性评估”方法，以及如何落地到企业业务中，适合想了解实际应用的开发者。


### 2. 视频与课程
- **[生成数据：通过估计数据分布的梯度学习](https://youtu.be/nv-WTeKRLl0)** - 斯坦福大学Yang Song（扩散模型核心研究者）主讲。  
  ✅ 核心内容：从数学原理到工程实践，覆盖“分数匹配”“扩散模型训练技巧”，以及在图像、文本合成中的应用，适合想深入理论的学习者。

- **[Hugging Face 合成数据实战课](https://huggingface.co/learn/course/en/chapter9)** - 免费官方实操课程。  
  ✅ 核心内容：用`diffusers`库生成图像、`gretel-synthetics`生成表格数据，配套数据集和代码，1小时就能上手生成第一份合成数据。

- **[Deep Learning for Generative Models](https://www.coursera.org/specializations/generative-ai)** - Coursera深度学习专项课（Andrew Ng参与打造）。  
  ✅ 核心内容：系统覆盖GAN、Diffusion、Transformer生成模型，含时序、图像合成实战，适合构建完整知识体系。


## 二、开源库（按数据类型分类，附实用场景）
### 1. 文本、表格与时间序列数据（企业最常用）
| 开源库 | 核心功能 | 适用场景 |
|--------|----------|----------|
| **[gretel-synthetics](https://github.com/gretelai/gretel-synthetics)** | 支持结构化表格、非结构化文本（如客服对话）、多变量时序（如传感器数据）；内置差分隐私算法，可通过隐私审计。 | 金融交易记录生成、医疗病历脱敏、IoT传感器数据扩充 |
| **[SDV](https://github.com/sdv-dev/SDV)** | 专攻**关系型数据**（如“用户表+订单表”联动生成）；支持时序数据缺失值填充与生成；自带数据真实性评估工具。 | 电商平台仿真数据、企业CRM数据补全、数据库测试数据生成 |
| **[ydata-synthetic](https://github.com/ydataai/ydata-synthetic)** | 集成GAN、VAE、Diffusion多种模型；对小数据集适配性强；支持生成后的数据质量可视化。 | 小样本行业数据生成（如制造业故障记录）、表格数据 anonymization |
| **[Temporal Fusion Transformers](https://github.com/google-research/google-research/tree/master/tft)** | Google提出的时序生成模型；擅长长周期、多特征时序数据（如股价、电力负荷）。 | 能源消耗预测数据生成、金融时序训练数据扩充 |


### 2. 图像（高保真生成首选）
- **[StyleGAN-T](https://github.com/NVlabs/stylegan3)** - NVLabs 2023年升级版本（替代原StyleGAN3）。  
  ✅ 核心功能：生成超高清（1024x1024）人脸、物体图像；支持“风格迁移”（如将猫的纹理迁移到狗图像）；解决了原版本的“姿态扭曲”问题。  
  ✅ 适用场景：自动驾驶视觉训练数据（如特殊天气下的道路图像）、游戏角色素材生成。

- **[Denoising Diffusion Pytorch](https://github.com/lucidrains/denoising-diffusion-pytorch)** - 轻量型扩散模型实现。  
  ✅ 核心功能：代码简洁易改，支持自定义图像尺寸与生成速度；可快速适配医学影像（如CT图）、卫星图像生成。  
  ✅ 优势：比Stable Diffusion更适合二次开发。

- **[Hugging Face Diffusers](https://github.com/huggingface/diffusers)** - 工业级扩散模型库。  
  ✅ 核心功能：集成Stable Diffusion、ControlNet等主流模型；支持“文本生成图像”“图像修复”“条件生成”（如指定物体位置）。  
  ✅ 适用场景：AI绘画、产品设计草图生成、数据集增强（如给原始图像加不同背景）。


### 3. 音频（音乐、语音生成）
- **[Jukebox](https://github.com/openai/jukebox/)** - OpenAI音乐生成经典模型。  
  ⚠️ 说明：2020年发布，支持生成多风格音乐，但生成速度较慢（1分钟音乐需数小时）。  
  ✅ 替代推荐：**[MusicGen](https://github.com/facebookresearch/audiocraft)**（Meta 2023年发布）  
  - 核心功能：文本描述生成音乐（如“欢快的钢琴独奏”）；支持15分钟长音频生成，速度比Jukebox快10倍。  
  - 适用场景：短视频背景音乐生成、游戏音效素材库构建。

- **[VITS](https://github.com/jaywalnut310/vits)** - 语音合成开源库。  
  ✅ 核心功能：生成自然度接近真人的语音；支持多语言（中、英、日）；可自定义说话人音色。  
  ✅ 适用场景：智能客服语音样本生成、有声书配音素材扩充。


### 4. 仿真（物理场景合成数据）
- **[AirSim](https://microsoft.github.io/AirSim/)** - 微软开源仿真工具。  
  ✅ 核心功能：搭建虚拟无人机、自动驾驶汽车场景；可生成带标注的图像（如目标检测框、深度图）、传感器数据（如LiDAR点云）。  
  ✅ 适用场景：无人机避障算法训练、自动驾驶低光/雨天场景数据生成。

- **[Unity Perception](https://github.com/Unity-Technologies/com.unity.perception)** - Unity引擎感知仿真工具包。  
  ✅ 核心功能：快速构建3D虚拟环境；自动生成目标检测、语义分割标注数据；支持与AI模型实时联动。  
  ✅ 适用场景：机器人视觉训练、工业质检场景仿真。

- **[NVIDIA Isaac Sim](https://developer.nvidia.com/isaac-sim)** - 高端机器人仿真平台。  
  ✅ 核心功能：基于物理引擎的高精度仿真；支持生成逼真的机器人关节数据、环境交互数据；适配NVIDIA GPU加速。  
  ✅ 适用场景：工业机器人操作训练、服务机器人场景适应性数据生成。


## 三、数据集资源（找真实数据练手，或直接用合成数据）
| 平台 | 平台特色 | 适用场景 |
|------|----------|----------|
| **[HuggingFace Datasets](https://huggingface.co/docs/datasets/index)** | 1. 支持文本、图像、音频等多类型数据；2. 可直接与PyTorch/TensorFlow联动，无需本地下载；3. 含大量开源合成数据集（如`gretelai/synthetic_finance`）。 | AI模型快速训练、合成数据与真实数据对比实验 |
| **[Kaggle Datasets](https://www.kaggle.com/datasets)** | 1. 含大量行业真实数据集（如医疗影像、金融交易）；2. 配套数据预处理教程与竞赛；3. 合成数据专题区（搜索“Synthetic Data”）。 | 数据科学入门练手、合成数据生成效果评估 |
| **[Papers with Code - Datasets](https://paperswithcode.com/datasets)** | 1. 按论文主题分类数据集（如“GAN生成图像”“Diffusion生成文本”）；2. 可直接查看数据集对应的SOTA模型与代码。 | 学术研究复现、跟踪合成数据领域最新数据标准 |
| **[Synthea](https://synthea.mitre.org/)** | 专注医疗领域的合成数据集平台。生成带完整病史的虚拟患者数据（如门诊记录、化验结果），符合HIPAA隐私规范。 | 医疗AI模型开发（如疾病预测）、医院流程仿真 |


## 四、学术论文（核心理论与里程碑进展）
### 1. 生成对抗网络（GANs，合成数据奠基技术）
- **[生成对抗网络](https://arxiv.org/abs/1406.2661)** - Ian Goodfellow（GAN之父）2014年经典论文。  
  ✅ 核心贡献：提出“生成器-判别器”对抗训练框架，开创了无监督生成数据的先河，是所有GAN变体的基础。

- **[条件生成对抗网络（cGAN）](https://arxiv.org/abs/1411.1784)** - Mehdi Mirza 2014年论文。  
  ✅ 核心贡献：给GAN增加“条件控制”（如指定生成“猫”或“狗”），让合成数据从“随机生成”升级为“定向生成”，奠定了实用化基础。

- **[Wasserstein GAN（WGAN）](https://arxiv.org/abs/1701.07875)** - 2017年突破型论文。  
  ✅ 核心贡献：解决了传统GAN“训练不稳定、生成数据质量波动大”的痛点，通过“Wasserstein距离”优化损失函数，让GAN更易训练。

- **[StyleGAN3](https://arxiv.org/abs/2106.12423)** - NVLabs 2021年论文。  
  ✅ 核心贡献：提出“平移不变性”改进，解决了此前GAN生成图像的“伪影扭曲”问题，让超高清图像生成成为可能。


### 2. Diffusion模型（当前主流高保真生成技术）
- **[通过估计数据分布的梯度进行生成建模](https://yang-song.github.io/blog/2021/score/)** - Yang Song 2021年综述论文。  
  ✅ 核心贡献：系统阐述“分数匹配”与“扩散过程”的关联，为Diffusion模型的理论落地提供了清晰框架。

- **[Stable Diffusion](https://arxiv.org/abs/2112.10752)** - Stability AI 2022年里程碑论文。  
  ✅ 核心贡献：通过“潜空间扩散”大幅降低计算成本，让Diffusion模型能在普通GPU上运行，推动了图像合成的工业化应用。

- **[Audio Diffusion](https://arxiv.org/abs/2208.05514)** - 2022年音频合成论文。  
  ✅ 核心贡献：将Diffusion模型从图像扩展到音频领域，实现了“文本/频谱图→音乐/语音”的高保真生成，是音频合成的主流方向之一。
