# Awesome Rust

## 应用程序

* [alacritty](https://github.com/alacritty/alacritty) - 跨平台、GPU增强的终端模拟器。
* [boringtun](https://github.com/cloudflare/boringtun) - 用户态的WireGuard VPN实现。
* [deno](https://github.com/denoland/deno) - 使用V8和Tokio构建的安全JavaScript/TypeScript运行时。
* [mdBook](https://github.com/rust-lang/mdBook) - 命令行工具，用于从Markdown文件创建电子书。
* [Sniffnet](https://github.com/GyulyVGC/sniffnet) - 易于监控网络流量的跨平台应用。
* [wasmer](https://github.com/wasmerio/wasmer) - 支持WASI和Emscripten的安全、快速的WebAssembly运行时。
* [zellij](https://github.com/zellij-org/zellij) - 功能齐全的终端复用器。
* [wezterm](https://github.com/wez/wezterm) - GPU加速的跨平台终端模拟器和多路复用器。

## 音频与音乐

* [ncspot](https://github.com/hrkfdn/ncspot) - 跨平台的ncurses Spotify客户端。
* [Spotifyd](https://github.com/Spotifyd/spotifyd) - 开源的运行在UNIX系统下的Spotify客户端守护进程。

## 区块链

* [Foundry](https://github.com/foundry-rs/foundry) - 以太坊应用开发的模块化工具集。
* [ethers-rs](https://github.com/gakonst/ethers-rs) - 完整的以太坊和Celo库及钱包实现。
* [rust-bitcoin](https://github.com/rust-bitcoin/rust-bitcoin) - 支持比特币数据结构与网络消息的库。

## 数据库

* [sled](https://crates.io/crates/sled) - 现代嵌入式数据库，支持高效的数据操作。
* [tikv](https://github.com/tikv/tikv) - 分布式键值数据库。
* [Qdrant](https://github.com/qdrant/qdrant) - 支持向量相似性搜索的开源引擎。

## 文件管理

* [broot](https://github.com/Canop/broot) - 可视化和导航文件树的新方式。
* [xplr](https://github.com/sayanarijit/xplr) - 可自定义的快速TUI文件管理器。

## 游戏

* [Veloren](https://gitlab.com/veloren/veloren) - 开源的多人像素RPG游戏。

## 图形

* [ivanceras/svgbob](https://github.com/ivanceras/svgbob) - 将ASCII图形转换为SVG图形。
* [linebender/resvg](https://github.com/linebender/resvg) - SVG渲染库。

## 图像处理

* [oxipng](https://github.com/shssoichiro/oxipng) - 多线程PNG优化工具。

## 操作系统

* [redox-os/redox](https://gitlab.redox-os.org/redox-os/redox) - 以安全、稳定为目标的类Unix通用操作系统。

## 社交网络

* [Rustodon](https://github.com/rustodon/rustodon) - Mastodon兼容的社交网络服务器。

## 系统工具

* [zoxide](https://github.com/ajeetdsouza/zoxide) - 快速替代`cd`，自动学习用户路径使用习惯。
* [dust](https://github.com/bootandy/dust) - 更直观的`du`工具。
* [lsd](https://github.com/lsd-rs/lsd) - 一个美观的`ls`替代工具，带有图标和丰富颜色。
* [ripgrep](https://crates.io/crates/ripgrep) - 结合了grep速度与Silver Searcher的易用性。
* [procs](https://github.com/dalance/procs) - 现代化的替代`ps`工具。

## 视频

* [gyroflow](https://github.com/gyroflow/gyroflow) - 使用陀螺仪数据的视频稳定应用。

## 虚拟化

* [firecracker](https://github.com/firecracker-microvm/firecracker) - 轻量级虚拟机，用于容器工作负载。

### 构建系统

- [Cargo](https://crates.io/) - Rust 的包管理工具
  - [cargo-edit](https://crates.io/crates/cargo-edit) - 命令行添加、编辑依赖项
  - [cargo-generate](https://github.com/cargo-generate/cargo-generate) - 使用模板快速生成Rust项目
  - [cargo-make](https://crates.io/crates/cargo-make) - 任务管理和构建工具
  - [cargo-outdated](https://crates.io/crates/cargo-outdated) - 检查依赖项是否有更新
  - [cargo-release](https://crates.io/crates/cargo-release) - 发布 Rust 项目的工具
  - [cargo-update](https://crates.io/crates/cargo-update) - 更新已安装的 Cargo 可执行文件
  - [cargo-watch](https://crates.io/crates/cargo-watch) - 源代码更改时自动编译项目
  - [cargo-expand](https://github.com/dtolnay/cargo-expand) - 展开宏，查看完整生成代码

### 调试工具

- [GDB](https://www.gnu.org/software/gdb/)
  - [gdbgui](https://github.com/cs01/gdbgui) - 浏览器界面的 GDB 前端
- [LLDB](https://lldb.llvm.org/)
  - [CodeLLDB](https://marketplace.visualstudio.com/items?itemName=vadimcn.vscode-lldb) - Visual Studio Code 的 LLDB 扩展

### 部署

- Docker
  - [rust-lang/docker-rust](https://github.com/rust-lang/docker-rust) - 官方 Rust Docker 镜像
  - [cargo-chef](https://github.com/LukeMathWalker/cargo-chef) - 缓存依赖的工具，提高 Docker 构建速度

### 格式化工具

- [rustfmt](https://github.com/rust-lang/rustfmt) - Rust 官方代码格式化工具
- [dprint](https://github.com/dprint/dprint) - 可插拔的代码格式化平台

### 集成开发环境（IDE）

- [Visual Studio Code](https://code.visualstudio.com/)
  - [rust-analyzer](https://marketplace.visualstudio.com/items?itemName=rust-lang.rust-analyzer) - Rust 语言服务器扩展，替代 RLS
- [IntelliJ IDEA](https://www.jetbrains.com/idea/)
  - [intellij-rust](https://github.com/intellij-rust/intellij-rust) - IntelliJ 平台的 Rust 插件

### 数据库

- [SQLite](https://www.sqlite.org/)
  - [rusqlite](https://crates.io/crates/rusqlite) - SQLite 的 Rust 绑定

### 测试框架

- [cargo-tarpaulin](https://crates.io/crates/cargo-tarpaulin) - 代码覆盖率工具
- [mockall](https://github.com/asomers/mockall) - Rust 的 mock 对象库，用于单元测试

### 分布式系统
- **Apache Kafka**：
  - [fede1024/rust-rdkafka](https://github.com/fede1024/rust-rdkafka)：Kafka Rust 客户端（基于 librdkafka）
  - [kafka-rust/kafka-rust](https://github.com/kafka-rust/kafka-rust)：Apache Kafka 的 Rust 客户端
- **HDFS**：
  - [hyunsik/hdfs-rs](https://github.com/hyunsik/hdfs-rs)：HDFS 的 Rust 绑定

### eBPF
- [aya/aya-rs](https://github.com/aya-rs/aya)：为开发人员优化的 eBPF 工具库
- [libbpf/libbpf-rs](https://github.com/libbpf/libbpf-rs)：eBPF 的轻量级工具库

### 邮件处理
- [lettre/lettre](https://github.com/lettre/lettre)：SMTP 库，用于发送邮件
- [jdrouet/mrml](https://github.com/jdrouet/mrml)：用于生成通用邮件模板的库

### 编码
- **JSON**：
  - [serde-rs/json](https://github.com/serde-rs/json)：用于序列化和反序列化 JSON 的工具
- **CSV**：
  - [BurntSushi/rust-csv](https://github.com/BurntSushi/rust-csv)：快速、灵活的 CSV 读取和写入工具

### 文件系统
- [OpenDAL](https://github.com/apache/opendal)：统一的数据访问层，支持从多种存储服务检索数据
- [Stebalien/tempfile](https://github.com/Stebalien/tempfile)：处理临时文件的库

### 游戏开发
- **游戏引擎**：
  - [Bevy](https://github.com/bevyengine/bevy)：数据驱动的游戏引擎
  - [ggez](https://github.com/ggez/ggez)：用于创建 2D 游戏的轻量级框架
  - [Fyrox](https://fyrox.rs/)：3D 游戏引擎

### 图形处理
- [image-rs/image](https://github.com/image-rs/image)：基础图像处理功能和格式转换

### GUI
- [emilk/egui](https://github.com/emilk/egui)：简单、快速的跨平台即时模式 GUI 库
- [iced-rs/iced](https://github.com/iced-rs/iced)：跨平台 GUI 库，灵感来源于 Elm

### 网络编程
- [hyperium/hyper](https://github.com/hyperium/hyper)：用于 HTTP 的 Rust 实现
- [tokio-rs/axum](https://github.com/tokio-rs/axum)：基于 Tokio 的模块化 Web 框架

### 解析
- [pest-parser/pest](https://github.com/pest-parser/pest)：优雅的解析器生成器
- [rust-bakery/nom](https://github.com/rust-bakery/nom)：解析组合器库

### 系统信息
- [GuillaumeGomez/sysinfo](https://github.com/GuillaumeGomez/sysinfo)：跨平台系统信息获取库

### 日志
- [rust-lang/log](https://github.com/rust-lang/log)：Rust 标准日志库
- [tokio-rs/tracing](https://github.com/tokio-rs/tracing)：用于结构化日志和错误处理的应用级跟踪框架
