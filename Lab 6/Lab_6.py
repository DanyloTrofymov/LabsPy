import math


def degree(angle):
    return (angle * math.pi) / 180

def square(x1, y1, angle1):
    return (x1 * y1 * math.sin(degree(angle1))) / 2

qmax = float(0)

n = int(input("Введiть кiлькiсть трикутникiв: "))

for i in range(1, n+1):
    x = float(input("Введiть довжину першоi сторони трикутника: "))
    y = float(input("Введiть довжину другоi сторони трикутника: "))
    angle = float(input("Введiть кут у градусах: "))
    q = float(square(x, y, angle))
    q = round(q, 5)
    if q > qmax:
        qmax = q
        xmax = x
        ymax = y
        imax = i
        anglemax = angle
print("Найбiльший трикутник № ",  imax, " зi сторонами ", xmax, " i ", ymax, ", кутом ", anglemax, " i площею ", qmax)