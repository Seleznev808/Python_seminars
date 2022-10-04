list = [1.1, 1.2, 3.1, 5, 10.01]
list_float = []
for i in range(len(list)):
    if type(list[i]) == float:
        list_float.append(round(list[i] % 1, 2))
min = 1
max = 0
for i in range(len(list_float)):
    if list_float[i] <= min:
        min = list_float[i]
    if list_float[i] >= max:
        max = list_float[i]  
print("Список:", ', '.join(map(str, list)))
print("Разница между максимальным и минимальным значением дробной части элементов списка:", max-min)