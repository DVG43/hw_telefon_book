import re


start_data_1 = ['Усольцев Олег Валентинович', '', '',]

name = 'Усольцев Олег Валентинович'
name_2 = 'Усольцев'

pattern = r"\s"
marker = re.search(pattern, name)
# if len(marker) >= 0:

print(marker)