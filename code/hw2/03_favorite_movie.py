# -*-codding: utf-8 -*-

my_movies = "Терминатор, Пятый элемент, Аватар, Чужие, Назад в будущее"

# Выведите на консоль с помощью иc, последовательно:
#   первый фильм
print("первый фильм:", my_movies[:10])

#   последний
a = my_movies[-1:-16: -1]
print("последний:", a[::-1])

#   второй
print("второй:", my_movies[12: 25])

#   второй с конца
a = my_movies[-18:-24: -1]
print("второй с конца:", a[::-1])