def is_valid_walk(walk):
    # determine if walk is valid
    # if len(walk) != 10:
    #     return "False", len(walk)
    assert len(walk) == 10
    pos = [0, 0]
    for step in walk:
        if step == "n":
            pos[1] += 1
        elif step == "s":
            pos[1] -= 1
        elif step == "e":
            pos[0] += 1
        elif step == "w":
            pos[0] -= 1
    if pos[0] == pos[1] == 0:
        return "true", pos
    return "False", pos


way = ['n', 's', 'n', 's', 'n', 's', 'n', 's', 'n', 's',]
way2 = ['w','e','w','e','w','e','w','e','w','e','w','e']

print(is_valid_walk(way2))
