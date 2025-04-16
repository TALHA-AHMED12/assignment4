# Function to access an element by index
def access_element(lst, index):
    if 0 <= index < len(lst):
        return lst[index]
    else:
        return "Index out of range!"

# Function to modify an element by index
def modify_element(lst, index, new_value):
    if 0 <= index < len(lst):
        lst[index] = new_value
        return lst
    else:
        return "Index out of range!"

# Function to slice the list
def slice_list(lst, start, end):
    if 0 <= start <= end <= len(lst):
        return lst[start:end]
    else:
        return "Invalid slice range!"

# Main interactive game
def index_game():
    # Initial list
    my_list = ['apple', 'banana', 'cherry', 'date', 'fig']

    while True:
        print("\nCurrent list:", my_list)
        print("Choose an operation:")
        print("1 - Access element")
        print("2 - Modify element")
        print("3 - Slice list")
        print("4 - Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            index = int(input("Enter index to access: "))
            result = access_element(my_list, index)
            print("Result:", result)

        elif choice == '2':
            index = int(input("Enter index to modify: "))
            new_value = input("Enter new value: ")
            result = modify_element(my_list, index, new_value)
            print("Updated list:", result)

        elif choice == '3':
            start = int(input("Enter start index: "))
            end = int(input("Enter end index: "))
            result = slice_list(my_list, start, end)
            print("Sliced list:", result)

        elif choice == '4':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

# Run the game
index_game()
