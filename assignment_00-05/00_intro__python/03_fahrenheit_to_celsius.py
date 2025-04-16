def main():
    # Prompt the user to enter a temperature in Fahrenheit
    fahrenheit = input("Enter temperature in Fahrenheit: ")
    
    # Convert the input to a float
    fahrenheit = float(fahrenheit)
    
    # Convert Fahrenheit to Celsius using the correct formula
    celsius = (fahrenheit - 32) * 5.0 / 9.0
    
    # Print the result
    print("Temperature:", fahrenheit, "F =", celsius, "C")

# Run the program
if __name__ == "__main__":
    main()
