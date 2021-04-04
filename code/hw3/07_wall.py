# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd

rx, ry = 1000, 600
sd.resolution = rx, ry

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for

# TODO здесь ваш код
for row in range(0, ry, 50):
    for line in range(0, rx, 100):
        
        lbPoint = sd.get_point(line,row)
        rtPoint = sd.get_point(line + 100, row + 50)
        sd.rectangle(lbPoint, rtPoint, width = 1)

sd.pause()
