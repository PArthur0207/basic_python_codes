# Initialize current highest number
current_highest_number = None

# Keep asking until the user becomes invalid
while True:
    try:    
        # Ask the user to input a number
        number = int(input("Enter your number here: "))
        # Compare numbers to see which is highest in each iteration
        if current_highest_number is None or number > current_highest_number:
            current_highest_number = number
    except ValueError:
        print("Invalid input, ending run.")
        break    

# Print the highest number
print(f"The highest number you inputted is {current_highest_number}")