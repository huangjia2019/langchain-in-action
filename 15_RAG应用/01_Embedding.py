# 设置OpenAI的API密钥
import os
os.environ["OPENAI_API_KEY"] = 'Your OpenAI Key'

# 初始化Embedding类
from langchain.embeddings import OpenAIEmbeddings
embeddings_model = OpenAIEmbeddings()

# Embed文本
embeddings = embeddings_model.embed_documents(
    [
        "您好，有什么需要帮忙的吗？",
        "哦，你好！昨天我订的花几天送达",
        "请您提供一些订单号？",
        "12345678",
    ]
)
print(len(embeddings), len(embeddings[0]))

# Embed查询
embedded_query = embeddings_model.embed_query("刚才对话中的订单号是多少?")
print(embedded_query[:3])