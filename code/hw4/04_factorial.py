# -*- coding: utf-8 -*-

import simple_draw as sd


sd.resolution = (1200, 600)

# нарисовать ветку дерева из точки (300, 5) вертикально вверх длиной 100

point_0 = sd.get_point(600, 5)


# 1) Написать функцию draw_branches, которая должна рисовать две ветви дерева из начальной точки
# Функция должна принимать параметры:
# - точка начала рисования,
# - угол рисования,
# - длина ветвей,
# Отклонение ветвей от угла рисования принять 30 градусов,


def fork_branch(stPoint, ang, vLen, incle = 30):
    stPointList = []
    stPointList.append(stPoint)
    # branchCount = 0
    # ang = ang - incle
    # if vLen < 10:
    #     return
    # vector = sd.vector(stPoint, ang, vLen)
    # inc = ang - incle
    # vLen *= 0.65
    # stPointList.append(vector)
    # print(stPointList[0])

    while True:
        i = 2
        if vLen < 10:
            break
        for point in stPointList:            
            # negAngle = ang - incle
            posAngle = ang + incle
            vectorA = sd.vector(point, posAngle, vLen,)
            # vectorB = sd.vector(point, negAngle, vLen,)

            # stPointList[point] = vectorA
            # stPointList[point] = vectorB
            
            vLen *= 0.65



fork_branch(point_0, 90, 100)







def mirror_Branch(stPoint, ang, vLen, aa= 30):
    if vLen < 10:
        return
    vector = sd.vector(stPoint, ang, vLen)
    sp = vector
    a = ang - aa
    vl= vLen * 0.65
    mirror_Branch(sp, a, vl, aa)
# mirror_Branch(point_0, 90, 100, ) 


# 2) Сделать draw_branches рекурсивной
# - добавить проверку на длину ветвей, если длина меньше 10 - не рисовать
# - вызывать саму себя 2 раза из точек-концов нарисованных ветвей,
#   с параметром "угол рисования" равным углу только что нарисованной ветви,
#   и параметром "длинна ветвей" в 0.75 меньшей чем длина только что нарисованной ветви


# 
def recursive_fork_branch(stPoint, ang, vLen, incle = 30):
    if vLen < 10:
        return
    posAngle =ang + incle
    negAngle =ang - incle
    posVectorStart = stPoint
    negVectorStart = stPoint
    for branch in range(0,5):
        posVector = sd.vector(posVectorStart, posAngle, vLen)
        negVector = sd.vector(negVectorStart, negAngle, vLen)
        posVectorStart = posVector
        negVectorStart = negVector
        posAngle += incle
        negAngle -= incle
        vLen = vLen * 0.75
        # vector = sd.vector(positiveEndPOint, a, vLen)
        # recursive_fork_branch(posVectorStart, posAngle, vLen, )
        # recursive_fork_branch(posVectorStart, posAngle, vLen,)
        # recursive_fork_branch(negVectorStart, negAngle, vLen)

# fork_branch(point_0, 90, 100)
# recursive_fork_branch(point_0, 90, 100)


# recursive_fork_branch(point_0, 90, 100,)



# 3) первоначальный вызов:
# root_point = get_point(300, 30)
# draw_bunches(start_point=root_point, angle=90, length=100)

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# Возможный результат решения см lesson_004/results/exercise_04_fractal_01.jpg

# можно поиграть -шрифтами- цветами и углами отклонения

# TODO здесь ваш код

# 4) Усложненное задание (делать по желанию)
# - сделать рандомное отклонение угла ветвей в пределах 40% от 30-ти градусов
# - сделать рандомное отклонение длины ветвей в пределах 20% от коэффициента 0.75
# Возможный результат решения см lesson_004/results/exercise_04_fractal_02.jpg

# Пригодятся функции
# sd.random_number()



sd.pause()


