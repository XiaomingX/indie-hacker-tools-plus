import streamlit as st
import pandas as pd
import numpy as np

# 设置页面标题和图标
st.set_page_config(page_title="Streamlit 快速 Demo", page_icon="🌟")

# 页面标题
st.title("🎉 Streamlit 快速 Demo")

# 输入框
name = st.text_input("请输入你的名字：", "")

# 显示输入内容
if name:
    st.write(f"👋 你好, {name}!")

# 滑块
age = st.slider("请选择你的年龄：", 0, 100, 25)

# 显示滑块值
st.write(f"🧓 你的年龄是：{age}")

# 数据表格
st.subheader("📊 数据表格展示")
data = pd.DataFrame(
    np.random.randn(10, 3),
    columns=["列1", "列2", "列3"]
)
st.dataframe(data)

# 图表
st.subheader("📈 折线图")
st.line_chart(data)

# 侧边栏
st.sidebar.header("侧边栏选项")
selected_option = st.sidebar.selectbox(
    "选择一个选项：",
    ["选项1", "选项2", "选项3"]
)

st.sidebar.write(f"你选择了：{selected_option}")

# 文件上传
st.subheader("📂 文件上传")
uploaded_file = st.file_uploader("上传文件：", type=["csv", "txt"])

if uploaded_file is not None:
    file_data = pd.read_csv(uploaded_file)
    st.write("文件内容：")
    st.dataframe(file_data)