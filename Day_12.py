import random

logo = """
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_| 
"""

def game_type():
    diff_status  = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if diff_status == "easy":
        attempt = 10
    else:
        attempt = 5

    print(f"You have {attempt} attempts remaining to guess the number.")
    return attempt

def game(attempt_num):
    while attempt_num > 0:

        guess = int(input ("Make a guess: "))
        if guess == correct_num:
            print(f"You got it! The answer was {correct_num}.")
            break
        elif guess < correct_num:
            print("Too low.")
        elif guess > correct_num:
            print("Too high.")

        attempt_num -=1
        if attempt_num > 0:
            print(f"Guess again.\nYou have {attempt_num} attempts remaining to guess the number.")
        else:
            print("You've run out of guesses, you lose.")



print(logo)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

correct_num = random.choice(range(1,101))

attempt_num = game_type()
game(attempt_num)

