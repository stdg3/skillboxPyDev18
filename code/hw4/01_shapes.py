# -*- coding: utf-8 -*-

import simple_draw as sd
sd.resolution=(1200, 600)


# Часть 1.
# Написать функции рисования равносторонних геометрических фигур:
# - треугольника
# - квадрата
# - пятиугольника
# - шестиугольника
# Все функции должны принимать 3 параметра:
# - точка начала рисования
# - угол наклона
# - длина стороны

# point = sd.get_point(150, 100)

def triangle(p, ang, vl, color=sd.COLOR_YELLOW):
    sp = p
    step = 360 / 3
    vector = sd.vector(p, ang, vl, color = color)
    ang += step
    vector = sd.vector(start = vector, angle = ang, length = vl, color= color)
    line = sd.line(sp, vector, color = color)
    # vector = sd.vector(start = sp, angle = 60, length = vl)







def rect(p, ang, vl, color):
    step = 360 / 4
    vector = sd.vector(p, ang, vl, color = color)
    ang += step
    vector = sd.vector(start = vector, angle = ang, length = vl, color = color)
    ang += step
    vector = sd.vector(start = vector, angle = ang, length = vl, color = color)
    ang += step
    vector = sd.vector(start = vector, angle = ang, length = vl, color = color)





def patiugl(p, ang, vl, color):
    sp = p
    step = 360 / 6
    vector = sd.vector(p, ang, vl, color = color)
    ang += step
    vector = sd.vector(start = vector, angle = ang, length = vl,color = color)
    ang += step
    vector = sd.vector(start = vector, angle = ang, length = vl, color = color)
    ang += step
    vector = sd.vector(start = vector, angle = ang, length = vl, color = color)
    ang += step
    vector = sd.vector(start = vector, angle = ang, length = vl, color = color)
    sd.line(sp, vector,color = color)
    #vector = sd.vector(start = sp, angle = 62, length = vl)





def shestiugl(p, ang, vl, color):
    sp = p
    step = 360 / 5
    vector = sd.vector(p, ang, vl, color = color)
    ang += step
    vector = sd.vector(start = vector, angle = ang, length = vl, color = color)
    ang += step
    vector = sd.vector(start = vector, angle = ang, length = vl, color = color)
    ang += step
    vector = sd.vector(start = vector, angle = ang, length = vl, color = color)
    sd.line(sp, vector, color = color)
    #vector = sd.vector(start = sp, angle = 62, length = vl)



# Использование копи-пасты - обязательно! Даже тем кто уже знает про её пагубность. Для тренировки.
# Как работает копипаста:
#   - одну функцию написали,
#   - копипастим её, меняем название, чуть подправляем код,
#   - копипастим её, меняем название, чуть подправляем код,
#   - и так далее.
# В итоге должен получиться ПОЧТИ одинаковый код в каждой функции

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# sd.line()
# Результат решения см lesson_004/results/exercise_01_shapes.jpg

# TODO здесь ваш код

# Часть 1-бис.
# Попробуйте прикинуть обьем работы, если нужно будет внести изменения в этот код.
# Скажем, связывать точки не линиями, а дугами. Или двойными линиями. Или рисовать круги в угловых точках. Или...
# А если таких функций не 4, а 44?

# Часть 2 (делается после зачета первой части)
#
# Надо сформировать функцию, параметризированную в местах где была "небольшая правка".
# Это называется "Выделить общую часть алгоритма в отдельную функцию"
# Потом надо изменить функции рисования конкретных фигур - вызывать общую функцию вместо "почти" одинакового кода.
#
# В итоге должно получиться:
#   - одна общая функция со множеством параметров,
#   - все функции отрисовки треугольника/квадрата/етс берут 3 параметра и внутри себя ВЫЗЫВАЮТ общую функцию.
#
# Не забудте в этой общей функции придумать, как устранить разрыв
#   в начальной/конечной точках рисуемой фигуры (если он есть)

# Часть 2-бис.
# А теперь - сколько надо работы что бы внести изменения в код? Выгода на лицо :)
# Поэтому среди программистов есть принцип D.R.Y. https://clck.ru/GEsA9
# Будьте ленивыми, не используйте копи-пасту!
if __name__ == "__main__":
    point = sd.get_point(850, 300)
    shestiugl(p = point, ang = 0, vl = 100, color=sd.COLOR_YELLOW)
    point = sd.get_point(150, 300)
    patiugl(p = point, ang = 0, vl = 100, color = sd.COLOR_YELLOW)
    point = sd.get_point(850, 100)
    rect(p = point, ang = 0, vl = 100, color= sd.COLOR_YELLOW)
    point = sd.get_point(150, 100)
    triangle(p = point, ang = 0, vl = 100)

sd.pause()
