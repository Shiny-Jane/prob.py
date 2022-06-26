#Посчитать, сколько пар (стоят рядом) верхнего и нижнего регистра находится в веденном с клавиатуры слове.
# (Пример HjkLM- 1 пара нижнего, 1 пара верхнего), а также сколько всего букв в слове, сколько гласных и согласных.

a = input("Введите любое слово с разными регистрами:  ")
b = "АЕЁИОУЫЭЮЯаеёиоуыэюяEYUIOAJeyuioaj"

i = 0
glas = 0
soglas = 0
para_lower = 0
para_upper = 0

for i in range(0, len(a)-1):
    if a[i].islower() and a[i+1].islower():
        para_lower += 1
    if a[i].isupper() and a[i+1].isupper():
        para_upper += 1
print("Пар нижнего регистра: ", para_lower)
print("Пар верхнего регистра: ",para_upper)
print("Число букв в слове:  ",len(a))

for i in a:
    if i in b:
        glas +=1
    else:
        soglas +=1
print("Гласных:   ", glas)
print("Согласных:   ", soglas)





