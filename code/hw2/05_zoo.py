zoo = ['lion', 'kangaroo', 'elephant', 'monkey', ] 

# посадите медведя (bear) между львом и кенгуру
zoo.insert(1, "beer")

print(zoo)

# добавьте птиц из списка birds в последние клетки зоопарка
birds = ['rooster', 'ostrich', 'lark', ]

zoo += birds[0], birds[1], birds[2]

print(zoo)

# уберите слона
zoo.remove("elephant")

print(zoo)

# выведите на консоль в какой клетке сидит лев (lion) и жаворонок (lark).
print(
    "number-lion:",(zoo.index("lion")) +1,
    "\nnumber-lark:",(zoo.index("lark")) +1,
    )
