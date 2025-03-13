# Keep asking until the user becomes invalid
while True:
    try:    
        # Ask the user to input a number
        number = int(input("Enter your number here: "))
    except ValueError:
        print("Invalid input, ending run.")
        break    

# Compare numbers to see which is highest in each iteration
# Print the highest number