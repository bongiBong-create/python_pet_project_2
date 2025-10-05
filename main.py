import random

hidden_number = random.randint(1, 5)
counter = 0
flag = True

while flag:
    client_number = int(input("Угадайте число "))
    counter += 1

    if client_number > hidden_number:
        print("Загаданное число меньше.")
    elif client_number < hidden_number:
        print("Загаданное число больше.")
    else:
        print(f"Поздравляем! Вы угадали число за {counter} попыток")
        flag = False