from pprint import pprint
import csv
from data_processing import devision_name
from data_processing import change_telefon_namber
from data_processing import compere_list_2
from data_processing import remove_duplicates


def remove_double(contacts_list_a):
    len_contact_list = len(contacts_list_a)  # определяем длинну телефонной книги
    new_contact_list = []
    for element_contacts_list in contacts_list_a:
        position = 1
        while position < len_contact_list:
            any_element = compere_list_2(element_contacts_list, contacts_list_a[position])
            position += 1
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
    with open("phonebook_raw.csv", encoding='UTF-8') as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)

    for meber in contacts_list:
        devision_name(meber)      #разделяем фио на составные.
    for member in contacts_list:     #меняем телефоны.
        aaa = change_telefon_namber(member[5])
        member[5] = aaa
    contact_list_for_write = remove_double(contacts_list)   # убираем дублирование
    pprint(contact_list_for_write)


# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
    with open("phonebook.csv", "w") as f:
        datawriter = csv.writer(f, delimiter=',')
        # Вместо contacts_list подставьте свой список
        datawriter.writerows(contact_list_for_write)
