a = float(input("Введите длину ребра куба: "))

while a <= 0:
    a = float(input("Введите длину ребра куба больше 0: "))
s = 4*a*a
v = a*a*a 
print("Длина ребра " + str(a))
print("Площадь боковой поверхности " + str(s))
print("Объем куба " + str(v))


