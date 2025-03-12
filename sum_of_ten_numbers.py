#Initialize total for proper increment
total = 0

# Ask the user to input ten numbers
print("Please input 10 numbers: ")
for rep in range(10):
    number = int(input(f"Number {rep + 1}: "))
    total = total + number # Add the result of the inputted numbers   

# Print the sum of the 10 numbers
print(f"The total of your numbers is {total}")