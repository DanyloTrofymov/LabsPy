#Трофимов Данило ІП-02
#Лабораторна робота 4
#Варіант 5

import math

while True:

    s = float(0)
    x = float(input("введите значение x: "))
    n = int(input("введите количество членов ряда: "))

    if n > 0:
        for i in range(n):
            q = (x**(i))/math.factorial(i)
            s = s + q
        print("Сумма первых", n, "членов равна", s)
        break
    else:
        print("количество членов ряда должно быть больше 0")
        continue