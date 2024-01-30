import hashlib
import random
import string
from collections import Counter
import statistics

all_numbers = []

for _ in range(50000):
    seed = ''.join(random.choices(string.ascii_letters + string.digits, k=64))

    hashed_seed = hashlib.sha256(seed.encode()).hexdigest()

    random.seed(int(hashed_seed, 16))  
    for _ in range(5):
        number = random.randint(1, 111)
        all_numbers.append(number)

number_frequency = Counter(all_numbers)

sorted_numbers = sorted(number_frequency.items(), key=lambda x: x[1], reverse=True)

frequencies = number_frequency.values()
std_dev = statistics.stdev(frequencies)

with open("results.txt", "w") as file:
    for num, count in sorted_numbers:
        file.write(f"Number: {num}, Frequency: {count}\n")
    file.write(f"\nStandard Deviation of Frequencies: {std_dev}\n")

print("Results and standard deviation have been written to results.txt")
