# Add each number in a list or dictionary.
numbers = []
number_counts = {}
unique_numbers = []

# Asks user to input 10 numbers.
print("Please input 10 numbers: ")
for rep in range (10):
    num = int(input(f"Number {rep + 1}: "))
    numbers.append(num)
    number_counts[num] = number_counts.get(num, 0) + 1

# Check if numbers have already been inputted.
for num in numbers:
    if number_counts[num] == 1:
        unique_numbers.append(num)

# Print only the unique numbers.
print(f"Numbers without duplicate {unique_numbers}")