#Посчитать, сколько раз встречается определенная цифра(цифра – это от 0 до 9) в списке чисел.
# Количество введенных чисел в список и искомая цифра задаются с клавиатуры. Числа выбираются рандомно.

a = int(input("Введите желаемое кол-во чисел в списке:    "))
b = int(input("Введите искомую цифру (от 0 до 9):    "))

import random
i = 0

c = [random.randint(0,9) for i in range(a)]
print(c)
print(c.count(b))
