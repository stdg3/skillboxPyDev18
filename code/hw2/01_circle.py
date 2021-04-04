# -*- codding: utf-8 -*-

radius = 42
pi = 3.141526

# площадь круга S = Pi*r^2

s = pi * (radius  ^ 2 )

s = round(s, 4)

point = (23, 34)

point2 = (30, 30)

n = ((point[0] ** 2) + (point[1] ** 2)) ** 0.5

n2 = ((point2[0] ** 2) + (point2[1] ** 2)) ** 0.5

res, res2 = False, False

if n < radius:
    res = True

if n2 < radius:
    res2 = True


print("S =", s, 
            "\npoint({a}, {b}) In Circle: ".format(a=point[0], b=point[1]), res,
            "\npoint2({a}, {b}) In Circle: ".format(a=point2[0], b=point2[1]), res2
    ) 



# x = []

# y = []

# for _ in range(radius + 1):
    # x.append(_)

# for _ in range(radius, -1, -1):
    # y.append(_)


# print(round(s, 4))

# print(x, "\n\n", y)
