# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd

sd.resolution = (1200, 600)

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)
# TODO здесь ваш код

def moreLines():
    x1, y1 = 50, 50
    x2, y2 = 350, 450    
    for _ in range(7):
        startPoint = sd.get_point(x1, y1)
        endPoint = sd.get_point(x2, y2)
        sd.line(startPoint, endPoint, color = rainbow_colors[_])
        x1 += 25
        x2 += 25
        #y1 += 50
        #y2 += 50

# moreLines()

# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво
# TODO здесь ваш код

def fakeRainbow():
    x1, y1 = 50, 50
    x2, y2 = 350, 450
    point = sd.get_point(600, 0)
    radius = 200
    for _ in range(7):
        sd.circle(point, radius = radius, width = 3, color = rainbow_colors[_])
        radius += 50 


fakeRainbow()

sd.pause()
