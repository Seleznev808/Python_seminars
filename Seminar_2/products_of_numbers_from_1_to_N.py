N = int(input("Введите число N: "))
product = 1
list = []
for i in range(1, N + 1):
    product *= i
    list.append(product)
print(f"Произведение чисел от 1 до {N} =", ', '.join(map(str, list)))