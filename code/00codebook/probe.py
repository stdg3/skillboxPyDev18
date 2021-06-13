
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
        self.split_num()
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
                    # print("sol sağ eşit", self.slice_left, self.slice_right, )
                    return True

for num in Lotery_number(12521):
    print(num)
