# Ask the user to input one number
number1 = int(input("Please enter the first number here: "))

# Ask the user to input the 9 remaining number
for rep in range(9):
    num2_10 = int(input("Please enter the next number here: "))
    number1 -= num2_10 # Continually subtract the succeeding 9 numbers from the first number

# Print the result
print(f"Your first number minus the rest of your numbers is {number1}")