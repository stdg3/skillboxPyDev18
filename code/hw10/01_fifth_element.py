# -*- coding: utf-8 -*-

# Умножить константу BRUCE_WILLIS на пятый элемент строки, введенный пользователем

BRUCE_WILLIS = 42

def bruce():
    
    input_data = input('Если хочешь что-нибудь сделать, сделай это сам: ')
    leeloo = int(input_data[4])
    return BRUCE_WILLIS * leeloo

try:
    q = bruce()
    print(f"- Leeloo Dallas! Multi-pass № {q}!")
except IndexError as errIndex:
    print("err index", errIndex)
except ValueError as errVal:
    print("err val", errVal)
except Exception as ex:
    print("other errors")

# Ообернуть код и обработать исключительные ситуации для произвольных входных параметров
# - ValueError - невозможно преобразовать к числу
# - IndexError - выход за границы списка
# - остальные исключения
# для каждого типа исключений написать на консоль соотв. сообщение




