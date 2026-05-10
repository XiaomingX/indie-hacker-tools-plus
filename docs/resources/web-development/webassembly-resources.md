# WebAssembly (Wasm) 生态资源精选 (2026 Checklist)

> [!TIP]
> **Indie Hacker Insight**: 2026 年，Wasm 已不再是“实验性技术”，而是 **Web 性能优化的核武器**。
> - **场景选型**：计算密集型任务（图像处理、加密、音视频解码、复杂物理模拟）必须选 Wasm。
> - **语言首选**：**Rust** 是目前 Wasm 生态最成熟、工具链最完备的语言。
> - **跨平台**：利用 **WASI**，让你的 Wasm 代码不仅运行在浏览器，还能在服务器和边缘侧运行。

---

## 🏗️ 编译工具链 (Compilers & Toolchains)

- [ ] [**Rust + wasm-pack**](https://rustwasm.github.io/wasm-pack/) - **[首选]** Rust 转 Wasm 的一站式工具，支持一键打包发布到 npm。
- [ ] [**Emscripten**](https://emscripten.org/) - 将 C/C++ 遗留项目搬到 Web 的黄金标准，支持完整的 POSIX 接口。
- [ ] [**AssemblyScript**](https://www.assemblyscript.org/) - 使用类 TypeScript 语法编写 Wasm，JS 开发者的低门槛切入点。
- [ ] [**TinyGo**](https://tinygo.org/) - 专为 Wasm 优化的 Go 编译器，生成的二进制体积远小于官方 Go 编译器。

---

## 🚀 运行时与服务器端 (Runtimes & Non-Web)

- [ ] [**Wasmtime**](https://wasmtime.dev/) - Bytecode Alliance 主导的高性能 Wasm 运行时，符合 WASI 标准。
- [ ] [**Wasmer**](https://wasmer.io/) - 极其强大的跨平台运行时，支持在一个二进制文件中运行 Wasm、C++、Rust 等。
- [ ] [**Spin**](https://www.fermyon.com/spin) - 基于 Wasm 的 Serverless 框架，极速冷启动，是 Lambda 的强力竞争者。
- [ ] [**Worker1 (Cloudflare)**](https://workers.cloudflare.com/) - 边缘计算标配，原生支持 Wasm 模块，全球低延迟响应。

---

## 🛠️ 实用库与移植版 (Libraries & Ports)

- [ ] [**FFmpeg.wasm**](https://ffmpegwasm.netlify.app/) - 浏览器端的视频转码神器，无需服务器即可处理音视频流。
- [ ] [**OpenCV.js**](https://docs.opencv.org/4.x/d5/d10/tutorial_js_root.html) - 计算机视觉库的 Wasm 移植版，支持在网页端进行实时人脸识别。
- [ ] [**SQL.js**](https://sql.js.org/) - SQLite 的 Wasm 移植版，让你的单机 Web 应用拥有完整的关系型数据库能力。
- [ ] [**Squoosh**](https://squoosh.app/) - Google 出品的极致图片压缩工具，核心编码器全部基于 Wasm。

---

## 🔍 调试与性能分析 (Debug & Performance)

- [ ] [**WABT**](https://github.com/WebAssembly/wabt) - 官方二进制工具包，包含反编译（wasm2wat）和格式转换工具。
- [ ] [**Twiggy**](https://rustwasm.github.io/twiggy/) - Wasm 代码体积分析工具，精准找出占用空间的冗余代码。
- [ ] [**Chrome DevTools Wasm Debugger**](https://developer.chrome.com/docs/devtools/wasm/) - 现代浏览器已支持直接在 Wasm 源码上打断点调试。

---

## 💡 选型建议
1. **高性能 Web 前端组件**：选 **Rust** + **wasm-bindgen**。
2. **移植老牌 C++ 游戏/库**：选 **Emscripten**。
3. **构建极速 Edge 函数**：选 **Cloudflare Workers** + **Rust-Wasm**。
4. **轻量化数据处理（如 Excel/PDF）**：选 **AssemblyScript** 快速实现。
