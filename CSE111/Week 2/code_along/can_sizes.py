import math



def main():
    print()
    name = "#1 Picnic"
    radius = 6.83  
    height = 10.16
    volume = round(compute_volume(radius,height))
    surface_area = round(compute_surface_area(radius,height))

    print(f"The volume of the cylinder is {volume}")
    print(f"The surface area of the cylinder is {surface_area}")    




def compute_volume(radius,height):
    """Compute the volume of the cylinder"""

    volume = math.pi * radius **2 * height

    #return volume value
    return volume

def compute_surface_area(radius, height):
    
    #calute the Surface area of cylinder
    surface_area = 2 * math.pi * radius * (radius + height)

    #return surface_area
    return surface_area

def can_storage_efficiency ():
        # calute the Storage efficiency of the can
    efficiency =

main()