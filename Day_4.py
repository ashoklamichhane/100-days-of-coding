import random

while True:
    choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

    if choice == 0:
        # Rock
        print("""
            _______
        ---'   ____)
            (_____)
            (_____)
            (____)
        ---.__(___)
        """)
    elif choice == 1:
        # Paper
        print("""
            _______
        ---'    ____)____
                ______)
                _______)
                _______)
        ---.__________)
        """)
    elif choice == 2:
        # Scissors
        print("""
            _______
        ---'   ____)____
                ______)
            __________)
            (____)
        ---.__(___)
        """)
    else:
        print("Invalid selection")

    comp = random.randint(0,2)
    print(comp)
    if comp == 0:
        # Rock
        print("""
            _______
        ---'   ____)
            (_____)
            (_____)
            (____)
        ---.__(___)
        """)
    elif comp == 1:
        # Paper
        print("""
            _______
        ---'    ____)____
                ______)
                _______)
                _______)
        ---.__________)
        """)
    elif comp == 2:
        # Scissors
        print("""
            _______
        ---'   ____)____
                ______)
            __________)
            (____)
        ---.__(___)
        """)


    if choice == comp:
        print("It's a draw")
    elif choice == 0 and comp == 1:
        print("You lose")
    elif choice == 0 and comp == 2:
        print("You won!")
    elif choice == 1 and comp == 0:
        print("You won!")
    elif choice == 1 and comp == 2:
        print("You lose")
    elif choice == 2 and comp == 0:
        print("You lose")
    elif choice == 2 and comp == 1:
        print("You won!")

    game_over = input('Do you want to Quit, type "No"\n').lower()
    if game_over == "no":
        break
