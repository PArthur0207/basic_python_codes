# Ask the user to input 10 numbers
for rep in range(10):
    number = int(input(f"Please enter the number {rep + 1} here: "))
# Put inputted numbers into a dictionary
# Check if inputed number is already in the dictionary, put into a different dictionary (only once) if yes
# Print the duplicated numbers only once