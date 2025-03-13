# Put inputted numbers into a dictionary
number_list = []
duplicates = []

# Ask the user to input 10 numbers
for rep in range(10):
    number = int(input(f"Please enter the number {rep + 1} here: "))
    if number in number_list:
        # Check if inputed number is already in the dictionary, put into a different dictionary (only once) if yes
        if number in duplicates: 
            pass
        else:
            duplicates.append(number)
    number_list.append(number)

# Print the duplicated numbers only once
print(duplicates)