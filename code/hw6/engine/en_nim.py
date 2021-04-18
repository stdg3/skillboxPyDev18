"""
...
"""

STACKCOUNTER = 3
MAXITEMINSTACK = 30

_stack = []

from random import randint


# def init_players():    
#     print("How much players will be play?[2-5]", end=": ")
#     playerCounter = int(input())
#     for _ in range(0, playerCounter):
#         name = input("{} Player input name: ".format(_ + 1))
#         _players.append(name)
#     print("Let's Go")
#     return _players[0]


def new_stack():
    for _ in range(STACKCOUNTER):
        stack = randint(1, MAXITEMINSTACK + 1)
        _stack.append(stack)

    # view_stack()


def take_stone(quantity, stack_number):
    stackNR = stack_number - 1
    next_gamer = False
    if 0 <= stackNR < STACKCOUNTER: # geçerli stack
        if 0 < quantity <= _stack[stackNR]:
            _stack[stackNR] -= quantity
            next_gamer = True
        else:
            print("Girilen değer alınabilecek maximumdan büyük!")
    else:
        print("Geçerli stack seçiniz")
    # view_stack()
    return(next_gamer)


def to_next_player(_players, curentPl):
    if game_over_ctrl():
        return(curentPl)
    else:
        indCurPlyr = _players.index(curentPl)
        if indCurPlyr == len(_players) - 1:
            indCurPlyr = 0
        else:
            indCurPlyr += 1
        # print(_players[indCurPlyr])
        return(_players[indCurPlyr])


def view_stack():
    print(_stack)
    

def game_over_ctrl():
    contGame = any(_stack)
    # print(contGame)
    # for _ in _stack:
    #     if _ == 0:
    #         over = True
    return not contGame

if __name__ == "__main__":
    pass
