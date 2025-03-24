import random

def greeting(name):
    print("\n" + "="*50)
    print("🎮 ROCK PAPER SCISSORS GAME 🎮".center(50))
    print("="*50 + "\n")
    print(f"👋 Hello, {name.title()}! Welcome to the game!")
    print("\nChoose your weapon:")
    print("🪨 Rock (r)")
    print("📄 Paper (p)")
    print("✂️ Scissors (s)")
    
    user_choice = input("\n🎯 Your choice: ").lower()
    
    computer_choices = ["Rock", "Paper", "Scissor"]
    computer_choice = random.choice(computer_choices)
    print(f"\n🤖 Computer chose: {computer_choice}")
    
    computer_choice = computer_choice.lower()
    print("\n" + "-"*20 + " RESULT " + "-"*20)
    
    if user_choice in ['rock', 'r'] and computer_choice == 'rock':
        print("It's a tie!")
    elif user_choice in ['paper', 'p'] and computer_choice == 'paper':
        print("It's a tie!")
    elif user_choice in ['scissor', 's'] and computer_choice == 'scissor':
        print("It's a tie!")
    elif user_choice in ['rock', 'r']:
        if computer_choice == 'paper':
            print("You lose!")
        else:
            print("You win!")
    elif user_choice in ['paper', 'p']:
        if computer_choice == 'scissor':
            print("You lose!")
        else:
            print("You win!")
    elif user_choice in ['scissor', 's']:
        if computer_choice == 'rock':
            print("You lose!")
        else:
            print("You win!")
    else:
        print("Invalid choice. Please try again.")
    
    print("-"*50 + "\n")

if __name__ == "__main__":
    print("\n" + "="*50)
    print("🎮 WELCOME TO ROCK PAPER SCISSORS 🎮".center(50))
    print("="*50 + "\n")
    
    name = input("👋 Enter your name: ")
    while True:
        greeting(name)
        play_again = input("🎯 Want to play again? (y/n): ").lower()
        if play_again != 'y':
            print("\n👋 Thanks for playing! See you next time!\n")
            break

