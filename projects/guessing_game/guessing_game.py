# guessing_game.py

import random

def main():
    """Main function to run the number guessing game."""
    print("Welcome to the Number Guessing Game!")
    
    # Define the range for the random number
    lower_bound = 1
    upper_bound = 100
    secret_number = random.randint(lower_bound, upper_bound)

    attempts = 0
    guess = None

    while guess != secret_number:
        try:
            guess = int(input(f"Guess a number between {lower_bound} and {upper_bound}: "))
            attempts += 1

            if guess < lower_bound or guess > upper_bound:
                print(f"Please enter a number within the range {lower_bound} to {upper_bound}.")
            elif guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You've guessed the number {secret_number} in {attempts} attempts.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")

if __name__ == "__main__":
    main()
