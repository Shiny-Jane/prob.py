#Дан список. Выведите те его элементы, которые встречаются в списке только один раз.
# Элементы нужно выводить в том порядке, в котором они встречаются в списке.

####1 СПОСОБ####

a = [1, 3, 3, 'T', 0, 'T', 2, 2, 'sos']

for i in a:
    if a.count(i) >= 2:
        continue
    else:
        print(i)

####2 СПОСОБ#####

b = [1, 3, 3, 'T', 0, 'T', 2, 2, 'sos']
d = []
for i in b:
    if a.count(i) == 1:
        d.append(i)
print(d)