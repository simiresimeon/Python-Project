#PROGRAM
#Work along with your instructor to write a Python program that gets a customer’s subtotal as 
# input and gets the current day of the week from your computer’s operating system. 
# Your program must not ask the user to enter the day of the week. 
# Instead, it must get the day of the week from your computer’s operating system.

#If the subtotal is $50 or greater and today is Tuesday or Wednesday, your program must subtract 10% from the subtotal. 
# Your program must then compute the total amount due by adding sales tax of 6% to the subtotal. 
# Your program must print the discount amount if applicable, the sales tax amount, and the total amount due.

#Requirements
#Your program asks the user for the subtotal but does not ask the user for the day of the week. 
#Your program gets the day of the week from your computer’s operating system.
#Your program correctly computes and prints the discount amount if applicable.
#Your program correctly computes and prints the sales tax amount and the total amount due.

#ENHANCEMENT#
#Add code to your program that the computer will execute if today is Tuesday or Wednesday and the customer is not purchasing enough to receive the discount. 
#This added code should compute and print the difference between $50 and the subtotal which is the additional amount the customer would need to purchase in order to receive the discount.
#Near the beginning of your program replace the code that asks the user for the subtotal with a loop that repeatedly asks the user for a price and a quantity and computes the subtotal. This loop should repeat until the user enters "0" for the quantity.


from datetime import datetime 
DISCOUNT_RATE= 0.1
TAX_RATE= 0.06
# Tells us the exact date of the current moment
today= datetime.now()
# Returns the day of the week as an integer where
# Monday is 0 and Sunday is 6.
DOW= today.weekday()
quantity= 1
subtotal= 0
while quantity != 0:
    quantity= int(input("Enter the quantity: "))
    if quantity != 0:
        price= float(input("Enter the price: "))
        subtotal += quantity * price

print(f"Total order {subtotal}")
discount=0
if DOW==2 or DOW==3:
    if subtotal > 50:
        discount= subtotal * DISCOUNT_RATE
        print(f"Discount {discount:.2f}")
    else:
        short=50-subtotal
        print(f"You need {short} more of purchase to get a discount")
subtotal -=discount
tax = subtotal * TAX_RATE
total = subtotal + tax

print(f"Tax {tax:.2f}")
print(f"Total Due {total}")