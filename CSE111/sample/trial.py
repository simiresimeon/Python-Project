#The base price of a large pizza is $10.95

price = 10.95

number_of_toppings = int(input("How many toppings?"))

price_per_toppings = 1.45

toppings_cost = number_of_toppings * price_per_toppings

price = price + toppings_cost

print(f"Price: ${price:.2f}")