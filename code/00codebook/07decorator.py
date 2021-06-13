import time

def time_track(func,):
    def inner_func(*args):
        started_at = time.time()
        result = func(*args)
        ended_at = time.time()
        elapsed = round(ended_at - started_at, 4)
        print(f'working {elapsed} sec')
        return result
    return inner_func

@time_track # func = time_track(digit) \n res = func(3141, 5926, 2718, 2818)
def digits(*args):
    total = 1
    for number in args:
        total *= number ** 5000
    return len(str(total))


print(digits(3141, 5926, 2718, 2818))


