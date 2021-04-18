# -*- coding: utf-8 -*-

# Составить список всех живущих на районе и Вывести на консоль через запятую
# Формат вывода: На районе живут ...
# подсказка: для вывода элементов списка через запятую можно использовать функцию строки .join()
# https://docs.python.org/3/library/stdtypes.html#str.join

# TODO здесь ваш код


# import district.central_street.house1 as csh1
from district.central_street.house1 import room1 as csh1 
from district.soviet_street.house2 import room2 as ssh2

r1 = csh1.folks
r2 = ssh2.folks
rs = r1 + r2

print(r1, "\n", r2)
print("На районе живут:", ", ".join(rs))