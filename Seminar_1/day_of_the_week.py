day_week = int(input("Введите порядковый номер дня недели: "))
if 1 <= day_week <= 5:
    print("Это будний день")
elif day_week == 6 or day_week == 7:
    print("Это выходной")
else:
    print("Попробуйте еще раз")