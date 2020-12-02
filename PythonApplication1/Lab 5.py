#Трофимов Данило ІП-02
#Лабораторна робота 4
#Варіант 11

sum = int
num = int

for i in range (1, 10):
    for j in range (0, 10):
        for k in range (0, 10):
            sum=i ** 3 + j ** 3 + k ** 3
            num=i * 100 + j * 10 + k
            if (sum == num):
                print(num)