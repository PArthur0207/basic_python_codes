# Add the number on a dictionary
numbers = []
unique_numbers = []

# Ask user to input 10 numbers
print("Please enter 10 numbers: ")
for rep in range(10):
    num = int(input(f"Number {rep + 1}: "))
    numbers.append(num)
    if num not in unique_numbers:
        unique_numbers.append(num)
print(unique_numbers)

# Check if the number is already inputted
# Print all inputted numbers exactly once