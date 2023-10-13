import os
os.environ["OPENAI_API_KEY"] = 'Your OpenAI Key'

# 导入langchain的实用工具和相关的模块
from langchain.utilities import SQLDatabase
from langchain.llms import OpenAI
from langchain_experimental.sql import SQLDatabaseChain

# 连接到FlowerShop数据库（之前我们使用的是Chinook.db）
db = SQLDatabase.from_uri("sqlite:///FlowerShop.db")

# 创建OpenAI的低级语言模型（LLM）实例，这里我们设置温度为0，意味着模型输出会更加确定性
llm = OpenAI(temperature=0, verbose=True)

# 创建SQL数据库链实例，它允许我们使用LLM来查询SQL数据库
db_chain = SQLDatabaseChain.from_llm(llm, db, verbose=True)

# 运行与鲜花运营相关的问题
response = db_chain.run("有多少种不同的鲜花？")
print(response)

response = db_chain.run("哪种鲜花的存货数量最少？")
print(response)

response = db_chain.run("平均销售价格是多少？")
print(response)

response = db_chain.run("从法国进口的鲜花有多少种？")
print(response)

response = db_chain.run("哪种鲜花的销售量最高？")
print(response)


'''> Entering new SQLDatabaseChain chain...
有多少种不同的鲜花？
SQLQuery:SELECT COUNT(DISTINCT "Name") FROM "Flowers";
SQLResult: [(5,)]
Answer:有5种不同的鲜花。
> Finished chain.
有5种不同的鲜花。


> Entering new SQLDatabaseChain chain...
哪种鲜花的存货数量最少？
SQLQuery:SELECT "Name", "StockQuantity" FROM "Flowers" ORDER BY "StockQuantity" ASC LIMIT 5;
SQLResult: [('Orchid', 50), ('Lily', 80), ('Rose', 100), ('Daisy', 120), ('Tulip', 150)]
Answer:Orchid的存货数量最少。
> Finished chain.
Orchid的存货数量最少。


> Entering new SQLDatabaseChain chain...
平均销售价格是多少？
SQLQuery:SELECT AVG("SalePrice") FROM "Flowers";
SQLResult: [(2.66,)]
Answer:平均销售价格是2.66。
> Finished chain.
平均销售价格是2.66。


> Entering new SQLDatabaseChain chain...
从法国进口的鲜花有多少种？
SQLQuery:SELECT COUNT(*) FROM "Flowers" WHERE "Source" = 'France';
SQLResult: [(1,)]
Answer:从法国进口的鲜花有1种。
> Finished chain.
从法国进口的鲜花有1种。


> Entering new SQLDatabaseChain chain...
哪种鲜花的销售量最高？
SQLQuery:SELECT "Name", "SoldQuantity" FROM "Flowers" ORDER BY "SoldQuantity" DESC LIMIT 5;
SQLResult: [('Tulip', 25), ('Daisy', 15), ('Rose', 10), ('Lily', 5), ('Orchid', 2)]
Answer:Tulip的销售量最高。
> Finished chain.
Tulip的销售量最高。'''
