import secrets
from collections import Counter
import statistics

def generate_random_number():
    return secrets.randbelow(111) + 1  # Generates a number between 1 and 111

# Generate numbers 500 times
numbers = [generate_random_number() for _ in range(500)]

# Count the frequency of each number
number_frequency = Counter(numbers)

# Calculate the standard deviation of the frequencies
frequencies = list(number_frequency.values())
std_dev = statistics.stdev(frequencies)

# Sort by frequency (high to low)
sorted_numbers = sorted(number_frequency.items(), key=lambda x: x[1], reverse=True)

# Print sorted frequencies and the standard deviation
for num, freq in sorted_numbers:
    print(f"Number: {num}, Frequency: {freq}")

print(f"\nStandard Deviation of Frequencies: {std_dev}")
