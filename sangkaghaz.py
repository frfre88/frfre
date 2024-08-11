import random


user_wins = 0
computer_wins = 0
options = ["r", "p", "s"]


while True:
    user_input = input("type R / P / S or Q to quit: ").lower()

    if (user_input == "q"): break


    if (user_input not in options): continue

    random_nomber = random.randint(0, 2)

    computer_pick = options[random_nomber]


    if (user_input == "r" and computer_pick == "s") or (user_input == "p" and computer_pick == "r") or (user_input == "s" and computer_pick == "p"):

        print("you won!")
        user_wins += 1


    elif (computer_pick == "r" and user_input == "s") or (computer_pick == "p" and user_input == "r") or (computer_pick == "s" and user_input == "p"):

        print("computer won!")
        computer_wins += 1

    elif (user_input == computer_pick):
        print("bazi mosavy shod!")


print("you: ", user_wins)
print("computer: ", computer_wins)