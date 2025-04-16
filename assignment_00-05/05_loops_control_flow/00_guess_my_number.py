import random

def guess_my_number():
    # Randomly pick a number between 0 and 99
    secret_number = random.randint(0, 99)
    
    print("I am thinking of a number between 0 and 99...")
    
    # Initialize the user's guess
    guess = None
    
    # Continue looping until the guess is correct
    while guess != secret_number:
        # Prompt the user to enter a guess
        guess = int(input("Enter a guess: "))
        
        if guess < secret_number:
            print("Your guess is too low")
        elif guess > secret_number:
            print("Your guess is too high")
    
    print(f"Congrats! The number was: {secret_number}")

# Run the game
guess_my_number()
