'''欢迎来到LangChain实战课
https://time.geekbang.org/column/intro/100617601
作者 黄佳'''
from dotenv import load_dotenv  # 用于加载环境变量
load_dotenv()  # 加载 .env 文件中的环境变量
import openai # 导入OpenAI
# openai.api_key = '你的OpenAI API Key' # API Key

prompt_text = "您是一位专业的鲜花店文案撰写员。对于售价为{}元的{}，您能提供一个吸引人的简短描述吗？" # 设置提示

flowers = ["玫瑰", "百合", "康乃馨"]
prices = ["50", "30", "20"]

# 循环调用Text模型的Completion方法，生成文案
for flower, price in zip(flowers, prices):
    prompt = prompt_text.format(price, flower)
    response = openai.completions.create(
        model="gpt-3.5-turbo-instruct",
        prompt=prompt,
        max_tokens=100
    )
    print(response.choices[0].text.strip()) # 输出文案