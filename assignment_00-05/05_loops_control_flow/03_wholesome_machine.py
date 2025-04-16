# The correct affirmation
affirmation = "I am capable of doing anything I put my mind to."

# Keep asking the user until they type it correctly
while True:
    user_input = input("Please type the following affirmation: ")
    
    if user_input == affirmation:
        print("That's right! :)")
        break  # Exit the loop when the correct affirmation is typed
    else:
        print("Hmmm That was not the affirmation. Please try again.")
