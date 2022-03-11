from pprint import pprint
import csv
from data_processing import devision_name
from data_processing import change_telefon_namber
from data_processing import compere_list_2
from data_processing import remove_duplicates
# Ваша задача: починить адресную книгу, используя регулярные выражения.
# Структура данных будет всегда:
# lastname,firstname,surname,organization,position,phone,email
# Предполагается, что телефон и e-mail у человека может быть только один.
# Необходимо:
#
# поместить Фамилию, Имя и Отчество человека в поля lastname, firstname и surname соответственно. В записной книжке изначально может быть Ф + ИО, ФИО, а может быть сразу правильно: Ф+И+О;
# привести все телефоны в формат +7(999)999-99-99. Если есть добавочный номер, формат будет такой: +7(999)999-99-99 доб.9999;
# объединить все дублирующиеся записи о человеке в одну


def remove_double (contacts_list):
    len_contact_list = len(contacts_list)  # определяем длинну телефонной книги
    new_contact_list = []
    for element_contacts_list in contacts_list:
        position = 1
        while position < len_contact_list:
            any_element = compere_list_2(element_contacts_list, contacts_list[position])
            position += 1
            print(any_element)
        if any_element == 'no':
            new_contact_list.append(element_contacts_list)
        else:
            if any_element in new_contact_list:
                pass
            else:
                new_contact_list.append(any_element)
    fifish_contact_list = remove_duplicates(new_contact_list)
    return fifish_contact_list


if __name__ == '__main__':
    with open("phonebook_raw.csv",encoding='UTF-8') as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)

    for meber in contacts_list:
        devision_name(meber)      #разделяем фио на составные.
    for member in contacts_list:     #меняем телефоны.
        aaa = change_telefon_namber(member[5])
        member[5] = aaa
    pprint(contacts_list)
    pprint(remove_double(contacts_list)) # убираем дублирование , у



# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
#     with open("phonebook.csv", "w") as f:
#         datawriter = csv.writer(f, delimiter=',')
#         # Вместо contacts_list подставьте свой список
#         datawriter.writerows(contacts_list)
