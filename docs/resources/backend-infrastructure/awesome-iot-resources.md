# Awesome-IoT：物联网开发实用资源大全
本文整理了物联网（IoT）开发全流程的核心资源，涵盖框架、库、工具、平台等关键领域。已剔除维护停滞、活跃度低的内容，补充了主流工具的核心优势与适用场景，力求新手也能快速理解和选用。


## 一、开发框架（Framework）
框架是IoT开发的“基础骨架”，直接决定开发效率与设备兼容性。以下为当前活跃且实用的主流框架：

### 常用框架
- **[ESP-IDF](https://github.com/espressif/esp-idf)**  
  乐鑫（Espressif）官方原生框架，专为ESP32系列芯片（ESP32/ESP32-S3/ESP32-C6等）设计。  
  ✅ 核心功能：原生支持Wi-Fi 6、BLE 5.3、Zigbee等无线协议，集成低功耗管理、OTA固件升级、安全加密（Secure Boot）等核心能力。  
  📌 适用场景：工业传感器、智能家居设备、可穿戴设备等需要双模无线连接的开发。

- **[Johnny-Five](https://github.com/rwaldron/johnny-five)**  
  基于JavaScript的“零门槛”IoT/机器人框架，底层依赖Firmata协议。  
  ✅ 核心优势：无需掌握C/C++，前端开发者可直接用JS控制硬件；支持Arduino、Raspberry Pi等200+硬件。  
  📌 适用场景：创客项目、入门级机器人（如避障小车）、快速原型验证。

- **[GoBot](https://github.com/hybridgroup/gobot)**  
  基于Golang的工业级IoT/机器人框架，以“并发高效”著称。  
  ✅ 核心优势：继承Go语言的跨平台与并发特性，支持ROS（机器人操作系统）、MQTT等协议，兼容树莓派、STM32等硬件。  
  📌 适用场景：工业设备控制、分布式机器人系统、高并发IoT网关。

- **[Serverless](https://github.com/serverless/serverless)**  
  主流无服务器开发框架，摆脱服务器运维负担。  
  ✅ 核心升级：不再局限于AWS Lambda，现已支持Azure Functions、Google Cloud Functions等主流云厂商；提供自动扩缩容、按需付费能力。  
  📌 适用场景：IoT设备数据的云端处理（如日志分析、规则引擎触发）、轻量化API后端。

- **[Sming](https://github.com/SmingHub/Sming)**  
  面向嵌入式设备的高性能异步C/C++框架。  
  ✅ 核心优势：异步架构可高效处理多网络请求（如同时连接Wi-Fi和MQTT），内存占用低（最低支持256KB RAM），兼容ESP8266/ESP32。  
  📌 适用场景：资源受限的低功耗设备（如智能门锁、环境监测节点）。


## 二、核心库（Library）
库是框架的“补充模块”，专注于单一功能（如协议解析、硬件控制），可直接嵌入项目快速实现需求。

### 1. 硬件开发SDK
SDK（软件开发工具包）是芯片/平台厂商提供的“官方工具集”，兼容性最佳。
- **[ESP8266 Arduino Core](https://github.com/esp8266/Arduino)**  
  ESP8266芯片的Arduino适配核心库，让ESP8266可以直接用Arduino IDE开发。  
  ✅ 核心优势：无缝对接Arduino生态（上万种现成库），支持NodeMCU、Wemos D1等主流开发板，新手易上手。  
  📌 适用场景：入门级Wi-Fi设备（如智能插座、温湿度传感器）。

- **[Azure IoT Device SDKs](https://github.com/Azure/azure-iot-sdks)**  
  微软Azure IoT的官方设备SDK，原名“Azure IoT SDK”，现已全面升级。  
  ✅ 核心功能：支持MQTT/AMQP/HTTP协议，提供设备孪生、OTA更新、安全认证等能力，覆盖C/C++、Python、Java等多语言。  
  📌 适用场景：需要对接Azure云平台的工业设备、智能家居产品。

### 2. Arduino生态常用库
Arduino是IoT入门首选平台，以下库是高频刚需：
- **[ArduinoJson](https://github.com/bblanchon/ArduinoJson)**  
  嵌入式领域最流行的JSON解析库（当前v7版本）。  
  ✅ 核心优势：解析速度快，内存占用极低（最小仅需200字节RAM），支持JSON序列化/反序列化。  
  📌 适用场景：设备与云端的JSON数据交互（如上报温湿度、接收控制指令）。

- **[WiringPi](https://github.com/WiringPi/WiringPi)**  
  树莓派的GPIO（通用输入输出）控制库，语法类似Arduino。  
  ✅ 核心优势：简化引脚操作（如数字读写、PWM输出），支持I2C、SPI等通信协议。  
  📌 适用场景：树莓派控制LED、舵机、传感器等硬件（注：树莓派4B+需适配新版系统）。

### 3. 底层开发库
面向需要自定义硬件逻辑或物理仿真的场景：
- **[Simbody](https://github.com/simbody/simbody)**  
  高性能多体动力学C++库，专注物理仿真。  
  ✅ 核心功能：模拟刚体运动、碰撞检测、力反馈等物理特性，精度接近专业仿真工具。  
  📌 适用场景：机器人运动规划、无人机姿态控制等需要物理建模的开发。


## 三、调试与桥接工具（原“App”分类优化）
这类工具用于设备调试、数据转发，是开发过程中的“得力助手”。
- **[MQTTX](https://github.com/emqx/MQTTX)**  
  跨平台MQTT协议调试工具（支持Windows/macOS/Linux）。  
  ✅ 核心功能：支持MQTT 3.1.1/5.0协议，可视化订阅/发布消息，自动保存连接配置，内置日志查看。  
  📌 适用场景：调试MQTT设备的连接、消息格式正确性（如验证传感器是否正确上报数据）。

- **[Theengs App](https://app.theengs.io)**  
  移动端BLE（蓝牙低功耗）转MQTT桥接工具。  
  ✅ 核心功能：自动扫描并连接90+种BLE传感器（如小米温湿度计、蓝牙血压计），将数据转发到MQTT broker。  
  📌 适用场景：没有Wi-Fi模块的BLE设备快速上云（如家庭环境监测）。

- **[Serial Studio](https://serial-studio.github.io/)**  
  补充新增：跨平台串口调试+数据可视化工具。  
  ✅ 核心功能：支持串口/网络（TCP/UDP）通信，可将设备输出的原始数据转为折线图、仪表盘等可视化图表。  
  📌 适用场景：实时查看传感器数据变化（如监测温度波动曲线）。


## 四、嵌入式操作系统（OS）
IoT设备的“大脑”，负责资源调度、任务管理，尤其适合多任务场景。
- **[AWS IoT Device OS](https://github.com/aws/amazon-freertos)**  
  原名“Amazon FreeRTOS”，专为微控制器（MCU）设计的轻量OS。  
  ✅ 核心功能：集成AWS云原生安全（设备认证、数据加密），支持低功耗休眠，兼容ESP32、STM32、Nordic等主流MCU。  
  📌 适用场景：需要对接AWS的低功耗边缘设备（如农业土壤传感器）。

- **[RIOT](https://github.com/RIOT-OS/RIOT)**  
  开源“友好型”IoT操作系统，以“轻量+实时”为核心。  
  ✅ 核心优势：内存占用仅2KB起，支持LoRa、BLE、6LoWPAN等协议，社区活跃（定期更新）。  
  📌 适用场景：低功耗广域网（LPWAN）设备、传感器网络节点。

- **[Zephyr](https://github.com/zephyrproject-rtos/zephyr)**  
  当前最热门的嵌入式RTOS之一，由Linux基金会主导。  
  ✅ 核心升级：支持ARM/x86/RISC-V等150+架构，模块化设计可按需裁剪，集成蓝牙、Wi-Fi、CAN总线等常用协议栈。  
  📌 适用场景：工业IoT、可穿戴设备、汽车电子等高性能需求场景。

- **[Contiki-NG](https://github.com/contiki-ng/contiki-ng)**  
  原“Contiki”的升级版本，专注低功耗广域网。  
  ✅ 核心功能：支持IPv6/6LoWPAN，内存占用极低（适合8位MCU）。  
  📌 适用场景：学术研究（如传感器网络）、老旧低功耗设备开发。


## 五、安全工具（Security）
IoT设备安全至关重要，以下工具用于检测漏洞、防护攻击：
- **[IoTSeeker](https://github.com/rapid7/IoTSeeker)**  
  网络IoT设备扫描工具，由安全厂商Rapid7开发。  
  ✅ 核心功能：扫描局域网内的IoT设备，检测是否使用默认密码、开放高危端口等隐患。  
  📌 适用场景：企业/家庭IoT网络安全审计（**需获得网络授权，禁止非法扫描**）。

- **[nShield](https://github.com/fnzv/nShield)**  
  轻量级IoT设备防DDoS工具，基于iptables实现。  
  ✅ 核心功能：拦截恶意流量，限制单IP连接数，资源占用低（适合边缘网关）。  
  📌 适用场景：小型IoT网关、暴露在公网的设备防护。


## 六、IoT平台
平台是连接“设备-云端-应用”的核心枢纽，提供设备管理、数据流转等能力。
| 平台名称                | 链接                                  | 核心功能                                  | 适用场景                          |
|-------------------------|---------------------------------------|-------------------------------------------|-----------------------------------|
| **Blynk IoT Cloud**     | https://blynk.io/                     | 可视化APP搭建（拖拽组件），支持多设备管理  | 创客项目、个人智能家居控制        |
| **ThingsBoard**         | https://github.com/thingsboard/thingsboard | 设备管理、规则引擎、数据可视化，支持边缘计算 | 工业IoT、中型企业级项目            |
| **Toit**                | https://toit.io/                      | 基于Toit语言（类Python），集成OTA与设备管理 | 快速开发量产级IoT设备              |
| **HiveMQ**              | https://github.com/hivemq/hivemq-community-edition | 轻量MQTT broker，支持集群部署            | 中小型MQTT设备网络                |
| **阿里云IoT平台**       | https://www.aliyun.com/product/iot     | 设备接入、数据存储、AI分析，生态完善      | 国内量产设备、电商智能硬件项目    |


## 七、云服务（Cloud Services）
主流云厂商提供的IoT专属服务，无需自建服务器即可实现云端能力。
- **[AWS IoT Core](https://aws.amazon.com/iot/)**  
  亚马逊IoT核心服务，支持千万级设备接入。  
  ✅ 核心功能：设备认证、消息路由、与AWS Lambda（数据处理）、S3（存储）无缝集成。

- **[Azure IoT Hub](https://azure.microsoft.com/en-us/services/iot-hub/)**  
  微软IoT云枢纽，主打“企业级可靠性”。  
  ✅ 核心功能：设备孪生（远程查看设备状态）、OTA更新、与Power BI（可视化）集成。

- **[Google Cloud IoT Core](https://cloud.google.com/solutions/iot)**  
  谷歌云IoT服务，擅长“数据与AI结合”。  
  ✅ 核心功能：对接BigQuery（数据分析）、TensorFlow（AI建模），支持边缘计算节点。

- **[EMQX Cloud](https://www.emqx.com/en/cloud)**  
  全托管MQTT服务，专注“设备连接”。  
  ✅ 核心功能：支持千万级并发，全球节点覆盖，按需扩容，无需维护broker。


## 八、数据可视化
将IoT设备产生的“原始数据”转为直观图表，便于监控与分析。
- **[ECharts](https://github.com/ecomfe/echarts)**  
  百度开源的全能可视化库，新手友好。  
  ✅ 核心功能：支持折线图、仪表盘、地理热力图等50+图表，可实时更新数据（适合IoT监控面板）。

- **[D3.js](https://github.com/mbostock/d3)**  
  专业级数据可视化库，灵活性极强。  
  ✅ 核心功能：直接操作DOM，可定制任意复杂图表（如设备状态流转图），但需掌握JavaScript基础。

- **[Freeboard](https://github.com/Freeboard/freeboard)**  
  开源IoT仪表盘搭建工具，“零代码”上手。  
  ✅ 核心功能：拖拽组件即可搭建仪表盘，支持MQTT、HTTP等数据源接入（适合快速展示传感器数据）。


## 九、硬件开发
IoT开发的“物理载体”，从入门到工业级的主流硬件选型：
- **[Arduino](https://www.arduino.cc/)**  
  入门首选开源硬件平台，生态极其丰富。  
  ✅ 主流型号：Uno R4（性能升级）、Nano ESP32（集成Wi-Fi/BLE）；支持传感器、执行器等模块“即插即用”。

- **[Raspberry Pi](https://www.raspberrypi.org/)**  
  迷你计算机，适合“强算力”场景。  
  ✅ 主流型号：Pi 5（高性能，可做网关）、Pi Pico（微控制器，低功耗）；适用场景：设备控制、小型服务器、边缘计算。

- **[ESP32/ESP8266](https://www.espressif.com/)**  
  乐鑫主力芯片，性价比之王。  
  ✅ ESP8266：单Wi-Fi，适合入门；ESP32：Wi-Fi+BLE双模，性能强（如ESP32-S3支持AI加速），是量产设备首选。

- **[NodeMCU](http://www.nodemcu.com/)**  
  基于ESP8266/ESP32的开发板，支持Lua编程。  
  ✅ 核心优势：固件内置网络库，用几行Lua代码即可实现Wi-Fi连接（适合快速验证网络功能）。


## 十、中间件
连接“设备-平台-应用”的“胶水层”，处理数据流转、业务逻辑。
- **[Kuzzle](https://github.com/kuzzleio/kuzzle)**  
  开源IoT后端中间件，主打“实时与地理能力”。  
  ✅ 核心功能：支持实时消息推送、地理围栏（设备进出区域报警）、数据加密。

- **[ThingSpeak](https://github.com/iobridge/ThingSpeak)**  
  轻量IoT数据存储与分析平台。  
  ✅ 核心功能：支持HTTP/MQTT接入数据，集成MATLAB分析工具（适合学生做数据实验）。

- **[Apache Kafka](https://kafka.apache.org/)**  
  补充新增：高吞吐消息队列，适合大规模数据流转。  
  ✅ 核心功能：支持百万级消息/秒，持久化存储，用于工业IoT的设备数据流分发。


## 十一、开发工具
提升开发效率的“利器”，涵盖编译、调试、管理全流程。
- **[PlatformIO](https://github.com/platformio/platformio)**  
  跨平台IoT开发工具，支持VS Code插件。  
  ✅ 核心功能：集成库管理（自动下载依赖）、多平台编译（Arduino/ESP-IDF/STM32）、远程调试。

- **[ESP-IDF Extension for VS Code](https://marketplace.visualstudio.com/items?itemName=espressif.esp-idf-extension)**  
  补充新增：乐鑫官方VS Code插件。  
  ✅ 核心功能：一键搭建ESP-IDF开发环境，支持代码补全、烧录、调试（ESP32开发必备）。


## 十二、家庭自动化平台
专注于“智能家居设备联动”，适合个人或小型场景部署。
- **[Home Assistant](https://github.com/balloob/home-assistant)**  
  全球最火的开源家庭自动化平台，本地化部署更安全。  
  ✅ 核心功能：支持5000+品牌设备（小米、苹果、三星等），可自定义自动化规则（如“开门自动开灯”）。

- **[Homebridge](https://github.com/nfarina/homebridge)**  
  让非HomeKit设备支持苹果HomeKit的“桥接服务器”。  
  ✅ 核心功能：适配小米、华为等非苹果设备，通过Siri控制（如“嘿 Siri，关闭客厅灯”）。

- **[Node-RED](https://github.com/node-red/node-red)**  
  可视化编程工具，“零代码”连接设备与服务。  
  ✅ 核心功能：拖拽节点即可实现逻辑（如“温湿度超过30℃触发风扇”），支持对接MQTT、云平台。

- **[openHAB](https://github.com/openhab/openhab-distro)**  
  无厂商锁定的开源家庭自动化软件，适合技术玩家。  
  ✅ 核心功能：支持多协议（Zigbee、Z-Wave、MQTT），可深度定制设备交互逻辑。


## 十三、嵌入式语言与工具
针对“资源受限设备”的编程语言与实用工具：

### 编程语言
- **[MicroPython](https://github.com/micropython/micropython)**  
  微控制器版Python，兼顾开发效率与性能。  
  ✅ 核心优势：语法与Python一致，支持ESP32、Pi Pico等设备，内置网络库（如uMQTT）。

- **[PikaScript](https://github.com/pikasTech/pikaScript)**  
  超轻量Python引擎，专为“极小内存设备”设计。  
  ✅ 核心优势：内存占用仅4KB起，支持8位/16位MCU（如STM32F103、51单片机）。

### 实用工具
- **[Sonoff-Tasmota](https://github.com/arendst/Sonoff-Tasmota)**  
  开源智能设备固件，适配多品牌设备。  
  ✅ 核心功能：替换原厂固件，支持Web控制、MQTT接入、OTA更新（如改造小米智能插座）。

- **[ESP8266 Deauther](https://github.com/spacehuhn/esp8266_deauther)**  
  网络测试工具，**仅用于合法授权的网络审计**。  
  ✅ 核心功能：检测Wi-Fi网络安全性，模拟断开设备连接（用于测试自家网络防护能力）。


## 十四、网络协议库（MQTT为主）
MQTT是IoT设备通信的“通用语言”，以下是主流协议实现库：
- **[EMQX](https://github.com/emqx/emqx)**  
  超高扩展性MQTT broker（消息代理），社区活跃（星数20k+）。  
  ✅ 核心功能：支持MQTT 5.0，千万级设备并发连接，分布式部署，适合企业级场景。

- **[Mosquitto](https://github.com/eclipse/mosquitto)**  
  轻量MQTT broker，适合小型部署。  
  ✅ 核心优势：内存占用低（仅几百KB），支持Windows/Linux，新手易搭建。

- **[MQTT.js](https://github.com/mqttjs/MQTT.js)**  
  浏览器/Node.js的MQTT客户端库。  
  ✅ 核心功能：支持浏览器端直连MQTT broker（如Web仪表盘接收设备数据）。

- **[Paho MQTT](https://www.eclipse.org/paho/)**  
  补充新增：Eclipse官方多语言MQTT客户端库。  
  ✅ 核心优势：支持C/C++、Python、Java等10+语言，兼容性强（量产设备首选）。


## 十五、机器人开发
IoT与机器人的交叉领域，涵盖仿真与控制工具：
- **[ROS 2](https://docs.ros.org/en/humble/index.html)**  
  主流机器人操作系统，支持IoT设备集成。  
  ✅ 核心功能：分布式节点通信，兼容MQTT、ZMQ等协议，可连接传感器、执行器（如无人机、机械臂）。

- **[AirSim](https://github.com/microsoft/AirSim)**  
  基于Unreal/Unity的无人机/自动驾驶仿真工具。  
  ✅ 核心功能：模拟真实物理环境（风速、障碍物），可测试IoT设备的远程控制算法。

- **[hubot](https://github.com/github/hubot)**  
  可定制的自动化机器人，适合团队协作。  
  ✅ 核心功能：支持Slack、Discord等平台，可编写脚本实现IoT设备状态查询（如“hubot，查客厅温度”）。


## 十六、学习资源
从入门到进阶的IoT学习渠道，涵盖课程与资讯：

### 免费课程
- [物联网专项课程（密歇根大学）](https://www.coursera.org/specializations/iot) - Coursera经典课程，从硬件到云端全流程讲解。
- [嵌入式系统与IoT安全（北京大学）](https://www.icourse163.org/course/PKU-1460454163) - 国内慕课，聚焦设备安全与通信协议。
- [ESP32开发实战（电子发烧友）](https://www.elecfans.com/column/esp32/) - 实操导向，适合新手快速上手硬件开发。

### 实用网站
- [Eclipse IoT](https://iot.eclipse.org) - 开源IoT项目集合（如MQTT、数字孪生标准）。
- [IoT For All](https://www.iotforall.com/) - 全球IoT资讯平台，涵盖技术趋势与案例。
- [电子发烧友IoT频道](https://www.elecfans.com/iot/) - 国内IoT技术社区，提供方案与教程。


## 十七、数据分析与数字孪生
将IoT数据转化为“决策依据”，实现设备的虚拟映射：
- **[NetData](https://github.com/firehol/netdata)**  
  分布式实时监控工具，轻量且高效。  
  ✅ 核心功能：监控设备CPU、内存、网络等指标，秒级更新，支持MQTT数据接入。

- **[Eclipse Ditto](https://github.com/eclipse/ditto)**  
  开源数字孪生管理平台。  
  ✅ 核心功能：维护设备的虚拟镜像（数字孪生），支持设备状态同步与远程控制。

- **[Azure Digital Twins](https://azure.microsoft.com/en-us/products/digital-twins)**  
  补充新增：云原生数字孪生平台。  
  ✅ 核心功能：构建智能空间模型（如智慧工厂、智慧楼宇），关联多设备数据进行分析。


## 十八、AI与物联网（边缘AI）
将AI模型部署到IoT设备端，实现低延迟智能决策：
- **[TensorFlow Lite for Microcontrollers](https://www.tensorflow.org/lite/microcontrollers)**  
  谷歌开源边缘AI框架，专为MCU设计。  
  ✅ 核心功能：支持在ESP32、STM32等设备上运行轻量AI模型（如手势识别、异常检测），内存占用低至16KB。

- **[PyTorch Mobile](https://pytorch.org/mobile/)**  
  PyTorch的移动端/边缘端部署工具。  
  ✅ 核心功能：将图像识别、预测模型压缩后部署到IoT设备（如智能摄像头的人脸检测）。  
  📌 适用场景：无需联网的本地智能设备（如防跌倒监测手环、工业异常检测传感器）。
