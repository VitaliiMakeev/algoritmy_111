"""
Задание 3.
Определить количество различных (уникальных) подстрок
с использованием хеш-функции
Дана строка S длиной N, состоящая только из строчных латинских букв

Подсказка: вы должны в цикле для каждой подстроки вычислить хеш
Все хеши записываем во множество.
Оно отсечет дубли.

Экономия на размере хранимых данных (для длинных строк) и
скорость доступа вместе с уникальностью элементов,
которые даёт множество, сделают решение коротким и эффективным.

Пример:
рара - 6 уникальных подстрок

рар
ра
ар
ара
р
а
"""
import hashlib


def hesh_word(word):

    tmp = set()
    tmp_1 = set()
    for i in range(len(word)):
        for k in word:
            if k == word[i]:
                res = hashlib.sha256(k.encode()).hexdigest()
                tmp_1.add(k)
                tmp.add(res)
            else:
                st_1 = str(word[i] + k)
                res_1 = hashlib.sha256(st_1.encode()).hexdigest()
                tmp_1.add(word[i] + k)
                tmp.add(res_1)
        if word[-i:] == word or word[-i:] == '':
            continue
        else:
            res_2 = hashlib.sha256(word[:i].encode()).hexdigest()
            res_3 = hashlib.sha256(word[-i:].encode()).hexdigest()
            tmp_1.add(word[:i])
            tmp_1.add(word[-i:])
            tmp.add(res_2)
            tmp.add(res_3)
    print(f'{word} - {len(tmp)} уникальных подстрок\n')
    for l in tmp_1:
        print(l)


hesh_word('mama')