# awesome-reversing

## 逆向工程学习资源合集

这是一个帮助您从零开始学习逆向工程的资源合集！

### **汇编（Assembly）**

**推荐书籍：**
- 推荐阅读《计算机系统：程序员的视角》的第 3 章，讲解详细、通俗易懂。
- 如果不喜欢看书，也可以使用以下在线资源：

**Linux平台的汇编资源：**
- [汇编语言教程](https://asmtutor.com/)
- [汇编艺术](https://www.plantation-productions.com/Webster/www.artofasm.com/Linux/index.html)

**Windows平台的汇编资源：**
- [汇编艺术（Windows版）](https://www.plantation-productions.com/Webster/www.artofasm.com/Windows/index.html)
- [汇编语言教程](https://sonictk.github.io/asm_tutorial/)

**其他平台和通用资源：**
- [了解CPU的工作原理](https://cpu.land)
- [X86指令集手册](https://www.felixcloutier.com/x86/index.html)
- [X86汇编语言笔记](https://cs.lmu.edu/~ray/notes/x86assembly/)
- [在线汇编编译器Godbolt](https://godbolt.org/)
- [汇编与x86-64课程](https://p.ost2.fyi/courses/course-v1:OpenSecurityTraining2+Arch1001_x86-64_Asm+2021_v1/about)

---

### **汇编语言项目实战**

在学会汇编语言后，您可以尝试做一些项目，如制作引导加载程序（bootloader）或简单的操作系统（OS）。

- [如何理解启动过程并编写自己的操作系统](https://de-engineer.github.io/Understanding-booting-process-and-writing-own-os/)
- [操作系统开发指南](http://brokenthorn.com/Resources/OSDev1.html)
- [《从0到1的操作系统》](https://raw.githubusercontent.com/tuhdo/os01/master/Operating_Systems_From_0_to_1.pdf)
- [操作系统开发讲义](https://cs.bham.ac.uk/~exr/lectures/opsys/10_11/lectures/os-dev.pdf)
- [通过编写GUI来学习x86-64汇编](https://gaultier.github.io/blog/x11_x64.html)

---

### **操作系统内部原理（OS Internals）**

**推荐学习路径：**
1. 《计算机科学的要素》（TECS） + [Nand2Tetris课程](https://www.coursera.org/learn/build-a-computer)
2. 《计算机系统：程序员的视角》（CSAPP） + [视频讲座](https://scs.hosted.panopto.com/Panopto/Pages/Sessions/List.aspx#folderID=%22b96d90ae-9871-4fae-91e2-b1627b43e25e%22)
3. 《操作系统：三大易学部分》 + [视频讲座](https://www.youtube.com/watch?v=DcBa3dBBOtM&list=PLRJWiLCmxyxi2RCPVYfewxJIWJzc_colw)

**如果不喜欢看书，可以参考以下资源：**
- [操作系统视频教程1](https://www.youtube.com/playlist?list=PLmbPuZ0NsyGS8ef6zaHd2qYylzsHxL63x)
- [操作系统视频教程2](https://www.youtube.com/playlist?list=PLgre7dUq8DGKbtnlMuJPvPYlvLdXOC9uh)
- [操作系统三大易学部分在线资源](https://pages.cs.wisc.edu/~remzi/OSTEP/)
- [操作系统课程（推荐）](https://www.youtube.com/playlist?list=PLunILarQwxnl0SZ2zsgyVjU9NDD_Rn-re)

---

### **入门指南**

如果您对如何开始感到困惑，可以参考以下资源：
- [逆向工程路线图](https://wiki.bi0s.in/reversing/roadmap)
- [COMPSCI 390R：逆向工程与漏洞分析](https://pwn.umasscybersec.org/lectures/index.html)
- [Begin.Re：逆向工程入门](https://www.begin.re/)
- [Artik的逆向工程资源](https://artik.blue/reversing)
- [Octopus Labs的示例页面](https://legend.octopuslabs.io/sample-page.html)
- [逆向工程视频1](https://www.youtube.com/watch?v=mDyQBM-_T1g)
- [逆向工程视频2](https://www.youtube.com/watch?v=gPsYkV7-yJk)
- [逆向工程视频3](https://www.youtube.com/watch?v=d4Pgi5XML8E)
- [逆向工程视频4（推荐）](https://www.youtube.com/watch?v=9vKG8-TnawY)


## 开始动手实践

如果你想亲身体验和学习逆向工程，以下是一些有用的资源：

- [Crackmes 练习网站](https://crackmes.one/)
- [Reversing.kr 挑战题](http://reversing.kr/challenge.php)
- [IOLI Crackme 逆向练习](https://github.com/Maijin/radare2-workshop-2015/tree/master/IOLI-crackme)
- [0x00sec 逆向与 Crackme 挑战合集](https://0x00sec.org/t/challenge-collection-reverse-engineering-and-crackme/3027)
- [恶意软件分析视频课程（YouTube）](https://www.youtube.com/watch?v=n06QSoICU6c&list=PLt9cUwGw6CYG2DSfjXEE3GotkQDa5b-6s)
- [免费二进制分析课程](https://maxkersten.nl/binary-analysis-course/)

## 代码去混淆 (Deobfuscation)

了解代码混淆及其应对方法：

- [了解恶意软件的代码混淆技术](https://www.vadesecure.com/en/blog/malware-analysis-understanding-code-obfuscation-techniques)
- [手动解包 Remcos 恶意软件](https://apr4h.github.io/2021-05-01-Manually-Unpacking-Remcos-Malware/)
- [使用 x64dbg 解包恶意软件](https://www.varonis.com/blog/x64dbg-unpack-malware)
- [YouTube 视频：代码去混淆演示](https://www.youtube.com/watch?v=bEsQ8UYioU4)
- [Black Hat 2007 会议论文](https://www.blackhat.com/presentations/bh-usa-07/Yason/Whitepaper/bh-usa-07-yason-WP.pdf)

## 反调试和反分析 (Anti-debug & Anti-analysis)

学习如何检测和应对反调试和反分析技术：

- [反调试与反仿真技术](https://wikileaks.org/vault7/document/2015-07-PoC-Anti_Debugging_and_Anti_Emulation/2015-07-PoC-Anti_Debugging_and_Anti_Emulation.pdf)
- [终极反逆向参考文献](https://anti-reversing.com/Downloads/Anti-Reversing/The_Ultimate_Anti-Reversing_Reference.pdf)
- [检查反调试和反分析技术](https://anti-debug.checkpoint.com/)
- [五种反调试技术](https://www.malwarebytes.com/blog/news/2014/09/five-anti-debugging-tricks-that-sometimes-fool-analysts)

## C++ 逆向工程

如果你对 C++ 逆向感兴趣，以下资源值得一看：

- [C++ 虚函数的逆向分析](https://alschwalm.com/blog/static/2016/12/17/reversing-c-virtual-functions/)
- [Black Hat 2007 的 C++ 逆向分析白皮书](https://www.blackhat.com/presentations/bh-dc-07/Sabanal_Yason/Paper/bh-dc-07-Sabanal_Yason-WP.pdf)

## Windows 系统研究

要研究 Windows 系统的内部机制，推荐以下资源：

- [Windows 内核学习博客](https://de-engineer.github.io)
- [微软官方的 Windows 内核书籍](https://learn.microsoft.com/en-us/sysinternals/resources/windows-internals)
- [Windows 进程内部分析](https://www.youtube.com/watch?v=4AkzIbmI3q4&feature=emb_title)
- [ReactOS 源代码 (Windows 的开源实现)](https://doxygen.reactos.org/index.html)
- [设备驱动程序、内核和 HAL 中的关键数据结构](https://codemachine.com/articles/kernel_structures.html)
- [EPROCESS 数据结构解析](https://info-savvy.com/understanding-eprocess-structure/)
- [线程挂起机制的内部分析](https://ntopcode.wordpress.com/2018/01/16/anatomy-of-the-thread-suspension-mechanism-in-windows-windows-internals/)

## 高质量的 Windows 研究博客

一些高质量的博客和网站，专注于 Windows 研究和逆向工程：

- [Secret.club](https://secret.club/)
- [wumb0.in](https://t.co/TQttGxnkVF)
- [voidsec.com](https://t.co/Rz220SAwbt)
- [PopPopRet 博客](https://poppopret.blogspot.com/?m=1)
- [RageStorm 博客](https://www.ragestorm.net/blogs/?cat=13)

## 其他资源

更多与逆向工程和 Windows 研究相关的资料：

- [GuidedHacking 论坛](https://guidedhacking.com)
- [编译器优化对逆向工程的影响](https://www.msreverseengineering.com/blog/2014/6/23/compiler-optimizations-for-reverse-engineers)
- [Windows 内核驱动程序的静态逆向工程方法](https://posts.specterops.io/methodology-for-static-reverse-engineering-of-windows-kernel-drivers-3115b2efed83)
- [Windows 容器逆向工程](https://unit42.paloaltonetworks.com/what-i-learned-from-reverse-engineering-windows-containers/)

## 符号执行 (Symbolic Execution)

如果你想深入学习符号执行，以下资源将对你有帮助：

- [SMT 解算器介绍](https://de-engineer.github.io/SMT-Solvers/)
- [YouTube 上的符号执行课程](https://www.youtube.com/watch?v=yRVZPvHYHzw)
- [符号执行课程 (OpenSecurityTraining2)](https://p.ost2.fyi/courses/course-v1:OpenSecurityTraining2+RE3201_symexec+2021_V1/course)
- [如何学习 z3 解算器](https://github.com/ViRb3/z3-python-ctf)

这些资源涵盖了从基础到高级的逆向工程和 Windows 内核研究方法。无论你是刚刚入门，还是想深入研究 Windows 系统的工作原理，这些资源都能为你提供丰富的学习材料。

