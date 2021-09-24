# import random
#
# num = random.randint(0, 10)
#
# guess = int(input("Введите число от 0 до 10 : "))
#
# while num != guess:
#     if guess < num:
#         print("Мало")
#         guess = int(input("Введите число от 0 до 10  "))
#     elif guess > num:
#         print("Многo")
#         guess = int(input("Введите число от 0 до 10 : "))
#     else:
#         print("Вы угадали")



import random
            #камень бумага ножницы
choices = ["камень", "бумага", "ножницы"]
print("камень > ножницы, ножницы > бумага , бумага > камень")
player = input("Выберите: камень, ножницы , бумага или выйти (quit): ")
while player != "quit":
    player = player.lower()
    computer = random.choice(choices)
    print("Вы выбрали",player,"компьтер выбрал",computer)
    if player == computer:
        print("ничья")
    elif player == "камень":
        if computer == "ножницы":
            print("Вы выйграли")
        else:
            print("Вы проиграли!")
    elif player == "бумага":
        if computer == "камень":
            print("Вы выйграли")
        else:
            print("Вы проиграли")

    elif player == "ножницы":
        if computer == "бумага":
                print("Вы выйрали")
        else:
            print("Вы проиграли")
    else:
        print("Произошла какая-то ошибка")
    print()
    player = input("Выберите: камень, ножницы , бумага или выйти (quit): ")

