# awesome-tensorflow （ TensorFlow 2.x 学习资源精选：从入门到实战 ）

> 说明：本列表聚焦 **TensorFlow 2.x**（当前主流稳定版本），精选维护活跃、权威实用的学习资源，覆盖从基础入门到项目实战的全流程，帮助不同阶段学习者高效掌握 TensorFlow。


## 一、入门与核心教程
（针对初学者建立基础认知，或进阶者巩固核心用法，均适配 TF 2.x 语法）

- [TensorFlow 官方入门教程](https://www.tensorflow.org/tutorials) -  TensorFlow 官方出品的权威教程，覆盖基础语法、图像分类、NLP、模型部署等场景，附带可直接运行的 Colab 代码，新手入门首选。
- [TensorFlow 基础示例库](https://github.com/aymericdamien/TensorFlow-Examples) - 星数超 5 万的经典入门资源，更新至 TF 2.x，包含线性回归、CNN、RNN 等常见模型的极简示例，代码注释清晰，适合边看边练。
- [Effective TensorFlow 2](https://github.com/vahidk/EffectiveTensorflow2) - 原「Effective TensorFlow」的 TF 2.x 升级版，聚焦高效建模技巧（如自动求导、批处理优化、内存管理），帮你避开常见坑，写出更规范的 TF 代码。
- [Coursera：TensorFlow 深度学习专项课](https://www.coursera.org/specializations/tensorflow-in-practice) - 由 Google 工程师授课的官方专项课，包含 4 门核心课程（基础、CNN、RNN、生成式 AI），全部基于 TF 2.x，学完可动手完成图像识别、文本生成等实战项目。


## 二、经典与实战项目
（基于真实场景的模型实现，覆盖计算机视觉、NLP 等热门方向，可直接复用或二次开发）

- [TensorFlow 项目模板（TF 2.x）](https://github.com/Mrgemy95/Tensorflow-Project-Template) - 结构化的项目脚手架，包含数据加载、模型训练、日志记录、模型保存等标准化模块，新手可直接套用快速搭建项目。
- [图像描述生成（Show, Attend and Tell 复现）](https://github.com/yunjey/show_attend_and_tell) - 经典「注意力机制+图像描述」项目的 TF 实现，代码逻辑清晰，适合学习「视觉-语言跨模态建模」的基础思路。
- [神经风格迁移（Neural Style Transfer）](https://github.com/tensorflow/docs/blob/master/site/en/tutorials/generative/style_transfer.ipynb) - 替换原过时仓库，推荐 TensorFlow 官方风格迁移教程，基于 TF 2.x 实现「将照片转化为艺术画」，附带原理讲解和交互式代码。
- [超分辨率重建（SRGAN & Real-ESRGAN TF 版）](https://github.com/idealo/image-super-resolution) - 整合经典 SRGAN 与更优的 Real-ESRGAN 模型的 TF 实现，支持将低清图放大 4 倍并优化细节，可直接用于图片画质增强实战。
- [脑肿瘤分割（U-Net 实战）](https://github.com/zsdonghao/u-net-brain-tumor) - 医学影像分割经典项目，基于 U-Net 模型实现脑肿瘤区域精准标注，代码包含数据预处理、模型微调全流程，适合学习语义分割。
- [实时目标检测（YOLOv8 TF 版）](https://github.com/ultralytics/ultralytics) - 替换老旧 YOLO 实现，Ultralytics 库支持 YOLOv8（当前最新版）的 TensorFlow 后端，可快速实现图片/视频中的目标检测、跟踪，文档完善且社区活跃。
- [BERT 文本分类（TF 版）](https://github.com/huggingface/transformers) - Hugging Face Transformers 库的核心示例，支持将预训练 BERT 模型快速适配到情感分析、文本分类等 NLP 任务，是工业界 NLP 开发必备工具。


## 三、高效开发工具与库
（扩展 TensorFlow 功能，提升建模、调试、部署效率）

- [Keras（TensorFlow 官方高级 API）](https://keras.io/) - 原仓库链接保留，但补充核心说明：Keras 现已作为 TensorFlow 的官方高级 API（TF Keras），支持快速构建模型（Sequential/Functional/子类化），语法简洁且兼容多后端（TF/PyTorch/JAX），是 TF 2.x 推荐的建模方式。
- [TensorLayerX](https://github.com/tensorlayer/TensorLayerX) - 跨框架深度学习库，基于 TF 2.x 等后端，提供丰富的模型组件（如 Transformer、ResNet），优势是「一份代码可在多框架运行」，适合需要跨平台开发的场景。
- [TensorFlow-Probability（TFP）](https://www.tensorflow.org/probability) - TensorFlow 官方概率编程扩展库，可实现贝叶斯神经网络、概率分布建模等，适合需要「不确定性估计」的任务（如医疗诊断、风险预测）。
- [TensorFlow Datasets（TFDS）](https://www.tensorflow.org/datasets) - 官方数据加载库，包含 500+ 常用数据集（如 MNIST、CIFAR-10、IMDB），支持一键下载、预处理和批处理，极大简化数据准备流程。
- [TensorBoard](https://www.tensorflow.org/tensorboard) - TF 官方可视化工具，可实时监控训练损失/精度、可视化模型结构、查看数据分布，是调试和优化模型的核心工具。
- [Speedster](https://github.com/nebuly-ai/nebullvm/tree/main/apps/accelerate/speedster) - 模型推理加速工具，自动优化 TF 模型的推理速度（支持 CPU/GPU/TPU），无需手动改代码，适合将训练好的模型部署到生产环境。
- [TensorFlow Lite（TFLite）](https://www.tensorflow.org/lite) - 官方轻量化部署工具，可将 TF 模型转换为移动端/嵌入式设备支持的格式，适合开发 AI 手机应用、边缘计算设备（如树莓派）。


## 四、权威学习资料
（经典书籍、论文与官方文档，帮你系统性深化理解）

- [TensorFlow 2.x 官方文档](https://www.tensorflow.org/guide) - 最权威的知识手册，涵盖从基础概念（张量、自动求导）到高级技巧（自定义训练循环、分布式训练）的全部内容，附带大量代码示例。
- 论文：
  - [TensorFlow: A System for Large-Scale Machine Learning](https://arxiv.org/abs/1605.08695) - TF 核心架构的奠基论文，适合想理解 TF 底层数据流原理的进阶学习者。
  - [TensorFlow 2.0: Design and Implementation](https://arxiv.org/abs/2002.09286) - 讲解 TF 2.x 核心改进（如动态图优先、Keras 整合）的论文，帮你理解新版本的设计思路。
- 书籍：
  - [《Hands-On Machine Learning with Scikit-Learn, Keras & TensorFlow》（第 2 版）](https://www.oreilly.com/library/view/hands-on-machine-learning/9781492032632/) - 替换过时的第一版，本书是机器学习入门经典，第 2 版全面适配 TF 2.x，通过大量实战案例讲解从数据预处理到模型部署的全流程，新手友好。
  - [《TensorFlow in Action》](https://www.manning.com/books/tensorflow-in-action) - 聚焦 TF 2.x 实战，深入讲解自定义模型、分布式训练、TFLite 部署等工业级技巧，适合有基础后进阶学习。
