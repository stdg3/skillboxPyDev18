# -*- coding: utf-8 -*-
import simple_draw as sd
sd.resolution = (1200, 600)

# Добавить цвет в функции рисования геом. фигур. из упр lesson_004/01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом

# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()
# и константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# Результат решения см lesson_004/results/exercise_02_global_color.jpg

# TODO здесь ваш код

colors = {
    1: "COLOR_RED",
    2: "COLOR_ORANGE",
    3: "COLOR_YELLOW",
    4: "COLOR_GREEN",
    5: "COLOR_CYAN",
    6: "COLOR_BLUE",
    7: "COLOR_PURPLE",
}

for key, val in colors.items():
    print(key, "-", val)

def colorfulDraws():
    while True:
        number = int(input("Select color: "))
        if 0 < number < 8:
            go(number)
            break


def go(number):
    if number == 1:
        draw(sd.COLOR_RED)
    elif number == 2:
        draw(sd.COLOR_ORANGE)
    elif number == 3:
        draw(sd.COLOR_YELLOW)
    elif number == 4:
        draw(sd.COLOR_GREEN)
    elif number == 5:
        draw(sd.COLOR_CYAN)
    elif number == 6:
        draw(sd.COLOR_BLUE)
    else:
        draw(sd.COLOR_PURPLE)


def draw(clr):
    point = sd.get_point(850, 300)
    shestiugl(p = point, ang = 0, vl = 100, color=clr)
    point = sd.get_point(150, 300)
    patiugl(p = point, ang = 0, vl = 100, color = clr)
    point = sd.get_point(850, 100)
    rect(p = point, ang = 0, vl = 100, color= clr)
    point = sd.get_point(150, 100)
    triangle(p = point, ang = 0, vl = 100, color=clr)
    



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



if __name__ == "__main__":
    colorfulDraws()






sd.pause()
