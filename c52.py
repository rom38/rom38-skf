# %%

import json
import requests

r = requests.get('https://baconipsum.com/api/?type=all-meat&paras=3&start-with-lorem=1&format=html')  # делаем запрос на сервер по переданному адресу
print(r.content)

# %%

r = requests.get('https://baconipsum.com/api/'
                '?type=all-meat&paras=3&'
                'start-with-lorem=1&format=html')
print(r.status_code)  # узнаем статус полученного ответа

# %%

r = requests.get('https://baconipsum.com/api/'
                '?type=meat-and-filler')  # попробуем поймать json-ответ
print(r.content)

# %%

r = requests.get('https://baconipsum.com/api/?type=meat-and-filler')
texts = json.loads(r.content)  # делаем из полученных байтов Python-объект для удобной работы
print(texts)
print(type(texts))  # проверяем тип сконвертированных данных

for text in texts:  # выводим полученный текст. Но для того чтобы он влез в консоль, оставим только первые 50 символов.
    print(text[:50], '\n')
# %%

r = requests.get('https://api.github.com')

print(r.content)

# %%

r = requests.get('https://api.github.com')

d = json.loads(r.content)  # делаем из полученных байтов Python-объект для удобной работы

print(type(d))
print(d['issues_url'])  # обращаемся к полученному объекту как к словарю и попробуем напечатать одно из его значений
# %%

# отправляем пост-запрос
r = requests.post('https://httpbin.org/post', data={'key': 'value'})
# содержимое ответа и его обработка происходит так же,
# как и с ГЕТ-запросами, разницы никакой нету
print(r.content)
# %%

data = {'key': 'value'}
# отправляем пост-запрос, но только в этот раз
# тип передаваемых данных будет JSON
r = requests.post('https://httpbin.org/post', json=json.dumps(data))
print(r.content)

# %%

r = requests.get('https://baconipsum.com/api/?type=meat-and-filler&paras=5')
# делаем из полученных байтов Python-объект для удобной работы
texts = json.loads(r.content)
print(texts[0])
print(type(texts))  # проверяем тип сконвертированных данных
# выводим полученный текст. Но для того чтобы он влез в консоль,
# оставим только первые 50 символов.
for text in texts:
    print(text[:50], '\n')
# %%
