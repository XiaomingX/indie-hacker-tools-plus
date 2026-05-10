# 2026 全球顶级科技公司面试准备指南 (Checklist)

> [!TIP]
> **Indie Hacker Insight**: 虽然独立开发者不需要通过面试来获得工作，但顶级大厂的面试题库（如 LeetCode）是锻炼算法思维和代码鲁棒性的绝佳场地。
> - **AI 时代的面试**：大厂现在更看重你对系统架构的理解以及如何利用 AI 提升开发效率，而非单纯的手写红黑树。
> - **语言选择**：Python 是面试时的首选（简洁、库多），但在涉及底层系统时，C++ 或 Rust 的表现会加分。
> - **白板面试**：即使是线上远程，也要保持“边写边讲 (Talk while coding)”的习惯，展示你的逻辑链条。

---

## 🗺️ 学习路线与基础 (Roadmap)

- [ ] [**选择一门主力语言**](https://github.com/jwasham/coding-interview-university#pick-a-programming-language) - 推荐 Python 或 Java，如果是底层系统岗选 C++/Rust。
- [ ] [**大 O 表示法与复杂度分析**](https://bigocheatsheet.com/) - 深入理解时间与空间复杂度，这是所有算法的基准。
- [ ] [**核心数据结构**](#数据结构) - 数组、链表、堆栈、队列、哈希表。
- [ ] [**核心算法**](#算法) - 二分查找、快速排序、归并排序、深度/广度优先搜索 (DFS/BFS)。

---

## 🏗️ 数据结构实战要点 (Data Structures)

- [ ] [**动态数组 (Dynamic Arrays)**](https://github.com/jwasham/practice-python/blob/master/dynamic_array/dynamic_array.py) - 理解自动扩容机制与均摊复杂度。
- [ ] [**链表 (Linked Lists)**](https://github.com/jwasham/practice-python/blob/master/linked_list/linked_list.py) - 掌握单向、双向链表及循环链表的逆序与去重。
- [ ] [**哈希表 (Hash Tables)**](https://github.com/jwasham/practice-python/blob/master/hash_table/hash_table.py) - 理解碰撞处理（链地址法 vs 开放地址法）。
- [ ] [**树 (Trees)**](https://github.com/jwasham/practice-python/blob/master/binary_search_tree/bst.py) - 重点在于二叉搜索树 (BST) 的遍历与平衡树的概念。
- [ ] [**堆与优先级队列 (Heaps)**](https://github.com/jwasham/practice-python/blob/master/heap/heap.py) - 掌握大顶堆/小顶堆的构建与堆排序。

---

## ⚡ 算法高频考点 (Algorithms)

- [ ] [**排序 (Sorting)**](https://www.youtube.com/playlist?list=PL9xmBV_5YoZOZSbGAXAPIq1BeUf4j20pl) - 熟练掌握快速排序与归并排序的实现。
- [ ] [**递归与动态规划 (DP)**](https://www.youtube.com/watch?v=OQ5jsbhAv_M) - 从阶乘到复杂的背包问题，掌握“最优子结构”的拆解。
- [ ] [**图论 (Graphs)**](https://www.youtube.com/playlist?list=PL9xmBV_5YoZOCvIclv82v_e8s1L_f2W6x) - 掌握邻接矩阵、BFS、DFS 以及最短路径算法 (Dijkstra)。
- [ ] [**位运算 (Bitwise)**](https://github.com/jwasham/coding-interview-university/blob/main/extras/cheat%20sheets/bits-cheat-sheet.pdf) - 面试中的“黑魔法”，常用于性能优化和空间压缩。

---

## 🛠️ 实战练习平台 (Practice)

- [ ] [**LeetCode**](https://leetcode.com/) - **[必选]** 建议刷完“Top 100 Liked Questions”。
- [ ] [**HackerRank**](https://www.hackerrank.com/) - 适合进行系统的语言基础练习。
- [ ] [**AlgoExpert**](https://www.algoexpert.io/) - 包含极高质量的视频解析，适合进阶学习。
- [ ] [**System Design Primer**](https://github.com/donnemartin/system-design-primer) - 高级岗面试的核心：如何架构可扩展的系统。

---

## 💡 选型建议
1. **备考大厂（Amazon/Google/Facebook）**：必须熟读《Cracking the Coding Interview》，刷够 300+ LeetCode 题目。
2. **注重工程能力**：不仅要通过算法，更要展示你对 **Clean Code** 和 **Unit Testing** 的坚持。
3. **系统设计岗**：深入研究 **CAP 定理**、**分片 (Sharding)** 和 **缓存策略**。
