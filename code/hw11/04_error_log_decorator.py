# -*- coding: utf-8 -*-

# Написать декоратор, который будет логировать (записывать в лог файл)
# ошибки из декорируемой функции и выбрасывать их дальше.
#
# Имя файла лога - function_errors.log
# Формат лога: <имя функции> <параметры вызова> <тип ошибки> <текст ошибки>
# Лог файл открывать каждый раз при ошибке в режиме 'a'


def log_errors(err_log_file):
    def decorate_it(func):
        def try_it(*args):
            try:
                func(*args)
            except ValueError as e:
                log_err(
                    err_log_file,
                    func.__name__,
                    args,
                    "ValueError",
                    e
                    )
                print(f"Name:{func.__name__}, {args} ValueError - message:{e}")
            except ZeroDivisionError as e:
                log_err(
                    err_log_file,
                    func.__name__,
                    args,
                    "ZeroDivisionError",
                    e
                    )
                print(f"Name:{func.__name__}, {args} ZeroDivisionError - message:{e}")
            # except Exception as e:
            #     print(f"Name:{func.__name__}, Exception - message:{e}")
        return try_it
    return decorate_it


def log_err(file, func_name, params, err_type, mess):
    print("-----------------------------", file)
    file = open(file, mode="a", encoding="utf8")
    try:
        file.write(f"[{func_name}] [{params}] [{err_type}] [{mess}]\n")
        file.close()
    except Exception:
        print("can't write err log")


# Проверить работу на следующих функциях
@log_errors('function_errors.log')
def perky(param):
    return param / 0


perky(42)
# input()


@log_errors('function_errors.log')
def check_line(line):
    name, email, age = line.split(' ')
    if not name.isalpha():
        raise ValueError("it's not a name")
    if '@' not in email or '.' not in email:
        raise ValueError("it's not a email")
    if not 10 <= int(age) <= 99:
        raise ValueError('Age not in 10..99 range')


lines = [
    'Ярослав bxh@ya.ru 600',
    'Земфира tslzp@mail.ru 52',
    'Тролль nsocnzas.mail.ru 82',
    'Джигурда wqxq@gmail.com 29',
    'Земфира 86',
    'Равшан wmsuuzsxi@mail.ru 35',
]
for line in lines:
    try:
        check_line(line)
    except Exception as exc:
        print(f'Invalid format: {exc}')
perky(42)


# Усложненное задание (делать по желанию).
# Написать декоратор с параметром - именем файла

# @log_errors('function_errors.log')
# def func():
#     pass
