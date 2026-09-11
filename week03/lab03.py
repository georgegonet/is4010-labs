def generate_mad_lib(adjective, noun, verb):
    """Return a nonempty story containing all three supplied words."""
    return f"One day, a {adjective} {noun} decided to {verb} across the countryside."
import random

def guessing_game():
    """Run an interactive number-guessing game."""
    secret = random.randint(1, 100)

    while True:
        guess_str = input("Enter your guess: ")
        guess = int(guess_str)

        if guess < secret:
            print("Too low!")
        elif guess > secret:
            print("Too high!")
        else:
            print("Correct! You guessed the number!")
            break
