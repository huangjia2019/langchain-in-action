'''欢迎来到LangChain实战课
https://time.geekbang.org/column/intro/100617601
作者 黄佳'''

import os
os.environ["OPENAI_API_KEY"] = '你的OpenAI API Key'

import openai
# openai.api_key = '你的OpenAI API Key'

response = openai.Completion.create(
  model="text-davinci-003",
  temperature=0.5,
  max_tokens=100,
  prompt="请给我的花店起个名")

print(response.choices[0].text.strip())