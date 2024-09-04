print('''
                            .sssssssss.
                        .sssssssssssssssssss
                      sssssssssssssssssssssssss
                     ssssssssssssssssssssssssssss
                      @@sssssssssssssssssssssss@ss
                      |s@@@@sssssssssssssss@@@@s|s
               _______|sssss@@@@@sssss@@@@@sssss|s
             /         sssssssss@sssss@sssssssss|s
            /  .------+.ssssssss@sssss@ssssssss.|
           /  /       |...sssssss@sss@sssssss...|
          |  |        |.......sss@sss@ssss......|
          |  |        |..........s@ss@sss.......|
          |  |        |...........@ss@..........|
           \  \       |............ss@..........|
            \  '------+...........ss@...........|
             \________ .........................|
                      |.........................|
                     /...........................\\
                    |.............................|
                       |.......................|
                           |...............|
''')

print("Welcome to Treasure Island")
print("Your mission is to find the treasure")
print("You are at the crossroads were do you want to go")
f_input = input('Type "left" or "right"\n')

if (f_input).lower() == "right":
    print("You fell into a hole. Game Over")
elif (f_input).lower() == "left":
    print('You have come to a lake. There is an Island in the middle of the lake')
    s_input = input('Type "wait" to wait for a boat. Type "swim" to swim across\n')
    if (s_input).lower() == "swim":
        print("You get attached by an angry trout. Game Over")
    else:
        print('You arrive at the Island unharmed and there is a house wih  3 doors')
        t_input = input('One red, One yellow and One blue, which colour do you choose\n')
        if (t_input).lower() == "yellow":
            print("You win")
        elif (t_input).lower() != "yellow":
            print("You loose")