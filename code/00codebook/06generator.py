# Generator
# fonksiyonda return yerine yield kullanımı
# yield anlık olarak parametreleri hafızada tutacak şekilde 
# "return" işlemini yapar ve kaldığı yerden devam etmek için 
# __next__ metodunu bekler
# return == StopIteration
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n + 1):
        yield a
        a, b = b, a + b
print(type(fibonacci))
for val in fibonacci(9):
    print(val)
