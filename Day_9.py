print('''
        ____________
      /   ,,____,,   \:.
      |__| [][][] |__|:  :
        /  [][][]  \   :  :
ejm98  /   [][][]   \   :  :
      /    [][][]    \   ..
=====|________________|
'''
)

bid_db = {}

while True:
    user = input("What is your name?: ")
    amount = input("What is your bid?: $")

    bid_db[user] = amount
    print(bid_db)
    user_status = input("Are there any other bidders? Type 'yes' or 'no'\n")

    if user_status.lower() == "no":
        max_value = 0
        winner = {}
        for key in bid_db:
            if int(bid_db[key]) > max_value:
                winner = {}
                max_value = int(bid_db[key])
                winner[key] = bid_db[key]
        print(winner)
        break


print(f"The winner is {user} with a bid of ${amount}")