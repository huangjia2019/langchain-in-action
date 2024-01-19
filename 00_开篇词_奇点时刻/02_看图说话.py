'''欢迎来到LangChain实战课
https://time.geekbang.org/column/intro/100617601
作者 黄佳'''

from dotenv import load_dotenv  # 用于加载环境变量
load_dotenv()  # 加载 .env 文件中的环境变量

#---- Part 0 导入所需要的类
import os
import requests
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration
from langchain.tools import BaseTool
# from langchain import OpenAI
from langchain_openai import OpenAI
from langchain.agents import initialize_agent, AgentType
# from langchain.agents import create_react_agent # 未来需要改成下面的设计

#---- Part I 初始化图像字幕生成模型
# 指定要使用的工具模型（HuggingFace中的image-caption模型）
hf_model = "Salesforce/blip-image-captioning-large"

# 初始化处理器和工具模型
# 预处理器将准备图像供模型使用
processor = BlipProcessor.from_pretrained(hf_model)
# 然后我们初始化工具模型本身
model = BlipForConditionalGeneration.from_pretrained(hf_model)

#---- Part II 定义图像字幕生成工具类
class ImageCapTool(BaseTool):
   
    name = "Image captioner"
    description = "为图片创作说明文案."

    def _run(self, url: str):
        # 下载图像并将其转换为PIL对象
        image = Image.open(requests.get(url, stream=True).raw).convert('RGB')
        # 预处理图像
        inputs = processor(image, return_tensors="pt")
        # 生成字幕
        out = model.generate(**inputs, max_new_tokens=20)
        # 获取字幕
        caption = processor.decode(out[0], skip_special_tokens=True)
        return caption
    
    def _arun(self, query: str):
        raise NotImplementedError("This tool does not support async")

#---- PartIII 初始化并运行LangChain智能体
# 设置OpenAI的API密钥并初始化大语言模型（OpenAI的Text模型）
# os.environ["OPENAI_API_KEY"] = '你的OpenAI API Key'
llm = OpenAI(temperature=0.2)

# 使用工具初始化智能体并运行
tools = [ImageCapTool()]
agent = initialize_agent(
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    tools=tools,
    llm=llm,
    verbose=True,
)
# 未来需要改成下面的设计
# agent = create_react_agent(
#     tools=tools,
#     llm=llm,
# )
img_url = 'https://mir-s3-cdn-cf.behance.net/project_modules/hd/eec79e20058499.563190744f903.jpg'
# agent.run(input=f"{img_url}\n请创作合适的中文推广文案")
agent.invoke(input=f"{img_url}\n请创作合适的中文推广文案")