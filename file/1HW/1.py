#Ввести в файл ‘input.txt’ 2 числа в одну строку через пробел. Вывести в файл ‘output.txt’ их разность

INPUT = open('input.txt', 'w')       # INPUT
a = [34,18]
b = [str(x) for x in a]
#print (" ".join(b))
INPUT.write (" ".join(b))
INPUT.close()
INPUT = open('input.txt', 'r')
print(INPUT.readline())
INPUT.close()

OUTPUT = open('output.txt', 'w')          #OUTPUT
c = str(a[0]-a[1])
OUTPUT.write((c))
OUTPUT.close()
OUTPUT = open('output.txt', 'r')
print(OUTPUT.readline())
OUTPUT.close()

