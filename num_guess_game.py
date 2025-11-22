import random
print("***********Welcome to the Number Guess Game!***********")
def choose_difficulty():
    print("\nSelect Difficulty Level:")
    print("1. Easy   (1–50, 10 attempts)")
    print("2. Medium (1–50, 7 attempts)")
    print("3. Hard   (1–100, 10 attempts)")

    while True:
        choice = input("Enter your choice (1/2/3): ").strip()
        if choice == "1":
            print("\n Easy Level")
            return 50, 10
        elif choice == "2":
            print("\n Medium Level")
            return 50, 7
        elif choice == "3":
            print("\nHard Level")
            return 100, 10
        else:
            print("Invalid choice! Please choose 1, 2, or 3.")

def number_guessing_game():
    max_num, attempts_left = choose_difficulty()
    secret_number = random.randint(1, max_num)

    print(f"\nGuess the number between 1 and {max_num}.")

    while attempts_left > 0:
        try:
            guess = int(input(f"\nEnter your guess ({attempts_left} attempts left): "))

            if guess <= 0 or guess > max_num:
                print(f"Please enter a number between 1 and {max_num}.")
                continue

            attempts_left -= 1

            if guess == secret_number:
                print(f"\n Congrats! The number was {secret_number}.")
                print(f"You guessed it with {attempts_left} attempts remaining!")
                return

            elif guess < secret_number:
                print("📉 Your guess is Lower.")
            else:
                print("Your guess is Higher.")

        except ValueError:
            print("Please enter a valid number.")

    print(f"\n Out of attempts! The number was {secret_number}.")
    print("******* GAME OVER *******")

while True:
    number_guessing_game()
    play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
    if play_again not in ("yes", "y"):
        print("\nThanks for playing!")
        break