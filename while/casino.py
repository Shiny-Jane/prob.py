# Казино. Число - от 1 до 10. Цвет - от 1 до 2 (1 -красный, 2 - черный).
# У пользователя 5 попыток

import random

a = random.randint(1,10)
b = random.randint(1,2)

i = 0

while i < 5:
    i = i + 1
    c = int (input('Введите число от 1 до 10:  '))
    d = int(input('Введите число (1 - красный, 2 - черный ):  '))

    if a == c  and  b ==d:
        print(f'Вы угадали число: {c}, и цвет: {d}. ПОЗДРАВЛЯЕМ!!!')
        break   #  пользователь всё угадал, цикл - закончен, программа - выполнена
    elif a != c  and  b ==d:
        print(f'Вы НЕ угадали число: {c}, но УГАДАЛИ ЦВЕТ: {d}')
    elif a == c  and  b !=d:
        print(f'Вы  УГАДАЛИ ЧИСЛО: {c}, но  НЕ угадали цвет: {d}')
    else:
        print(f'Вы  НИЧЕГО НЕ УГАДАЛИ! ')
else:
    print(f'Вы  НИЧЕГО НЕ УГАДАЛИ! ПОПЫТКИ ЗАКОНЧИЛИСЬ! ПРАВИЛЬНЫЙ ВАРИАНТ: {a}{b}')


