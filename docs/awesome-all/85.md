# Awesome LLM (大型语言模型)

🔥 大型语言模型（LLM）已经席卷了 **全球**，不再局限于 NLP 或 AI 社区。这里整理了一些关于大型语言模型，特别是与 ChatGPT 相关的研究论文，涵盖了 LLM 训练框架、部署工具、课程与教程，以及所有公开的 LLM 检查点和 API。

## 热门 LLM 项目

- [Deep-Live-Cam](https://github.com/hacksider/Deep-Live-Cam) - 只需一张图片即可实现实时换脸和一键视频深度伪造（未经过滤）。
- [MiniCPM-V 2.6](https://github.com/OpenBMB/MiniCPM-V) - 一款可以在手机上使用的 GPT-4V 级别的 MLLM，支持单图、多图和视频处理。
- [GPT-SoVITS](https://github.com/RVC-Boss/GPT-SoVITS) - 只需 1 分钟的语音数据，就能训练出优秀的语音合成模型！（少样本语音克隆）。


## 重要论文里程碑

|   日期   |      关键词      |     机构     |                                                                                              论文                                                                                             |
|:--------:|:----------------:|:------------:|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 2017-06  |     Transformers     |    Google    | [Attention Is All You Need](https://arxiv.org/pdf/1706.03762.pdf)                                                                                                                           |
| 2018-06  |       GPT 1.0        |    OpenAI    | [Improving Language Understanding by Generative Pre-Training](https://www.cs.ubc.ca/~amuham01/LING530/papers/radford2018improving.pdf)                                                           |
| 2018-10  |         BERT         |    Google    | [BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding](https://aclanthology.org/N19-1423.pdf)                                                                     |
| 2019-02  |        GPT 2.0       |    OpenAI    | [Language Models are Unsupervised Multitask Learners](https://d4mucfpksywv.cloudfront.net/better-language-models/language_models_are_unsupervised_multitask_learners.pdf)                   |
| 2019-09  |     Megatron-LM      |    NVIDIA    | [Megatron-LM: Training Multi-Billion Parameter Language Models Using Model Parallelism](https://arxiv.org/pdf/1909.08053.pdf)                                                                    |
| 2019-10  |         T5           |    Google    | [Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer](https://jmlr.org/papers/v21/20-074.html)                                                                  |
| 2020-01  |    Scaling Law       |    OpenAI    | [Scaling Laws for Neural Language Models](https://arxiv.org/pdf/2001.08361.pdf)                                                                                                                |
| 2020-05  |        GPT 3.0       |    OpenAI    | [Language models are few-shot learners](https://papers.nips.cc/paper/2020/file/1457c0d6bfcb4967418bfb8ac142f64a-Paper.pdf)                                                                  |
| 2021-01  |  Switch Transformers |    Google    | [Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity](https://arxiv.org/pdf/2101.03961.pdf)                                                           |
| 2021-08  |         Codex        |    OpenAI    | [Evaluating Large Language Models Trained on Code](https://arxiv.org/pdf/2107.03374.pdf)                                                                                                        |
| 2021-08  |   Foundation Models  |   Stanford   | [On the Opportunities and Risks of Foundation Models](https://arxiv.org/pdf/2108.07258.pdf)                                                                                                   |
| 2021-09  |         FLAN         |    Google    | [Finetuned Language Models are Zero-Shot Learners](https://openreview.net/forum?id=gEZrGCozdqR)                                                                                                 |
| 2021-10  |          T0          | HuggingFace  | [Multitask Prompted Training Enables Zero-Shot Task Generalization](https://arxiv.org/abs/2110.08207)                                                                                           |
| 2021-12  |         GLaM         |    Google    | [GLaM: Efficient Scaling of Language Models with Mixture-of-Experts](https://arxiv.org/pdf/2112.06905.pdf)                                                                                      |
| 2022-01  |          COT         |    Google    | [Chain-of-Thought Prompting Elicits Reasoning in Large Language Models](https://arxiv.org/pdf/2201.11903.pdf)                                                                                   |
| 2022-01  |         LaMDA        |    Google    | [LaMDA: Language Models for Dialog Applications](https://arxiv.org/pdf/2201.08239.pdf)                                                                                                          |
| 2022-04  |         PaLM         |    Google    | [PaLM: Scaling Language Modeling with Pathways](https://arxiv.org/pdf/2204.02311.pdf)                                                                                                           |
| 2022-05  |          OPT         |     Meta     | [OPT: Open Pre-trained Transformer Language Models](https://arxiv.org/pdf/2205.01068.pdf)                                                                                                       |
| 2022-06  |  Emergent Abilities  |    Google    | [Emergent Abilities of Large Language Models](https://openreview.net/pdf?id=yzkSU5zdwD)                                                                                                         |
| 2022-10  |     Flan-T5/PaLM     |    Google    | [Scaling Instruction-Finetuned Language Models](https://arxiv.org/pdf/2210.11416.pdf)                                                                                                          |
| 2022-11  |         BLOOM        | BigScience   | [BLOOM: A 176B-Parameter Open-Access Multilingual Language Model](https://arxiv.org/pdf/2211.05100.pdf)                                                                                         |
| 2022-12  |        OPT-IML       |     Meta     | [OPT-IML: Scaling Language Model Instruction Meta Learning through the Lens of Generalization](https://arxiv.org/pdf/2212.12017)                                                                |
| 2023-01  | Flan 2022 Collection |    Google    | [The Flan Collection: Designing Data and Methods for Effective Instruction Tuning](https://arxiv.org/pdf/2301.13688.pdf)                                                                       |
| 2023-02  |         LLaMA        |     Meta     | [LLaMA: Open and Efficient Foundation Language Models](https://research.facebook.com/publications/llama-open-and-efficient-foundation-language-models/)                                       |
| 2023-03  |        PaLM-E        |    Google    | [PaLM-E: An Embodied Multimodal Language Model](https://palm-e.github.io)                                                                                                                       |
| 2023-03  |         GPT 4        |    OpenAI    | [GPT-4 Technical Report](https://openai.com/research/gpt-4)                                                                                                                                     |
| 2023-05  |       PaLM 2         |    Google    | [PaLM 2 Technical Report](https://ai.google/static/documents/palm2techreport.pdf)                                                                                                              |
| 2023-07  |        LLaMA2        |     Meta     | [Llama 2: Open Foundation and Fine-Tuned Chat Models](https://arxiv.org/pdf/2307.09288.pdf)                                                                                                      |
| 2023-12  |         Mamba        | CMU&Princeton | [Mamba: Linear-Time Sequence Modeling with Selective State Spaces](https://arxiv.org/pdf/2312.00752)                                                                                            |
| 2024-01  |         DeepSeek-v2   |    DeepSeek  | [DeepSeek-V2: A Strong, Economical, and Efficient Mixture-of-Experts Language Model](https://arxiv.org/abs/2405.04434)                                                                           |
| 2024-05  |         Mamba2       | CMU&Princeton | [Transformers are SSMs: Generalized Models and Efficient Algorithms Through Structured State Space Duality](https://arxiv.org/abs/2405.21060)                                                      |

## 其他相关论文
如果你对大语言模型（LLM）领域感兴趣，可以参考上面列出的里程碑论文，帮助你了解其发展历程和前沿动态。然而，每个方向的LLM都有其独特的见解和贡献，这些对全面理解该领域至关重要。以下是一些子领域的详细论文列表，供你参考：

- [LLM幻觉论文汇总](https://github.com/LuckyyySTA/Awesome-LLM-hallucination) - 收集关于LLM幻觉的相关论文。
- [LLM幻觉检测论文汇总](https://github.com/EdinburghNLP/awesome-hallucination-detection) - 收集LLM幻觉检测的相关研究论文。
- [LLM实用指南](https://github.com/Mooler0410/LLMsPracticalGuide) - 精选的LLM实用资源列表。
- [ChatGPT提示语合集](https://github.com/f/awesome-chatgpt-prompts) - 收集用于ChatGPT模型的提示语示例。
- [中文ChatGPT提示语合集](https://github.com/PlexPt/awesome-chatgpt-prompts-zh) - 适用于ChatGPT的中文提示语示例。
- [ChatGPT资源合集](https://github.com/humanloop/awesome-chatgpt) - 收集有关ChatGPT和GPT-3的资源。
- [思维链（Chain-of-Thought）论文汇总](https://github.com/Timothyxxx/Chain-of-ThoughtsPapers) - 涵盖“思维链提示引发LLM推理”相关研究。
- [深度推理提示语合集](https://github.com/logikon-ai/awesome-deliberative-prompting) - 介绍如何使用提示语引导LLM进行可靠推理和决策。
- [指令调优论文合集](https://github.com/SinclairCoder/Instruction-Tuning-Papers) - 包含“自然指令”（ACL 2022）、“FLAN”（ICLR 2022）和“T0”（ICLR 2022）等指令调优相关论文。
- [LLM阅读清单](https://github.com/crazyofapple/Reading_groups/) - 大语言模型相关论文和资源汇总。
- [语言模型推理研究](https://github.com/atfortes/LM-Reasoning-Papers) - 语言模型推理相关的论文和资源合集。
- [思维链推理平台](https://github.com/FranxYao/chain-of-thought-hub) - 衡量LLM推理性能的相关资源。
- [GPT资源合集](https://github.com/formulahendry/awesome-gpt) - 与GPT、ChatGPT、OpenAI、LLM相关的优质项目和资源。
- [GPT-3资源合集](https://github.com/elyase/awesome-gpt3) - 收集关于OpenAI GPT-3 API的演示和文章。
- [LLM人类偏好数据集合集](https://github.com/PolisAI/awesome-llm-human-preference-datasets) - 供LLM指令调优、强化学习（RLHF）和评估使用的人类偏好数据集。
- [RWKV教程](https://github.com/Hannibal046/RWKV-howto) - RWKV学习相关材料和教程。
- [大语言模型编辑论文汇总](https://github.com/zjunlp/ModelEditingPapers) - 关于大语言模型编辑的论文和资源合集。
- [LLM安全资源合集](https://github.com/corca-ai/awesome-llm-security) - 与LLM安全相关的工具、文档和项目资源。
- [LLM与人类对齐研究资源汇总](https://github.com/GaryYufei/AlignLLMHumanSurvey) - 关于大语言模型与人类对齐的论文和资源集合。
- [代码LLM资源合集](https://github.com/huybery/Awesome-Code-LLM) - 收集与代码LLM相关的研究和资源。
- [LLM压缩论文合集](https://github.com/HuangOwen/Awesome-LLM-Compression) - 关于LLM压缩的研究论文和工具。
- [LLM系统研究论文合集](https://github.com/AmberLJC/LLMSys-PaperList) - 研究LLM系统的相关论文集合。
- [LLM应用WebApp资源合集](https://github.com/snowfort-ai/awesome-llm-webapps) - 收集开源并积极维护的LLM应用Web应用。
- [日本语LLM资源汇总](https://github.com/llm-jp/awesome-japanese-llm) - 日本语LLM的概览。
- [LLM在医疗中的应用论文汇总](https://github.com/mingze-yuan/Awesome-LLM-Healthcare) - 关注LLM在医学领域应用的相关论文。
- [LLM推理论文合集](https://github.com/DefTruth/Awesome-LLM-Inference) - 以推理为主题的LLM相关论文汇总。
- [3D世界中的LLM研究资源](https://github.com/ActiveVisionLab/Awesome-LLM-3D) - 研究3D世界中多模态大语言模型的论文和资源合集。
- [LLM训练数据集合集](https://github.com/Zjh-819/LLMDataHub) - 专为聊天机器人训练设计的LLM数据集，包含数据集链接、大小、语言、用途和简要描述。
- [中文LLM资源合集](https://github.com/HqWu-HITCS/Awesome-Chinese-LLM) - 汇总开源中文大语言模型，包括小规模、可私有化部署、训练成本较低的模型及其应用、数据集和教程等。
- [LLM优化任务研究合集](https://github.com/FeiLiu36/LLM4Opt) - 探索LLM在优化任务中的应用，收集相关研究论文。
- [语言模型分析论文合集](https://github.com/Furyton/awesome-language-model-analysis) - 聚焦于语言模型的理论和实证分析，涉及学习动态、表现力、可解释性、泛化能力等议题。

## 大型语言模型（LLM）排行榜

以下是一些评估大型语言模型性能的排行榜平台和基准，涵盖了不同领域和任务，供开发者和研究者参考：

- **Chatbot Arena Leaderboard** - [Hugging Face平台](https://huggingface.co/spaces/lmsys/chatbot-arena-leaderboard)，通过匿名和随机对战的方式，评估大型语言模型（LLMs）在聊天中的表现。
- **Open LLM Leaderboard** - [Hugging Face平台](https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard)，专门跟踪、排名和评估发布的LLMs和聊天机器人。
- **Chinese Large Model Leaderboard** - [中文LLM排行榜](https://github.com/jeinlee1991/chinese-llm-benchmark)，专门评估中文大型语言模型。
- **CompassRank** - [CompassRank平台](https://rank.opencompass.org.cn)，评估语言和视觉模型的表现，提供一个全面、公正的行业参考。
- **InfiBench** - [InfiBench平台](https://infi-coder.github.io/infibench)，专注于评估大型语言模型在解决实际编程问题上的能力。
- **LawBench** - [法律领域评测平台](https://lawbench.opencompass.org.cn/leaderboard)，评估LLMs在法律领域的表现。
- **MathEval** - [MathEval平台](https://matheval.ai)，评估大型语言模型在数学领域的能力，涵盖20个领域和近30,000个数学问题。
- **MixEval** - [MixEval平台](https://mixeval.github.io/#leaderboard)，基于真实数据的动态评测平台，评估LLMs在混合任务中的表现，运行高效、成本低。
- **SuperBench** - [SuperBench平台](https://fm.ai.tsinghua.edu.cn/superbench/#/leaderboard)，一个综合性评测平台，评估LLMs在自然语言理解、推理和泛化等任务上的表现。
- **OlympicArena** - [学术领域评测平台](https://gair-nlp.github.io/OlympicArena/#leaderboard)，涵盖数学、物理、化学、生物学等多个学科。
- **We-Math** - [We-Math平台](https://we-math.github.io/#leaderboard)，评估大型多模态模型在数学推理上的能力。

### 开源大语言模型 (LLM)

#### Meta
- [Llama 3 系列](https://llama.meta.com/)
- [OPT 系列](https://arxiv.org/abs/2205.01068)

#### Mistral AI
- [Mistral 7B](https://mistral.ai/news/announcing-mistral-7b/)
- [Mixtral 系列](https://mistral.ai/news/mixtral-of-experts/)

#### Google
- [Gemma 系列](https://blog.google/technology/developers/google-gemma-2/)
- [T5](https://arxiv.org/abs/1910.10683)

#### Apple
- [OpenELM-1.1](https://huggingface.co/apple/OpenELM)

#### Microsoft
- [Phi 系列](https://huggingface.co/microsoft/phi-1)

#### Cohere
- [Command R-35B](https://huggingface.co/CohereForAI/c4ai-command-r-v01)

#### DeepSeek
- [DeepSeek 系列](https://huggingface.co/collections/deepseek-ai)

#### Alibaba
- [Qwen 系列](https://huggingface.co/collections/Qwen/qwen-65c0e50c3f1ab89cb8704144)

#### Baichuan
- [Baichuan 系列](https://huggingface.co/baichuan-inc)

#### Nvidia
- [Nemotron-4-340B](https://huggingface.co/nvidia/Nemotron-4-340B-Instruct)

#### Zhipu AI
- [GLM-2 系列](https://huggingface.co/THUDM)

#### Stability AI
- [StableLM 系列](https://huggingface.co/collections/stabilityai/stable-lm-650852cfd55dd4e15cdcb30a)

#### DataBricks
- [MPT-7B](https://www.databricks.com/blog/mpt-7b)

#### 上海人工智能实验室
- [InternLM 系列](https://huggingface.co/collections/internlm/internlm2-65b0ce04970888799707893c)

### LLM 数据
- [LLMDataHub](https://github.com/Zjh-819/LLMDataHub)
- [IBM 数据预处理工具包](https://github.com/IBM/data-prep-kit) - 高效处理非结构化数据的开源工具包。

### LLM 评估工具
- [lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness)
- [MixEval](https://github.com/Psycoy/MixEval)
- [lighteval](https://github.com/huggingface/lighteval)
- [OLMO-eval](https://github.com/allenai/OLMo-Eval)
- [instruct-eval](https://github.com/declare-lab/instruct-eval)
- [simple-evals](https://github.com/openai/simple-evals)
- [Giskard](https://github.com/Giskard-AI/giskard)
- [LangSmith](https://www.langchain.com/langsmith)
- [Ragas](https://github.com/explodinggradients/ragas)

## LLM训练框架

- [DeepSpeed](https://github.com/microsoft/DeepSpeed) - 一款深度学习优化库，旨在简化分布式训练和推理，提高效率和效果。
- [Megatron-DeepSpeed](https://github.com/microsoft/Megatron-DeepSpeed) - NVIDIA Megatron-LM的DeepSpeed版本，增强了对MoE模型训练、课程学习、3D并行等特性的支持。
- [torchtune](https://github.com/pytorch/torchtune) - PyTorch原生库，用于对大规模语言模型（LLM）进行微调。
- [NeMo Framework](https://github.com/NVIDIA/NeMo) - NVIDIA推出的生成式AI框架，支持LLM、语音识别（ASR）、文本到语音（TTS）等多个领域的研究。
- [Megatron-LM](https://github.com/NVIDIA/Megatron-LM) - 进行大规模Transformer模型训练的研究框架。
- [Colossal-AI](https://github.com/hpcaitech/ColossalAI) - 让大型AI模型训练变得更便宜、更高效、更易访问。
- [BMTrain](https://github.com/OpenBMB/BMTrain) - 高效的大型模型训练框架。
- [Mesh TensorFlow](https://github.com/tensorflow/mesh) - 提供便捷的模型并行化训练方案。
- [GPT-NeoX](https://github.com/EleutherAI/gpt-neox) - 基于DeepSpeed库的GPU并行自回归Transformer模型实现。

## LLM部署

> 参考：[llm-inference-solutions](https://github.com/mani-kantap/llm-inference-solutions)
- [SGLang](https://github.com/sgl-project/sglang) - 高效的LLM和视觉语言模型推理框架。
- [vLLM](https://github.com/vllm-project/vllm) - 高吞吐、低内存消耗的LLM推理和服务引擎。
- [TGI](https://huggingface.co/docs/text-generation-inference/en/index) - Hugging Face推出的LLM部署和服务工具包。
- [exllama](https://github.com/turboderp/exllama) - 为量化权重的Llama模型提供的更高效内存版本。
- [FastChat](https://github.com/lm-sys/FastChat) - 支持多种模型的分布式LLM服务系统，提供Web UI和OpenAI兼容的RESTful API。
- [LangChain](https://github.com/hwchase17/langchain) - 用于构建基于LLM的应用的Python/JavaScript库，支持通过组合模型实现复杂应用。

## LLM应用

- [MLflow](https://mlflow.org/) - 开源机器学习生命周期管理平台，支持实验跟踪、模型评估和部署。
- [YiVal](https://github.com/YiVal/YiVal) - 开源的GenAI-Ops工具，用于调优和评估LLM模型的提示、配置及模型参数。
- [LangChain](https://github.com/hwchase17/langchain) - 用于构建LLM链式应用的流行Python库。
- [Prompttools](https://github.com/hegelai/prompttools) - 用于测试和评估模型、向量数据库及提示的开源工具集。
- [Weights & Biases](https://wandb.ai/site/solutions/llmops) - 用于跟踪模型训练和提示优化实验的商业工具。

## LLM教程与课程

- [LLM课程](https://github.com/mlabonne/llm-course) - 带有路线图和Colab笔记本，帮助你深入了解大型语言模型（LLM）。
- [UWaterloo CS 886](https://cs.uwaterloo.ca/~wenhuche/teaching/cs886/) - 探索基础模型的最新进展。
- [CS25-Transformers United](https://web.stanford.edu/class/cs25/) - 斯坦福大学的Transformers课程。
- [ChatGPT提示工程](https://www.deeplearning.ai/short-courses/chatgpt-prompt-engineering-for-developers/) - 专为开发者设计的ChatGPT提示工程课程。
- [普林斯顿大学：理解大型语言模型](https://www.cs.princeton.edu/courses/archive/fall22/cos597G/) - 普林斯顿大学关于大型语言模型的课程。
- [CS324 - 大型语言模型](https://stanford-cs324.github.io/winter2022/) - 斯坦福大学的LLM课程。
- [GPT状态分析](https://build.microsoft.com/en-US/sessions/db3f4859-cd30-4445-a0cd-553c3304f8e2) - 了解GPT模型的最新发展。
- [构建GPT：从零开始的代码实现](https://www.youtube.com/watch?v=kCc8FmEb1nY) - 一部详尽的GPT从零实现教程。
- [BPE最简实现](https://www.youtube.com/watch?v=zduSFxRajkE&t=1157s) - 介绍常用于LLM标记化的字节对编码（BPE）算法。
- [femtoGPT](https://github.com/keyvank/femtoGPT) - 使用纯Rust实现的最简生成预训练变换器（GPT）。
- [Neurips2022：基础模型的鲁棒性](https://nips.cc/virtual/2022/tutorial/55796) - 讨论基础模型的稳定性和鲁棒性。
- [ICML2022：大模型时代的技术与系统](https://icml.cc/virtual/2022/tutorial/18440) - 探索大模型的训练与应用。
- [GPT60行代码实现](https://jaykmody.com/blog/gpt-from-scratch/) - 用60行NumPy代码实现一个简单的GPT。

## LLM书籍推荐

- [《LangChain与生成式AI》](https://amzn.to/3GUlRng) - 本书展示如何使用Python、ChatGPT及其他LLM构建生成式AI应用，并附带[GitHub代码](https://github.com/benman1/generative_ai_with_langchain)。
- [《从零开始构建大型语言模型》](https://www.manning.com/books/build-a-large-language-model-from-scratch) - 详细指导如何构建一个可用的LLM。
- [《构建GPT：如何工作》](https://www.amazon.com/dp/9152799727?ref_=cm_sw_r_cp_ud_dp_W3ZHCD6QWM3DPPC0ARTT_1) - 从零开始讲解如何编写一个生成预训练变换器（GPT）。
- [《大型语言模型实战》](https://www.llm-book.com/) - 一本详细的图解书籍，带你深入了解大型语言模型及其应用。

## LLM相关思考

- [为什么所有GPT-3的公开复现都失败了？](https://jingfengyang.github.io/gpt)
- [指令调优的阶段性回顾](https://yaofu.notion.site/June-2023-A-Stage-Review-of-Instruction-Tuning-f59dbfc36e2d4e12a33443bd6b2012c2)
- [LLM驱动的自主代理](https://lilianweng.github.io/posts/2023-06-23-agent/)
- [为什么你应该从事AI代理的工作！](https://www.youtube.com/watch?v=fqVLjtvWgq8)
- [谷歌：我们没有护城河，OpenAI也没有](https://www.semianalysis.com/p/google-we-have-no-moat-and-neither)
- [AI竞争声明](https://petergabriel.com/news/ai-competition-statement/)
- [提示工程概述](https://lilianweng.github.io/posts/2023-03-15-prompt-engineering/)
- [乔姆斯基：ChatGPT的虚假承诺](https://www.nytimes.com/2023/03/08/opinion/noam-chomsky-chatgpt-ai.html)
- [ChatGPT的1750亿参数：技术分析](https://orenleung.super.site/is-chatgpt-175-billion-parameters-technical-analysis)
- [大型语言模型的下一代](https://www.notion.so/Awesome-LLM-40c8aa3f2b444ecc82b79ae8bbd2696b)
- [2023年大型语言模型训练](https://research.aimultiple.com/large-language-model-training/)
- [GPT如何获得其能力？追溯语言模型的涌现能力](https://yaofu.notion.site/How-does-GPT-Obtain-its-Ability-Tracing-Emergent-Abilities-of-Language-Models-to-their-Sources-b9a57ac0fcf74f30a1ab9e3e36fa1dc1)

## 其他资源

- [Arize-Phoenix](https://phoenix.arize.com/) - 用于机器学习可观察性的开源工具，支持在你的笔记本环境中运行并调整LLM、计算机视觉（CV）和表格数据模型。
- [Emergent Mind](https://www.emergentmind.com) - 最新的AI新闻，由GPT-4解析和解释。
- [ShareGPT](https://sharegpt.com) - 一键分享你与ChatGPT的对话。
- [主要LLM及数据可用性](https://docs.google.com/spreadsheets/d/1bmpDdLZxvTCleLGVPgzoMTQ0iDP2-7v7QziPrzPdHyM/edit#gid=0) - 主要LLM模型的概览及其数据可用性。
- [500+最佳AI工具](https://vaulted-polonium-23c.notion.site/500-Best-AI-Tools-e954b36bf688404ababf74a13f98d126)
- [Cohere Summarize Beta](https://txt.cohere.ai/summarize-beta/) - Cohere推出的文本摘要API。
- [chatgpt-wrapper](https://github.com/mmabrouk/chatgpt-wrapper) - 一个开源的Python API和CLI工具，用于与ChatGPT交互。
- [Open-evals](https://github.com/open-evals/evals) - 用于不同语言模型评估的扩展框架。
- [Cursor](https://www.cursor.so) - 一个强大的AI工具，用于编写、编辑和讨论代码。
- [AutoGPT](https://github.com/Significant-Gravitas/Auto-GPT) - 一个展示GPT-4功能的开源应用。
- [OpenAGI](https://github.com/agiresearch/OpenAGI) - 当LLM遇到领域专家时。
- [EasyEdit](https://github.com/zjunlp/EasyEdit) - 一个易于使用的框架，用于编辑大型语言模型。
- [chatgpt-shroud](https://github.com/guyShilo/chatgpt-shroud) - 一个Chrome扩展，用于保护用户隐私，允许轻松隐藏和显示ChatGPT聊天记录。适合屏幕共享时使用。
