import random
import string

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

generated_uuids = set()
with open('1wUUID.txt', 'w') as f:
    for _ in range(10000):
        unique_uuid = generate_unique_uuid()
        f.write(unique_uuid + '\n')

print("写入完成")