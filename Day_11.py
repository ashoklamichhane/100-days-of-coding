
import random

diagram = ("""
.------.            _     _            _    _            _
|A_  _ |.          | |   | |          | |  (_)          | |
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _' |/ __| |/ / |/ _' |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   <
'-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\
      |  \/ K|                            _/ |
      '------'                           |__/
""")

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def results(user_score, user_list, comp_score, comp_list):

    print(f"Your final hand = {user_list}, final score = {user_score}")
    print(f"Computer's final hand = {comp_list}, final_score = {comp_score}")

    if user_score == comp_score:
        print("Its a Tie")
    elif user_score > 21:
        print("You went over. You lose 😭")
    elif comp_score > 21:
        print("Opponent went over. You win 😁")
    elif user_score > comp_score:
        print("You win 😁")
    elif comp_score > user_score:
        print("You lose 😤")


def black_jack():
    user_list =  random.choices(cards, k=2)

    user_score = sum(user_list)
    print(f"Your cards: {user_list}, current score: {user_score}")
    comp_list = [random.choice(cards)]
    comp_score = sum(comp_list)
    print(f"Computer's first card: {comp_list}")

    add_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()
    user_bust = False
    while user_bust == False and add_card == "y":
        user_list.append(random.choice(cards))
        user_score = sum(user_list)
        print(f"Your cards: {user_list}, current score: {user_score}")
        print(f"Computer's first card: {comp_list}")
        if user_score > 21:
            user_bust = True
        else:
            add_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if add_card == "n":
                break


    if user_bust == False:
        while comp_score <= 16 and comp_score < user_score:
            comp_list.append(random.choice(cards))
            comp_score = sum(comp_list)
            # print(comp_list, comp_score)


    results(user_score, user_list, comp_score, comp_list)

while True:
    game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if game.lower() == "n":
        break
    else:
        print(chr(27) + "[2J") #clearing the console
        print(diagram)
        black_jack()