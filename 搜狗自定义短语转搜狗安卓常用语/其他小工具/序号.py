def generate_sequential_numbers():
    count = 0
    with open('序号.txt', 'w') as f:
        for i in range(10000):
            if i % 400 == 0:
                count += 1
            sequential_number = f"xh{str(count).zfill(3)}\n"
            f.write(sequential_number)

generate_sequential_numbers()
print("写入完成")