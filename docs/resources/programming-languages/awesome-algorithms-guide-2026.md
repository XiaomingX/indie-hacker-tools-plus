# 2026 核心算法与数据结构进阶指南 (Checklist)

> [!TIP]
> **Indie Hacker Insight**: 在构建高性能应用时，算法是“降本增效”的最底层手段。
> - **空间换时间**：利用 Bloom Filter 或 Redis 缓存，可以把 O(N) 的查询降至 O(1)。
> - **现代并发**：在 2026 年，掌握 Rust 的所有权模型或 Go 的并发模型比死记硬背排序算法更实用。
> - **AI 增强**：利用 GitHub Copilot 或 Claude 辅助编写复杂的动态规划代码，但必须通过单元测试验证逻辑边缘情况。

---

## 🏗️ 核心数据结构 (Essential Data Structures)

- [ ] [**数组与字符串 (Arrays & Strings)**](https://github.com/trekhleb/javascript-algorithms#data-structures) - 基础中的基础，掌握双指针与滑动窗口技巧。
- [ ] [**链表 (Linked Lists)**](https://github.com/trekhleb/javascript-algorithms/tree/master/src/data-structures/linked-list) - 理解指针操作、环检测与合并排序。
- [ ] [**栈与队列 (Stacks & Queues)**](https://github.com/trekhleb/javascript-algorithms/tree/master/src/data-structures/stack) - 理解 LIFO/FIFO，常用于表达式解析与任务调度。
- [ ] [**哈希表 (Hash Tables)**](https://github.com/trekhleb/javascript-algorithms/tree/master/src/data-structures/hash-table) - 理解散列函数、碰撞处理及其在数据库索引中的应用。
- [ ] [**树 (Trees)**](https://github.com/trekhleb/javascript-algorithms/tree/master/src/data-structures/tree) - 包含二叉树、红黑树、B+ 树（数据库核心）。
- [ ] [**图 (Graphs)**](https://github.com/trekhleb/javascript-algorithms/tree/master/src/data-structures/graph) - 掌握邻接矩阵/表，以及拓扑排序、Dijkstra 等算法。

---

## ⚡ 算法思维模式 (Algorithmic Paradigms)

- [ ] [**贪心算法 (Greedy)**](https://github.com/trekhleb/javascript-algorithms#greedy-algorithms) - 寻找局部最优解，适用于哈夫曼编码、最小生成树。
- [ ] [**分治法 (Divide and Conquer)**](https://github.com/trekhleb/javascript-algorithms#divide-and-conquer-algorithms) - 归并排序、快速排序、大整数乘法的核心思想。
- [ ] [**动态规划 (Dynamic Programming)**](https://github.com/trekhleb/javascript-algorithms#dynamic-programming-algorithms) - 解决重叠子问题，如背包问题、最长公共子序列。
- [ ] [**回溯法 (Backtracking)**](https://github.com/trekhleb/javascript-algorithms#backtracking-algorithms) - 解决约束满足问题，如八皇后、迷宫寻路。
- [ ] [**位运算技巧 (Bit Manipulation)**](https://github.com/trekhleb/javascript-algorithms#bit-manipulation-algorithms) - 极其高效的状态压缩与数值计算。

---

## 🛠️ 学习与可视化工具 (Tools)

- [ ] [**VisuAlgo**](https://visualgo.net/zh) - 将抽象的数据结构和算法通过动画直观呈现。
- [ ] [**Algorithm Visualizer**](https://algorithm-visualizer.org/) - 交互式可视化算法执行过程。
- [ ] [**GeeksforGeeks**](https://www.geeksforgeeks.org/fundamentals-of-algorithms/) - 全球最大的算法知识库，包含各主流语言实现。

---

## 💡 选型建议
1. **构建高性能缓存系统**：深入理解 **LRU/LFU** 算法与 **Consistent Hashing**。
2. **构建搜索推荐系统**：掌握 **Trie 树**、**倒排索引** 与 **向量检索 (ANN)**。
3. **处理大规模并行数据**：学习 **MapReduce** 模型与 **Log-Structured Merge-tree (LSM)**。
4. **底层架构开发**：必须精通 **红黑树** 与 **B+ 树** 以应对高性能索引需求。
