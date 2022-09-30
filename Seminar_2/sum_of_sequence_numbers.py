n = int(input("Введите число n: "))
sum = 0
for i in range(1, n + 1):
    sum += (1 + 1 / i) ** i
print("Сумма чисел последовательности (1+1/n)^n =", round(sum, 2))