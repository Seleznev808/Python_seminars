list = [2, 3, 4, 5, 6]
result_list = []
if len(list) % 2 == 0:
    for i in range(len(list) // 2):
        result_list.append(list[i] * list[-i - 1])
else:
    for i in range(len(list) // 2):
        result_list.append(list[i] * list[-i - 1])
    result_list.append(list[len(list) // 2] ** 2)    
print("Список:", ', '.join(map(str, list)))
print("Произведение пар чисел списка (первое и последнее и т.д.):", ', '.join(map(str, result_list)))