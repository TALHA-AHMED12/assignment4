def get_first_element(lst):
    # Print the first element of the list
    print("The first element is:", lst[0])

def main():
    # Prompt the user for the number of elements in the list
    n = int(input("How many elements are in the list? "))
    
    # Initialize an empty list
    lst = []
    
    # Prompt the user to input the list elements one at a time
    for i in range(n):
        element = input(f"Enter element {i + 1}: ")
        lst.append(element)
    
    # Call the function to get and print the first element
    get_first_element(lst)

# Run the program
if __name__ == "__main__":
    main()
