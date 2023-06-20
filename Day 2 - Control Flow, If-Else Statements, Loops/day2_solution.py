# Day 2 Challenge: Simple Guessing Game

import random

# Choose a random number between 1 and 100
number_to_guess = random.randint(1, 100)

# Loop until the user guesses the number
while True:
    user_guess = int(input("Guess a number between 1 and 100: "))
    if user_guess > number_to_guess:
        print("Too high!")
    elif user_guess < number_to_guess:
        print("Too low!")
    else:
        print("You guessed it! Congratulations!")
        break
