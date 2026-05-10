# 逆向工程 (Reverse Engineering) 学习资源精选 (2026 Checklist)

> [!TIP]
> **Indie Hacker Insight**: 2026 年，逆向工程已不仅仅是“破解”的代名词。
> - **AI 赋能**：利用 **LLM (如 Claude/GPT)** 配合 **Ghidra/IDA** 插件，可以自动解释复杂的汇编逻辑，效率提升 10x。
> - **跨平台重点**：除了 Windows，**Android (ARM64)** 和 **macOS (Apple Silicon)** 的逆向需求在 2026 年已占据半壁江山。
> - **防御视角**：通过逆向分析恶意软件，是独立开发者构建安全可靠应用的最佳学习方式。

---

## 🏗️ 基础理论与汇编 (Fundamentals & Assembly)

- [ ] [**CS:APP (深入理解计算机系统)**](https://csapp.cs.cmu.edu/) - **[底座]** 必读第 3 章，掌握汇编逻辑、内存模型与系统调用。
- [ ] [**CPU.land**](https://cpu.land/) - 极简可视化的 CPU 工作原理指南，适合快速建立直觉。
- [ ] [**Godbolt (Compiler Explorer)**](https://godbolt.org/) - 实时查看 C++/Rust 等源码编译后的汇编输出。
- [ ] [**OpenSecurityTraining2**](https://p.ost2.fyi/) - 免费且极高质量的 x86-64 和 ARM 汇编系统课程。

---

## 🛠️ 静态与动态分析工具 (Tools & Debuggers)

- [ ] [**Ghidra**](https://ghidra-sre.org/) - NSA 出品的开源逆向框架，反编译器（Decompiler）极其强大且免费。
- [ ] [**x64dbg**](https://x64dbg.com/) - Windows 平台最主流的动态调试器，完美替代老旧的 OllyDbg。
- [ ] [**Frida**](https://frida.re/) - **[2026 必备]** 跨平台动态插桩工具，支持在运行时修改进程行为，适用于移动端和桌面端。
- [ ] [**Binary Ninja**](https://binary.ninja/) - 商业级逆向利器，UI 精美且拥有极其优雅的 API 扩展能力。

---

## 🚀 进阶与实战练习 (Advanced & Practice)

- [ ] [**Crackmes.one**](https://crackmes.one/) - 收集了成千上万个不同难度的挑战题，从入门到骨灰级。
- [ ] [**Reversing.kr**](http://reversing.kr/) - 经典的逆向挑战网站，题目设计精巧。
- [ ] [**Unpacking Malware**](https://www.varonis.com/blog/x64dbg-unpack-malware) - 学习如何使用调试器对加壳的恶意软件进行手动脱壳。
- [ ] [**Android RE Guide**](https://github.com/ashishb/android-security-awesome) - 专注于移动端逆向、APK 分析与加密算法破解。

---

## 🛡️ 系统内核与反分析 (Internals & Anti-Analysis)

- [ ] [**Windows Internals**](https://learn.microsoft.com/en-us/sysinternals/resources/windows-internals) - 深入理解 Windows 内核机制的“圣经”。
- [ ] [**Anti-Debug Checkpoint**](https://anti-debug.checkpoint.com/) - 汇总了各种反调试、反仿真技术及其应对策略。
- [ ] [**Symbolic Execution (Z3)**](https://github.com/ViRb3/z3-python-ctf) - 学习使用 SMT 解算器自动化求解混淆逻辑或复杂的 Keygen 算法。

---

## 💡 选型建议
1. **初学者入门**：选 **CS:APP** + **Ghidra** + **Crackmes.one**。
2. **移动端 App 逆向**：选 **Frida** + **JADX** + **Ghidra**。
3. **恶意软件分析**：选 **x64dbg** + **Process Hacker** + **Any.Run (沙箱)**。
4. **自动化分析脚本**：选 **Python** + **IDAPython** 或 **Ghidra Scripting**。
