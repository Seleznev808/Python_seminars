N = int(input("Введите число N: "))
list = []
for i in range(-N, N + 1):
    list.append(i)
x1 = -2
x2 = 1
product = list[x1] * list[x2]
print(f"Список элементов от {-N} до {N}:", ', '.join(map(str, list)))
print(f"Произведение элементов на позициях {x1} и {x2} = {product}")