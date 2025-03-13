# Put inputted numbers into a list
number_list = []

# Count how many time each number is inputted
duplicate_count = {}

# Keep asking until user input is invalid
while True:
    try:
        # Ask the user to input number
        number = int(input("Please input your number here: "))
        number_list.append(number)
        if number in duplicate_count:
            duplicate_count[number] += 1
        else:
            duplicate_count[number] = 1
    except ValueError:
        print("Invalid input. Ending run")
        break

# Check which number is most frequent and print the result       