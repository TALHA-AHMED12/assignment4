# Function to double the number
def double(num):
    return num * 2

# Main function to interact with the user
def main():
    num = float(input("Enter a number: "))  # Asking for a number from the user
    result = double(num)  # Calling the double function
    print(f"Double that is {result}")  # Printing the doubled result

# Run the main function
main()
# This program defines a function to double a number and then interacts with the user to get a number, double it, and print the result. The main function is called to execute the program.