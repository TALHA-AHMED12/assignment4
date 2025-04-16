import random

def print_random_numbers():
    # Generate and print 10 random numbers between 1 and 100
    for _ in range(10):
        print(random.randint(1, 100), end=' ')

# Call the function to print the random numbers
print_random_numbers()
