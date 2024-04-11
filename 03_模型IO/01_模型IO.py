'''欢迎来到LangChain实战课
https://time.geekbang.org/column/intro/100617601
作者 黄佳'''
from dotenv import load_dotenv  # 用于加载环境变量
load_dotenv()  # 加载 .env 文件中的环境变量

# 导入LangChain中的提示模板
from langchain.prompts import PromptTemplate
# 创建原始模板
template = """您是一位专业的鲜花店文案撰写员。\n
对于售价为 {price} 元的 {flower_name} ，您能提供一个吸引人的简短描述吗？
"""
# 根据原始模板创建LangChain提示模板
prompt = PromptTemplate.from_template(template) 
# 打印LangChain提示模板的内容
print(prompt)

# 设置OpenAI API Key
# import os
# os.environ["OPENAI_API_KEY"] = '你的OpenAI API Key'

# 导入LangChain中的OpenAI模型接口
from langchain_openai import OpenAI
# 创建模型实例
model = OpenAI(model_name='gpt-3.5-turbo-instruct')
# 输入提示
input = prompt.format(flower_name=["玫瑰"], price='50')
# 得到模型的输出
output = model.invoke(input)
# 打印输出内容
print(output)
