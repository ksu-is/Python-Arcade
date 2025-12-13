import random

while True:
    # Set the range
    LOWER_BOUND = 1
    UPPER_BOUND = 10  # Change to 100, etc.

    secret_number = random.randint(LOWER_BOUND, UPPER_BOUND)

    print(f"\nI'm thinking of a number between {LOWER_BOUND} and {UPPER_BOUND}.")

    while True:
        guess = input("Enter your guess: ")

        if not guess.isdigit():
            print("Please enter a valid number.")
            continue

        guess = int(guess)

        if guess < secret_number:
            print("Sorry, that's incorrect! Try a higher number.")
        elif guess > secret_number:
            print("Sorry, that's incorrect! Try a lower number.")
        else:
            print("Correct! You guessed the number!")
            break  # Exit guessing loop

    # Ask to play again
    play_again = input("Would you like to play again? (y/n): ").lower()

    if play_again != "y":
        print("Thanks for playing!")
        break  # Exit game loop