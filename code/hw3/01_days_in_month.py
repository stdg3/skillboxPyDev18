# -*- coding: utf-8 -*-
import datetime
import calendar


# (if/elif/else)

# По номеру месяца вывести кол-во дней в нем (без указания названия месяца, в феврале 28 дней)
# Результат проверки вывести на консоль
# Если номер месяца некорректен - сообщить об этом

# Номер месяца получать от пользователя следующим образом
user_input = input("Input month number: ")
user_month = int(user_input)
#print('Вы ввели', month)

# TODO здесь ваш код
year = datetime.datetime.now()
# print(year) # 2021-MM-dd hh:mm:17.029738
year = year.year
month = calendar.monthrange(year, user_month) # 5 --> (0, 31)
print(calendar.month    _name[user_month] , month[1])