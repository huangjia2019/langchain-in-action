# 导入所需要的库
from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from tools.parsing_tool import letter_parser


# 生成文案的函数
def generate_letter(information):

    # 设计提示模板
    letter_template = """
         下面是这个人的微博信息 {information}
         请你帮我:
         1. 写一个简单的总结
         2. 挑两件有趣的特点说一说
         3. 找一些他比较感兴趣的事情
         4. 写一篇热情洋溢的介绍信
         \n{format_instructions}"""
    
    prompt_template = PromptTemplate(
        input_variables=["information"],
        template=letter_template,
        partial_variables={
            "format_instructions": letter_parser.get_format_instructions()
        },         
    )

    # 初始化大模型
    llm = ChatOpenAI(model_name="gpt-3.5-turbo")    

    # 初始化链
    chain = LLMChain(llm=llm, prompt=prompt_template)

    # 生成文案
    result = chain.run(information = information)
    return result