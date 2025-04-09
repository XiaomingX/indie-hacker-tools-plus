# coding=utf-8
import dashscope

messages = [{'role': 'system', 'content': 'You are a helpful assistant.'},
            {'role': 'user', 'content': '你是谁'}]
response = dashscope.Generation.call(
    model='abab6.5s-chat',
    messages=messages,
)
print(response)
