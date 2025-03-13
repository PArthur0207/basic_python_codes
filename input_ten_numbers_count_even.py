# Initialize count for incrementing
even_count = 0
# Ask the user to input 10 numbers
print("Please input 10 numbers: ")
for rep in range(10):
    number =  int(input(f"Input number {rep + 1} here: "))
    if number % 2 == 0: # Check if even or not, add to count if even
        even_count += 1

# Print the result
print(f"You have inputted {even_count} even numbers")