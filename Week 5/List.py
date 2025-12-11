clients =[]
new_client = ""

while new_client != "quit":
    new_client = input("Name of new Client: ")
    if new_client != "quit":
        clients.append(new_client)


print()
print("The clients are: ")
for client in clients:
    print(client)