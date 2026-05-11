#modules:
import math

number_items = int(input("Enter the number of items: "))
items_perbox = int(input("Enter the number of items per box: "))

number_boxes = math.ceil(number_items/items_perbox)

print()

print(f"For {number_items}, packing {items_perbox}, you will need {number_boxes}.")