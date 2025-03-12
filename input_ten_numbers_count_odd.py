# Intialized for proper increment
odd_count = 0
# Asks the user to input ten numbers
print("Please input 10 numbers: ")
for rep in range(10):
    number = input(f"Number {rep + 1}") # Check if odd or not and count how many odd
    if number % 2 == 1:
        odd_count += 1

# Print the count of how many odd numbers