def print_divisors(num):
    # Loop through numbers from 1 to num to find divisors
    print(f"Here are the divisors of {num}")
    for i in range(1, num + 1):
        if num % i == 0:
            print(i, end=" ")

def main():
    # Ask the user for a number
    num = int(input("Enter a number: "))
    # Call the print_divisors function to print divisors of the given number
    print_divisors(num)

# Run the main function
main()
