'''欢迎来到LangChain实战课
https://time.geekbang.org/column/intro/100617601
作者 黄佳'''
# 导入需要的库
from llama_cpp import Llama
from typing import Optional, List, Mapping, Any
from langchain.llms.base import LLM

# 模型的名称和路径常量
MODEL_NAME = 'llama-2-7b-chat.ggmlv3.q4_K_S.bin'
MODEL_PATH = '/home/huangj/03_Llama/'

# 自定义的LLM类，继承自基础LLM类
class CustomLLM(LLM):
    model_name = MODEL_NAME

    # 该方法使用Llama库调用模型生成回复
    def _call(self, prompt: str, stop: Optional[List[str]] = None) -> str:
        prompt_length = len(prompt) + 5
        # 初始化Llama模型，指定模型路径和线程数
        llm = Llama(model_path=MODEL_PATH+MODEL_NAME, n_threads=4)
        # 使用Llama模型生成回复
        response = llm(f"Q: {prompt} A: ", max_tokens=256)
        
        # 从返回的回复中提取文本部分
        output = response['choices'][0]['text'].replace('A: ', '').strip()

        # 返回生成的回复，同时剔除了问题部分和额外字符
        return output[prompt_length:]

    # 返回模型的标识参数，这里只是返回模型的名称
    @property
    def _identifying_params(self) -> Mapping[str, Any]:
        return {"name_of_model": self.model_name}

    # 返回模型的类型，这里是"custom"
    @property
    def _llm_type(self) -> str:
        return "custom"
    

# 初始化自定义LLM类
llm = CustomLLM()

# 使用自定义LLM生成一个回复
result = llm("昨天有一个客户抱怨他买了花给女朋友之后，两天花就枯了，你说作为客服我应该怎么解释？")

# 打印生成的回复
print(result)