def count_numbers():
    # Create an empty dictionary to store the number counts
    number_count = {}

    while True:
        # Ask the user to enter a number
        user_input = input("Enter a number: ")

        # If the user doesn't enter anything, stop the program
        if user_input == "":
            break
        
        # Convert the input to an integer
        number = int(user_input)

        # Count the occurrences of the number
        if number in number_count:
            number_count[number] += 1
        else:
            number_count[number] = 1

    # Print the results
    for number, count in number_count.items():
        print(f"{number} appears {count} times.")

# Call the function
count_numbers()
# This program counts the occurrences of numbers entered by the user. It uses a dictionary to store the numbers as keys and their counts as values. The program continues to prompt the user for numbers until an empty input is given, at which point it prints the count of each number entered.