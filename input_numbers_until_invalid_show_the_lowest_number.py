# Put inputted numbers in a dictionary
number_list = []

while True: # Repeat until input is invalid
    try:
        # Asks user to input number
        number = int(input("Please input a number: "))
        number_list.append(number)
    except ValueError:
        print("Invalid input")
        break
# Identify the lowest number
lowest_number = min(number_list)
# Print the lowest number
print(f"The lowest number you have inputted is {lowest_number}")