import random

def restart_game(answer, limit, lvl):
    if answer == "да":
        if lvl == "сложный":
            play_hard_game()
        else:
            play_game(limit)
    elif answer == "нет":
        print("Спасибо за игру!")
    else:
        print("Нормально общайся да")

def play_game(limit):
    hidden_number = random.randint(1, limit)
    counter = 0
    try:
        while client_number:= int(input("Угадайте число ")):
            counter += 1

            if client_number > hidden_number:
                print("Загаданное число меньше.")
            elif client_number < hidden_number:
                print("Загаданное число больше.")
            else:
                print(f"Поздравляем! Вы угадали число за {counter} попыток")
                break
    except ValueError:
        print("Введено некорректное значение")
        play_game(limit)

    answer = input("Сыграть еще раз? (да/нет)\n").lower()
    restart_game(answer, limit, lvl="несложный")

def play_hard_game(limit):
    hidden_number = random.randint(1, limit)
    counter = 0
    try:
        while counter < 10:
            client_number = int(input("Угадайте число "))
            counter += 1
            if client_number > hidden_number:
                print("Загаданное число меньше.")
            elif client_number < hidden_number:
                print("Загаданное число больше.")
            else:
                print(f"Поздравляем! Вы угадали число за {counter} попыток")
                break
        print("Вы проиграли")
    except ValueError:
        print("Введено некорректное значение")

    answer = input("Сыграть еще раз? (да/нет)\n").lower()
    restart_game(answer, limit=200,lvl="несложный")