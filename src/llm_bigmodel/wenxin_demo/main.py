from qianfan import ChatCompletion

# 2. 配置密钥（替换成你的AK和SK）
chat_client = ChatCompletion(
        ak="你的API Key",
        sk="你的Secret Key")
# 3. 调用文心X1.1，生成代码（prompt可根据需求修改）
response = chat_client.do(
        model="ernie-x1.1",  # 必须指定文心X1.1模型
        messages=[{"role": "user", "content": "生成一个Python脚本：打印1-10的平方，带注释"}])
# 4. 打印结果print("文心X1.1返回的代码：")
print(response["result"])