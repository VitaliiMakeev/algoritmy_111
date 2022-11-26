"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница или нет
есть ли в кэше соответствующая страница или нет

Пример кэша: {'url-адрес': 'хеш url-а'; 'url-адрес': 'хеш url-а'; ...}

Если страница в кэше есть, просто вернуть значение хеша, например, 'хеш url-а'
Если страницы в кэше нет, то вычислить хеш и записать в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
и одного из алгоритмов, например, sha512
Можете усложнить задачу, реализовав ее через ООП
"""
import hashlib
import json


def kesh_url(url):
    salt = 'my_salt_2'
    tmp = {}
    with open('data_url.json', 'r+') as f:
        reed = f.read()
        if url in reed:
            res = hashlib.sha512(salt.encode() + url.encode()).hexdigest()
            return res
        else:
            res = hashlib.sha512(salt.encode() + url.encode()).hexdigest()
            tmp[url] = res
            json.dump(tmp, f)
            f.write('\n')
            return 'Записано!'


print(kesh_url('https://translated.turbopages.org/proxy_u/en-ru.ru.e9457836-6381a068-c826c66f-74722d776562/https/stackoverflow.com/questions/2424000/read-and-overwrite-a-file-in-python'))







# -----------------------------------------------------------------------------------------------------
# Это я создал и добавил в файл один пример (ссылку: хеш ссылки), для тренировки (вспоминаю основы).
# import json
#
# salt = 'my_salt_2'
# url_1 = 'https://www.yandex.ru'
# hesh_1 = hashlib.sha512(salt.encode() + url_1.encode()).hexdigest()
# data = {}
# with open('data_url.json', 'w') as f:
#     f.seek(0)
#     data[url_1] = hesh_1
#     json.dump(data, f)
#     f.write('\n')
