# Enhancement:
# Added 4 tire prices for four different tire sizes.
# After calculating the volume, the program displays the price.
# If the customer chooses to buy, the program asks for the
# customer's phone number and stores it in volumes.txt.
# logged the price and phone number in volumes.txt

# import the math module so I can use math.pi
import math

from datetime import date
# get the width, aspect ratio and diameter from the user
width = float(input("Enter the width of the tire in mm "))
aspect_ratio = int(input("Enter the aspect ratio of the tire "))
diameter = float(input("Enter the diameter of the wheel in inches "))

# compute the volume of the tire
tire_volume = (math.pi * width ** 2 * aspect_ratio * (width * aspect_ratio + 2540 * diameter)) / 10000000000

# print the volume of the tire and round it to 2 decimal places for the user to see
print(f"The approximate volume is {tire_volume:.2f} liters")

price = 0

if width == 185 and aspect_ratio == 50 and diameter == 14:
    price = 100
elif width == 205 and aspect_ratio == 60 and diameter == 15:
    price = 150
elif width == 225 and aspect_ratio == 70 and diameter == 16:
    price = 200
elif width == 245 and aspect_ratio == 80 and diameter == 17:
    price = 250
else:
    print("Sorry, there is no tire with these specifications.")

if price > 0:
    print(f"The price of the tire is ${price}")

today = date.today()

if price > 0:
    purchase = input("Do you want to buy tires with the dimensions entered? (yes/no): ").lower()

    if purchase == "yes":
        phone_number = input("What is your phone number? ")
        with open("volumes.txt", "a") as file:
            file.write(f"{today}, {width}, {aspect_ratio}, {diameter}, {tire_volume:.2f}, ${price:.2f}, {phone_number}\n")
    else:
        print("Thank you for your patronage. See you again soon.")
        with open("volumes.txt", "a") as file:
            file.write(f"{today}, {width}, {aspect_ratio}, {diameter}, {tire_volume:.2f}\n")


