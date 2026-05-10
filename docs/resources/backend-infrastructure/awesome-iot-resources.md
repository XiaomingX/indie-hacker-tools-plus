# 物联网 (IoT) 全栈开发资源精选 (2026 Checklist)

> [!TIP]
> **Indie Hacker Insight**: 2026 年，物联网已不再是简单的“联网”，而是 **"端侧智能"** 与 **"协议互通"** 的闭环。
> - **标准互通**：强制关注 **Matter** 协议，这是打破智能家居厂商墙壁、实现跨生态控制的唯一正解。
> - **边缘 AI**：利用 **TensorFlow Lite for Microcontrollers**，在不到 10 元的 ESP32 芯片上即可实现语音唤醒与异常检测。
> - **低功耗通信**：对于远距离采集场景，**LoRaWAN** 和 **NB-IoT** 是平衡成本与功耗的最佳选择。

---

## 🏗️ 核心框架与硬件选型 (Frameworks & Hardware)

- [ ] [**ESP-IDF**](https://github.com/espressif/esp-idf) - **[量产首选]** 乐鑫官方框架，深度支持 ESP32 全系列，包含 Matter 和 Wi-Fi 6 协议栈。
- [ ] [**MicroPython**](https://micropython.org/) - 极大地降低了硬件开发门槛，像写 Python 脚本一样控制 GPIO 和网络。
- [ ] [**Zephyr RTOS**](https://zephyrproject.org/) - 针对工业级产品，提供极致的模块化与多架构支持（ARM, RISC-V）。
- [ ] [**Raspberry Pi Pico 2**](https://www.raspberrypi.com/documentation/microcontrollers/) - 基于双核 RISC-V 架构，是开发超低功耗、高性能嵌入式应用的平衡之选。

---

## ⚡ 通信协议与调试 (Protocols & Debugging)

- [ ] [**EMQX**](https://github.com/emqx/emqx) - 全球最流行的 MQTT 消息服务器，支持千万级设备并发连接。
- [ ] [**MQTTX**](https://mqttx.app/) - 跨平台 MQTT 调试工具，UI 精美且功能强大。
- [ ] [**Home Assistant**](https://www.home-assistant.io/) - 开源家庭自动化枢纽，支持 2000+ 品牌设备联动。
- [ ] [**Wireshark**](https://www.wireshark.org/) - 深度分析 TCP/UDP 和 MQTT 报文的必备利器。

---

## 🚀 边缘 AI 与数据可视化 (Edge AI & Vision)

- [ ] [**TensorFlow Lite for MCU**](https://www.tensorflow.org/lite/microcontrollers) - 在微控制器上部署深度学习模型，实现手势识别、语音唤醒等功能。
- [ ] [**ThingsBoard**](https://thingsboard.io/) - 开源 IoT 平台，提供强大的可视化仪表盘与规则引擎。
- [ ] [**Grafana**](https://grafana.com/) - 配合 InfluxDB，是展示 IoT 实时指标数据的行业标准。

---

## 🛡️ 安全与固件管理 (Security & OTA)

- [ ] [**Velero for IoT**](https://velero.io/) - 设备配置与元数据的备份与恢复方案。
- [ ] [**UpdateHub**](https://updatehub.io/) - 专业的 OTA (Over-the-Air) 固件升级管理平台，支持增量更新。
- [ ] [**Trivy (Container Scanning)**](https://github.com/aquasecurity/trivy) - 如果你在网关端运行容器，必装 Trivy 以扫描镜像漏洞。

---

## 💡 选型建议
1. **构建个人智能家居系统**：选 **Home Assistant** + **ESP32 (ESPHome)** + **Zigbee/Matter**。
2. **构建工业级远程监控系统**：选 **STM32/ESP32** + **MQTT** + **ThingsBoard**。
3. **实现极致功耗的传感器节点**：选 **Nordic nRF52 系列** + **Zephyr RTOS**。
4. **快速验证 IoT 原型**：选 **Node-RED** 可视化编排逻辑。
