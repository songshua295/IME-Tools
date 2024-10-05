import random
import time

def generate_unique_timestamps():
    end_timestamp = int(time.time() * 1000)
    start_timestamp = end_timestamp - 24 * 60 * 60 * 1000
    timestamps = []
    while len(timestamps) < 10000:
        random_timestamp = random.randint(start_timestamp, end_timestamp)
        if random_timestamp not in timestamps:
            timestamps.append(random_timestamp)
    return sorted(timestamps)

timestamps = generate_unique_timestamps()

with open('1w 时间戳.txt', 'w') as f:
    for timestamp in timestamps:
        f.write(str(timestamp) + '\n')