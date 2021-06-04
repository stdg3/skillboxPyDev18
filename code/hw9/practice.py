import zipfile

from pprint import pprint

from random import randint

#""" 
# сделать генератор текста на аснове статистики 
# идея проста: подсчитаем какие буквы наиболее часто стоят рядом
# точнее, подсчитаем как часто за буквой х идет буква у, на аснове некоего текста
# после этого начнем с произвольной буквы и каждую следующую будем выбирать в зависимости 
# частоты ее появления в статистике 
# 
# """

# zip_file_name = "voyna-i-mir.txt.zip"

# my_zip = zipfile.ZipFile(zip_file_name, "r")
# my_zip.printdir()



class Chatter:
    analize_count = 4

    def __init__(self, file_name):
        self.file_name = file_name
        self.stat = {}
    

    def unzip(self):
        # zip_file_name = "voyna-i-mir.txt.zip"
        my_zip = zipfile.ZipFile(self.file_name, "r")
        for file_in_zip in my_zip.namelist():
            # my_zip.namelist()
            print(file_in_zip, "extracting...")
            my_zip.extract(file_in_zip)
        self.file_name = file_in_zip


    def collect(self):
        if self.file_name.endswith(".zip"):
            self.unzip()
        self.sequence = " " * self.analize_count
        with open(self.file_name, mode="r", encoding="cp1251") as file:
            for line in file:
                # print(line)
                self._collect_for_line(line = line[:-1])


    def _collect_for_line(self, line):
        for char in line:
            if self.sequence in self.stat:
                if char in self.stat[self.sequence]:
                    self.stat[self.sequence][char] += 1
                else:
                    self.stat[self.sequence][char] = 1
            else:
                self.stat[self.sequence] = {char: 1}
            self.sequence = self.sequence[1:] + char


    def prepare(self):
        self.totals = {}
        self.stat_for_generate = {}
        for sequence, char_stat in self.stat.items():
            self.totals[sequence] = 0
            self.stat_for_generate[sequence] = []
            for char, count in char_stat.items():
                self.totals[sequence] += count
                self.stat_for_generate[sequence].append([count, char])        
                self.stat_for_generate[sequence].sort(reverse=True)


    def chat(self, nn, out_file_name = None):
        nn = 1000
        self.printed = 0
        if out_file_name is not None:
            file = open(out_file_name, "w", encoding="utf8")
        else:
            file = None
        sequence = " " * self.analize_count
        self.spaces_printed = 0
        while self.printed < nn:
            char = self._get_char(char_stat = self.stat_for_generate[sequence], total=self.totals[sequence])
            
            self._to_file_or_console_print(file, char)
            
            self._line_width_control(file, char,)
            sequence = sequence[1:] + char
        if file:
            file.close()


    def _get_char(self, char_stat, total):
        dice = randint(1, total)
        pos = 0
        for count, char in char_stat:
            pos += count
            if dice <= pos:
                break
        return char


    def _to_file_or_console_print(self, file, char):
        if file:
                file.write(char)
        else:
            print(char, end="")


    def _line_width_control(self, file, char,):        
        if char == " ":
            self.spaces_printed +=1
            if self.spaces_printed >= 10:
                if file:
                    file.write("\n")
                else:
                    print()
                self.spaces_printed = 0
        self.printed += 1


def extract_zip_file():
    zip_file_name = "voyna-i-mir.txt.zip"

    my_zip = zipfile.ZipFile(zip_file_name, "r")
    for file_in_zip in my_zip.namelist():
        # my_zip.namelist()
        print(file_in_zip, "extracting...")
        my_zip.extract(file_in_zip)


# file_name = "voyna-i-mir.txt"

# stat = {}
# stat = {
#     "а": {"т": 500, "х": 5},
#     "т": {"о": 100, "о": 50},

# }

# analize_count = 4
# sequence = " " * analize_count

# with open(file_name, mode="r", encoding="cp1251") as file:
#     for line in file:
#         # print(line)
#         line = line[:-1]
#         for char in line:
#             if sequence in stat:
#                 if char in stat[sequence]:
#                     stat[sequence][char] += 1
#                 else:
#                     stat[sequence][char] = 1
#             else:
#                 stat[sequence] = {char: 1}
#             sequence = sequence[1:] + char

# pprint(stat)
# print(len(stat))

# totals = {}
# stat_for_generate = {}

# for sequence, char_stat in stat.items():
#     totals[sequence] = 0
#     stat_for_generate[sequence] = []

#     for char, count in char_stat.items():
#         totals[sequence] += count
#         stat_for_generate[sequence].append([count, char])
    
#     stat_for_generate[sequence].sort(reverse=True)


# pprint(totals)
# pprint(stat_for_generate)

# nn = 1000
# printed = 0

# sequence = " " * analize_count
# spaces_printed = 0
# while printed < nn:
#     char_stat = stat_for_generate[sequence]
#     total = totals[sequence]
#     dice = randint(1, total)
#     pos = 0
#     for count, char in char_stat:
#         pos += count
#         if dice <= pos:
#             break
#     print(char, end="")
#     if char == " ":
#         spaces_printed +=1
#         if spaces_printed >= 10:
#             print()
#             spaces_printed = 0
#     printed += 1
#     sequence = sequence[1:] + char



chatterer = Chatter(file_name = "voyna-i-mir.txt")
chatterer.collect()
chatterer.prepare()
chatterer.chat(nn=1000, out_file_name="rand_words.txt")
