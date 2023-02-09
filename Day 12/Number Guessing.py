#Number Guessing Game Objectives:
import random
# Include an ASCII art logo.
from Art import logo
print(logo)
# Allow the player to submit a guess for a number between 1 and 100.
number = random.randint(0, 100)
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
def check_answer(number, turns):
    for x in range(0, turns):
        guess = int(input("Enter Number between 1 to 100: "))
        if guess == number:
            print(f"You got is, The number was {number}")
            break
        elif guess < number:
            print("Too Low")
        elif guess > number:
            print("Too High")
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
        tries = turns - (x + 1)
        if tries > 0:
            print(f"You have {tries} tries remaining")
# If they run out of turns, provide feedback to the player.
        else:
            print("You are out of Tries")
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
difficulty = input("Enter Difficulty: ").lower()

if difficulty == "easy":
    turns = 10
elif difficulty == "hard":
    turns = 5

check_answer(number, turns)


# Angela Answer:

# from random import randint
# from art import logo
#
# EASY_LEVEL_TURNS = 10
# HARD_LEVEL_TURNS = 5
#
# #Function to check user's guess against actual answer.
# def check_answer(guess, answer, turns):
#   """checks answer against guess. Returns the number of turns remaining."""
#   if guess > answer:
#     print("Too high.")
#     return turns - 1
#   elif guess < answer:
#     print("Too low.")
#     return turns - 1
#   else:
#     print(f"You got it! The answer was {answer}.")
#
# #Make function to set difficulty.
# def set_difficulty():
#   level = input("Choose a difficulty. Type 'easy' or 'hard': ")
#   if level == "easy":
#     return EASY_LEVEL_TURNS
#   else:
#     return HARD_LEVEL_TURNS
#
# def game():
#   print(logo)
#   #Choosing a random number between 1 and 100.
#   print("Welcome to the Number Guessing Game!")
#   print("I'm thinking of a number between 1 and 100.")
#   answer = randint(1, 100)
#   print(f"Pssst, the correct answer is {answer}")
#
#   turns = set_difficulty()
#   #Repeat the guessing functionality if they get it wrong.
#   guess = 0
#   while guess != answer:
#     print(f"You have {turns} attempts remaining to guess the number.")
#
#     #Let the user guess a number.
#     guess = int(input("Make a guess: "))
#
#     #Track the number of turns and reduce by 1 if they get it wrong.
#     turns = check_answer(guess, answer, turns)
#     if turns == 0:
#       print("You've run out of guesses, you lose.")
#       return
#     elif guess != answer:
#       print("Guess again.")
#
#
# game()



