# Import the math module so i can you the math.pi and math.sqrt.
import math

#Get the radius and the height from the user
radius= float(input("Enter the radius of a cone: "))
height= float(input("Enter the height of a cone: "))

# comput the surface area of the cone
radical = math.sqrt(radius**2 + height**2)
surface_area= math.pi * radius * (radius + radical)

# round the surface area to 1 decimal point
surface_area= round(surface_area, 1)

# print the surface area for the user to see
print(f'The surface area of the cone is {surface_area}')
