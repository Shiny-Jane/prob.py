number = 23
running = True

while running:
    guess = int (input('Введите целое число: '))
    if guess == number:
        print('ПОЗДРАВЛЯЕМ! ВЫ угадали!!!')
        running = False   # Это останавливает цикл и переводит к else или конечному сообщению
    elif guess > number:
        print('Нет, заданное число больше искомого')
    else:
        print('Нет, заданное число меньше искомого')
else:
    print('Цикл while закончен')
print('Завершение')
