# 导入一个搜索UID的工具
from tools.search_tool import get_UID

# 导入所需的库
from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent, Tool
from langchain.agents import AgentType

# 通过LangChain代理找到UID的函数
def lookup_V(flower_type: str) :
    # 初始化大模型
    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

    # 寻找UID的模板
    template = """given the {flower} I want you to get a related 微博 UID.
                  Your answer should contain only a UID.
                  The URL always starts with https://weibo.com/u/
                  for example, if https://weibo.com/u/1669879400 is her 微博, then 1669879400 is her UID
                  This is only the example don't give me this, but the actual UID"""
    # 完整的提示模板
    prompt_template = PromptTemplate(
        input_variables=["flower"], template=template
    )

    # 代理的工具
    tools = [
        Tool(
            name="Crawl Google for 微博 page",
            func=get_UID,
            description="useful for when you need get the 微博 UID",
        )
    ]

    # 初始化代理
    agent = initialize_agent(
        tools, 
        llm, 
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, 
        verbose=True
    )

    # 返回找到的UID
    ID = agent.run(prompt_template.format_prompt(flower=flower_type))

    return ID