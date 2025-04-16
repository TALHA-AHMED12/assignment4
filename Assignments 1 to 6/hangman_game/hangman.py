import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words)  # Randomly select a word from the list
    while '-' in word or ' ' in word:  # Ensure the word does not contain hyphens or spaces
        word = random.choice(words)
    return word  # Fixed: Moved return outside the while loop

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  # Unique letters in the word
    alphabet = set(string.ascii_uppercase) # All uppercase letters
    used_letters = set() # Letters guessed by the user

    lives = 6  # Number of lives

    while len(word_letters) > 0 and lives > 0:

        # letters used
        # ' '.join(['a', 'b', 'c']) -> 'a b cd'
        print('you have', lives , 'lives left and you have used these letters: ', ' '.join(used_letters))

        # what current word is (ie W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()  # Get user input and convert to uppercase
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

            else:
                lives -= 1
                print('Letter is not in word. You have', lives, 'lives left.')
        
        elif user_letter in used_letters:
            print('You have already guessed that letter. Try again.')

        else:
            print('Invalid character. Please try again.')

    # gets here when len(word_letters) == 0 OR lives == 0
    if lives == 0:
        print('You died, sorry. The word was', word)
    else:
        print('Congratulations! You guessed the word', word, '!!')

if __name__ == '__main__':
    hangman()  # Start the game when the script is run directly