# -*- coding: utf-8 -*-

# Есть словарь кодов товаров

goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

# Есть словарь списков количества товаров на складе.

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

# Рассчитать на какую сумму лежит каждого товара на складе.
#
# Вывести суммарную стоимость каждого товара на складе c помощью циклов
# То есть: всего по лампам, стульям, етс.
# Формат строки вывода: "<товар> - <кол-во> шт, стоимость <общая стоимость> руб"
#
# Алгоритм должен получиться приблизительно такой:
#
# цикл for по товарам с получением кода и названия товара
#     инициализация переменных для подсчета количества и стоимости товара
#     получение списка на складе по коду товара
#     цикл for по списку на складе
#         подсчет количества товара
#         подсчет стоимости товара
#     вывод на консоль количества и стоимости товара на складе

# TODO здесь ваш код

output = {}
for code in store.keys():
    # önce idleri al
    cost, t, c = 0, 0, 0
    # case = store[code] # the same in for
    for case in store[code]:
        # her bir store["id"] al --> {'quantity': 43, 'price': 97}
        # print("case : " , case)
        c += case["quantity"]
        t = case["quantity"] * case["price"]
        cost += t
    output[code] = {"count": c, "cost": cost}  # [c, cost]
    c = 0

for _key, _val in goods.items():
    for __key in output.keys():
        if _val == __key:
            print(_key, "-", output[__key]["count"], "adet, total:",
            output[__key]["cost"], "cash")

# <товар> - <кол-во> шт, стоимость <общая стоимость> руб
# pprint.pp(output)
