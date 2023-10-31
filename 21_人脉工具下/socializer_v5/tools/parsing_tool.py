# 导入所需的类
from langchain.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import List

# 定义一个名为TextParsing的模型，描述了如何解析大V信息
class TextParsing(BaseModel):
    summary: str = Field(description="大V个人简介")  # 大V的简介或背景信息
    facts: List[str] = Field(description="大V的特点")  # 大V的一些显著特点或者事实
    interest: List[str] = Field(description="这个大V可能感兴趣的事情")  # 大V可能感兴趣的主题或活动
    letter: List[str] = Field(description="一篇联络这个大V的邮件")  # 联络大V的建议邮件内容

    # 将模型对象转换为字典
    def to_dict(self):
        return {
            "summary": self.summary,
            "facts": self.facts,
            "interest": self.interest,  
            "letter": self.letter,    
        }

# 创建一个基于Pydantic模型的解析器，用于将文本输出解析为特定的结构
letter_parser: PydanticOutputParser = PydanticOutputParser(
    pydantic_object=TextParsing
)