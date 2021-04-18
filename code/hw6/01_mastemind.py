# -*- coding: utf-8 -*-


# Ним — математическая игра, в которой два игрока по очереди берут предметы,
# разложенные на несколько кучек. За один ход может быть взято любое количество предметов
# (большее нуля) из одной кучки. Выигрывает игрок, взявший последний предмет.
# В классическом варианте игры число кучек равняется трём.

# Составить модуль, реализующий функциональность игры.
# Функции управления игрой
#  разложить_камни()
#  взять_из_кучи(NN, KK)
#  положение_камней() - возвращает список [XX, YY, ZZ, ...] - текущее расположение камней
#  есть_конец_игры() - возвращает True если больше ходов сделать нельзя
#
#
# В текущем модуле (lesson_006/python_snippets/04_practice.py) реализовать логику работы с пользователем:
#  начало игры,
#  вывод расположения камней
#  ввод первым игроком хода - позицию и кол-во камней
#  вывод расположения камней
#  ввод вторым игроком хода - позицию и кол-во камней
#  вывод расположения камней


from engine.en_nim import new_stack, take_stone, view_stack, game_over_ctrl,  to_next_player

def init_players():   
    _players = [] 
    print("How much players will be play?[2-5]", end=": ")
    playerCounter = int(input())
    for _ in range(0, playerCounter):
        name = input("{} Player input name: ".format(_ + 1))
        _players.append(name)
    print("Let's Go")
    return _players


def start_nim():
    new_stack()
    players = init_players() 
    currentGamer = players[0]
    stoneTaked = False
    while True:
        view_stack()
        print(currentGamer)
        stackNr = int(input("Stack: "))
        q = int(input("Adet: "))
        if take_stone(q, stackNr):
            currentGamer = to_next_player(players, currentGamer)
        if game_over_ctrl():
            print("you winnn!", currentGamer)
            break

# import engine.en_nim as qwe

# print(qwe.__doc__)

# pl = init_players()
# to_next_player(pl)

# stackNr = int(input("Stack: "))
# q = int(input("Adet: "))

# take_stone(q, stackNr)

# start_nim()
# ===========================================

# Игра «Быки и коровы»
# https://goo.gl/Go2mb9
#
# Правила:
# Компьютер загадывает четырехзначное число, все цифры которого различны
# (первая цифра числа отлична от нуля). Игроку необходимо разгадать задуманное число.
# Игрок вводит четырехзначное число c неповторяющимися цифрами,
# компьютер сообщают о количестве «быков» и «коров» в названном числе
# «бык» — цифра есть в записи задуманного числа и стоит в той же позиции,
#       что и в задуманном числе
# «корова» — цифра есть в записи задуманного числа, но не стоит в той же позиции,
#       что и в задуманном числе
#
# Например, если задумано число 3275 и названо число 1234,
# получаем в названном числе одного «быка» и одну «корову».
# Очевидно, что число отгадано в том случае, если имеем 4 «быка».
#
# Формат ответа компьютера
# > быки - 1, коровы - 1

from engine.eng_cows import get_secret, SECRET_LEN, bulls_cows_counter


def your_guess():
    guess = -1
    get_gues = True
    while len(str(guess)) != SECRET_LEN or get_gues == True:
        guess = input("guess number of {dgt} digit: ".format(dgt=SECRET_LEN))
        for _ in str(guess):            
            if str(guess).count(_) > 1:
                # print("gigits can not repeat")
                get_gues = True
                break
            else:
                get_gues = False


    # print(guess)
    return int(guess)


def guess_bulls_cows():
    secret = get_secret()
    counter = 0
    while True:
        
        guess = your_guess()
        counter += 1
        bc = bulls_cows_counter(secret, guess)
        print(bc)
        if bc["bulls"] == SECRET_LEN:
            print("tried:", counter)
            print("u win", "\ndo u want to cont? y/n")
            devam = input()
            if devam == "y":
                secret = get_secret()
                counter = 0
            else:
                break

if __name__ == "__main__":
    
    start_nim()
    guess_bulls_cows()

