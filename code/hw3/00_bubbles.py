# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 600)

# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей
# TODO здесь ваш код



# Написать функцию рисования пузырька, принммающую 2 (или более) параметра: точка рисовании и шаг
# TODO здесь ваш код
def bub(point, step):
    rad = 50
    for _ in range(3):
        rad += step
        sd.circle(point, radius = rad, width = 1)


point = sd.get_point(200, 200)
# bub(point, 10)


# Нарисовать 10 пузырьков в ряд
# TODO здесь ваш код
def inlineBub():
    for _ in range(100, 1001, 100):
        point = sd.get_point(_, 100)
        bub(point, 10)

#inlineBub()


# Нарисовать три ряда по 10 пузырьков
# TODO здесь ваш код
def inrowBub():
    for __ in range(100, 301, 100):
        for _ in range(100, 1001, 100):
            point = sd.get_point(_, __)
            bub(point, 10)

# inrowBub()

# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
# TODO здесь ваш код
def ranBub():    
    for _ in range(100):
        point = sd.random_point()
        color = sd.random_color()
        bub(point, 5)

ranBub()


sd.pause()


