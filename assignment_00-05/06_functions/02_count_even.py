# Function to count even numbers in the list
def count_even(lst):
    even_count = 0
    for num in lst:
        if num % 2 == 0:
            even_count += 1
    print(f"The number of even numbers in the list is: {even_count}")

# Function to populate the list by asking user for integers
def populate_list():
    lst = []
    while True:
        user_input = input("Enter an integer or press enter to stop: ")
        if user_input == "":
            break  # Stop input when the user presses enter without typing anything
        else:
            try:
                number = int(user_input)
                lst.append(number)
            except ValueError:
                print("Please enter a valid integer.")
    return lst

# Main function to tie everything together
def main():
    lst = populate_list()
    count_even(lst)

# Run the main function
main()
# This program counts the number of even integers in a list. It prompts the user to enter integers one by one, and when the user presses enter without typing anything, it stops taking input. Then it counts and prints the number of even integers in the list.