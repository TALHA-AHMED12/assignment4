def num_in_stock(fruit):
    inventory = {
        "apple": 500,
        "banana": 300,
        "pear": 1000,
        "mango": 0,
        "orange": 200
    }
    return inventory.get(fruit.lower(), 0)

def main():
    fruit = input("Enter a fruit: ")
    count = num_in_stock(fruit)

    if count > 0:
        print("This fruit is in stock! Here is how many:\n")
        print(count)
    else:
        print("This fruit is not in stock.")

main()
# This program checks the stock of a specific fruit in an inventory. It defines a function to get the stock count of a fruit, and then interacts with the user to input a fruit name. It prints the stock count if the fruit is in stock, or a message indicating that the fruit is not in stock if it is not found in the inventory.