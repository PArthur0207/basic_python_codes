# Add the number on a dictionary
numbers = []

# Ask user to input 10 numbers
print("Please enter 10 numbers: ")
for rep in range(10):
    num = int(input(f"Number {rep + 1}: "))
    numbers.append(num)
print(numbers)

# Check if the number is already inputted
# Print all inputted numbers exactly once