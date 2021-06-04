# -*- coding: utf-8 -*-

from pprint import pprint

from abc import ABCMeta, abstractmethod

# raw log --> [2018-05-14 19:37:47.873687] OK


# Имеется файл events.txt вида:
#
# [2018-05-17 01:55:52.665804] NOK
# [2018-05-17 01:56:23.665804] OK
# [2018-05-17 01:56:55.665804] OK
# [2018-05-17 01:57:16.665804] NOK
# [2018-05-17 01:57:58.665804] OK
# ...
#
# Напишите программу, которая считывает файл
# и выводит число событий NOK за каждую минуту в другой файл в формате
#
# [2018-05-17 01:57] 1234
# [2018-05-17 01:58] 4321
# ...
#
# Входные параметры: файл для анализа, файл результата
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.

class Split_Logs(metaclass=ABCMeta):

    def __init__(self, file_name = "events.txt"):
        self.res_dict_min = {}
        self.res_dict_hour = {}
        self.res_dict_mnth = {}
        self.res_dict_year = {}
        self.file_name = file_name
        self.raw_dtime_min = None
        self.raw_dtime_hour = None
        self.raw_dtime_month = None
        self.raw_dtime_year = None
        self.raw_status = None
        

    def do_it(self):
        self._read_file()
        # self.write_by_min()

    @abstractmethod
    def write_log(self):
        pass

    @abstractmethod
    def write_log_H(self):
        pass
    
    def _read_file(self):
        with open(self.file_name, "r", encoding="utf8") as file:
            for line in file:
                # print(line)
                self._get_status(line)
                self._get_dtime_min(line)
                self._get_dtime_hour(line)
                self._get_dtime_month(line)
                self._get_dtime_year(line)
            self.write_log(self.res_dict_mnth, "M")
            self.write_log(self.res_dict_year, "Y")
                # if self.raw_status == "NOK":
                #     self._get_dtime_min(line)
                    # self._get_dtime_hour(line)
                    # self._get_dtime_month(line)
                    # self._get_dtime_year(line)
                    # self._check_dtime_in_dict()
                # print(raw_dtime_min)
                # break
        # self._write_to_file()

    def _get_dtime_min(self, line):
        start = line.find("[") + 1
        end = line.rfind(":")
        line = line[start: end]
        # print(line)
        if self.raw_dtime_min == line:
            self._count_nok(line, self.res_dict_min)
        else:
            # yeni dakika
            if self.raw_dtime_min:
                self.write_log(self.res_dict_min, "min")            
            self._count_nok(line, self.res_dict_min)
            self.raw_dtime_min = line
            
    
    def _get_dtime_hour(self, line):
        start = line.find("[") + 1
        end = line.find(" ") + 3
        line = line[start: end]
        if self.raw_dtime_hour == line:
            self._count_nok(line,self.res_dict_hour)
        else:
            if self.raw_dtime_hour:
                self.write_log(self.res_dict_hour, "H")
            self._count_nok(line, self.res_dict_hour)
            self.raw_dtime_hour = line
        # self.raw_dtime_hour = line
        # print(line)

    def _get_dtime_month(self, line):
        start = line.find("[") + 1
        end = line.find("-") + 3
        line = line[start: end]
        if self.raw_dtime_month == line:
            self._count_nok(line,self.res_dict_mnth)
        else:
            if self.raw_dtime_month:
                self.write_log(self.res_dict_mnth, "M")
            self._count_nok(line, self.res_dict_mnth)
            self.raw_dtime_month = line
    
    def _get_dtime_year(self, line):
        start = line.find("[") + 1
        end = start + 4
        line = line[start: end]
        if self.raw_dtime_year == line:
            self._count_nok(line,self.res_dict_year)
        else:
            if self.raw_dtime_year:
                self.write_log(self.res_dict_year, "Y")
            self._count_nok(line, self.res_dict_year)
            self.raw_dtime_year = line
            
    def _get_status(self, line):
        end_sep = line.rfind(" ") + 1
        self.raw_status = line[end_sep: (len(line) -1)]

    def _count_nok(self, _dtime, _dict):
        if self.raw_status == "NOK":
            if _dtime in _dict:
                _dict[_dtime] += 1
            else:
                _dict[_dtime] = 1

        
        
class Output_Logs(Split_Logs):

    def write_log(self, _dict, _working_item):
        
        if _dict:
            file = open("log_by_min.txt", "a", encoding="utf8")
            for key, val in _dict.items():
                w = "[" + str(key) + "] " + str(val) + "\n"
                file.write(w)
            file.close()
        if _working_item == "min":
            self.res_dict_min = {}        
        elif _working_item == "H":
            self.res_dict_hour = {}
        elif _working_item == "M":
            self.res_dict_mnth = {}
        elif _working_item == "Y":
            self.res_dict_year = {}

    def write_log_H(self, _dict):        
        if _dict:
            file = open("log_by_hour.txt", "a", encoding="utf8")
            for key, val in _dict.items():
                w = "[" + str(key) + "] " + str(val) + "\n"
                file.write(w)
            file.close()
        self.res_dict_hour = {}
    # def write_by_min(self):
    #     file = open("log_out_by_min.txt", "w", encoding="utf8")
    #     for key, val in self.res_dict.items():
    #         w = str(key) + " --> " + str(val) + "\n"
    #         file.write(w)
    #     file.close()


if __name__== "__main__":
    out = Output_Logs()
    out.do_it()
    # pprint(res_dict)
    
# После выполнения первого этапа нужно сделать группировку событий
#  - по часам
#  - по месяцу
#  - по году
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
