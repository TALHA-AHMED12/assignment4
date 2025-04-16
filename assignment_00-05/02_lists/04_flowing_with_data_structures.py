def add_three_copies(data_list, data):
    # Add three copies of the data to the list
    data_list.append(data)
    data_list.append(data)
    data_list.append(data)

def main():
    # Prompt the user for input
    message = input("Enter a message to copy: ")
    
    # Create an empty list
    data_list = []
    
    # Print the list before calling the function
    print("List before:", data_list)
    
    # Call the function that modifies the list
    add_three_copies(data_list, message)
    
    # Print the list after calling the function
    print("List after:", data_list)

# Run the program
if __name__ == "__main__":
    main()
# # This program demonstrates how to modify a list by passing it to a function. The user is prompted to enter a message, which is then added three times to an initially empty list. The list is printed before and after the function call to show the changes made.