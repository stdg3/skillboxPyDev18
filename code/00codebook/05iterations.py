# Iterators 
# döngü ile ele alınabilen objeler itere edilebilir objelerdir
# obje iterasyon için __iter__ & __next__ metodlarına sahip olmalı

class Fibonacci:
    def __init__(self, maks):
        self.a, self.b, self.i, self.n = 0, 1, 0, maks

    def __iter__(self):
        self.a, self.b, self.i = 0, 1, 0
        return self
    
    def __next__(self):        
        self.i += 1
        if self.i > 1:
            if self.i > self.n + 1:
                raise StopIteration()
            self.a, self.b = self.b, self.a + self.b
        return self.a

fib = Fibonacci(9)
for val in fib:
    print(val) # lazy evolution
