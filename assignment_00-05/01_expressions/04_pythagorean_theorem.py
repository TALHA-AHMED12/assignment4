import math

def main():
    # Ask the user for the lengths of the two perpendicular sides
    ab = float(input("Enter the length of AB: "))
    ac = float(input("Enter the length of AC: "))

    # Calculate the hypotenuse using the Pythagorean theorem
    bc = math.sqrt(ab**2 + ac**2)

    # Print the result
    print("The length of BC (the hypotenuse) is:", bc)

# Run the program
if __name__ == "__main__":
    main()
