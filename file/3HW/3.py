#В текстовом файле посчитать количество строк, а также для каждой отдельной строки определить количество в ней символов.

import os

f = open('1.txt','r')
a = f.readlines()
print(a)

res = 0
for i in a:
    if i !=' ':
        res +=1
        print(len(i)-1)
print(f'Строк в файле : {res} ')