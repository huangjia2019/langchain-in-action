# 设置OpenAI的API密钥
import os
os.environ["OPENAI_API_KEY"] = 'Your OpenAI Key'

# 导入文档加载器模块，并使用TextLoader来加载文本文件
from langchain.document_loaders import TextLoader
loader = TextLoader('./OneFlower/易速鲜花花语大全.txt', encoding='utf8')

# 使用VectorstoreIndexCreator来从加载器创建索引
from langchain.indexes import VectorstoreIndexCreator
index = VectorstoreIndexCreator().from_loaders([loader])

# 定义查询字符串, 使用创建的索引执行查询
query = "玫瑰花的花语是什么？"
result = index.query(query)
print(result) # 打印查询结果


# 替换成你所需要的工具
from langchain.text_splitter import CharacterTextSplitter
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
embeddings = OpenAIEmbeddings()
index_creator = VectorstoreIndexCreator(
    vectorstore_cls=Chroma,
    embedding=OpenAIEmbeddings(),
    text_splitter=CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
)