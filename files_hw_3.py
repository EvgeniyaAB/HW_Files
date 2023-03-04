new_d = {}

from pathlib import Path
file_name_1 = str(Path('1.txt'))
print(file_name_1)
file_name_2 = str(Path('2.txt'))
print(file_name_2)
file_name_3 = str(Path('3.txt'))
print(file_name_3)

try:
    with open('1.txt', 'r', encoding='utf-8') as file:
        res_1 = file.read()
        file.seek(0)
        a = int(len(file.readlines()))
        new_d[file_name_1] = a
        print(a)

except:
    print('ошибка')

try:
    with open('2.txt', 'r', encoding='utf-8') as file:
        res_2 = file.read()
        file.seek(0)
        b = int(len(file.readlines()))
        new_d[file_name_2] = b
        print(b)

except:
    print('ошибка')

try:
    with open('3.txt', 'r', encoding='utf-8') as file:
        res_3 = file.read()
        file.seek(0)
        c = int(len(file.readlines()))
        new_d[file_name_3] = c
        print(c)

except:
    print('ошибка')


new_d_sort = dict(sorted(new_d.items(), key=lambda item: item[1]))

print(new_d_sort)
for key, value in new_d_sort.items():
    try:
        with open('new_f4.txt', 'a') as file:
            file.writelines(f'{key}\n{value}\n')
            s = open(key, encoding='utf-8')
            file.writelines(s)
            file.writelines('\n')

            s.close()
    except:
        print('ошибка')