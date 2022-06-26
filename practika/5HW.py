#С клавиатуры вводится 7-значное число. Если четных цифр в нем больше, чем нечетных, то найти сумму всех его цифр
# если нечетных больше, то найти произведение 1 3 и 6 цифры.
a = input("Введите 7-ми значное число:  ")
b = list(a)
print(b)

i = 0
chet = 0
ne_chet = 0

for i in b:
    if int(i) % 2 == 0:
        chet += 1
    else:
        ne_chet +=1

if chet > ne_chet:
    print(int(b[0])+int(b[1])+int(b[2])+int(b[3])+int(b[4])+int(b[5])+int(b[6]))
else:
    print(int(b[0])*int(b[2])*int(b[5]))