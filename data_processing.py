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
   if list_for_compere_1[:2] == list_for_compere_2[:2]:
      counter = 0
      while counter <= 6:
           if list_for_compere_1[counter] == "":
               list_for_compere_1[counter] = list_for_compere_2[counter]
               counter += 1
           else:
               counter += 1
   return list_for_compere_1