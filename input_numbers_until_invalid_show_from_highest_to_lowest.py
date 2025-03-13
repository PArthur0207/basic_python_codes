# Keep asking until the user input is invalid
while True:
    try:
        # Ask the user to input a number
        number = int(input("Please input your number here: "))
    except ValueError:
        print("Invalid input. Ending run")
        break

# Add the inputted numbers in a dictionary
# Put into highest to lowest order, and print the result