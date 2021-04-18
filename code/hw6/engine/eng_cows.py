from random import randint

SECRET_LEN = 4

# print("*".join(str(_) for _ in secret))

def get_secret():
    secret = []
    secret.append(randint(1,9))
    while len(secret) < SECRET_LEN:
        n = randint(0,9)
        if not n in secret:
            secret.append(n)
    print(secret)
    # s = "".join(str(_) for _ in secret)
    # print(s)
    return int("".join(str(_) for _ in secret))

# def your_guess():
#     guess = -1
#     get_gues = True
#     while len(str(guess)) != SECRET_LEN or get_gues == True:
#         guess = input("guess number of {dgt} digit: ".format(dgt=SECRET_LEN))
#         for _ in str(guess):            
#             if str(guess).count(_) > 1:
#                 # print("gigits can not repeat")
#                 get_gues = True
#                 break
#             else:
#                 get_gues = False
#     print(guess)

def bulls_cows_counter(secret, guess):
    bc_dict = {
        "bulls": 0,
        "cows": 0,
    }   
    if secret == guess:
       bc_dict["bulls"] = 4
       return bc_dict
    else:
        secret = str(secret)    
        guess = str(guess)
        for _index, _val in enumerate(guess):
            if secret.count(_val):
                if secret[_index] == guess[_index]:
                    bc_dict["bulls"] += 1
                else:
                    bc_dict["cows"] += 1        
    return bc_dict


