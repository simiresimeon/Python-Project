payment=float(input("What is the payment amount? "))

while payment < 0:
    print(f"sorry the payment cannot be negative")

    payment= float(input("What is the payment amount? "))

    print("...")
    print("...")
    print("...")    
    print("...")


print(f"The amount is: ${payment:.2f}")