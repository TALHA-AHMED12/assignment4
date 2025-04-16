# Constant for the adult age
ADULT_AGE = 18

def is_adult(age):
    # Check if the age is greater than or equal to the adult age
    if age >= ADULT_AGE:
        return True
    else:
        return False

def main():
    # Ask the user for the person's age
    age = int(input("How old is this person?: "))
    
    # Call the is_adult function and print the result
    print(is_adult(age))

# Run the main function
main()
