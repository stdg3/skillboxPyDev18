# -*- coding: utf-8 -*-


# Есть файл с протоколом регистраций пользователей на сайте - registrations.txt
# Каждая строка содержит: ИМЯ ЕМЕЙЛ ВОЗРАСТ, разделенные пробелами
# Например:
# Василий test@test.ru 27
#
# Надо проверить данные из файла, для каждой строки:
# - присутсвуют все три поля
# - поле имени содержит только буквы
# - поле емейл содержит @ и .
# - поле возраст является числом от 10 до 99
#
# В результате проверки нужно сформировать два файла
# - registrations_good.log для правильных данных, записывать строки как есть
# - registrations_bad.log для ошибочных, записывать строку и вид ошибки.
#
# Для валидации строки данных написать метод, который может выкидывать исключения:
# - НЕ присутсвуют все три поля: ValueError
# - поле имени содержит НЕ только буквы: NotNameError (кастомное исключение)
# - поле емейл НЕ содержит @ и .(точку): NotEmailError (кастомное исключение)
# - поле возраст НЕ является числом от 10 до 99: ValueError
# Вызов метода обернуть в try-except.

from os import sep
from pprint import pprint


class NotNameError(Exception):
    def __init__(self, message="name must be alpha chars"):
        self.message = message
    
    def __str__(self):
        return self.message


class NotEmailError(Exception):
    def __init__(self, message="e-mail must have @ ind ."):
        self.message = message
    
    def __str__(self):
        return self.message


def validate_line(l):
    try:
        # count_data(l)
        if len(l) != 3:
            raise ValueError("please, given 3 argument")
        
        if not str(l[0]).isalpha():
            raise NotNameError()

        if not "." in l[1] and not "@" in l[1]:
            raise NotEmailError()
        
        if not 10 <= int(l[2]) < 99:
            raise ValueError("age error")  # age: "" --> invalid literal for int() with base 10: ''
        
        return True
    except ValueError as e:
        return e   
    except NotNameError as e:
        return e
    except NotEmailError as e:
        return e


def print_logins(mess, data):
    if mess:
        file = open("validLogins.txt", "a", encoding="utf8")
        file.write(f"{data}\n")
        file.close()
    else:
        file = open("invalidLogins.txt", "a", encoding="utf8")
        file.write(f"{data} '{mess}'\n")
        file.close()


vals = []
with open("registrations.txt", mode="r", encoding="utf8") as f:
    for line in f:
        vals = []
        line = line[:-1]
        vals.append(line.split(" "))
        res = validate_line(vals[0])
        if res:
            # print("OK")
            print_logins(res, line)
        else:
            # print("NOK", res)
            print_logins(res, line)
    vals = []

# llll = ["abc", "a@.", "45",]
# print(validate_line(llll))
