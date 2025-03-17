#!/usr/bin/env python3
"""
numberGuessingGame.py - A simple number guessing game.

Author: Carlos Valerio (CarlosValerioM)
Date: 2025/03/12
License: MIT
Dependencies: None (built-in functions only)

Description:
This script runs a number guessing game where the player tries to guess a randomly generated number between 1 and 100.
The game offers two difficulty levels:
1. 'Easy' - The player has 10 attempts.
2. 'Hard' - The player has 5 attempts.

The script provides hints if the guess is too high or too low. The game ends when the player either guesses correctly or runs out of attempts.

Usage:
Run the script and follow the prompts:
    python numberGuessingGame.py

Example Output:
    Type 'easy' or 'hard' to set difficulty: easy
    Guess my number (1-100): 50
    Too high! Try a lower number. Lives remaining: 9
    Guess my number (1-100): 25
    Too low! Try a higher number. Lives remaining: 8
    Guess my number (1-100): 33
    Congratulations! You guessed correctly. The number was 33.
"""
import random

def main():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)

    # Ask for difficulty level
    difficulty = input("Type 'easy' or 'hard' to set difficulty: ").strip().lower()
    lives = 10 if difficulty == 'easy' else 5  # Set lives based on difficulty

    guess = None  # Initialize guess

    while lives > 0 and guess != secret_number:
        try:
            # Get user input and ensure it's a valid number
            guess = int(input("Guess my number (1-100): "))

            if guess > secret_number:
                lives -= 1
                print(f"Too high! Try a lower number. Lives remaining: {lives}")

            elif guess < secret_number:
                lives -= 1
                print(f"Too low! Try a higher number. Lives remaining: {lives}")

        except ValueError:
            print("Invalid input! Please enter a number between 1 and 100.")

    # Check if the user won or lost
    if lives == 0:
        print(f"Sorry! You lost. The correct number was {secret_number}.")
    else:
        print(f"Congratulations! You guessed correctly. The number was {secret_number}.")

if __name__ == '__main__':
    main()