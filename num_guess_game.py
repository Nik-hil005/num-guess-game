import random

def number_guessing_game():
    print("Welcome to the Number Guess Game!")
    print("Guess the number between 1 and 50.")
    print("You have 7 attempts to get it right.")

    secret_number = random.randint(1, 50)
    attempts_left = 7

    while attempts_left > 0:
        try:
            guess = int(input(f"Enter your guess! ({attempts_left} attempts left): "))


            if guess <= 0 or guess > 50:
                print("Please enter a number between 0 and 50.")
                continue

            attempts_left -= 1

            if guess == secret_number:
                print(f"Congrats! The number was {secret_number}. You nailed it with {attempts_left} attempts remaining.")
                break
            elif guess < secret_number:
                print("Your guess is below the mark.")
            else:
                print("Your guess overshot the target.")
        except ValueError:
            print("Please enter a valid number.")

    if attempts_left == 0:
        print(f"Out of attempts! The number was {secret_number}.")
        print("*******GAME OVER*******")

while True:
    number_guessing_game()
    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again not in ("yes", "y"):
        print("Thanks for playing!")
        break