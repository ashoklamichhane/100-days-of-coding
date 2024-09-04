import random


def secret_word(word_choice, user_choice, attempts):
    placeholder = ""
    for i in range(len(word_choice)):
        if user_choice == word_choice[i]:
            placeholder += str(user_choice)
            attempts += 1
        else:
            placeholder += "_"
    print(placeholder)

words = ["camel","baboon","aardvark"]

word_choice = random.choice(words)
print(word_choice)

attempts = 6
while attempts > 0:
    user_choice = str(input("Choose a letter:\n"))
    secret_word(word_choice, user_choice)


# print(user_choice)



# for letter in word_choice:
#     if letter  == user_choice:
#         print("Yes")
#     else:
#         print("No")