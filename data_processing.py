import re


# start_data_1 = ['Усольцев Олег Валентинович', '', '',]
start_data_1 =['Наркаев', 'Вячеслав Рифхатович']
# name = 'Усольцев Олег Валентинович'
# name_2 = 'Усольцев'
# def devision_name (start_data_1):
pattern = r"\s"
n = 0
while n <= 2:
    marker = re.findall(pattern, start_data_1[n])
    if len(marker) >= 1:
        new_name = re.split(pattern, start_data_1[n])
        print (new_name)
        start_data_1[0] = new_name[0]
        print(start_data_1[0])
        start_data_1[1] = new_name[1]
        print(start_data_1[1])
        start_data_1[2] = new_name[2]
        print(start_data_1[2])
        n += 1
    else:
        n +=1
    print (start_data_1)
    # return (start_data_1)

# print(start_data_1)