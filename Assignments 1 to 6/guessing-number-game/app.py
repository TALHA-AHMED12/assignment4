import random

print('='*50)
print('🎮 WELCOME TO THE NUMBER GUESSING GAME! 🎮')
print('='*50)
print('\n🎲 Game Instructions 🎲')
print('🔸 Guess three numbers between 0 to 9')
print('🔸 You have ten chances to guess correctly')
print('🔸 Good luck! 🍀\n')
print('='*50)

while True:
    startGame = input('🎯 Are you ready to play? (yes/no): ')
    if startGame.lower() in ['yes', 'y']:  # Fixed condition
        attempts = 1
        print('\n🎲 The random numbers have been generated! 🎲')
        print('⭐ Time to test your luck! ⭐\n')
        random_number1 = random.randint(0,9)
        random_number2 = random.randint(0,9)
        random_number3 = random.randint(0,9)

        for attempts in range(1,11):
            print('='*30)
            print(f'🎯 Attempt {attempts} out of 10')
            print('='*30)
            print(f'The random numbers are: {random_number1}, {random_number2}, {random_number3}')
            guess1 = int(input('Enter your 1st number: '))
            guess2 = int(input('Enter your 2nd number: '))
            guess3 = int(input('Enter your 3rd number: '))
            if guess1 == random_number1 and guess2 == random_number2 and guess3 == random_number3:
                print('\n🎉 Congratulations! 🎉')
                print('🌟 You have guessed all numbers correctly! 🌟')
                break
            elif guess1 == random_number1 or guess2 == random_number2 or guess3 == random_number3:
                if guess1 == random_number1:
                    print('You have guessed the 1st number correctly 👌❌❌.')
                elif guess2 == random_number2:
                    print('You have guessed the 2nd number correctly ❌👌❌.')
                elif guess3 == random_number3:
                    print('You have guessed the 3rd number correctly ❌❌👌.')
                attempts += 1
                continue

            elif guess1 == random_number1 or guess2 == random_number2:
                print('You have guessed two numbers correctly. Please try again 👌👌❌.')
                attempts += 1
                continue
            elif guess1 == random_number1 or guess3 == random_number3:
                print('You have guessed two numbers correctly. Please try again 👌❌👌.')
                attempts += 1
                continue
            elif guess2 == random_number2 or guess3 == random_number3:
                print('You have guessed two numbers correctly. Please try again ❌👌👌.')
                attempts += 1
                continue
            else:
                print('Sorry! You have guessed the wrong number. Please try again ❌❌❌.')
                attempts += 1
                continue
        print('\n😔 Game Over! Better luck next time! 🎮')
    elif startGame.lower() in ['no', 'n']:  # Fixed condition
        print('\n❗ Come on! Give it a try - it\'s fun! 🎮')
        print('='*50)
        break
