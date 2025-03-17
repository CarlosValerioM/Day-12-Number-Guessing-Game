# Day-12-Number-Guessing-Game
Your Number Guessing Game - Difficulty: Easy/Hard

## Author:
Carlos Valerio (CarlosValerioM)

## Date:
2025/03/17

## License:
MIT License

## Dependencies:
None (built-in functions only)

## Description:
`numberGuessingGame.py` is a simple Python script where the player must guess a randomly generated number between 1 and 100.
The game offers two difficulty levels:
1. 'Easy' - The player has 10 attempts.
2. 'Hard' - The player has 5 attempts.

The game provides hints if the guess is too high or too low. The player wins by guessing the number before running out of attempts.

## Usage:

1. Clone this repository:

```bash
git clone https://github.com/CarlosValerioM/Day-12-Number-Guessing-Game.git
```
Navigate to the project directory:

```bash
cd Day-12-Number-Guessing-Game
```
Run the script:

```bash
python numberGuessingGame.py
```
The script will prompt you for input, and based on your responses, it will guide you towards the correct number.

## Example Output:
```bash
Type 'easy' or 'hard' to set difficulty: easy
Guess my number (1-100): 50
Too high! Try a lower number. Lives remaining: 9
Guess my number (1-100): 25
Too low! Try a higher number. Lives remaining: 8
Guess my number (1-100): 33
Congratulations! You guessed correctly. The number was 33.
```
## How it works:
1. The user selects a difficulty level.
2. A random number between 1 and 100 is generated.
3. The user enters a guess, and the script provides feedback if the guess is too high or too low.
4. The player wins by guessing the correct number before running out of attempts.

## License:
This project is licensed under the MIT License.
