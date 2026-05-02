#Assignment: Meal Price Calculator
#Author: Simire Simeon Obamiegie


#This program calculates the total cost of a meal including tax and change due.
#Defined menu List items and their prices.
#Add a drink option to the meal.
#Added a welcome message that includes the customer's name.

menu = {
    "Hamburger": 5.99,
    "Cheeseburger": 6.49,
    "Chicken Nuggets": 4.99,
    "Fries": 2.49,
    "Soda": 1.99,
}


print("Hey, Welcome To MC Donalds!")
customer_name= input("What is your name? ")
print()

print(f"Hey {customer_name}! \nHere is our Meal Menu:")
print()

#Menu display.
for item, price in menu.items():
    print(f"{item}: ${price:.2f}")

print("\n--- Order Details ---")

drink= input("\nWould you like a drink with your meal? (yes/no)")
if drink.lower() == "yes":
    drink_price = menu["Soda"]
else:
    print("okay")


child_meal= float(input("What is the price of a child meal? "))
adult_meal= float (input("What is the price of an adult meal? "))
number_of_children= int(input("How many children are there? "))
number_of_adults= int(input("How many adults are there? "))

subtotal= (float(child_meal) * number_of_children) + (float(adult_meal) * number_of_adults) + (float (drink_price) * (number_of_children + number_of_adults))
print()

print(f"Subtotal: ${subtotal:.2f}")
print()

sales_tax_rate = float(input("What is the sales tax rate? $"))

Sales_tax = (float(subtotal) * (sales_tax_rate / 100))
print(f"Sales Tax: ${Sales_tax:.2f}")

total= (float(subtotal) + (Sales_tax))

print(f"Total: ${total:.2f}")
print()

payment_amount= float(input("What is the payment amount? "))
change= (float(payment_amount) - float(total))

print(f"Change: ${change:.2f}")
