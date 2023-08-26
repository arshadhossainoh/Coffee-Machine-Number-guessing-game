import random

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

# function to check user's guess against actual answer
def check_answer(guess, answer, turns):
    if guess > answer:
        print("Too high..")
        return turns - 1
    elif guess < answer:
        print("Too low..")
        return turns - 1
    else:
        print(f"You got it, the answer is {answer}")

# function to set difficulty
def set_difficulty():
    level = input("choose a difficulty. type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def game():
    print("Welcome to the Number Guessing Game!")
    print("I am thinking of a number between 1 & 100")
    answer = random.randint(1, 100)
    print(f"the correct answer is {answer}")
    turns = set_difficulty()
    

    guess = 0

    while guess != answer:
        print(f"you have {turns} attempts remaining to guess the number")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("you are out of guesses, you lose")
            return



game()