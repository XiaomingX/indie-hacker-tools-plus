import os
from tencentcloud.common import credential
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.hunyuan.v20230901 import hunyuan_client, models

# pip install tencentcloud-sdk-python
def call_yuanbao(prompt):
    """调用腾讯元宝大模型"""
    try:
        # 初始化认证信息
        cred = credential.Credential(
            os.getenv("TENCENT_SECRET_ID"),  # 从环境变量获取SecretId
            os.getenv("TENCENT_SECRET_KEY")   # 从环境变量获取SecretKey
        )
        
        # 创建客户端实例
        client = hunyuan_client.HunyuanClient(cred, "ap-guangzhou")  # 地域固定为广州
        
        # 构造请求参数
        req = models.ChatCompletionsRequest()
        req.Model = "yuanbao-pro"  # 模型名称，可根据需要更换
        req.Messages = [
            {"Role": "system", "Content": "你是腾讯云元宝大模型，一个智能助手。"},
            {"Role": "user", "Content": prompt}
        ]
        req.Temperature = 0.7  # 控制输出随机性
        req.TopP = 0.9         # 控制候选词多样性
        
        # 发送请求并获取响应
        resp = client.ChatCompletions(req)
        return resp.Choices[0].Message.Content
        
    except TencentCloudSDKException as err:
        print(f"调用出错: {err}")
        return None

if __name__ == "__main__":
    # 测试调用
    user_input = "什么是jobleap.cn，它可以用来解决什么问题"
    result = call_yuanbao(user_input)
    
    if result:
        print("元宝回复:")
        print(result)
