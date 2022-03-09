import re


start_data_1 = ['Лагунцов Иван', '', '']
#start_data_1 =['Наркаев', 'Вячеслав Рифхатович','']
# name = 'Усольцев Олег Валентинович'
# name_2 = 'Усольцев'
#def devision_name (start_data_1):
pattern = r"\s"
marker = re.findall(pattern, start_data_1[0])
if len(marker) >= 1:
    new_name = re.split(pattern, start_data_1[0])
    if len(new_name) == 3:
        print(new_name)
        start_data_1[0] = new_name[0]
        start_data_1[1] = new_name[1]
        start_data_1[2] = new_name[2]
    else:
        start_data_1[0] = new_name[0]
        start_data_1[1] = new_name[1]
print (start_data_1)

marker_1 = re.findall(pattern, start_data_1[1])
if len(marker_1) >= 1:
    new_name = re.split(pattern, start_data_1[1])
    start_data_1[1] = new_name[0]
    start_data_1[2] = new_name[1]

print (start_data_1)
    #return (start_data_1)

# print(start_data_1)