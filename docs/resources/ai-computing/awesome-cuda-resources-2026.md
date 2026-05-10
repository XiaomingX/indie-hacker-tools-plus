# CUDA 学习与性能优化资源 (2026 Checklist)

> [!TIP]
> **Indie Hacker Insight**: 2026 年，掌握 CUDA 意味着你能为你的 AI 应用构建**独有的算力护城河**。
> - **不要重复造轮子**：优先使用 **cuBLAS** 和 **cuDNN**，手动编写核函数仅用于解决 20% 的特定算法瓶颈。
> - **关注 Tensor Cores**：在 Hopper (H100) 和 Blackwell 架构上，利用 Tensor Cores 进行混合精度运算是性能翻倍的关键。

---

## 📚 基础到进阶 (Foundations & Mastery)

- [ ] [**NVIDIA CUDA 官方入门**](https://developer.nvidia.com/cuda-training) - 系统学习核函数、线程模型（Grid/Block/Thread）与内存层级。
- [ ] [**CUDA 12.x+ 编程指南**](https://docs.nvidia.com/cuda/cuda-c-programming-guide/index.html) - 官方文档，包含最新的异步内存管理与流 (Stream) 优化特性。
- [ ] [**GTC 2023 - CUDA 性能优化实战**](https://www.nvidia.com/en-us/gtc/on-demand/?search=CUDA%20advanced%20optimization) - 聚焦现代架构（Ampere/Hopper）的性能榨取技巧。
- [ ] [**CUDA 内存优化实战 (2026)**](https://www.nvidia.com/en-us/gtc/on-demand/?search=CUDA%20memory%20optimization) - 解决全局内存访问对齐与共享内存银行冲突。

---

## 🛠️ 核心库选型 (Essential Libraries)

- [ ] [**Thrust**](https://github.com/thrust/thrust) - CUDA 官方算法库，API 兼容 C++ STL（如 `sort`, `reduce`），快速原型首选。
- [ ] [**cuBLAS**](https://developer.nvidia.com/cublas) - 高性能线性代数库，矩阵乘法运算的行业标准。
- [ ] [**cuDNN**](https://developer.nvidia.com/cudnn) - 深度学习算子库，PyTorch/TensorFlow 的核心加速引擎。
- [ ] [**NCCL**](https://developer.nvidia.com/nccl) - 多 GPU 与多节点通信标准，分布式训练必备。
- [ ] [**Modern GPU**](https://nvlabs.github.io/moderngpu/) - 提供工业级最优的扫描、流压缩等并行算法模板。

---

## 🔬 进阶研究与论文 (Research & Papers)

- [ ] [**Efficient Parallel Scan**](http://www.idav.ucdavis.edu/publications/print_pub?pub_id=1041) - 并行前缀和算法的理论根基。
- [ ] [**Tensor Cores for Science**](https://arxiv.org/abs/2006.12656) - 研究如何利用 Tensor Cores 加速传统科学计算任务。
- [ ] [**NVLabs Research**](https://research.nvidia.com/) - 关注 NVIDIA 实验室关于统一内存、多卡拓扑的最新研究成果。

---

## ⚡ 工程实践优化 (Engineering Tips)

- [ ] [**Fast Histograms (Ampere/Hopper)**](https://developer.nvidia.com/blog/fast-histograms-on-gpus-using-shared-memory-and-atomics/) - 利用共享内存原子操作实现 3-8 倍加速。
- [ ] [**Parallel Reduction 终极优化**](https://developer.nvidia.com/blog/parallel-reduction-in-cuda/) - 掌握从基础归约到 Warp 级归约的完整演进。
- [ ] [**Unified Memory Best Practices**](https://developer.nvidia.com/blog/unified-memory-best-practices-for-cuda/) - 掌握 `cudaMemAdvise` 指令，避免页迁移开销。
- [ ] [**NVIDIA Nsight Systems/Compute**](https://developer.nvidia.com/nsight-systems) - 熟练使用性能分析工具，定位代码瓶颈。

---

## 💡 选型建议
1. **追求开发速度**：首选 **Thrust**。
2. **构建深度学习推理框架**：深度集成 **cuDNN** 与 **TensorRT**。
3. **处理大规模非结构化数据**：重点参考 **Modern GPU** 的流压缩算法。
4. **多卡集群作业**：务必使用 **NCCL** 进行拓扑感知通信。
