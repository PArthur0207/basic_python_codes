# Ask the user to input 2 numbers
num1 = int(input("Input the first number here: "))
num2 = int(input("Input the second number here: "))
# Check which number is smaller, print the smaller one
if num1 < num2:
    print(f"The smaller number is {num1}")
elif num2 < num1:
    print(f"The smaller number is {num2}")