import random

# Constants
NUM_ROUNDS = 5

# Welcome message
print("Welcome to the High-Low Game!")
print("--------------------------------")

# Track score
score = 0

# Play the game for NUM_ROUNDS rounds
for round_num in range(1, NUM_ROUNDS + 1):
    print(f"Round {round_num}")

    # Generate numbers
    your_number = random.randint(1, 100)
    computer_number = random.randint(1, 100)

    # Show user's number
    print(f"Your number is {your_number}")

    # Get user's guess
    guess = input("Do you think your number is higher or lower than the computer's?: ").lower()

    # Validate input
    while guess != "higher" and guess != "lower":
        guess = input("Please enter either higher or lower: ").lower()

    # Determine outcome
    if your_number > computer_number and guess == "higher":
        print(f"You were right! The computer's number was {computer_number}")
        score += 1
    elif your_number < computer_number and guess == "lower":
        print(f"You were right! The computer's number was {computer_number}")
        score += 1
    else:
        print(f"Aww, that's incorrect. The computer's number was {computer_number}")

    print(f"Your score is now {score}")
    print()  # Blank line between rounds

# Final message
print("Thanks for playing!")

# Ending messages based on score
if score == NUM_ROUNDS:
    print("Wow! You played perfectly!")
elif score >= NUM_ROUNDS // 2:
    print("Good job, you played really well!")
else:
    print("Better luck next time!")
# End of the game