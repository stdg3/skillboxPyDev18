# -*- coding: utf-8 -*-


# Описание предметной области:
#
# При торгах на бирже совершаются сделки - один купил, второй продал.
# Покупают и продают ценные бумаги (акции, облигации, фьючерсы, етс). Ценные бумаги - это по сути долговые расписки.
# Ценные бумаги выпускаются партиями, от десятка до несколько миллионов штук.
# Каждая такая партия (выпуск) имеет свой торговый код на бирже - тикер - https://goo.gl/MJQ5Lq
# Все бумаги из этой партии (выпуска) одинаковы в цене, поэтому говорят о цене одной бумаги.
# У разных выпусков бумаг - разные цены, которые могут отличаться в сотни и тысячи раз.
# Каждая биржевая сделка характеризуется:
#   тикер ценнной бумаги
#   время сделки
#   цена сделки
#   обьем сделки (сколько ценных бумаг было куплено)
#
# В ходе торгов цены сделок могут со временем расти и понижаться. Величина изменения цен называтея волатильностью.
# Например, если бумага №1 торговалась с ценами 11, 11, 12, 11, 12, 11, 11, 11 - то она мало волатильна.after_1st_line
# А если у бумаги №2 цены сделок были: 20, 15, 23, 56, 100, 50, 3, 10 - то такая бумага имеет большую волатильность.
# Волатильность можно считать разными способами, мы будем считать сильно упрощенным способом -
# отклонение в процентах от средней цены за торговую сессию:
#   средняя цена = (максимальная цена + минимальная цена) / 2
#   волатильность = ((максимальная цена - минимальная цена) / средняя цена) * 100%
# Например для бумаги №1:
#   average_price = (12 + 11) / 2 = 11.5
#   volatility = ((12 - 11) / average_price) * 100 = 8.7%
# Для бумаги №2:
#   average_price = (100 + 3) / 2 = 51.5
#   volatility = ((100 - 3) / average_price) * 100 = 188.34%
#
# В реальности волатильность рассчитывается так: https://goo.gl/VJNmmY
#
# Задача: вычислить 3 тикера с максимальной и 3 тикера с минимальной волатильностью.
# Бумаги с нулевой волатильностью вывести отдельно.
# Результаты вывести на консоль в виде:
#   Максимальная волатильность:
#       ТИКЕР1 - ХХХ.ХХ %
#       ТИКЕР2 - ХХХ.ХХ %
#       ТИКЕР3 - ХХХ.ХХ %
#   Минимальная волатильность:
#       ТИКЕР4 - ХХХ.ХХ %
#       ТИКЕР5 - ХХХ.ХХ %
#       ТИКЕР6 - ХХХ.ХХ %
#   Нулевая волатильность:
#       ТИКЕР7, ТИКЕР8, ТИКЕР9, ТИКЕР10, ТИКЕР11, ТИКЕР12
# Волатильности указывать в порядке убывания. Тикеры с нулевой волатильностью упорядочить по имени.
#
# Подготовка исходных данных
# 1. Скачать файл https://drive.google.com/file/d/1l5sia-9c-t91iIPiGyBc1s9mQ8RgTNqb/view?usp=sharing
#       (обратите внимание на значок скачивания в правом верхнем углу,
#       см https://drive.google.com/file/d/1M6mW1jI2RdZhdSCEmlbFi5eoAXOR3u6G/view?usp=sharing)
# 2. Раззиповать средствами операционной системы содержимое архива
#       в папку python_base_source/lesson_012/trades
# 3. В каждом файле в папке trades содержится данные по сделакам по одному тикеру, разделенные запятыми.
#   Первая строка - название колонок:
#       SECID - тикер
#       TRADETIME - время сделки
#       PRICE - цена сделки
#       QUANTITY - количество бумаг в этой сделке
#   Все последующие строки в файле - данные о сделках
#
# Подсказка: нужно последовательно открывать каждый файл, вычитывать данные, высчитывать волатильность и запоминать.
# Вывод на консоль можно сделать только после обработки всех файлов.
#
# Для плавного перехода к мультипоточности, код оформить в обьектном стиле, используя следующий каркас
#
# class <Название класса>:
#
#     def __init__(self, <параметры>):
#         <сохранение параметров>
#
#     def run(self):
#         <обработка данных>

# TODO написать код в однопоточном/однопроцессорном стиле

import os
from glob import glob
import csv
from unzip_module import unzip_file
import threading
from utils import time_track


class Volatility(threading.Thread):

    def __init__(self, file="trades/TICKER_SiH9.csv", *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.csv_file_path = file
        self.volatility = 0
        self.ticker_name = None

    def run(self):
        price_list = []
        with open(self.csv_file_path, encoding="utf-8") as r_file:
            file_reader = csv.reader(r_file, delimiter=",")
            after_1st_line = False
            for row in file_reader:
                if after_1st_line:
                    # print(f"{row[0]} - {row[1]} - {row[2]} - {row[3]}")
                    price_list.append(row[2])
                    self.ticker_name = row[0]
                else:
                    after_1st_line = True
            # vol = volatility_calculator(min(price_list), max(price_list))
        min_price, max_price = float(min(price_list)), float(max(price_list))
        average = (min_price + max_price) / 2
        self.volatility = round(((max_price - min_price) / average) * 100, 3)
        # print(f"{self.ticker_name}: {self.volatility}")


def get_files_csv(container_folder):
    return list(glob(os.path.join(container_folder, "*csv")))


def show_tickers_result(t_min, t_max, zeros):
    print("Max volatility")
    for ticker in t_max:
        print(f"    {ticker[0]} - {ticker[1]} %")

    print("Min volatility")
    for ticker in t_min:
        print(f"    {ticker[0]} - {ticker[1]} %")

    for _ in zeros:
        print(_, end=", ")


@time_track
def main():

    zip_archive = "trades.zip"
    container_folder = unzip_file(zip_archive)

    csv_files = get_files_csv(container_folder)

    vol_counters = [Volatility(file=f) for f in csv_files]
    for vol_counter in vol_counters:
        vol_counter.start()

    for vol_counter in vol_counters:
        vol_counter.join()

    raw_ticket_vols = {}
    zero_tickets = []
    for vol_counter in vol_counters:
        if vol_counter.volatility == 0.0:
            zero_tickets.append(vol_counter.ticker_name)
            continue
        raw_ticket_vols[vol_counter.ticker_name] = vol_counter.volatility

    sorted_ticks = sorted(raw_ticket_vols.items(), key=lambda x: x[1], reverse=True)
    min_tickets = sorted_ticks[-3:]
    max_tickets = sorted_ticks[:3]
    zero_tickets.sort()
    
    show_tickers_result(min_tickets, max_tickets, zero_tickets)


if __name__ == "__main__":
    main()
