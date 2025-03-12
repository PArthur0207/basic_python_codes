# Add each number in a list or dictionary.
numbers = []

# Asks user to input 10 numbers.
print("Please input 10 numbers: ")
for rep in range (10):
    num = int(input(f"Number {rep + 1}: "))
    numbers.append(num)
print(numbers)

# Check if numbers have already been inputted.
# Print only the unique numbers.

