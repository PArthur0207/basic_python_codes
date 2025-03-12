# Add each number in a list or dictionary.
numbers = []
number_counts = {}

# Asks user to input 10 numbers.
print("Please input 10 numbers: ")
for rep in range (10):
    num = int(input(f"Number {rep + 1}: "))
    numbers.append(num)
    number_counts[num] = number_counts.get(num, 0) + 1
print(number_counts)
print(numbers)

# Check if numbers have already been inputted.
# Print only the unique numbers.

