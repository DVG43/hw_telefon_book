import re
from pprint import pprint


def devision_name (start_data_1):
    pattern = r"\s"
    marker = re.findall(pattern, start_data_1[0])
    if len(marker) >= 1:
        new_name = re.split(pattern, start_data_1[0])
        if len(new_name) == 3:
            start_data_1[0] = new_name[0]
            start_data_1[1] = new_name[1]
            start_data_1[2] = new_name[2]
        else:
            start_data_1[0] = new_name[0]
            start_data_1[1] = new_name[1]

    marker_1 = re.findall(pattern, start_data_1[1])
    if len(marker_1) >= 1:
        new_name = re.split(pattern, start_data_1[1])
        start_data_1[1] = new_name[0]
        start_data_1[2] = new_name[1]

    return (start_data_1)

def compere_list(list_for_compere):
    new_lis = []
    for member_in_list in list_for_compere:
        new_member = member_in_list [:2]
        new_lis.append(new_member)
    return new_lis

def compere_list_2(list_for_compere_1,list_for_compere_2):
   indikator = 'no'
   if list_for_compere_1[:2] == list_for_compere_2[:2]:
      counter = 0
      while counter <= 6:
           if list_for_compere_1[counter] == "":
               list_for_compere_1[counter] = list_for_compere_2[counter]
               counter += 1
           else:
               counter += 1
      if len(list_for_compere_1) == 8:
          list_for_compere_1.pop(-1)
      return list_for_compere_1
   else:
      return indikator

def change_telefon_namber (namber_telefon):
    patern = r"(\+\d)(\s+)(\S+)(\s+)(\d+)(\S+)"
    resalt = re.sub(patern, r"\1\3\5\6", namber_telefon) # убирали пробелы
    patern_1 = r"(\+\d)(\d{3,5})(\d{3})(\d{2})(\d{2})"
    resalt_1 = re.sub(patern_1, r"+7(\2)\3-\4-\5", resalt)  #изменили cплошной телефон
    patern_2 = r"(\d)(\s+)(\d+)(\D+)(\d+)(\D+)(\d{2})(\d{2})"
    resalt_2 = re.sub(patern_2, r"\1(\3)\5-\7-\8", resalt_1)  #взяли в скобки первые три цыфры
    patern_3 = r"(8)(\S)(\d+)(\S)(\d+)(.+)"
    resalt_3 = re.sub(patern_3,r"+7\2\3\4\5\6",resalt_2 )  #замена 8
    patern_4 = r"(\+7)(\S+)(.+)(доб.)(\s+)(\d+)(.+)"
    resalt_4 = re.sub(patern_4,r"\1\2 \4\6",resalt_3 )  #работа с добавочным номером

    return resalt_4