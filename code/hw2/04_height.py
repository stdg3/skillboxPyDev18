# -*- codding: utf-8 -*-

myDic = []

a, b, c = ["a", 175], ["b", 180], ["c", 185]

myDic.append(a)
myDic.append(b)
myDic.append(c)

avg = (myDic[0][1] + myDic[1][1] + myDic[2][1]) / len(myDic) 

print("a -", myDic[1][1],"cm")

print("average: ", avg)
