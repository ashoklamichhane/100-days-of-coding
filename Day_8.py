print(
    '''
,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,
a8"     "" ""     'Y8 a8P_____88 I8[    "" ""     'Y8 88P'   "Y8
8b         ,adPPPPP88 8PP"""""""  '"Y8ba,  ,adPPPPP88 88
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88
 '"Ybbd8"' '"8bbdP"Y8  '"Ybbd8"' '"YbbdP"' '"8bbdP"Y8 88
            88             88
           ""             88
                          88
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8
8b         88 88       d8 88       88 8PP""""""" 88
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88
 '"Ybbd8"' 88 88'YbbdP"'  88       88  '"Ybbd8"' 88
              88
              88
    '''
)

letter_list = list("abcdefghijklmnopqrstuvwxyz")

def cipher(user_request, shift_num, user_message):
    result = ""

    if user_request == "encode":
        for letter in user_message:
            i_num = letter_list.index(letter)
            result +=letter_list[i_num + shift_num]
    elif  user_request == "decode":
        for letter in user_message:
            i_num = letter_list.index(letter)
            result +=letter_list[i_num - shift_num]
    return result


while True:

    user_request = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    # print(user_request)

    if user_request not in ["encode","decode"]:
        print("Invalid choice")
        break

    print("Type your message:")
    user_message = input().lower()

    print("Type the shift number:")
    shift_num = int(input())

    final_result = cipher(user_request,shift_num ,user_message)
    print(f"Here's the encoded result: {final_result}")

    user_status = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")

    if user_status.lower() == "no":
        break