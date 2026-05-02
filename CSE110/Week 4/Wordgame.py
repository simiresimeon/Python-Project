#Author: Simire Simeon Obamiegie



secret="Moroni"
print()
print("Welcome to the word guessing game! ")
print()

guess= input("What is your guess? ")
guess_count= 0

while guess!= secret:
     
    print("Your guess was not correct.")
 
    guess= input("What is your guess? ")
    guess_count += 1

print("Congratulations! You guessed it! ")
print(f"It took you {guess_count} guesses. ")