print(
    '''
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------.
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ '.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ '.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   '._____.'  | || ||____|  |____|| || |  |________|  | || |   '._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------'
|_____________________|
    '''
)

def calc(operator, num1, num2):
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        result = num1/num2
    return result

num_1 = float(input("What's the first number?: "))

while True:

    operator = input("[+, -, *, /] From the list pick an operation: ")
    num_2 = float(input("What's the next number?: "))

    result = calc(operator,num_1, num_2)

    print(f"{num_1} {operator} {num_2} = {result}" )

    cal_cont = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation, stop to end ")
    if cal_cont == "y":
        num_1 = result
    elif cal_cont.lower() == "stop":
        break
    else:
        print(chr(27) + "[2J")
        num_1 = float(input("What's the first number?: "))

