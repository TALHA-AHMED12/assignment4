def main():
    # Ask the user for the two numbers
    numerator = int(input("Please enter an integer to be divided: "))
    denominator = int(input("Please enter an integer to divide by: "))

    # Perform division and calculate the remainder
    quotient = numerator // denominator
    remainder = numerator % denominator

    # Print the result
    print(f"The result of this division is {quotient} with a remainder of {remainder}")

# Run the program
if __name__ == "__main__":
    main()
# This program calculates the quotient and remainder of two integers. It prompts the user to enter a numerator and a denominator, performs integer division to find the quotient, and uses the modulus operator to find the remainder. Finally, it prints the results in a formatted string.