import random

import art
import game_data


score = 0
random.shuffle(game_data.data)
print(art.logo)

for user in range(len(game_data.data) - 1):

    user_a = (game_data.data[user])
    user_b = (game_data.data[user + 1])


    print(f"Compare A: {user_a["name"]}, a {user_a["description"]}, from {user_a["country"]}")
    print(art.vs)
    print(f"Compare B: {user_b["name"]}, a {user_b["description"]}, from {user_b["country"]}")
    user_sel = input("Who has more followers? Type 'A' or 'B': ").lower()

    if user_sel == "a":
        if user_a["follower_count"] >= user_b["follower_count"]:
            score +=1
        else:
            print(chr(27) + "[2J")
            print(art.logo)
            print(f"Sorry, that's wrong. Final score: {score}")
            break

    elif user_sel == "b":
        if user_a["follower_count"] <= user_b["follower_count"]:
            score +=1
        else:
            print(chr(27) + "[2J")
            print(art.logo)
            print(f"Sorry, that's wrong. Final score: {score}")
            break

    print(chr(27) + "[2J")
    print(art.logo)
    print(f"You're right! Current score: {score}")