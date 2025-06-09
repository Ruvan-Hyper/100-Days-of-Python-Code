from random import randint
from art import logo
print(logo)

EASY_LEVEL_TURN = 10
HARD_LEVEL_TURN = 5

def check_answer(user_guess, actual_answer,turn):
    if user_guess > actual_answer:
        print("To High")
        return turn - 1
    elif user_guess < actual_answer:
        print("To Low")
        return turn - 1
    else:
        print(f"You got it! The answer is {actual_answer}")

def set_difficulty():
    level = input("Chose a difficulty: Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURN
    else:
        return HARD_LEVEL_TURN

def game():
    # Choosing a random number between 1 and 100
    print(f"Pssst, the correct answer is {answer}")
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
answer = randint(1, 100)

turns = set_difficulty()
# Repeat the guessing functionality if they get it wrong
guess = 0
while guess != answer:
    print(f"You have {turns} attempts remaining to guess the number:")
    # Let the user guess a number
    guess = int(input("Make your guess:"))
    turns = check_answer(guess,answer,turns)
    if turns == 0:
        print("You have run out of guesses, You Lose!")
    elif guess != answer:
        print("Guess again.")

game()