def namelist(names):
    res = ""
    for d in names:
        res += res.join(d.values()) + ", "
        # for val in d.values():
        #     res = ",".join(val)
            # if names.index(d) + 1 == len(names):
            #     res += f"& {val}"
            #     return res
            # res += f"{val}, "
    res = res[:-2]
    last_comma = res.rfind(",")
    res = res[:last_comma] + res[last_comma:].replace(",", " &")

    # res = res[:10].replace(",", " &")
    print(res, last_comma)
    # print(left + rigght)
    return res


namelist([{'name': 'Bart'},{'name': 'Lisa'},{'name': 'Maggie'},{'name': 'Homer'},{'name': 'Marge'}])
# 'Bart, Lisa, Maggie, Homer & Marge'   Bart & Lisa'