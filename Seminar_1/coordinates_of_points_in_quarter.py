quarter_number = int(input("Введите номер четверти: "))
if quarter_number == 1:
    print(f"Координаты точек в {quarter_number} четверти: x > 0, y > 0")
elif quarter_number == 2:
    print(f"Координаты точек в {quarter_number} четверти: x < 0, y > 0")
elif quarter_number == 3:
    print(f"Координаты точек в {quarter_number} четверти: x < 0, y < 0")
elif quarter_number == 4:
    print(f"Координаты точек в {quarter_number} четверти: x > 0, y < 0")
else:
    print("Попробуйте еще раз!")