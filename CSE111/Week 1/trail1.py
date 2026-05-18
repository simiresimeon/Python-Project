#print(f'21 % 5 == {21 % 5}')
#print(f'45 % 5 == {45 % 5}')
#print(f'5 % 1 == {5 % 1}')
#print(f'3 % 8 == {3 % 8}')
#print(f'-3 % 8 == {-3 % 8}')
#print(f'3 % -8 == {3 % -8}')
#print(f'-3 % -8 == {-3 % -8}') 


span = float (input('Distance the cable must span in meters: '))
dip = float (input('Distance the cable will sag in meters: '))

length =span + (8 * dip ** 2) / (3 * span)

print(f'The length of the cable is {length:.2f} meters.')