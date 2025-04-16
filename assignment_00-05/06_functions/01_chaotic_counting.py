import random

DONE_LIKELIHOOD = 0.5  # 50% chance to stop early

# Function that returns True with some likelihood
def done():
    return random.random() < DONE_LIKELIHOOD

# Function that counts from 1 to 10, but may stop early based on done()
def chaotic_counting():
    for i in range(1, 11):
        if done():
            return  # Exit early if done() returns True
        print(i, end=" ")
    # If loop finishes, we reach here and continue to main()
    print()

# Main function
def main():
    print("I'm going to count until 10 or until I feel like stopping, whichever comes first.")
    chaotic_counting()
    print("I'm done.")

# Run the main function
main()
# This program counts from 1 to 10, but may stop early based on a random chance.