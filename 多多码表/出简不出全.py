import pandas as pd

file_path = input("请输入文件路径：")
df = pd.read_csv(file_path, sep='\t', encoding='utf-16')

# 处理编码重复的情况
duplicate_codes = df['编码'].duplicated(keep=False)
if not duplicate_codes.any():
    output_file_path = input("请输入输出文件路径：")
    df.to_csv(output_file_path, sep='\t', index=False, encoding='utf-16')
else:
    groups = df.groupby('编码')
    result_rows = []
    for code, group in groups:
        words = group['词'].tolist()
        if len(words) == len(set(words)):
            # 词不重复，保留所有行
            result_rows.extend(group.to_dict('records'))
        else:
            # 词重复，只保留首次出现的行
            first_word = words[0]
            result_rows.append(group[group['词'] == first_word].iloc[0].to_dict())

    result_df = pd.DataFrame(result_rows)

# 处理词重复的情况
seen_words = set()
final_result_rows = []
for row in result_df.to_dict('records'):
    word = row['词']
    if word not in seen_words:
        final_result_rows.append(row)
        seen_words.add(word)

final_result_df = pd.DataFrame(final_result_rows)
output_file_path = input("请输入输出文件路径：")
final_result_df.to_csv(output_file_path, sep='\t', index=False, encoding='utf-16')