# 基础导入（合并重复导入，保留核心依赖）
import argparse
import os
import sys
import asyncio
import logging
import toml
from typing import Dict, Any, Optional, List
from dotenv import load_dotenv
from pathlib import Path
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage


# ------------------------------
# 模块1：基础工具（配置/日志/LLM）
# ------------------------------
class Config:
    """简化配置类：仅保留「加载TOML」和「读取环境变量」核心功能"""
    def __init__(self, config_path: Optional[str] = None):
        load_dotenv()  # 加载.env文件的环境变量
        self.config_data = self._load_config(config_path)

    def _load_config(self, config_path: Optional[str]) -> Dict[str, Any]:
        """加载TOML配置文件，无则返回空字典"""
        if not config_path:
            return {}
        try:
            return toml.load(config_path)
        except Exception as e:
            print(f"配置文件加载失败：{e}")
            return {}

    def get(self, key_path: List[str], default: Any = None) -> Any:
        """读取嵌套配置（如["llm", "model"]），无则返回默认值"""
        value = self.config_data
        for key in key_path:
            if not isinstance(value, dict) or key not in value:
                return default
            value = value[key]
        return value


def setup_logger(name: str = "open-manus", level: str = "INFO") -> logging.Logger:
    """简化日志配置：仅保留控制台输出，去掉复杂的文件轮转"""
    logger = logging.getLogger(name)
    logger.setLevel(getattr(logging, level.upper(), logging.INFO))
    
    # 避免重复添加处理器
    if not logger.handlers:
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)
    
    return logger


class LLMManager:
    """简化LLM管理：去掉冗余方法，仅保留「初始化LLM」和「生成文本」核心功能"""
    def __init__(self, config: Config):
        self.config = config
        self.llm = self._init_llm()
        self.logger = setup_logger("llm-manager")

    def _init_llm(self) -> ChatOpenAI:
        """初始化OpenAI LLM：优先从配置读，其次读环境变量"""
        # 1. 读取配置/环境变量的关键参数
        api_key = self.config.get(["api", "openai_api_key"]) or os.getenv("OPENAI_API_KEY")
        model = self.config.get(["llm", "model"], "gpt-3.5-turbo")  # 用gpt-3.5降低门槛
        temperature = self.config.get(["llm", "temperature"], 0.7)

        # 2. 校验API Key
        if not api_key:
            raise ValueError("请在配置文件或环境变量中设置 OPENAI_API_KEY")

        # 3. 初始化LLM
        try:
            return ChatOpenAI(
                api_key=api_key,
                model=model,
                temperature=temperature,
                request_timeout=60
            )
        except Exception as e:
            raise Exception(f"LLM初始化失败：{e}")

    def generate_text(self, user_prompt: str, system_prompt: Optional[str] = None) -> str:
        """生成文本：支持系统提示词+用户提示词"""
        messages = []
        if system_prompt:
            messages.append(SystemMessage(content=system_prompt))
        messages.append(HumanMessage(content=user_prompt))

        try:
            self.logger.debug(f"向LLM发送请求：{user_prompt[:50]}...")
            return self.llm.invoke(messages).content
        except Exception as e:
            self.logger.error(f"LLM生成失败：{e}")
            return f"生成错误：{str(e)}"


# ------------------------------
# 模块2：核心Agent（Manus交互逻辑）
# ------------------------------
class Manus:
    """简化Manus类：去掉复杂的工具链和 artifact 处理，保留核心对话能力"""
    def __init__(self, config: Config):
        self.config = config
        self.llm_manager = LLMManager(config)
        self.logger = setup_logger("manus")
        self.system_prompt = """你是一个帮助用户解决问题的助手，回答简洁、准确，基于用户需求提供有用信息。"""

    async def chat(self, user_input: str) -> str:
        """异步聊天：处理用户输入，返回LLM响应"""
        if user_input.lower() in ["quit", "exit"]:
            self.logger.info("聊天结束")
            return "再见！"
        
        # 调用LLM生成响应
        self.logger.info(f"处理用户输入：{user_input[:30]}...")
        return self.llm_manager.generate_text(
            user_prompt=user_input,
            system_prompt=self.system_prompt
        )


# ------------------------------
# 模块3：运行入口（命令行+交互）
# ------------------------------
def parse_cli_args() -> argparse.Namespace:
    """简化命令行参数：仅保留「配置文件路径」和「日志级别」"""
    parser = argparse.ArgumentParser(description="OpenManus 简化版")
    parser.add_argument("--config", type=str, help="配置文件路径（TOML格式）")
    parser.add_argument("--log-level", type=str, default="INFO", help="日志级别（DEBUG/INFO/WARNING）")
    return parser.parse_args()


async def interactive_chat(manus: Manus):
    """交互式聊天：循环接收用户输入，直到输入quit"""
    print("=== Manus 交互式聊天（输入 quit 退出）===")
    while True:
        try:
            user_input = input("\n你：")
            response = await manus.chat(user_input)
            print(f"Manus：{response}")
            if user_input.lower() in ["quit", "exit"]:
                break
        except KeyboardInterrupt:
            print("\n\n聊天被中断，再见！")
            break


def main():
    """主函数：端到端流程（解析参数→初始化配置→初始化Manus→启动交互）"""
    # 1. 解析命令行参数
    args = parse_cli_args()

    # 2. 初始化配置和日志
    config = Config(args.config)
    logger = setup_logger(level=args.log_level)
    logger.info("开始初始化 Manus...")

    # 3. 初始化Manus（依赖配置和LLM）
    try:
        manus = Manus(config)
    except Exception as e:
        logger.error(f"Manus初始化失败：{e}")
        sys.exit(1)

    # 4. 启动交互式聊天
    asyncio.run(interactive_chat(manus))


if __name__ == "__main__":
    main()