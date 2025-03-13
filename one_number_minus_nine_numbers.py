# Ask the user to input one number
number1 = int(input("Please enter the first number here: "))

# Ask the user to input the 9 remaining number
for rep in range(10):
    num2_10 = int(input("Please enter the next number here: "))
# Continually subtract the succeeding 9 numbers from the first number
# Print the result