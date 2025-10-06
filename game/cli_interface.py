from .logic import play_game, play_hard_game

def start_game():
    lvl = input("Выберите уровень сложности: легкий, средний, сложный\n").lower()

    if lvl in ("легкий", "средний", "сложный"):
        if lvl == "легкий":
            play_game(50)
        elif lvl == "средний":
            play_game(100)
        elif lvl == "сложный":
            play_hard_game(200)
    else:
        print("Введите корректный уровень сложности")
        start_game()