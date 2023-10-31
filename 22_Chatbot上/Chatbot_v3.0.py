# 导入所需的库
import os
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Qdrant
from langchain.memory import ConversationSummaryMemory
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain
from langchain.document_loaders import PyPDFLoader
from langchain.document_loaders import Docx2txtLoader
from langchain.document_loaders import TextLoader

# 设置OpenAI API密钥
os.environ["OPENAI_API_KEY"] = 'Your Key'  

# ChatBot类的实现-带检索功能
class ChatbotWithRetrieval:

    def __init__(self, dir):

        # 加载Documents
        base_dir = dir # 文档的存放目录
        documents = []
        for file in os.listdir(base_dir): 
            file_path = os.path.join(base_dir, file)
            if file.endswith('.pdf'):
                loader = PyPDFLoader(file_path)
                documents.extend(loader.load())
            elif file.endswith('.docx') or file.endswith('.doc'):
                loader = Docx2txtLoader(file_path)
                documents.extend(loader.load())
            elif file.endswith('.txt'):
                loader = TextLoader(file_path)
                documents.extend(loader.load())
        
        # 文本的分割
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=200, chunk_overlap=0)
        all_splits = text_splitter.split_documents(documents)
        
        # 向量数据库
        self.vectorstore = Qdrant.from_documents(
            documents=all_splits, # 以分块的文档
            embedding=OpenAIEmbeddings(), # 用OpenAI的Embedding Model做嵌入
            location=":memory:",  # in-memory 存储
            collection_name="my_documents",) # 指定collection_name
        
        # 初始化LLM
        self.llm = ChatOpenAI()
        
        # 初始化Memory
        self.memory = ConversationSummaryMemory(
            llm=self.llm, 
            memory_key="chat_history", 
            return_messages=True
            )
        
        # 设置Retrieval Chain
        retriever = self.vectorstore.as_retriever()
        self.qa = ConversationalRetrievalChain.from_llm(
            self.llm, 
            retriever=retriever, 
            memory=self.memory
            )

    # 交互对话的函数
    def chat_loop(self):
        print("Chatbot 已启动! 输入'exit'来退出程序。")
        while True:
            user_input = input("你: ")
            if user_input.lower() == 'exit':
                print("再见!")
                break
            # 调用 Retrieval Chain  
            response = self.qa(user_input)
            print(f"Chatbot: {response['answer']}")

if __name__ == "__main__":
    # 启动Chatbot
    folder = "OneFlower"
    bot = ChatbotWithRetrieval(folder)
    bot.chat_loop()
