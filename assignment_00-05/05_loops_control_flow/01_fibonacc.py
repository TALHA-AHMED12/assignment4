# Define the maximum value for the Fibonacci sequence
MAX_VALUE = 10000

def fibonacci_up_to_max():
    # Initialize the first two terms in the Fibonacci sequence
    a, b = 0, 1
    
    # Print the first term
    print(a, end=" ")
    
    # Continue generating and printing the Fibonacci sequence terms
    while b <= MAX_VALUE:
        print(b, end=" ")
        a, b = b, a + b  # Update a and b to the next two terms

# Run the function to print Fibonacci terms up to the maximum value
fibonacci_up_to_max()
