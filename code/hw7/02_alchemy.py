# -*- coding: utf-8 -*-

# Создать прототип игры Алхимия: при соединении двух элементов получается новый.
# Реализовать следующие элементы: Вода, Воздух, Огонь, Земля, Шторм, Пар, Грязь, Молния, Пыль, Лава.
# Каждый элемент организовать как отдельный класс.
# Таблица преобразований:
#   Вода + Воздух = Шторм
#   Вода + Огонь = Пар
#   Вода + Земля = Грязь
#   Воздух + Огонь = Молния
#   Воздух + Земля = Пыль
#   Огонь + Земля = Лава

# Сложение элементов реализовывать через __add__
# Если результат не определен - то возвращать None
# Вывод элемента на консоль реализовывать через __str__
#
# Примеры преобразований:
#   print(Water(), '+', Air(), '=', Water() + Air())
#   print(Fire(), '+', Air(), '=', Fire() + Air())

# TODO здесь ваш код

class Water:
    def __str__(self):
        return "Water"
    
    def __add__(self, second):
        return Element(self, second)


class Air:
    def __str__(self):
        return "Air"
    
    def __add__(self, second):
        return Element(self, second)


class Fire:
    def __str__(self):
        return "Fire"
    
    def __add__(self, second):
        return Element(self, second)

class Ground:
    def __str__(self):
        return "Ground"
    def __add__(self, second):
        return Element(self, second)    


class Storm:
    def __str__(self):
        return "Storm"
    def __add__(self, second):
        return Element(self, second)

class Vapor:
    def __str__(self):
        return "Vapor"
    def __add__(self, second):
        return Element(self, second)

class Mud:
    def __str__(self):
        return "Mud"
    def __add__(self, second):
        return Element(self, second)

class Lightning:
    def __str__(self):
        return "Lightning"
    def __add__(self, second):
        return Element(self, second)

class Dust:
    def __str__(self):
        return "Dust"
    def __add__(self, second):
        return Element(self, second)

class Lava:
    def __str__(self):
        return "Lava"
    def __add__(self, second):
        return Element(self, second)

class Element:
    def __init__(self, e1, e2):
        self.elm1 = e1
        self.elm2 = e2
    
    def __str__(self):
        key = str(self.elm1) + "-" + str(self.elm2)
        table = {
        "Water-Air": "Strom",
        "Water-Fire": "Vapor",
        "Water-Ground": "Mud",
        "Air-Fire": "Lightning",
        "Air-Ground": "Dust",
        "Fire-Ground": "Lava",
        "Fire-Air": "vvvvv",
        }
        if key in table.keys():
            return table[key]
        else:
            return str(None)

b = Water() + Water()
print(b)
print(Water(), '+', Air(), '=', Water() + Air())
print(Fire(), '+', Air(), '=', Fire() + Air())

# print(table[key])

# Усложненное задание (делать по желанию)
# Добавить еще элемент в игру.
# Придумать что будет при сложении существующих элементов с новым.