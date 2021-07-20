numb = 199819884756

def smallest(n):
    n = [int(x) for x in str(n)]
    print((n[1:]), "asdasdads")
    sm = min(n[1:])
    print(sm, "sm")

    indexx = n[1:].index(min(n[1:])) + 1
    print(indexx, "indx, min num is", n[indexx])
    minNum = n.pop(indexx)
    for i, val in enumerate(n):
        if val > minNum:
            n.insert(i, minNum)
            n = map(str, n)
            n = int("".join(n))
            if minNum == 0:
                
                return [n, i, indexx]
            return [n, indexx, i]
    #         minNum = i
    #         break
    # n = map(str, n)
    # n = int("".join(n))
    # return [n, indexx, minNum]

print(smallest(numb))