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
def extract_zip_file():
    zip_file_name = "voyna-i-mir.txt.zip"

    my_zip = zipfile.ZipFile(zip_file_name, "r")
    for file_in_zip in my_zip.namelist():
        # my_zip.namelist()
        print(file_in_zip, "extracting...")
        my_zip.extract(file_in_zip)


file_name = "voyna-i-mir.txt"

stat = {}
# stat = {
#     "а": {"т": 500, "х": 5},
#     "т": {"о": 100, "о": 50},

# }

analize_count = 4
sequence = " " * analize_count

with open(file_name, mode="r", encoding="cp1251") as file:
    for line in file:
        # print(line)
        line = line[:-1]
        for char in line:
            if sequence in stat:
                if char in stat[sequence]:
                    stat[sequence][char] += 1
                else:
                    stat[sequence][char] = 1
            else:
                stat[sequence] = {char: 1}
            sequence = sequence[1:] + char

# pprint(stat)
# print(len(stat))

totals = {}
stat_for_generate = {}

for sequence, char_stat in stat.items():
    totals[sequence] = 0
    stat_for_generate[sequence] = []

    for char, count in char_stat.items():
        totals[sequence] += count
        stat_for_generate[sequence].append([count, char])
    
    stat_for_generate[sequence].sort(reverse=True)


# pprint(totals)
# pprint(stat_for_generate)

nn = 1000
printed = 0

sequence = " " * analize_count
spaces_printed = 0
while printed < nn:
    char_stat = stat_for_generate[sequence]
    total = totals[sequence]
    dice = randint(1, total)
    pos = 0
    for count, char in char_stat:
        pos += count
        if dice <= pos:
            break
    print(char, end="")
    if char == " ":
        spaces_printed +=1
        if spaces_printed >= 10:
            print()
            spaces_printed = 0
    printed += 1
    sequence = sequence[1:] + char

