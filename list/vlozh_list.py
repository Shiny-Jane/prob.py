# Создай список, замени первый его элемент на [1, 2, 3], затем в конец списка добавь сумму элементов вложенного списка.

### 1 СПОСОБ)

a = [18, 38, '$', 1, 'H']            # исходный список
a[0] = [1,2,3]                          # первый элемент исходного списка меняем на вложенный список
sum(a[0])                               # находим сумму элементов вложенного списка
a.append(sum(a[0]))                     # добавляем это значение в конец списка  a  с вложенным списком
print('1 СПОСОБ  :\n', a)

### 2 СПОСОБ)

import random
i = 0
b = [random.randint(0,10) for i in range(2)]+ [random.choice('Fan$Y') for i in range(3)]
print('2 СПОСОБ\n Список b random: ', b)
b[0] = [1,2,3]
sum(b[0])
b.append(sum(b[0]))
print(b)