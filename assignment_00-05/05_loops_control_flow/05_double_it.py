# Ask the user for a number
curr_value = int(input("Enter a number: "))

# Keep doubling the number until it is 100 or greater
while curr_value < 100:
    curr_value = curr_value * 2
    print(curr_value, end=" ")
