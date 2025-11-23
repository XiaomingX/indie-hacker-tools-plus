# awesome-CUDA（CUDA 学习资源精选 · 2024 实用版）


## 一、基础到进阶讲座（兼顾原理与现代架构）
这部分资源覆盖 CUDA 核心逻辑与**现代 GPU 架构（Ampere、Hopper、Ada Lovelace）** 的落地实践，从零基础入门到性能优化逐步递进，标注了资源的时效性与适用场景。

1.  **CUDA C/C++ 官方入门教程**  
    🔗 链接：[NVIDIA CUDA 基础培训](https://developer.nvidia.com/cuda-training)  
    核心内容：用通俗语言讲解 CUDA 核心概念——  
    - 核函数：GPU 上执行的「并行函数」，是 CUDA 编程的入口；  
    - 线程模型：线程→线程块→网格的层级结构（类比“员工→部门→公司”的并行分工）；  
    - 内存层级：全局内存（慢、大）、共享内存（快、小）、寄存器内存（极快、极小）的使用场景；  
    配套 **CUDA Toolkit 12.x+** 可运行示例（如向量加法、基础矩阵乘法）。  
    适用人群：零基础，想快速建立 CUDA 编程框架认知的开发者。

2.  **经典 CUDA 基础（补充参考）**  
    🔗 链接：[CUDA C/C++ 基础（2013）](https://www.olcf.ornl.gov/wp-content/uploads/2013/02/Intro_to_CUDA_C-TS.pdf)  
    核心内容：同原文档（核函数、内存管理、线程同步等基础）。  
    注意事项：**架构背景较旧**（无 Tensor Cores、统一内存等现代特性），仅适合辅助理解“CUDA 底层原理的历史根基”。

3.  **CUDA 高级优化与现代架构实践**  
    🔗 链接：[GTC 2023 - CUDA 性能优化实战](https://www.nvidia.com/en-us/gtc/on-demand/?search=CUDA%20advanced%20optimization)  
    核心内容：聚焦现代 GPU 特性的优化技巧，含真实工程案例（性能提升 10-50 倍）：  
    - 架构特性：Tensor Cores（加速矩阵运算）、异步拷贝引擎（计算与数据传输重叠）；  
    - 内存优化：避免全局内存“非对齐访问”、共享内存银行冲突解决方案；  
    - 并行策略：指令级并行（ILP）与线程级并行（TLP）的协同设计。  
    适用人群：有基础后，需解决“GPU 利用率低、性能不达预期”的工程师。

4.  **CUDA 内存优化实战（2024 版）**  
    🔗 链接：[GTC 2024 - 内存带宽瓶颈突破](https://www.nvidia.com/en-us/gtc/on-demand/?search=CUDA%20memory%20optimization)  
    核心内容：比旧版更贴近当前架构的内存优化方案：  
    - 异步数据传输：用流（Stream）实现“CPU 计算-GPU 计算-数据传输”三重叠；  
    - 统一内存：页迁移机制解析与 `cudaMemAdvise` 优化指令；  
    - 实战案例：矩阵转置的“共享内存+寄存器分块”优化（比 naive 实现快 15 倍）。  
    适用人群：受困于“内存读写成为性能瓶颈”的开发者。


## 二、必用 CUDA 库（附选型指南，避免重复造轮子）
CUDA 生态的成熟库可大幅降低开发成本，以下是**生产级常用库**，标注了“适用场景”和“替代方案”。

### 1. 通用并行算法库
- **Thrust**  
  🔗 链接：[GitHub - thrust/thrust](https://github.com/thrust/thrust)  
  核心内容：**CUDA Toolkit 自带**的并行算法库，API 完全兼容 C++ STL（如 `thrust::sort`、`thrust::reduce`），无需手动写核函数即可实现并行。底层会根据 GPU 架构自动优化。  
  选型建议：快速原型开发、中小规模并行任务（性能满足 80% 场景）；需极致性能可搭配底层 API 二次优化。

- **Modern GPU**  
  🔗 链接：[NVLabs Modern GPU](https://nvlabs.github.io/moderngpu/index.html)  
  核心内容：包含“工业级最优”的 CUDA 算法模板（扫描、流压缩、排序等），附带详细性能分析（如内存访问模式、线程利用率），代码可直接复用。  
  适用人群：需要定制高性能算法的资深开发者（如图形学、大规模数据处理）。

### 2. NVIDIA 官方核心库（生产必备）
这些库由 NVIDIA 深度优化，性能远超手动实现，是工业界标准：
| 库名称   | 核心功能                  | 适用场景                          | 官方链接                                  |
|----------|---------------------------|-----------------------------------|-------------------------------------------|
| cuBLAS   | 高性能线性代数运算        | 矩阵乘法、向量运算（科学计算核心） | https://developer.nvidia.com/cublas       |
| cuFFT    | 快速傅里叶变换            | 信号处理、图像处理、频谱分析      | https://developer.nvidia.com/cufft        |
| cuDNN    | 深度学习算子优化          | 卷积、池化（TensorFlow/PyTorch 依赖） | https://developer.nvidia.com/cudnn      |
| NCCL     | 多GPU/多节点通信          | 分布式训练、大规模并行计算        | https://developer.nvidia.com/nccl         |

### 3. 历史参考库（谨慎使用）
## 三、经典论文与现代研究方向
从经典论文理解“并行算法本质”，从现代研究把握“优化前沿”，附论文获取渠道。

### 1. 奠基性经典论文（算法设计根基）
- **《高效并行扫描算法》**  
  🔗 链接：[UC Davis 论文](http://www.idav.ucdavis.edu/publications/print_pub?pub_id=1041)  
  价值：并行“扫描（前缀和）”的经典分治法实现，是 `Thrust`、`Modern GPU` 中扫描函数的理论源头，帮你理解“如何将串行算法拆分为并行任务”。

- **《高效流压缩在宽 SIMD 架构上的实现》**  
  🔗 链接：[Chalmers 大学论文](http://www.cse.chalmers.se/~uffe/streamcompaction.pdf)  
  价值：流压缩（筛选稀疏数据）的核心论文，CUDPP 早期版本的理论依据，对处理“非结构化数据的并行筛选”很有启发。

### 2. 现代研究方向（2020+ 前沿）
| 研究方向                | 核心内容                          | 论文获取渠道                          |
|-------------------------|-----------------------------------|---------------------------------------|
| Tensor Cores 通用加速   | 用深度学习专用的 Tensor Cores 加速科学计算 | arXiv、NVIDIA Research                |
| 统一内存优化            | 页迁移机制与异构内存调度策略        | NVIDIA Research、GTC 论文集           |
| 多GPU 拓扑感知通信      | 基于 GPU 硬件拓扑的通信路径优化    | IEEE Xplore、NVIDIA DevBlog 配套论文  |

### 3. 工程实践论文
- **《CUDA 直方图计算优化》**  
  建议替换为：[GTC 2022 - 直方图加速实战](https://www.nvidia.com/en-us/gtc/on-demand/?search=CUDA%20histogram%20optimization)  
  价值：结合现代架构的“共享内存+原子操作”优化，解决直方图计算中的“内存竞争”问题，附性能对比数据。


## 四、实用优化文章（直接解决工程问题）
均来自 NVIDIA 开发者博客（Parallel Forall）或 GTC 技术博客，**附可运行代码**，针对现代架构优化。

1.  **GPU 直方图加速（Ampere/Hopper 适用）**  
    🔗 链接：[Fast Histograms with Shared Atomics](https://developer.nvidia.com/blog/fast-histograms-on-gpus-using-shared-memory-and-atomics/)  
    核心技巧：利用 Ampere 架构的“共享内存原子操作吞吐量提升”，结合寄存器分块减少全局内存访问，比传统实现快 3-8 倍。

2.  **并行归约（Reduce）终极优化**  
    🔗 链接：[Parallel Reduction in CUDA](https://developer.nvidia.com/blog/parallel-reduction-in-cuda/)  
    核心技巧：从“基础归约”到“warp 级归约”“shuffle 指令优化”“Tensor Cores 加速”的完整演进，给出适配不同架构的最优代码模板。

3.  **统一内存最佳实践（2024）**  
    🔗 链接：[Unified Memory Best Practices](https://developer.nvidia.com/blog/unified-memory-best-practices-for-cuda/)  
    核心技巧：什么时候该用统一内存（如内存受限场景）、如何用 `cudaMemAdvise` 指令避免“页迁移 overhead”，附实际项目案例。

4.  **多GPU 通信优化（NCCL 实战）**  
    🔗 链接：[NCCL 2.19 新特性与性能调优](https://developer.nvidia.com/blog/nccl-2-19-features-and-performance/)  
    核心技巧：NCCL 通信原语（`allreduce`、`broadcast`）的正确用法，多GPU 拓扑感知配置，解决“分布式训练中的通信延迟”问题。
