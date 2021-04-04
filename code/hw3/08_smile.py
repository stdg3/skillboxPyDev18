# -*- coding: utf-8 -*-

# (определение функций)
import simple_draw as sd

# Написать функцию отрисовки смайлика в произвольной точке экрана
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.

# TODO здесь ваш код

sd.resolution = 1200, 600

def drawSomeLikeSmile(xx = 300, yy = 300 , randColor = (255,255,0)):
    x, y = xx, yy
    radius = 90
    smileCenter = sd.get_point(x, y)

    propEyeDist = radius / 3
    eyeProp = radius / 6
    propEyeDistx2 = propEyeDist * 2
    x_propEyeDist = x - propEyeDist

    # left eye
    eyeXl = x - propEyeDist
    eyeYl = y + propEyeDist
    leftEye = sd.get_point(eyeXl, eyeYl)

    # right eye
    eyeXr = x + propEyeDist
    eyeYr = eyeYl
    rightEye = sd.get_point(eyeXr, eyeYr)

    # circles smile & eyes
    sd.circle(smileCenter, radius = radius, color = randColor)
    sd.circle(leftEye, radius = eyeProp, color = randColor)
    sd.circle(rightEye, radius = eyeProp, color = randColor)


    # lips center line left start point
    lipsCenterLX = x - propEyeDist
    lipsCenterLY = y - propEyeDistx2
    lipsCenterLP = sd.get_point(lipsCenterLX, lipsCenterLY)

    # lips center line right end point
    lipsCenterRX = x + propEyeDist
    lipsCenterRY = lipsCenterLY
    lipsCenterRP = sd.get_point(lipsCenterRX, lipsCenterRY)

    # draw center lips line
    sd.line(lipsCenterLP, lipsCenterRP, color = randColor)


    # left smile start point
    leftLipsStartPoint = lipsCenterLP

    # left lips end point
    leftLipsEndPointX = x - propEyeDistx2
    leftLipsEndPointY = y - propEyeDist
    leftLipsEndPoint = sd.get_point(leftLipsEndPointX, leftLipsEndPointY)

    # draw left lips line
    sd.line(leftLipsStartPoint, leftLipsEndPoint, color = randColor)


    #  right smile start point
    rightLipsStartPoint = lipsCenterRP

    # right lips end point
    rightLipsEndPointX = x + propEyeDistx2
    rightLipsEndPointY = y - propEyeDist
    rightLipsEndPoint = sd.get_point(rightLipsEndPointX, rightLipsEndPointY)

    sd.line(rightLipsStartPoint, rightLipsEndPoint, color = randColor)


# drawSomeLikeSmile()

for _ in range(50):
    a = sd.random_point()
    c = sd.random_color()
    drawSomeLikeSmile(a.x, a.y, randColor = c)
    #print(c)
#print(a.x, a.y)




sd.pause()
