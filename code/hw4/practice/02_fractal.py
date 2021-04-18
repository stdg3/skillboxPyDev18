# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 600)

# нарисовать ветку дерева из точки (300, 5) вертикально вверх длиной 100

point_0 = sd.get_point(600, 5)


def branch(stPoint, ang, vLen, aa):

    if vLen < 1:
        return
    vector = sd.vector(stPoint, ang, vLen)
    sp = vector
    a = ang - aa
    vl= vLen * 0.65
    branch(sp, a, vl, aa)


for aa in range(0, 21, 10):
    if aa == 0:
        continue
    branch(point_0, 90, 200, aa)

for aa in range(-20, 0, 10):
    if aa == 0:
        continue
    branch(point_0, 90, 200, aa)


sd.pause()
