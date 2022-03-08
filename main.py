from pprint import pprint
import csv

# Ваша задача: починить адресную книгу, используя регулярные выражения.
# Структура данных будет всегда:
# lastname,firstname,surname,organization,position,phone,email
# Предполагается, что телефон и e-mail у человека может быть только один.
# Необходимо:
#
# поместить Фамилию, Имя и Отчество человека в поля lastname, firstname и surname соответственно. В записной книжке изначально может быть Ф + ИО, ФИО, а может быть сразу правильно: Ф+И+О;
# привести все телефоны в формат +7(999)999-99-99. Если есть добавочный номер, формат будет такой: +7(999)999-99-99 доб.9999;
# объединить все дублирующиеся записи о человеке в одну



if __name__ == '__main__':
    with open("phonebook_raw.csv",encoding='UTF-8') as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)
    pprint(contacts_list)
    # contacts_list.remove('')
    # pprint(contacts_list)

# TODO 1: выполните пункты 1-3 ДЗ
#   ваш код
    new_contakt_list =[]
    for strings_tabl in contacts_list:
        new_strings_tabl = '*'.join(strings_tabl)
        new_contakt_list.append(new_strings_tabl)
    pprint(new_contakt_list)

# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
#     with open("phonebook.csv", "w") as f:
#         datawriter = csv.writer(f, delimiter=',')
#         # Вместо contacts_list подставьте свой список
#         datawriter.writerows(contacts_list)
