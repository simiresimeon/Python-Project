import random

secret_number= random.randint(1,100)

guess_count= 0

guess= int(input("Guess a number: "))

while guess != secret_number:

    if guess == 50:
        print("You are getting close!")

    if guess > secret_number :
        print("that was too high, guess low!")
    else:
        print("that was too low, guess higher!")
        

    guess= int(input("guess again: "))
    guess_count += 1

print("You got it! ")
print(f"and it only took you {guess_count} guesses. ")