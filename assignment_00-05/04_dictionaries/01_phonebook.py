def phonebook():
    # Create an empty dictionary to store the phonebook
    phonebook_dict = {}

    while True:
        # Show the menu of options to the user
        print("\nPhonebook Menu:")
        print("1. Add a contact")
        print("2. Look up a phone number")
        print("3. Display all contacts")
        print("4. Exit")
        
        # Ask the user for a choice
        choice = input("Please select an option (1-4): ")

        if choice == "1":
            # Add a contact
            name = input("Enter the name: ")
            number = input("Enter the phone number: ")
            phonebook_dict[name] = number
            print(f"{name} has been added to the phonebook.")
        
        elif choice == "2":
            # Look up a phone number
            name = input("Enter the name to look up: ")
            if name in phonebook_dict:
                print(f"The phone number for {name} is {phonebook_dict[name]}.")
            else:
                print(f"{name} is not found in the phonebook.")
        
        elif choice == "3":
            # Display all contacts in the phonebook
            if phonebook_dict:
                print("\nPhonebook:")
                for name, number in phonebook_dict.items():
                    print(f"{name}: {number}")
            else:
                print("The phonebook is empty.")
        
        elif choice == "4":
            # Exit the program
            print("Exiting the phonebook program.")
            break
        
        else:
            print("Invalid choice. Please choose a valid option (1-4).")

# Run the phonebook program
phonebook()
