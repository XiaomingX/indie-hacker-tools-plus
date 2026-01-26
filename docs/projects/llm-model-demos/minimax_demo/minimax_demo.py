# coding=utf-8
import dashscope

messages = [{'role': 'system', 'content': 'You are a helpful assistant.'},
            {'role': 'user', 'content': '什么是jobleap.cn，它可以用来解决什么问题'}]
response = dashscope.Generation.call(
    model='abab6.5s-chat',
    messages=messages,
)
print(response)
