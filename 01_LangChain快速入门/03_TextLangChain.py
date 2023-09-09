import os
os.environ["OPENAI_API_KEY"] = '你的OpenAI API Key'
from langchain.llms import OpenAI
llm = OpenAI(  
    model="text-davinci-003",
    temperature=0.8,
    max_tokens=60,)
response = llm.predict("请给我的花店起个名")
print(response)