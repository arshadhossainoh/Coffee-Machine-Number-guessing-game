logo = """
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     
"""

vs = """
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
"""

import random
import os
from gameData import data


print(logo)

score = 0

# Format account data into printable format
def format_data(account):
   name = account["name"]
   description = account["description"]
   country = account["country"]
   return f"{name}, a {description}, from {country}"

# Take the user guess and follower counts and returns if they got it right
def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"

game_on = True
account_B = random.choice(data)

while game_on:
# generate a random account from the game data
    account_A = account_B
    account_B = random.choice(data)
    if account_A == account_B:
        account_B = random.choice(data)

    print(f"Compare A: {format_data(account_A)}")
    print(vs)
    print(f"Against B: {format_data(account_B)}")

    guess = input("who has more following? type 'a' or 'b': \n")

    a_follower_count = account_A["follower_count"]
    b_follower_count = account_B["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    os.system('cls')

    if is_correct:
        score += 1
        print(f"you are right, current score {score}!")
    else:
        game_on = False
        print(f"sorry, that's wrong, final score {score}")
