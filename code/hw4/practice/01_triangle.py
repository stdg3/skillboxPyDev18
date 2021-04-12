# -*- coding: utf-8 -*-

# pip install simple_draw

import simple_draw as sd

# нарисовать треугольник из точки (300, 300) с длиной стороны 200
length = 200
point = sd.get_point(300, 300)

# vector = sd.vector(point, 0, 200)
# vector = sd.vector(vector, 120, 200)
# vector = sd.vector(vector, 240, 200)


# определить функцию рисования треугольника из заданной точки с заданным наклоном

def draw_triangle(stPoint, vecLen, vecAngle=0):
    a = 0
    for _ in range(0,3):
        vector = sd.vector(stPoint, vecAngle + a, vecLen)
        stPoint = vector
        a += 120

for _ in range(0, 360, 60):
    draw_triangle(point, 200, vecAngle=_)



sd.pause()