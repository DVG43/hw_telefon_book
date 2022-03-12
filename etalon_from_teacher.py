from pprint import pprint
import csv
import re

# читаем адресную книгу в формате CSV в список contacts_list
with open("phonebook_raw.csv") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
pprint(contacts_list)

# TODO 1: выполните пункты 1-3 ДЗ
# ваш код

# Задание 1
first_result = []
for item in contacts_list:
    sub_list = []
    for elm in item[0:3]:
        sub_list.extend(elm.split())
    sub_list.extend(item[3:])
    first_result.append(sub_list)

# Задание 2
for item in first_result:
    pattern_phone = r"(\+7|8)(\s?\(?)(\d{3})(\-?\)?\s?)(\d{3})(\-?)(\d{2})(\-?)(\d{2})(\s?)(\(?)([д]?[о]?[б]?\.?)(\s?)(\d?\d?\d?\d?)(\)?)"
    result = re.sub(pattern_phone, r"+7(\3)\5-\7-\9\10\12\14", item[5])
    item[5] = result
pprint(first_result)

# Задание 3
dictionary = {}
for name, *specifications in first_result[1:]:
    if name not in dictionary:
        dictionary[name] = [""] * 6
    for i, (old, new) in enumerate(zip(dictionary[name], specifications)):
        dictionary[name][i] = old if old else new
contacts_result = [[k, *v] for k, v in dictionary.items()]

# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w") as f:
    datawriter = csv.writer(f, delimiter=',')
    # Вместо contacts_list подставьте свой список
    datawriter.writerows(contacts_result)
