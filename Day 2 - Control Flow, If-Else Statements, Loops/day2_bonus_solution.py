# Day 2 Bonus Challenge: Simple Guessing Game with Limited Guesses

import random

# Choose a random number between 1 and 100
number_to_guess = random.randint(1, 100)

# Limit the number of guesses
max_attempts = 10

for attempt in range(max_attempts):
    user_guess = int(input("Guess a number between 1 and 100: "))
    if user_guess > number_to_guess:
        print("Too high!")
    elif user_guess < number_to_guess:
        print("Too low!")
    else:
        print("You guessed it! Congratulations!")
        break
else:
    print(f"Sorry, you didn't guess the number within {max_attempts} attempts. The number was {number_to_guess}.")
