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

from utils import time_track
import os
from glob import glob
import csv
from unzip_module import unzip_file
import threading


class Volatility(threading.Thread):

    def __init__(self, files, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.csv_files = files

    def run(self):
        
        volat_res = {}
        zero_tickers = []

        for cfile in self.csv_files:
            vol = self._get_vol_by_file(cfile)
            if vol[1] == 0.0:
                zero_tickers.append(vol[0])
                continue
            volat_res[vol[0]] = float(vol[1])

        volat_res = sorted(volat_res.items(), key=lambda x: x[1], reverse=True)
        min_tickets = volat_res[-3:]
        max_tickets = volat_res[:3]
        zero_tickers.reverse()
        self._show_tickers_result(min_tickets, max_tickets, zero_tickers)

    def _get_vol_by_file(self, file):
        with open(file, encoding="utf-8") as r_file:
            file_reader = csv.reader(r_file, delimiter=",")
            after_1st_line = False
            price_list = []
            name = ""
            for row in file_reader:
                if after_1st_line:
                    # print(f"{row[0]} - {row[1]} - {row[2]} - {row[3]}")
                    price_list.append(row[2])
                    name = row[0]
                else:
                    after_1st_line = True
            # vol = volatility_calculator(min(price_list), max(price_list))
            min_price, maxx_price = float(min(price_list)), float(max(price_list))
            average = (min_price + maxx_price) / 2
            vol = round(((maxx_price - min_price) / average) * 100, 3)
            return [name, vol]

    def _show_tickers_result(self, t_min, t_max, zeros):
        print("Max volatility")
        for ticker in t_max:
            print(f"    {ticker[0]} - {ticker[1]} %")

        print("Min volatility")
        for ticker in t_min:
            print(f"    {ticker[0]} - {ticker[1]} %")

        for _ in zeros:
            print(_, end=", ")


    # def volatility_calculator(min_price, maxx_price):
    #     min_price, maxx_price = float(min_price), float(maxx_price)
    #     average = (min_price + maxx_price) / 2
    #     return round(((maxx_price - min_price) / average) * 100, 3)


    # def run():
    #     path_to_files = unzip_file("trades.zip")
    #     csv_files = get_files_csv(path_to_files)

    #     volat_res = {}
    #     zero_tickers = []

    #     for cfile in csv_files:
    #         vol = read_csv(cfile)
    #         if vol[1] == 0.0:
    #             zero_tickers.append(vol[0])
    #             continue
    #         volat_res[vol[0]] = float(vol[1])

    #     volat_res = sorted(volat_res.items(), key=lambda x: x[1], reverse=True)
    #     min_tickets = volat_res[-3:]
    #     max_tickets = volat_res[:3]
    #     zero_tickers.reverse()
    #     show_tickers_result(min_tickets, max_tickets, zero_tickers)


    # def show_tickers_result(t_min, t_max, zeros):
    #     print("Max volatility")
    #     for ticker in t_max:
    #         print(f"    {ticker[0]} - {ticker[1]} %")

    #     print("Min volatility")
    #     for ticker in t_min:
    #         print(f"    {ticker[0]} - {ticker[1]} %")

    #     for _ in zeros:
    #         print(_, end=", ")




def get_files_csv(container_folder):
    return list(glob(os.path.join(container_folder, "*csv")))

@time_track
def main():
    zip_archive = "trades.zip"
    container_folder = unzip_file(zip_archive)
    csv_files = get_files_csv(container_folder)



    a = Volatility(csv_files)
    a.run()

if __name__ == "__main__":
    main()
