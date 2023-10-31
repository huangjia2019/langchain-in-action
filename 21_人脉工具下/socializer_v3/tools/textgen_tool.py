# 导入所需要的库
from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain


# 生成文案的函数
def generate_letter(information):

    # 设计提示模板
    ice_breaker_template = """
         下面是这个人的微博信息 {information}
         请你帮我:
         1. 写一个简单的总结
         2. 挑两件有趣的事情说一说
         3. 找一些他比较感兴趣的事情
         4. 写一篇热情洋溢的介绍信
     """ 
    summary_prompt_template = PromptTemplate(
        input_variables=["information"],
        template=ice_breaker_template
    )

    # 初始化大模型
    llm = ChatOpenAI(model_name="gpt-3.5-turbo")    

    # 初始化链
    chain = LLMChain(llm=llm, prompt=summary_prompt_template)

    # 生成文案
    result = chain.run(information = information)
    return result