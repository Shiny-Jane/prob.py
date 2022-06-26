# Добавьте на свой рабочий стол папку, в ней создайте 3 текстовых файла: test_1.txt, test_2.txt, test_3.txt.
# Затем переименуйте файлы на: rename_1.txt, rename_2.txt, rename_3.txt.
# После этого удалите созданную папку.
# Все операции выполнять с помощью встроенных функций библиотеки os

import os

#os.mkdir('test')
# os.chdir('test')
print(os.getcwd())

# with open('test_1', 'w') as f:
#     f.write('1')
# with open('test_2', 'w') as f:
#     f.write('2')
# with open('test_3', 'w') as f:
#     f.write('3')
# os.rename('test_1','rename_1')
# os.rename('test_2','rename_2')
# os.rename('test_3','rename_3')
os.rmdir('test')