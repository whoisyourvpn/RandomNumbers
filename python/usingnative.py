import random
from collections import Counter
import statistics

def generate_random_number():
    return random.randint(1, 111) 

iterations = 500 

numbers = [generate_random_number() for _ in range(iterations)]

number_frequency = Counter(numbers)

frequencies = list(number_frequency.values())
std_dev = statistics.stdev(frequencies)

print(f"{iterations} Iterations: Standard Deviation of Frequencies: {std_dev}")
