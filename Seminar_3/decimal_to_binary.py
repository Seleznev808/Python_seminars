decimal_number = int(input("Введите целое число: "))
list = []
while decimal_number >= 1:
    list.append(decimal_number % 2)
    decimal_number //= 2
print("Ваше число в двоичном представлении:", ''.join(map(str, list[::-1])))