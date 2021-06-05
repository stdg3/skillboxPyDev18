# -*- coding: utf-8 -*-
from random import randint
from datetime import datetime
import customExctentions as myExc
import time


# День сурка
#
# Напишите функцию one_day() которая возвращает количество кармы от 1 до 7
# и может выкидывать исключения:
# - IamGodError
# - DrunkError
# - CarCrashError
# - GluttonyError
# - DepressionError
# - SuicideError
# Одно из этих исключений выбрасывается с вероятностью 1 к 13 каждый день
#
# Функцию оберните в бесконечный цикл, выход из которого возможен только при накоплении
# кармы до уровня ENLIGHTENMENT_CARMA_LEVEL. Исключения обработать и записать в лог.
# При создании собственных исключений максимально использовать функциональность
# базовых встроенных исключений.

ENLIGHTENMENT_CARMA_LEVEL = 777

def one_day():
    karma = randint(1,7)
    # print(f"karma {karma}")
    if randint(1,13) == 1:
        try:
            raiseRandomExc()            
        except myExc.IamGodError as e:
            log_my_errors(e)
        except myExc.DrunkError as e:
            log_my_errors(e)
        except myExc.CarCrashError as e:
            log_my_errors(e)
        except myExc.GluttonyError as e:
            log_my_errors(e)
        except myExc.DepressionError as e:
            log_my_errors(e)
        except myExc.SuicideError as e:
            log_my_errors(e)

    return karma

def raiseRandomExc():
    r = randint(1,6)
    if r == 1:
        raise myExc.IamGodError()
    elif r == 2:
        raise myExc.DrunkError()
    elif r == 3:
        raise myExc.CarCrashError()
    elif r == 4:
        raise myExc.GluttonyError()
    elif r == 5:
        raise myExc.DepressionError()
    elif r == 6:
        raise myExc.SuicideError()

def log_my_errors(message):
    dt = datetime.now().strftime("%Y/%m/%d %H:%M%S")
    file = open("riseLog.txt", "a", encoding="utf8")
    file.write(f"[{dt}] '{message}'\n")
    file.close()
    # time.sleep(0.5)

if __name__ == "__main__":
    karma = 0
    while True:
        karma += one_day()
        if karma >= ENLIGHTENMENT_CARMA_LEVEL:
            break

# https://goo.gl/JnsDqu
