'''欢迎来到LangChain实战课
https://time.geekbang.org/column/intro/100617601
作者 黄佳'''
# 导入HuggingFace API Token
import os
os.environ['HUGGINGFACEHUB_API_TOKEN'] = 'Your HuggingFace API Token'

# 导入必要的库
from transformers import AutoTokenizer, AutoModelForCausalLM

# 加载预训练模型的分词器
tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-2-7b-chat-hf")

# 加载预训练的模型
# 使用 device_map 参数将模型自动加载到可用的硬件设备上，例如GPU
model = AutoModelForCausalLM.from_pretrained(
          "meta-llama/Llama-2-7b-chat-hf", 
          device_map = 'auto')  

# 定义一个提示，希望模型基于此提示生成故事
prompt = "请给我讲个玫瑰的爱情故事?"

# 使用分词器将提示转化为模型可以理解的格式，并将其移动到GPU上
inputs = tokenizer(prompt, return_tensors="pt").to("cuda")

# 使用模型生成文本，设置最大生成令牌数为2000
outputs = model.generate(inputs["input_ids"], max_new_tokens=2000)

# 将生成的令牌解码成文本，并跳过任何特殊的令牌，例如[CLS], [SEP]等
response = tokenizer.decode(outputs[0], skip_special_tokens=True)

# 打印生成的响应
print(response)