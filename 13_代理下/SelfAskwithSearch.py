# 设置OpenAI和SERPAPI的API密钥
import os
os.environ["OPENAI_API_KEY"] = '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'
os.environ["SERPAPI_API_KEY"] = '3f880ddf94585cfc847b255b54355e5b0453620e5e94e980c904d50a7145cd04'

from langchain import OpenAI, SerpAPIWrapper 
from langchain.agents import initialize_agent, Tool
from langchain.agents import AgentType

llm = OpenAI(temperature=0)
search = SerpAPIWrapper()
tools = [
    Tool(
        name="Intermediate Answer", 
        func=search.run,
        description="useful for when you need to ask with search",
    )
]

self_ask_with_search = initialize_agent(
    tools, llm, agent=AgentType.SELF_ASK_WITH_SEARCH, verbose=True
)
self_ask_with_search.run(
    "使用玫瑰作为国花的国家的首都是哪里?"  
)