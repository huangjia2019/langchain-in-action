'''欢迎来到LangChain实战课
https://time.geekbang.org/column/intro/100617601
作者 黄佳'''

# import os
# os.environ["OPENAI_API_KEY"] = '你的OpenAI API Key'

from langchain_openai import OpenAI
llm = OpenAI(  
    model="gpt-3.5-turbo-instruct",
    temperature=0.8,
    max_tokens=60,)
response = llm.predict("请给我的花店起个名")
print(response)