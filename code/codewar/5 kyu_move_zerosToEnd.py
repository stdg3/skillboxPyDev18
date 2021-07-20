def move_zeros(array):
    for _ in range(array.count(0)):
        array.remove(0)
        array.append(0)

    # while 0 in array:
    #     array.remove(0)
    # limit = array.count(0)
    # print(limit)
    # for _ in range(0, limit):
    #     print(array, "asdasd", _, limit)
    #     array.append(array.pop(0))

    return array

arrr = [1, 0, 1, 2, 0, 1, 3]
# print("555", arrr.pop(arrr.find(0)))
print(move_zeros(arrr))