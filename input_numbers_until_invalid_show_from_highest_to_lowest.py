# Add the inputted numbers in a dictionary
number_list = []

# Keep asking until the user input is invalid
while True:
    try:
        # Ask the user to input a number
        number = int(input("Please input your number here: "))
        number_list.append(number)
    except ValueError:
        print("Invalid input. Ending run")
        break

# Put into highest to lowest order, and print the result
number_list.sort(reverse=True)
print(f"Your numbers in descending order is {number_list}")