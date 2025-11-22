import random

def number_guess_game():
    print("Welcome to the Number Guess Game!")
    number = random.randint(1, 50)
    attempts = 0

    while True:
        guess = int(input("Enter your guess (1-100): "))
        attempts += 1

        if guess < number:
            print("Too low! Try again.")
        elif guess > number:
            print("Too high! Try again.")
        else:
            print(f"🎉 Correct! The number was {number}.")
            print(f"You guessed it in {attempts} attempts.")
            break

number_guess_game()