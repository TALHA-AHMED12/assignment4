import random

def roll_dice():
    # Local variables inside the function
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    print("Rolled:", die1, "and", die2)

def main():
    print("Rolling two dice three times:\n")

    # Loop to roll dice three times
    for i in range(3):
        roll_dice()

# Run the program
if __name__ == "__main__":
    main()
