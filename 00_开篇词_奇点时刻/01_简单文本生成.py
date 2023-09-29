'''欢迎来到LangChain实战课
https://time.geekbang.org/column/intro/100617601
作者 黄佳'''

import os
os.environ["OPENAI_API_KEY"] = '你的Open AI API Key'
from langchain.llms import OpenAI
llm = OpenAI(model_name="text-davinci-003",max_tokens=200)
text = llm("请给我写一句情人节红玫瑰的中文宣传语")
print(text)