import random
import sqlite3
from datetime import datetime

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

file_path = input("请输入文件 搜狗自定义短语 的路径：")

try:
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
except FileNotFoundError:
    print(f"文件 {file_path} 不存在。")
    exit()

filtered_lines = [line.replace('=', ',') for line in lines if not line.startswith(';') and line.strip()!= '']

new_file_path = "新—搜狗转到常用语.csv"
with open(new_file_path, 'w', encoding='utf-8') as new_file:
    column_names = "UUID,GROUP_NAME,CATEGORY_TYPE,CONTENT,INPUT_CODE,CANDIDATE_INDEX,IS_DELETE,ORDER_TIMESTAMP,UPDATE_TIMESTAMP,SYNC_STATUS"
    new_file.write(column_names + "\n")
    generated_uuids = set()
    group_name_counter = 1
    group_name_repeat_count = 0
    category_type = "1"
    is_delete = "0"
    sync_status = "1"
    order_timestamp = 1727927599296
    update_timestamp = 1727927599296
    common_phrases = []
    for line in filtered_lines:
        uuid_str = generate_unique_uuid()
        group_name = f"xh{str(group_name_counter).zfill(2)}"
        group_name_repeat_count += 1
        if group_name_repeat_count == 200:
            group_name_counter += 1
            group_name_repeat_count = 0
        content_parts = line.strip().split(',')
        input_code = content_parts[0] if len(content_parts) > 0 else ""
        candidate_index = content_parts[1] if len(content_parts) > 1 else ""
        content = content_parts[2] if len(content_parts) > 2 else ""
        new_line = f"{uuid_str},{group_name},{category_type},{content},{input_code},{candidate_index},{is_delete},{order_timestamp},{update_timestamp},{sync_status}\n"
        order_timestamp += 1
        update_timestamp += 1
        new_file.write(new_line)
        common_phrases.append(new_line)

print(f"已处理文件 {file_path}，并将结果保存到 {new_file_path}。")

answer = input("是否追加到 db 文件中？（输入 y 表示是，其他表示否）")
if answer == 'y':
    db_path = input("请输入 sqlite3 文件 shortcutphrase_common_phrase_list_db 的文件路径：")
    clear_answer = input("追加前是否清空 非默认常用语？（输入 y 表示是，输入 n 表示否）")
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    if clear_answer == 'y':
        cursor.execute("DELETE FROM COMMON_PHRASES_INFO WHERE GROUP_NAME<>'默认'")
        conn.commit()
    for phrase in common_phrases:
        values = phrase.strip().split(',')
        cursor.execute("INSERT INTO COMMON_PHRASES_INFO VALUES (?,?,?,?,?,?,?,?,?,?)", values)
    conn.commit()

    cursor.execute("SELECT DISTINCT GROUP_NAME FROM COMMON_PHRASES_INFO")
    group_names = cursor.fetchall()
    with open('GROUP_NAME.txt', 'w', encoding='utf-8') as gn_file:
        for name in group_names:
            gn_file.write(name[0] + '\n')
    print("分组名称：GROUP_NAME.txt 已生成")
    conn.close()