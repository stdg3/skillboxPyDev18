# Functional Style

# def 
# lambda
# __call__

# map, filter - döngüyle ele alınabilecek iterable objelerle çalışır

def mul_by_2(x):
    return x * 2

def is_odd(x):
    return x % 2 # True/False

nums = [1, 2, 3, 4]

res = map(mul_by_2, filter(is_odd, nums))

print(res) # 0x7f69d4ff0000
print(list(res)) # anca çağrıldığı zaman liste ele alınır [2, 6]


res = map(lambda x: x + 10, nums)
print(list(res))

# labbda x: = def func_name(x):
# lambda için tavsiye edilen 2-3 parametrelik kullanım
# traceback'te lambda objeler aynı adrese ilişkilendirilir
# dolayısılyla serialize işlemlerinde karmaşıklık yaratır

res = map(lambda x, y: x + y, [1, 3, 5], [2, 4, 6])
print(list(res))

func = lambda a: a + 1
print(func(2)) # 3
print(func.__name__) # <lambda>

class Multiplier:
    def __init__(self, n):
        self.n = n
    
    def __call__(self, x): # by_3456() __call__ metodunu çağırır
        return x * self.n
    
by_3456 = Multiplier(3456)
# sonraki __call__ çağırımlarında 
# constructor'da atanan değere ilişkilendirilir (instance)
print(by_3456(78)) # 269568
