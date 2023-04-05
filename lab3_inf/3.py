# 3 задание:
# 20 + 22 = 42   (1593 + 1929 = 7049)
# 15 + 17 - 29 = 3   (893 + 1149 - 3357 = 29)
# 24 - 8 = 16   (2297 - 249 = 1017)
# 3 * 4 = 12   (29 * 57 = 569)
# 14 + 9 = 23   (777 + 317 = 2109)


import re

s = input()
m = []                                                   #создание массива для измененных чисел

if s.isalpha() == False:                                 #проверка на дураков
    chisla = re.findall("\d+", s)
    razdel_po_probelam = re.split(" ", s)

    for i in range(len(chisla)):                         #преобразование чисел с помощью функции и
        x = int(chisla[i])                               #записывание их в массив m
        m.append(4*x*x-7)

    index = 0
    for i in range(len(razdel_po_probelam)):
        if razdel_po_probelam[i].isdigit() == True:      #проверка, является ли подстрочка в razdel_po_probelam числом
            m_str = str(m[index])                        #превращение m в строки
            razdel_po_probelam[i] = m_str                #переписывание числа
            index += 1

    s1 = " ".join(razdel_po_probelam)                    #склеивание массив в строку по пробелам
    print(s1)
else:
    print("Ошибка. Введите число!")