def fibonacci(n):
    if n in [1, 2]:                       
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def nega_fibonacci(n):
    if n == 1:                       
        return 1
    elif n == 2:                       
        return -1
    else:
        num1, num2 = 1, -1
        for i in range(2, n):
            num1, num2 = num2, num1 - num2
        return num2


n = int(input("Введите число: "))
list = [0]
for i in range(1, n + 1):
    list.append(fibonacci(i))
    list.insert(0, nega_fibonacci(i))
print("Числа негафиббоначи и числа Фиббоначи:")
print(', '.join(map(str, list)))