# 导入sqlite3库，它是Python内置的轻量级数据库。
import sqlite3

# 连接到数据库
conn = sqlite3.connect('FlowerShop.db')
cursor = conn.cursor()

# 执行SQL命令来创建Flowers表
cursor.execute('''
        CREATE TABLE Flowers (
            ID INTEGER PRIMARY KEY, 
            Name TEXT NOT NULL, 
            Type TEXT NOT NULL, 
            Source TEXT NOT NULL, 
            PurchasePrice REAL, 
            SalePrice REAL,
            StockQuantity INTEGER, 
            SoldQuantity INTEGER, 
            ExpiryDate DATE,  
            Description TEXT, 
            EntryDate DATE DEFAULT CURRENT_DATE 
        );
    ''')

# 插入5种鲜花的数据
flowers = [
    ('Rose', 'Flower', 'France', 1.2, 2.5, 100, 10, '2023-12-31', 'A beautiful red rose'),
    ('Tulip', 'Flower', 'Netherlands', 0.8, 2.0, 150, 25, '2023-12-31', 'A colorful tulip'),
    ('Lily', 'Flower', 'China', 1.5, 3.0, 80, 5, '2023-12-31', 'An elegant white lily'),
    ('Daisy', 'Flower', 'USA', 0.7, 1.8, 120, 15, '2023-12-31', 'A cheerful daisy flower'),
    ('Orchid', 'Flower', 'Brazil', 2.0, 4.0, 50, 2, '2023-12-31', 'A delicate purple orchid')
]

for flower in flowers:
    cursor.execute('''
        INSERT INTO Flowers (Name, Type, Source, PurchasePrice, SalePrice, StockQuantity, SoldQuantity, ExpiryDate, Description) 
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);
    ''', flower)

# 提交更改
conn.commit()

# 关闭数据库连接
conn.close()
