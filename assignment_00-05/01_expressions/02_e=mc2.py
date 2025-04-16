def main():
    # Speed of light constant in meters per second
    C = 299_792_458

    # Prompt the user to enter mass
    mass = float(input("Enter kilos of mass: "))

    print("\ne = m * C^2...")

    # Display the entered mass and the speed of light
    print("m =", mass, "kg")
    print("C =", C, "m/s")

    # Calculate energy
    energy = mass * C ** 2

    # Display the result
    print(f"\n{energy} joules of energy!")

# Run the program
if __name__ == "__main__":
    main()
