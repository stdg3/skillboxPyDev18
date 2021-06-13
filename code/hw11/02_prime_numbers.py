# -*- coding: utf-8 -*-


# Есть функция генерации списка простых чисел
import time


def get_prime_numbers(n):
    prime_numbers = []
    for number in range(2, n+1):
        for prime in prime_numbers:
            if number % prime == 0:
                break
        else:
            prime_numbers.append(number)
    return prime_numbers

# Часть 1
# На основе алгоритма get_prime_numbers создать класс итерируемых обьектов,
# который выдает последовательность простых чисел до n
#
# Распечатать все простые числа до 10000 в столбик


class PrimeNumbers:
    def __init__(self, n):
        self.n = n
        self.i = None
        self.c = 0

    def __iter__(self):
        if self.n < 2:
            raise BaseException("input can'n be less 2")
        self.i = -1
        self.c = 1
        self.get_prime_numbers(self.n)
        self.lennn = len(self.prime_numbers)
        return self

    def get_prime_numbers(self, n):
        prime_numbers = []
        for number in range(2, n+1):
            for prime in prime_numbers:
                if number % prime == 0:
                    break
            else:
                prime_numbers.append(number)
        self.prime_numbers = prime_numbers

    def __next__(self):
        # res = False # self.get_prime()

        # ======= 0.68 sn, aktif çözümden 0.15 sn daha yavaş
        # while True: # if false
        #     # res = self.get_prime()
        #     self.i += 1
        #     if self.i > self.n:
        #         raise StopIteration()
        #     for i in range(2, self.i):
        #         # print(f"checking {i} for {self.i}\n")
        #         if (self.i % i == 0):
        #             # not prime
        #             break
        #     else:
        #         # print("asal", self.i)
        #         # return f"{self.i} asal"
        #         return self.i
        #     # res =  False
        # =======

        # +++++++++++++++++++++++
        self.i += 1
        # print(self.prime_numbers)
        if self.i == self.lennn:
            raise StopIteration()
        # print("lenk",self.lennn, "i", self.i)
        # print(len(self.prime_numbers), self.i)
        return self.prime_numbers[self.i]
        # if self.i < self.lennn:
        # +++++++++++++++++++++++

        # return self.prime_numbers[self.i]
        # else:
        #     print("iter", self.c, end=":")
        #     self.c += 1
        #     return self.i

    def get_prime(self):
        self.i += 1
        if self.i > self.n:
            # print("stop")
            raise StopIteration()
        for i in range(2, self.i):
            # print(f"checking {i} for {self.i}\n")
            if (self.i % i == 0):
                # not prime
                break
        else:
            # print("asal", self.i)
            return f"{self.i} asal"
        return False

# prime_number_iterator = PrimeNumbers(n=2)


s = time.time()
for number in PrimeNumbers(10):  # 10000
    print(number)
    # input()
    # time.sleep(0.5)

e = time.time()
se = (e-s)
print(se)

# print(get_prime_numbers(10000))

# TODO после подтверждения части 1 преподователем, можно делать
# Часть 2
# Теперь нужно создать генератор, который выдает последовательность простых чисел до n
# Распечатать все простые числа до 10000 в столбик


def prime_numbers_generator(n):
    for sayi in range(1, n + 1):
        if sayi > 1:
            for i in range(2, sayi):
                if (sayi % i) == 0:
                    # print(sayi," Asal Sayı Değildir.")
                    break
            else:
                # print(sayi," Asal Sayıdır.")
                yield sayi
                # print(sayi," Asal Sayıdır.")


print(type(prime_numbers_generator))
s = time.time()
for number in prime_numbers_generator(n=10):  # 10000
    print(number)
e = time.time()
print(e-s)  # 0.6sec

# Часть 3
# Написать несколько функций-фильтров, которые выдает True, если число:
# 1) "счастливое" в обыденном пониманиии - сумма первых цифр равна сумме последних
#       Если число имеет нечетное число цифр (например 727 или 92083),
#       то для вычисления "счастливости" брать равное количество цифр с начала и конца:
#           727 -> 7(2)7 -> 7 == 7 -> True
#           92083 -> 92(0)83 -> 9+2 == 8+3 -> True
# 2) "палиндромное" - одинаково читающееся в обоих направлениях. Например 723327 и 101
# 3) придумать свою (https://clck.ru/GB5Fc в помощь)
#
# Подумать, как можно применить функции-фильтры к полученной последовательности простых чисел
# для получения, к примеру: простых счастливых чисел, простых палиндромных чисел,
# простых счастливых палиндромных чисел и так далее. Придумать не менее 2х способов.
#
# Подсказка: возможно, нужно будет добавить параметр в итератор/генератор.


class Lotery_number:
    def __init__(self, n):
        self.n = n
        self.list_from_int = None
        self.num = None
        self.slice_left = 0
        self.slice_right = 0
        self.sum_right = 0
        self.sum_left = 0

    def __iter__(self):
        self.num = -1
        return self

    def __next__(self):
        if self.num == self.n:
            raise StopIteration()
        self.num += 1
        if self.split_num():
            print("lucky number:", self.num)
        return self.num

    def split_num(self):
        self.list_from_int = list(map(lambda x: int(x), str(self.num)))
        if self.num > 9:
            if len(self.list_from_int) % 2 == 0:
                stop_n = len(self.list_from_int)//2
            else:
                stop_n = (len(self.list_from_int)-1)//2
            self.slice_left = self.list_from_int[:stop_n]
            self.slice_right = self.list_from_int[-stop_n:]
            self.sum_left = sum(self.slice_left)
            self.sum_right = sum(self.slice_right)
            # print(self.slice_left, "left slice", "sum", self.sum_left)
            # print(self.slice_right, "right slice", "sum", self.sum_right)
            if self.sum_left == self.sum_right:
                ll = self.slice_right.reverse()
                if self.slice_left == self.slice_right:
                    # print("sol sağ eşit", self.slice_left, self.slice_right,)
                    return True


for num in Lotery_number(12521):
    print(num)
