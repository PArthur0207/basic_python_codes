count = 0 # Initialized for counting the loops
total = 0 # Initialized to get the total of every number inputted

while True: # Keep asking until user input is invalid, count every loop
    try:
        # Ask the user to input a number
        number = float(input("Input your number here: "))
        count += 1
        total += number
    except ValueError:
        print("Invalid input. Ending run")
        break

# Divide the total of the number by the number of times looped and show the result  
print(f"The average of what you inputted is {total / count}")