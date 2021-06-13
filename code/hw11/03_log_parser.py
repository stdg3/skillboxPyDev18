# -*- coding: utf-8 -*-
from getpass import getuser
# На основе своего кода из lesson_009/02_log_parser.py напишите итератор (или генератор)
# котрый читает исходный файл events.txt и выдает число событий NOK за каждую минуту
# <время> <число повторений>
#
# пример использования:
#
# grouped_events = <создание итератора/генератора>
# for group_time, event_count in grouped_events:
#     print(f'[{group_time}] {event_count}')
#
# на консоли должно появится что-то вроде
#
# [2018-05-17 01:57] 1234
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
username = getuser()
log_file = f"/home/{username}/Videos/skillboxPy/skillboxPyDev18/code/hw9/hw/events.txt"


def get_status(min_line):
    end_sep = min_line.rfind(" ") + 1
    return True if min_line[end_sep: (len(min_line) - 1)] == "NOK" else None


def get_min(min_line):
    start = min_line.find("[") + 1
    end = min_line.rfind(":")
    return min_line[start: end]


def file_opp(decor_func):
    def inner():
        status = None
        res_stat = {}
        with open(log_file, "r", encoding="utf8") as file:
            for line in file:
                status = get_status(line)  # if NOK -> True
                min_from_curr_line = get_min(line)

                if min_from_curr_line in res_stat:
                    if status:
                        res_stat[min_from_curr_line] += 1
                else:
                    if res_stat:
                        key = list(res_stat.keys())[0]
                        decor_func(key, res_stat[key])
                    res_stat = {}
                    if status:
                        res_stat[min_from_curr_line] = 1
    return inner


@file_opp
def read_file(group_time, event_count):
    print(f'[{group_time}] {event_count}')
    # input()


# print(dir_path)
read_file()
