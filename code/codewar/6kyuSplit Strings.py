def solution(s):
    if len(s) % 2 == 1:
        s += "_"
    print(s)
    return [s[i:2:] for i in range(len(s) // 2)]

print(solution("qweqrtyuıpğ"))

li = "qweqrtyuıpğ" #['1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b']
lists = []
list_temp = []
if len(li) % 2 == 1:
        li += "_"
for _, __ in enumerate(li, 1):
    list_temp.append(__)
    if _ % 2 == 0 or _ == len(li):
        lists.append("".join(list_temp))
        list_temp = []
print(lists, list_temp)