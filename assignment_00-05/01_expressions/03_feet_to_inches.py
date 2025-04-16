def main():
    # Ask the user to enter a measurement in feet
    feet = float(input("Enter length in feet: "))

    # Convert feet to inches
    inches = feet * 12

    # Print the result
    print(f"{feet} feet is {inches} inches.")

# Run the program
if __name__ == "__main__":
    main()
# This program converts feet to inches. It prompts the user to enter a measurement in feet and then calculates the equivalent measurement in inches by multiplying the feet value by 12. Finally, it prints the result in a formatted string.