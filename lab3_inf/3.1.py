# 3 задание:
# 20 + 22 = 42   (1593 + 1929 = 7049)
# 15 + 17 - 29 = 3   (893 + 1149 - 3357 = 29)
# 24 - 8 = 16   (2297 - 249 = 1017)
# 3 * 4 = 12   (29 * 57 = 569)
# 14 + 9 = 23   (777 + 317 = 2109)


import re

s = input()
if s.isalpha() == False:
    chisla = re.findall("\d+", s)
    for i in range(len(chisla)):
        k=str(4 * (int(chisla[i])) * (int(chisla[i])) - 7)
        s=(re.sub(chisla[i], k, s))
    print(s)
else:
    print("Ошибка. Введите число!")