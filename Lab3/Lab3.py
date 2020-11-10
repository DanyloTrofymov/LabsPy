#Трофимов Данило ІП-02
#Лабораторна робота 3
#Варіант 5

import math

x = float(0.56)
n = float(0)
s = float(0)
k = float(1)
m = float(0.0001)

while math.fabs(k) > m: 
    k = ((-1)**(n))*((x**(2)*(n+1))/(2**n+1))
    s = k + s
    n = n + 1
    print("{:12.9f}".format(s))
