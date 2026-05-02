payment= -1

while payment < 0:
    payment = float(input("What is the payment amount? "))
    
print(f"The amount is ${payment:.2f}")