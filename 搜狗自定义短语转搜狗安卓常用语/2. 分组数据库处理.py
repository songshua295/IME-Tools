import sqlite3
import random
import time


def generate_unique_uuid():
    while True:
        uuid_part1 = ''.join(random.choice('0123456789abcdef') for _ in range(8))
        uuid_part2 = ''.join(random.choice('0123456789abcdef') for _ in range(4))
        uuid_part3 = ''.join(random.choice('0123456789abcdef') for _ in range(4))
        uuid_part4 = ''.join(random.choice('0123456789abcdef') for _ in range(4))
        uuid_part5 = ''.join(random.choice('0123456789abcdef') for _ in range(12))
        generated_uuid = f"{uuid_part1}-{uuid_part2}-{uuid_part3}-{uuid_part4}-{uuid_part5}"
        if generated_uuid not in generated_uuids:
            generated_uuids.add(generated_uuid)
            return generated_uuid


db_filename = input("请输入分组数据库shortcutphrase_common_phrase_group_db的路径：")
conn = sqlite3.connect(db_filename)
cursor = conn.cursor()

# 清空表
cursor.execute("DELETE FROM COMMON_PHRASES_GROUP_INFO")

generated_uuids = set()
order_index = 1
update_timestamp = 1728036777087

# 打开分组数据库文件，并覆盖到数据库中
with open('GROUP_NAME.txt', 'r', encoding='utf-8') as file:
    for line in file:
        group_name = line.strip()
        category_uuid = generate_unique_uuid()
        cursor.execute("INSERT INTO COMMON_PHRASES_GROUP_INFO (CATEGORY_UUID, GROUP_NAME, CATEGORY_TYPE, IS_DELETE, ORDER_INDEX, UPDATE_TIMESTAMP) VALUES (?,?,?,?,?,?)",
                       (category_uuid, group_name, 1, 0, order_index, update_timestamp))
        order_index += 1
        update_timestamp += 1

conn.commit()
conn.close()