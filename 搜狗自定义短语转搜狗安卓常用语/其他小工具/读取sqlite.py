import sqlite3
import csv

# 获取要读取的 SQLite 文件名
sqlite_filename = input("请输入 SQLite 文件名：")

# 连接到 SQLite 数据库文件
conn = sqlite3.connect(sqlite_filename)

# 创建一个游标对象
cursor = conn.cursor()

# 获取表的字段名
cursor.execute("PRAGMA table_info(COMMON_PHRASES_INFO)")
column_names = [column[1] for column in cursor.fetchall()]

# 执行查询语句以获取 COMMON_PHRASES_INFO 表的数据
cursor.execute("SELECT * FROM COMMON_PHRASES_INFO")

# 获取查询结果
results = cursor.fetchall()

# 指定要写入的 CSV 文件名
csv_filename = '原来的shortcutphrase_common_phrase_list_db.csv'

# 将结果写入 CSV 文件
with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    # 写入表头
    writer.writerow(column_names)
    for row in results:
        writer.writerow(row)

# 关闭游标和连接
cursor.close()
conn.close()