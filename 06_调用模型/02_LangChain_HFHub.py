'''欢迎来到LangChain实战课
https://time.geekbang.org/column/intro/100617601
作者 黄佳'''
# 导入HuggingFace API Token
import os
os.environ['HUGGINGFACEHUB_API_TOKEN'] = 'Your HuggingFace API Token'

# 导入必要的库
from langchain import PromptTemplate, HuggingFaceHub, LLMChain

# 初始化HF LLM
llm = HuggingFaceHub(
    repo_id="google/flan-t5-small",
    #repo_id="meta-llama/Llama-2-7b-chat-hf",
)

# 创建简单的question-answering提示模板
template = """Question: {question}
              Answer: """

# 创建Prompt          
prompt = PromptTemplate(template=template, input_variables=["question"])

# 调用LLM Chain --- 我们以后会详细讲LLM Chain
llm_chain = LLMChain(
    prompt=prompt,
    llm=llm
)

# 准备问题
question = "Rose is which type of flower?"

# 调用模型并返回结果
print(llm_chain.run(question))