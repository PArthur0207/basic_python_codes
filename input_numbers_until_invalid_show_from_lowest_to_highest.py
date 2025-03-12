# Store the inputted numbers in a dictionary
number_list = []

while True: # Keep asking until input is invalid
    try:
        # Asks the user to input number
        number = int(input("Please input the number here: "))
        number_list.append(number)
    except ValueError:
        print("Invalid input")
        break

# Print the numbers from lowest to highest
number_list.sort()
print(f"The number in ascending order are {number_list}")
