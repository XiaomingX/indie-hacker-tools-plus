# 机器学习后门 (ML Backdoor) 研究资源精选 (2026 Checklist)

> [!TIP]
> **Indie Hacker Insight**: 2026 年，机器学习后门研究已从传统的“图像投毒”演变为 **"大模型权重劫持"** 与 **"提示词注入后门"**。
> - **权重风险**：从非官方渠道下载的开源模型权重可能隐藏了针对特定触发词（Trigger）的恶意逻辑。
> - **供应链安全**：在 2026 年，验证预训练模型的安全性已成为独立开发者接入 AI 时的标准流程。
> - **生成式后门**：关注如何通过微调（Fine-tuning）在 LLM 中植入难以察觉的“条件偏见”。

---

## 🏗️ 核心综述与理论基础 (Surveys & Theory)

- [ ] [**Backdoor Learning: A Survey (2022)**](https://arxiv.org/abs/2007.08745) - 系统梳理后门攻击原理、方法与早期防御策略。
- [ ] [**Trojaning Language Models**](https://arxiv.org/abs/2008.00312) - 深入探讨针对 NLP 模型的特洛伊木马攻击。
- [ ] [**BadEncoder: Backdoor Attacks on Pre-trained Encoders**](https://arxiv.org/abs/2108.00352) - 研究如何在自监督学习阶段植入后门。

---

## 🛠️ 后门研究工具箱 (Research Toolboxes)

- [ ] [**BackdoorBox**](https://github.com/THU-MIG/BackdoorBox) - **[推荐]** 清华出品，集成多种攻击与防御算法的 Python 框架。
- [ ] [**OpenBackdoor**](https://github.com/thunlp/OpenBackdoor) - 专注于文本领域（NLP）的后门攻击与防御框架。
- [ ] [**TrojanZoo**](https://github.com/jcleonard/TrojanZoo) - 一个通用的后门学习平台，支持多种模型架构。
- [ ] [**BackdoorBench**](https://github.com/THU-MIG/BackdoorBench) - 后门攻击的标准化评测基准，适合进行学术对比。

---

## ⚡ 前沿方向：LLM 与生成模型 (LLM & Generative)

- [ ] [**Poisoning LLMs during Fine-tuning**](https://arxiv.org/abs/2305.00840) - 研究在下游任务微调时注入恶意行为的风险。
- [ ] [**Backdoor Attacks on Diffusion Models**](https://arxiv.org/abs/2301.03662) - 针对图像扩散模型的后门攻击研究。
- [ ] [**Universal Prompt Injection**](https://arxiv.org/abs/2307.15043) - 探讨如何通过特定的 Prompt 触发 LLM 的隐藏后门逻辑。

---

## 🛡️ 检测与防御方案 (Detection & Defense)

- [ ] [**Neural Cleanse**](https://ieeexplore.ieee.org/document/8835365) - 经典的后门检测框架，利用逆向工程识别异常触发器。
- [ ] [**STRIP: A Defence Against Trojan Attacks**](https://arxiv.org/abs/1902.06531) - 通过输入扰动和熵分析来实时检测后门触发。
- [ ] [**Model Sanitization**](https://arxiv.org/abs/2206.10405) - 学习如何从已污染的模型中“清洗”掉后门权重。

---

## 💡 选型建议
1. **进行学术研究原型开发**：选 **BackdoorBox** 或 **BackdoorBench**。
2. **评估开源大模型安全性**：重点研究 **Prompt Injection Detection** 与 **Weight Sanitization**。
3. **构建鲁棒的联邦学习系统**：参考 **FLIP 框架** 等具有数学保证的防御策略。
4. **防御文本类攻击**：必用 **OpenBackdoor** 进行基准测试。
