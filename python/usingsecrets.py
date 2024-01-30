import secrets
from collections import Counter

def generate_random_number():
    return secrets.randbelow(111) + 1  # Generates a number between 1 and 111

# Generate numbers 500 times
numbers = [generate_random_number() for _ in range(500)]

# Count the frequency of each number
number_frequency = Counter(numbers)

# Sort by frequency (high to low)
sorted_numbers = sorted(number_frequency.items(), key=lambda x: x[1], reverse=True)

# Print sorted frequencies
for num, freq in sorted_numbers:
    print(f"Number: {num}, Frequency: {freq}")
