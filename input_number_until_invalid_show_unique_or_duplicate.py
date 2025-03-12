# Put numbers into a dictionary
unique_numbers = []

while True: # Repeat process until the input is invalid
    try:
        # Asks user to input numbers
        number = int(input("Please enter a number: "))
        if number in unique_numbers:  # Check if number is in dictionary print 'duplicate' if not print 'unique'
            print("Duplicate")
        else:
            print("Unique")
            unique_numbers.append(number)
    except ValueError:
        print("Ivalid input, ending run")    
        break