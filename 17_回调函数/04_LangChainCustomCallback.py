# 设置OpenAI API密钥
import os
os.environ["OPENAI_API_KEY"] = 'Your OpenAI Key'

import asyncio
from typing import Any, Dict, List

from langchain.chat_models import ChatOpenAI
from langchain.schema import LLMResult, HumanMessage
from langchain.callbacks.base import AsyncCallbackHandler, BaseCallbackHandler

# 创建同步回调处理器
class MyFlowerShopSyncHandler(BaseCallbackHandler):
    def on_llm_new_token(self, token: str, **kwargs) -> None:
        print(f"获取花卉数据: token: {token}")

# 创建异步回调处理器
class MyFlowerShopAsyncHandler(AsyncCallbackHandler):

    async def on_llm_start(
        self, serialized: Dict[str, Any], prompts: List[str], **kwargs: Any
    ) -> None:
        print("正在获取花卉数据...")
        await asyncio.sleep(0.5)  # 模拟异步操作
        print("花卉数据获取完毕。提供建议...")

    async def on_llm_end(self, response: LLMResult, **kwargs: Any) -> None:
        print("整理花卉建议...")
        await asyncio.sleep(0.5)  # 模拟异步操作
        print("祝你今天愉快！")

# 主要的异步函数
async def main():
    flower_shop_chat = ChatOpenAI(
        max_tokens=100,
        streaming=True,
        callbacks=[MyFlowerShopSyncHandler(), MyFlowerShopAsyncHandler()],
    )

    # 异步生成聊天回复
    await flower_shop_chat.agenerate([[HumanMessage(content="哪种花卉最适合生日？只简单说3种，不超过50字")]])

# 运行主异步函数
asyncio.run(main())
