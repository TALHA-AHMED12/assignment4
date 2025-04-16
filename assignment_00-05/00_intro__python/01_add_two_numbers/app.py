def main():
    # Prompt the user to enter the first number
    first_number = input("Enter the first number: ")
    
    # Convert the input to an integer
    first_number = int(first_number)
    
    # Prompt the user to enter the second number
    second_number = input("Enter the second number: ")
    
    # Convert the input to an integer
    second_number = int(second_number)
    
    # Calculate the sum of the two numbers
    total = first_number + second_number
    
    # Print the total sum with an appropriate message
    print("The sum of", first_number, "and", second_number, "is:", total)

# Call the main function to run the program
if __name__ == "__main__":
    main()
