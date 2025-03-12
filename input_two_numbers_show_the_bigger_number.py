# Asks user to input two numbers
num1 = int(input("Input the first number here: "))
num2 = int(input("Input the second number here: "))
# Print the bigger number
if num1 > num2:
    print(f"The bigger number is {num1}")
elif num2 > num1:
    print(f"The bigger number is {num2}")
else:
    print("There is no bigger number")