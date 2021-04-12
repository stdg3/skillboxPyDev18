# -*- coding: utf-8 -*-

import simple_draw as sd
import random

sd.resolution = (1200, 600)
# познакомится с параметрами библиотечной функции рисования снежинки sd.snowflake()

point = sd.get_point(300, 300)

# sd.snowflake(center = point, length = 80)

# print(point.x)
def getSnowfall(adet):
    #sFlakes = []
    snFlakesDict = initsFlakes(adet) # elimizde adet kadar kar tanesi ve çapı var



    # point.y = sd.resolution[1] + 100
    vertical = sd.resolution[1]
    while True:
        if vertical < 0:
            break
        sd.clear_screen()
        for _ in range(0, adet):
            centerP = snFlakesDict[_][0]
            rad = snFlakesDict[_][1]
            print(centerP, rad)
            sd.snowflake(centerP, rad)
            centerP.y -= 10
            snFlakesDict[_][0] = centerP
            vertical = centerP.y
        vertical -= 1
        # sd.snowflake(center = point, length = 80, )    
        # a = point.y
        # point = sd.get_point(point.x, point.y - 1)
        sd.sleep(0.01)
        if sd.user_want_exit():
            break
# a = sd.random_point()
# print(a.x, "asdasd")

def initsFlakes(s):
    """
        gelen s kartanesi adedine göre:
        random radius ve center point içeren dict oluşturur
    """
    snowflakes = {}
    if s > 0:
        y = sd.resolution[1]
        for _ in range(0, s):
            radius = getRandomRadius()
            y += radius
            randPoint = getRandomPointAboveScr(y)
            snowflakes[_] = [randPoint, radius]
    return snowflakes


def getRandomPointAboveScr(y):
    """
        y --> random oluşturulmuş radius ve sd.resolution'ının topalmı
        sd.random_point()'ten gelen y'nin yerine geçmekte
    """
    ranPoint = sd.random_point()
    ranPoint.y = 300 # prod'da y
    return ranPoint


def getRandomRadius():
    """
        20-60 arası 10'ar aralıkla
        kar tanesi radiusu oluşturur

    """
    radius = random.randint(2, 6)
    radius *= 10
    return radius


getSnowfall(adet = 5)

# ab = initsFlakes(4)
# print(ab[0][0].x)



# sd.snowflake(center=point_0, length=200, factor_a=0.5)

# реализовать падение одной снежинки

sd.pause()
