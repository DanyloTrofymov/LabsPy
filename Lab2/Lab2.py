#Трофимов Данило ІП-02
#Лабораторна робота 2
#Варіант 14

x = float(input("Введите длину первой стороны треугольника: ")) #ввод первой стороны треугольника
y = float(input("Введите длину второй стороны треугольника: ")) #ввод второй стороны треугольника
z = float(input("Введите длину третей стороны треугольника: ")) #ввод третей стороны треугольника

if (x + y > z) and (x + z > y) and (y + z > x):
    print("Треугольник существует")
else:
    print("Треугольник не существует")


