def validBraces(string):
    open_br = ["(", "{", "["]
    close_br = [")", "}", "]"]
    flag = True
    while flag:
        for x in string:
            if x in close_br:              
                close_index = string.index(x)
                if close_index > 0:
                    prev_char = close_index - 1
                    cl_br_list_i = close_br.index(x)
                    if not string[prev_char] in open_br:
                        return False
                    op_br_list_i = open_br.index(string[prev_char])

                    if cl_br_list_i == op_br_list_i:
                        string = string[:prev_char] + string[close_index+1:]
                else:
                    return False
        else:
            flag = False
    print(string, "son hali")
    return True if not string else False


print(validBraces("()[{}()]()[]"))
