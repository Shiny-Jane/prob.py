import random

i = 0
v = 0
p = 0
while i < 7:
    i = i + 1  # i+=1
    a = int(input("Введите первое число от 0 до 20: "))
    b = int(input("Введите второе число от 0 до 20: "))
    c = random.randint(0, 20)
    print(c)
    d = random.randint(0, 20)
    print(d)
    if a > c and b > d:
        v += 1
    else:
        p += 1

if v == p:
    if i == 4:
        f = c
        g = d
    print(f, g)
print(f"Пара, введёных пользователем чисел оказалась больше: {v} раз ")





