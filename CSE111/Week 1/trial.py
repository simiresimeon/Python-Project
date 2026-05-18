#The base price of a large pizza is $10.95

price = 10.95

number_of_toppings = int(input("How many toppings?"))

price_per_toppings = 1.45

toppings_cost = number_of_toppings * price_per_toppings

#price = price + toppings_cost
price += toppings_cost

print(f"Price: ${price:.2f}")



balance = float(input("Enter your balance: "))

if balance > 500:
    interest= balance * 0.05
    balance += interest
print(f"balance: ${balance:.2f}")
