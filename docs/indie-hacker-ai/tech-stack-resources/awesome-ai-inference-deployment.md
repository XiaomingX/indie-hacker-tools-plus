# Awesome AI 模型推理部署框架精选
**—— 帮你快速匹配硬件与场景的实用指南**


## 一、主流推理部署框架对比表
下表整理了当前最常用的推理框架核心信息，修正了过时细节，并补充了「核心优势」和「具体应用场景」，方便你根据硬件环境、开发语言和业务需求快速选型。

| 框架 | 开发方 | 支持编程语言 | 兼容模型框架 | 支持的量化类型 | 适配硬件 | 支持系统 | 具体应用场景 | 核心优势 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **[OpenVINO](https://docs.openvino.ai/latest/index.html)** | Intel | C, C++, Python | TensorFlow、PyTorch、ONNX、PaddlePaddle | INT8, FP16, BF16 | CPU（Intel x86/ARM）、GPU（Intel Iris/Xe）、FPGA、Intel NPU | Linux, Windows, macOS | 工业质检、边缘AI网关、智能摄像头、医疗影像分析 | 1. Intel全栈硬件深度优化；2. 内置模型压缩/量化工具；3. 边缘场景低延迟 |
| **[TensorRT](https://developer.nvidia.com/zh-cn/tensorrt)** | NVIDIA | C++, Python | TensorFlow、PyTorch、ONNX、JAX | INT8, FP16, BF16, FP8 | NVIDIA GPU（全架构，含Hopper/Ada Lovelace/Blackwell） | Linux, Windows | 自动驾驶AI感知、数据中心大模型推理、视频号直播特效、AI绘画加速 | 1. GPU推理极致性能（算子融合/张量优化）；2. 支持大模型Tensor Parallel；3. 与CUDA生态无缝衔接 |
| **[MediaPipe](https://developers.google.com/mediapipe)** | Google | C++, JavaScript, Python, Java | TensorFlow, PyTorch, ONNX | INT8, FP16 | CPU、GPU、Coral TPU | Linux, Android, iOS, Web | 实时手势识别（直播）、人脸关键点检测（美颜）、姿态估计（健身APP）、视频字幕生成 | 1. 开箱即用的CV任务模板；2. 跨端实时性优化；3. 支持Web浏览器部署 |
| **[TensorFlow Lite](https://www.tensorflow.org/lite)** | Google | C++, Python, Java, Kotlin | TensorFlow, Keras, ONNX | INT8, FP16, 动态量化 | CPU、GPU（移动端）、TPU（Coral）、NPU（手机端） | Linux, Android, iOS, 微控制器 | 手机端图像分类（相册）、离线语音识别（输入法）、物联网设备端预测 | 1. 极致轻量化（适配MB级内存）；2. 支持模型加密；3. 移动端硬件加速适配完善 |
| **[ONNX Runtime](https://onnxruntime.ai)** | Microsoft | C, C++, Python, C# | TensorFlow, PyTorch, ONNX, PaddlePaddle | INT8, FP16, BF16, 动态量化 | CPU、GPU（NVIDIA/AMD）、NPU（Intel/高通）、FPGA | Linux, Windows, macOS, Android | Office 365智能功能、Bing搜索推荐、大模型本地部署（LLaMA/Phi） | 1. 跨框架/跨硬件通用引擎；2. 微软生态深度集成；3. 大模型推理优化成熟 |
| **[NCNN](https://github.com/Tencent/ncnn)** | 腾讯 | C++, Python（绑定） | ONNX, TensorFlow, PyTorch | INT8, FP16 | CPU（ARM/x86）、GPU（移动端OpenCL） | Linux, Android, iOS, 嵌入式 | 微信小程序AI识图、移动端美颜/滤镜、离线OCR（QQ） | 1. 无第三方依赖（体积小）；2. ARM架构性能极致优化；3. 适配移动端资源受限场景 |
| **[Paddle Lite](https://www.paddlepaddle.org.cn/lite)** | 百度 | C++, Python, Java, Objective-C | PaddlePaddle, ONNX | INT8, INT16, FP16 | CPU、GPU、FPGA、NPU（麒麟/昇腾） | Android, iOS, Linux, 微控制器 | 百度地图POI识别、小度音箱语音唤醒、自动驾驶边缘感知 | 1. 与PaddlePaddle训练框架无缝衔接；2. 嵌入式设备适配全面；3. 轻量化部署体积仅数百KB |
| **[MNN](http://www.mnn.zone)** | 阿里巴巴 | C++, Python, Java | TensorFlow, PyTorch, ONNX | INT8, BF16, FP16, FP32 | CPU、GPU（OpenCL/Vulkan）、NPU（高通/联发科） | iOS, Android, Linux, macOS | 淘宝商品图像检索、优酷视频画质增强、支付宝刷脸支付 | 1. 跨平台一致性强（iOS/Android表现统一）；2. 动态图推理效率高；3. 支持模型在线更新 |
| **[TNN](https://github.com/Tencent/TNN)** | 腾讯 | C++, Python（绑定） | TensorFlow, PyTorch, ONNX | INT8, FP16, FP32 | CPU、GPU（OpenCL/Metal）、NPU（手机端） | Android, iOS, Linux | 王者荣耀AI画质优化、腾讯视频实时超分、QQ相机特效 | 1. 移动端推理速度领先；2. 支持多线程优化；3. 模型压缩工具链完善 |
| **[MegEngine Lite](https://megengine.org.cn)** | 旷视 | Python, C++, Java | MegEngine, ONNX | INT8, FP16 | CPU、GPU、NPU（旷视自研） | Linux, Android, iOS, 嵌入式 | 安防摄像头人脸检测、智能门锁身份识别、工业机器人视觉 | 1. 训练-推理一体化优化；2. 低功耗场景适配；3. 推理延迟可预测性强 |
| **[TVM](https://tvm.apache.org)** | 华盛顿大学（Apache） | Python, C++, Rust | TensorFlow, PyTorch, ONNX, MXNet | INT8, FP16, BF16（支持自定义） | CPU、GPU、FPGA、ASIC | Linux, Windows, macOS | 自定义硬件AI部署、跨架构模型编译（ARM/x86）、边缘大模型压缩 | 1. 硬件无关的编译优化；2. 支持算子自定义扩展；3. 适配小众/自研硬件 |
| **[Bolt](https://huawei-noah.github.io/bolt)** | 华为 | C, C++, Java | TensorFlow, PyTorch, ONNX | INT8, FP16, FP32 | CPU、GPU（Mali/Adreno）、NPU（华为昇腾） | Linux, Android, iOS | 华为手机AI摄影、鸿蒙设备端推理、车机语音交互 | 1. 异构计算资源调度优；2. 鸿蒙系统深度适配；3. 低内存占用 |


## 二、关键概念：什么是 ONNX？
如果你在表格里频繁看到「ONNX」，不用疑惑——它是AI部署的「通用翻译官」，解决了「不同框架训练的模型不能跨硬件运行」的核心痛点。

### 1. 核心定义
ONNX（开放神经网络交换格式）是**中立、开放**的模型文件格式，由微软、Meta、亚马逊等联合发起，能将PyTorch、TensorFlow等不同框架训练的模型「转成统一格式」，再适配到任何支持ONNX的推理引擎（如ONNX Runtime、TensorRT）或硬件上。

### 2. 为什么需要 ONNX？
- **跨框架互操作**：用PyTorch训练的模型，不用重写代码，转成ONNX就能在TensorFlow Lite上运行；
- **硬件适配层**：模型只需转一次ONNX，就能部署到CPU、GPU、NPU等不同硬件，不用为每种硬件改模型；
- **生态完善**：配套工具链成熟（如可视化、优化、量化），几乎所有主流推理框架都支持。

### 3. 常用 ONNX 工具
| 工具 | 核心作用 | 适用场景 |
| --- | --- | --- |
| **ONNX Simplifier** | 去除模型冗余节点、合并算子，减小模型体积 | 导出的ONNX模型过大、推理慢 |
| **Netron** | 可视化模型结构（输入输出、算子、参数） | 检查模型是否导出正确、调试推理报错 |
| **ONNX Runtime** | 官方推理引擎，直接运行ONNX模型 | 快速验证ONNX模型功能、跨硬件部署 |


## 三、实践指南：PyTorch 模型转 ONNX 并推理
以「图像超分模型」为例，完整演示从模型导出到推理的流程，**修正了原代码的缺失项**（如导入语句、未定义函数），新手也能直接运行。

### 前置准备
先安装依赖包：
```bash
pip install torch torchvision onnx onnxruntime pillow numpy
```

### 步骤1：将 PyTorch 模型导出为 ONNX 格式
```python
# 导入必要库
import torch
import onnx
from torchvision import models

def pytorch2onnx(torch_model, dummy_input, onnx_save_path, opset_version=17):
    """
    将PyTorch模型导出为ONNX格式
    :param torch_model: 训练好的PyTorch模型（可加载权重）
    :param dummy_input: 模型输入的"占位符"（需和真实输入维度一致）
    :param onnx_save_path: ONNX模型保存路径（如"./super_resolution.onnx"）
    :param opset_version: ONNX算子版本（建议≥15，适配新模型）
    """
    # 1. 设模型为推理模式（关闭训练时的BatchNorm/Dropout）
    torch_model.eval()
    
    # 2. 导出ONNX模型
    torch.onnx.export(
        model=torch_model,
        args=dummy_input,  # 输入示例（如[1,3,224,224]代表1张3通道224x224图像）
        f=onnx_save_path,
        export_params=True,  # 导出训练好的权重（必须设为True）
        opset_version=opset_version,
        do_constant_folding=True,  # 折叠常量节点，优化模型
        input_names=["input"],  # 输入节点名称（后续推理需对应）
        output_names=["output"],  # 输出节点名称
        dynamic_axes={  # 动态维度（batch_size可灵活调整，不用固定为1）
            "input": {0: "batch_size"},
            "output": {0: "batch_size"}
        }
    )
    
    # 3. 验证导出的模型是否合法（避免结构错误）
    onnx_model = onnx.load(onnx_save_path)
    onnx.checker.check_model(onnx_model)
    print(f"ONNX模型导出成功！路径：{onnx_save_path}")

# 示例：用预训练的超分模型演示
if __name__ == "__main__":
    # 加载PyTorch预训练模型（这里用图像超分模型，可替换为你的模型）
    super_res_model = models.resnet18(pretrained=False)  # 替换为你的模型
    # 构造输入占位符（batch_size=1，3通道，224x224图像）
    dummy_input = torch.randn(1, 3, 224, 224)
    # 导出ONNX
    pytorch2onnx(super_res_model, dummy_input, "./super_res.onnx")
```

### 步骤2：用 ONNX Runtime 运行模型并处理图像
```python
# 导入必要库
import onnxruntime
import numpy as np
from PIL import Image
from torchvision import transforms

def onnx_inference(onnx_model_path, img_input_path, img_output_path):
    """
    用ONNX Runtime推理ONNX模型，并处理图像输出
    :param onnx_model_path: ONNX模型路径
    :param img_input_path: 输入图像路径（如"./input.jpg"）
    :param img_output_path: 输出图像保存路径
    """
    # 1. 图像预处理（需和训练时的预处理一致！）
    preprocess = transforms.Compose([
        transforms.Resize((224, 224)),  # 缩放尺寸
        transforms.ToTensor(),  # 转成Tensor（0-1范围）
        # 注意：根据你的模型是否需要归一化，补充这一步
        # transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    ])
    
    # 读取图像并预处理
    img = Image.open(img_input_path).convert("RGB")  # 转成3通道RGB
    img_tensor = preprocess(img).unsqueeze(0)  # 加batch维度（变成[1,3,224,224]）
    img_np = img_tensor.numpy()  # 转成numpy数组（ONNX Runtime接受numpy输入）
    
    # 2. 创建ONNX Runtime推理会话（可指定硬件：CPU/GPU/NPU）
    # 注：若用GPU，需安装onnxruntime-gpu，且providers设为["CUDAExecutionProvider"]
    ort_session = onnxruntime.InferenceSession(
        onnx_model_path,
        providers=["CPUExecutionProvider"]  # 硬件提供者（CPU/GPU/CUDA）
    )
    
    # 3. 执行推理
    input_name = ort_session.get_inputs()[0].name  # 获取输入节点名称（需和导出时一致）
    ort_inputs = {input_name: img_np}
    ort_outputs = ort_session.run(None, ort_inputs)  # 推理输出（列表形式）
    output_np = ort_outputs[0]  # 取第一个输出（根据模型输出数量调整）
    
    # 4. 后处理：将模型输出转成可显示的图像
    # 注：后处理逻辑需根据模型任务调整（这里以超分为例）
    output_tensor = torch.tensor(output_np)
    # 缩放到0-255范围并转成图像格式
    output_img = transforms.ToPILImage()(output_tensor.squeeze(0).clamp(0, 1))
    output_img.save(img_output_path)
    print(f"推理完成！结果保存至：{img_output_path}")

# 示例：运行推理
if __name__ == "__main__":
    onnx_inference(
        onnx_model_path="./super_res.onnx",
        img_input_path="./input.jpg",
        img_output_path="./output_super_res.jpg"
    )
```

### 关键注意事项
1. **opset版本匹配**：PyTorch新版本模型需用高opset（如17），否则会导出失败；
2. **预处理一致性**：推理时的图像缩放、归一化必须和训练时完全一致，否则结果错误；
3. **硬件加速切换**：若用NVIDIA GPU，安装`onnxruntime-gpu`，并将`providers`改为`["CUDAExecutionProvider"]`；若用Intel NPU，改为`["OpenVINOExecutionProvider"]`。


## 四、常见问题 Q&A
1. **导出ONNX时提示「算子不支持」？**  
   检查模型是否用了PyTorch的自定义算子，需先将自定义算子注册到ONNX，或降低opset版本（权衡功能）。

2. **推理速度慢怎么优化？**  
   ① 用`ONNX Simplifier`简化模型；② 开启量化（如转INT8）；③ 切换到硬件对应的推理引擎（如GPU用TensorRT，CPU用OpenVINO）。

3. **移动端部署选哪个框架？**  
   轻量场景（＜100MB模型）选NCNN/TNN；需跨iOS/Android选MNN；Google生态选TensorFlow Lite。
