import random

def print_decorated(text):
    print('✨' + '=' * 50 + '✨')
    print('🎮 ' + text)
    print('✨' + '=' * 50 + '✨')

print_decorated('WELCOME TO THE NUMBER GUESSING GAME! 🎲')
print('🤖 In this game you give me a number and I will try to guess it.')
print('🔄 If I am wrong, you tell me if your number is higher or lower than my guess.')
print('✅ If I am right, you tell me so and I will stop guessing.')
print('🎯 Let me know if you are ready to start!')
input('🎲 Press Enter to continue...')
print('🤔 Think of a number between 1 and 10 and let me know when you are ready.')
input('🎲 Press Enter to continue...')

low = 1
high = 10   
attempts = 0

while True:
    # Use binary search instead of random guessing
    guess = (low + high) // 2
    attempts += 1
    print('🔍 Is your number', guess, '?')
    response = input('⌨️  Enter "yes" if I guessed correctly, "higher" if your number is higher, or "lower" if your number is lower: ').lower()
    
    if response == 'yes':
        print_decorated(f'🎉 I guessed your number in {attempts} attempts! 🎉')
        break
    elif response == 'higher':
        if guess == 10:
            print('❌ Error: You said higher, but 10 is the maximum number allowed!')
            continue
        low = guess + 1
    elif response == 'lower':
        if guess == 1:
            print('❌ Error: You said lower, but 1 is the minimum number allowed!')
            continue
        high = guess - 1
    else:
        print('⚠️  Invalid input. Please enter "yes", "higher", or "lower".')
    
    if low > high:
        print_decorated('❌ Something went wrong! Your responses are inconsistent.')
        break

print('👋 Thanks for playing! Come back soon! 🎮')
