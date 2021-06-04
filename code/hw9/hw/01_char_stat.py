# -*- coding: utf-8 -*-

from pprint import pprint
from zipfile import ZipFile
from abc import ABCMeta, abstractmethod

# Подсчитать статистику по буквам в романе Война и Мир.
# Входные параметры: файл для сканирования
# Статистику считать только для букв алфавита (см функцию .isalpha() для строк)
#
# Вывести на консоль упорядоченную статистику в виде
# +---------+----------+
# |  буква  | частота  |
# +---------+----------+
# |    А    |   77777  |
# |    Б    |   55555  |
# |   ...   |   .....  |
# |    a    |   33333  |
# |    б    |   11111  |
# |   ...   |   .....  |
# +---------+----------+
# |  итого  | 9999999  |
# +---------+----------+
#
# Упорядочивание по частоте - по убыванию. Ширину таблицы подберите по своему вкусу
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.

raw_file = "../voyna-i-mir.txt"

class Alpha_Counter(metaclass=ABCMeta):
    tb_width = 15
    def __init__(self, file_name):
        self.file_name = file_name
        self.letters = {}
        self.total_lets = 0
    

    @abstractmethod
    def _sort_hertz_abc(self):
        pass

    @abstractmethod
    def _sort_alph_abc(self):
        pass

    @abstractmethod
    def _sort_alph_reverse(self):
        pass

    def _unzip(self):
        """not use
        """
        my_zip = ZipFile(self.file_name, mode="r")
        for files in my_zip.namelist():
            print(files, "--> exctracting...")
            my_zip.extract(files)
        self.file_name = files


    def take_off(self):
        self._get_letters()
        self._set_in_table()

        self._sort_hertz_abc()
        self._sort_alph_abc()
        self._sort_alph_reverse()


    def _get_letters(self):
        # first main def
        """get all chars from file
            and count it"""
        
        with open(self.file_name, "r", encoding="cp1251") as file:
            for line in file:
                self._chech_let_in_dict(line)
        
        # # overload sort
        # self.letters = dict(sorted(self.letters.items(), key=lambda item: item[1]))


    def _chech_let_in_dict(self, line):
        for let in line:
            if let.isalpha():
                if let in self.letters:
                    self.letters[let] += 1
                else:
                    self.letters[let] = 1
    

    def _set_in_table(self):
        # second main def
        with Create_table() as table:
            for key, val in self.letters.items():
                self.total_lets += val
                print("|" + key.center(self.tb_width) + "|" + str(val).center(self.tb_width) + "|")
                print("+" + "-" * self.tb_width + "+" + "-" * self.tb_width + "+")
            print("|" + "Total:".center(self.tb_width) + "|" + str(self.total_lets).center(self.tb_width) + "|")

   


class Create_table():
    def __enter__(self):
        print("+" + "-" * 15 + "+" + "-" * 15 + "+")
        print("|" + "Literals:".center(15) + "|" + "Frequence".center(15) + "|")
        print("+" + "-" * 15 + "+" + "-" * 15 + "+")
    
    def __exit__(self, exc_type, exc_val, exc_tab):
        print("+" + "-" * 15 + "+" + "-" * 15 + "+")


class My_Sort_Meth(Alpha_Counter):

    def _sort_hertz_abc(self):
        print("hertz")
        # overload sort
        self.letters = dict(sorted(self.letters.items(), key=lambda item: item[1]))
        self._set_in_table()
        
    
    def _sort_alph_abc(self):
        print("abc")
        trash = {}
        for key in sorted(self.letters):
            trash[key] = self.letters[key]
        self.letters = trash
        self._set_in_table()

        
    
    def _sort_alph_reverse(self):
        print("abc rev")
        trash = {}
        for key in sorted(self.letters, reverse=True):
            trash[key] = self.letters[key]
        self.letters = trash
        self._set_in_table()



if __name__ == "__main__":
    my_alpha = My_Sort_Meth(raw_file)
    my_alpha.take_off()




# После выполнения первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828

