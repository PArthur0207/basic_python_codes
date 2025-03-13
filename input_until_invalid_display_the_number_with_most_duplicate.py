# Keep asking until user input is invalid
while True:
    try:
        # Ask the user to input number
        number = int(input("Please input your number here: "))
    except ValueError:
        print("Invalid input. Ending run")
        break

# Put inputted numbers into a list
# Count how many time each number is inputted
# Check which number is most frequent and print the result       