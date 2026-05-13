from datetime import datetime 
DISCOUNT_RATE= 0.1
TAX_RATE= 0.06
today= datetime.now()
DOW= today.weekday()
quantity=0
price=1
while quantity != 0:
    quantity= int(input("Enter the quantity: "))
    price= float(input("Enter the price: "))
    subtotal += quantity * price
subtotal = float(input("Enter the subtotal: "))
print(f"Total order {subtotal}")
discount=0
if DOW==2 or DOW==3 or DOW==4:
    if subtotal > 50:
        discount= subtotal * DISCOUNT_RATE
        print(f"Discount {discount}")
    else:
        short=50-subtotal
        print(f"You need {short} more of purchase to get a discount")
subtotal -=discount
tax = subtotal * TAX_RATE
total = subtotal + tax

print(f"Tax {tax}")
print(f"Total Due {total}")