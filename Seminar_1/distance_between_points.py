print("Введите координаты точки a")
ax = int(input("x = "))
ay = int(input("y = "))
print("Введите координаты точки b")
bx = int(input("x = "))
by = int(input("y = "))
distance_points = round((((ax - bx) ** 2 + (ay - by) ** 2) ** 0.5), 2)
print(f"Расстояние между точками a и b - {distance_points}")