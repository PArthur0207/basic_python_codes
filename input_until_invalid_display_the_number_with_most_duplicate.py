# Put inputted numbers into a list
number_list = []

# Count how many time each number is inputted
duplicate_count = {}

# Keep asking until user input is invalid
while True:
    try:
        # Ask the user to input number
        number = int(input("Please input your number here: "))
        number_list.append(number)
        if number in duplicate_count:
            duplicate_count[number] += 1
        else:
            duplicate_count[number] = 1
    except ValueError:
        print("Invalid input. Ending run")
        break
   
most_frequent = None # Placeholder for the most frequent number inputted
most_frequent_count = 0   # Initialized to count how many times the most frequent number is inputted

# Check which number is most frequent and print the result 
for num, count in duplicate_count.items():
    if count > most_frequent_count:
        most_frequent = num
        most_frequent_count = count

print(f"Most frequent number is {most_frequent} inputtes {most_frequent_count} times")