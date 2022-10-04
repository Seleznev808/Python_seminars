list = [2, 3, 5, 9, 3]
sum = 0
for i in range(1, len(list), 2):
    sum += list[i]
print("Список:", ', '.join(map(str, list)))
print("Сумма элементов списка, стоящих на нечетной позиции:", sum)