#Трофимов Данило ІП-02
#Лабораторна робота 4
#Варіант 11

sum = int
num = int
a = int
b = int
c = int


for i in range (100, 1000):
    a = i // 100
    b = (i // 10) % 10
    c = i % 10
    num = i
    sum = a ** 3 + b ** 3 + c ** 3
    if (sum == num):
        print(num)
