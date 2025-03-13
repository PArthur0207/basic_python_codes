# Put inputted numbers into a list
number_list = []
# Keep asking until user input is invalid
while True:
    try:
        # Ask the user to input number
        number = int(input("Please input your number here: "))
        number_list.append(number)
    except ValueError:
        print("Invalid input. Ending run")
        break

# Count how many time each number is inputted
# Check which number is most frequent and print the result       