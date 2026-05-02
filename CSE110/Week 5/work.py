smallest = 8
my_list=[1,3,5]

for value in my_list:
    if value < smallest:
        smallest = value

print(f"The smallest is {smallest}")