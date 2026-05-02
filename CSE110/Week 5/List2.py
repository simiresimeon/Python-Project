friends= []
new_friend= ""
trial_count= ""
while new_friend != "end":
    new_friend = input("Type the name of a friend: ")
    trial_count += 1
    if new_friend != "end":
        friends.append(new_friend)


print()
print("Your friends are: ")
for friend in friends:
    print(friend)



