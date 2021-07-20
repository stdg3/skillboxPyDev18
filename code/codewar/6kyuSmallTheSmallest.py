def smallest(n):
    # your code
    n = [int(x) for x in str(n)]
    n = n[1:]
    m1, m2 = n[0], n[0]
    for x in n:
        if x <= m1:
            m1, m2 = x, m1
        elif x < m2:
            m2 = x
            print("asd")
    print(m2)
    
    n = list(reversed(n))
    
    # index_min = n.index(min(n[1:]))
    # min_num = n[index_min]
    # min_coun = n.count(min_num)
    # skip = n[index_min + 1:]
    # print("sk: ", skip)
    # if n.count(min_num) > 1:
    #     print("pr")
    #     index_min = n.index(min(n[1:]))

    # print(str(n))
    # print ("min:", min_num, "index:", index_min, "count min num", min_coun)


l = 1265325465
smallest(l)