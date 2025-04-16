def check_height(height):
    # Pre-specified minimum height for the rollercoaster ride
    MIN_HEIGHT = 50
    
    if height >= MIN_HEIGHT:
        print("You're tall enough to ride!")
    else:
        print("You're not tall enough to ride, but maybe next year!")

def main():
    # Prompt the user for their height
    height = int(input("How tall are you? "))
    
    # Check if the user is tall enough to ride
    check_height(height)

# Run the program
if __name__ == "__main__":
    main()
