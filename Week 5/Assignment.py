# Author: Simire Simeon Obamiegie
# Assignment: Shopping Cart Program

# This program helps users manage a shopping cart.
# It lets you add, view, remove items, and see the total cost.
# I made it simple and fun to use!
# A welcome message is shown at the start.

# Shopping cart lists
item_names = []
item_prices = []

print("Welcome to the Shopping Cart Program!")
print()
username = input("Please enter your name: ")
print(f"Hello, {username}! Let's manage your shopping cart.")
input("Press Enter to continue...")
print()


# Function to add a new item
def add_item():
    name = input("What item would you like to add? ")
    price_input = input(f"What is the price of '{name}'? ")
    if price_input.replace('.', '', 1).isdigit():
        price = float(price_input)
        item_names.append(name)
        item_prices.append(price)
        print(f"'{name}' has been added to the cart.\n")
    else:
        print("Invalid price. Please enter a number.\n")

# Function to display cart contents
def display_cart():
    if len(item_names) == 0:
        print("Your shopping cart is empty.\n")
    else:
        print("The contents of the shopping cart are:")
        for i in range(len(item_names)):
            print(f"{i + 1}. {item_names[i]} - ${item_prices[i]:.2f}")
        print()

# Function to remove an item
def remove_item():
    display_cart()
    if len(item_names) == 0:
        return
    choice = input("Which item would you like to remove? ")
    if choice.isdigit():
        index = int(choice) - 1
        if index in range(len(item_names)):
            removed = item_names.pop(index)
            item_prices.pop(index)
            print(f"'{removed}' has been removed.\n")
        else:
            print("Sorry, that is not a valid item number.\n")
    else:
        print("Invalid input. Please enter a number.\n")

# Function to compute total price
def compute_total():
    total = 0
    for price in item_prices:
        total += price
    print(f"The total price of the items in the shopping cart is ${total:.2f}\n")

# The Main loop of my program
def main():
    while True:


        print("Please select one of the following:")
        print("1. Add a new item")
        print("2. Display the contents of the shopping cart")
        print("3. Remove an item")
        print("4. Compute the total")
        print("5. Quit")
        choice = input("Please enter an option: ")

        if choice == "1":
            add_item()
        elif choice == "2":
            display_cart()
        elif choice == "3":
            remove_item()
        elif choice == "4":
            compute_total()
        elif choice == "5":
            print("Thank you for using the shopping cart program. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.\n")

# The Beginning of My shopping cart
main()