def fruit_shop():
    # Define the fruit prices in a dictionary
    fruit_prices = {
        "apple": 2.5,
        "durian": 10.0,
        "jackfruit": 5.0,
        "kiwi": 3.0,
        "rambutan": 7.5,
        "mango": 4.0
    }
    
    total_cost = 0  # Initialize the total cost

    # Loop through each fruit in the dictionary and ask the user for the quantity
    for fruit, price in fruit_prices.items():
        quantity = int(input(f"How many ({fruit}) do you want?: "))
        total_cost += quantity * price  # Add the cost for this fruit to the total
    
    # Print the total cost
    print(f"Your total is ${total_cost}")

# Run the fruit shop program
fruit_shop()
# This program defines a fruit shop where the user can input the quantity of various fruits they want to buy. The program calculates the total cost based on predefined prices for each fruit and prints the total amount due.