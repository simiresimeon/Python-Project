# Author: Simire Simeon Obamiegie
# Creative Addition: The game selects a random word from a list and limits guesses to 10 attempts.

import random

# List of possible secret words
word_list = ["Moroni", "Zion", "Nephi", "Laman", "Omni"]
secret = random.choice(word_list).lower()

print("\nWelcome to the word guessing game!\n")
print("Try to guess the secret word. You have 10 attempts.\n")

guess_count = 0
max_guesses = 10

while guess_count < max_guesses:
    guess = input("What is your guess? ").lower()
    guess_count += 1

    # Check if guess length matches secret word length
    if len(guess) != len(secret):
        print(f"Your guess must be {len(secret)} letters long.\n")
        continue

    # Generate hint using a for loop
    hint = ""
    for i in range(len(secret)):
        if guess[i] == secret[i]:
            hint += guess[i].lower() + " "  # Correct letter and position
        elif guess[i] in secret:
            hint += guess[i].upper() + " "  # Correct letter, wrong position
        else:
            hint += "_ "  # Letter not in word

    print("Hint:", hint.strip())

    if guess == secret:
        print("\n🎉 Congratulations! You guessed it!")
        print(f"It took you {guess_count} guesses.")
        break
    else:
        print("Your guess was not correct.\n")

if guess != secret:
    print(f"\nGame Over! The secret word was '{secret}'. Better luck next time!")