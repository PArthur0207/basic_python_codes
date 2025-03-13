# Ask the user to input 2 numbers
num1 = int(input("Input the first number here: "))
num2 = int(input("Input the second number here: "))
# Print the numbers in between if the first number is smaller
if num1 < num2:
    for number in range(num1 + 1,num2):
        print(number)
# Print the numbers in between if the second number is smaller