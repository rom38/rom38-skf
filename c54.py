# %%

import requests  # импортируем наш знакомый модуль
import lxml.html
from lxml import etree


# получим html главной странички официального сайта python
html = requests.get('https://www.python.org/').content

tree = lxml.html.document_fromstring(html)
# забираем текст тега <title> из тега <head>,
# который лежит в свою очередь внутри тега <html>
# (в этом невидимом теге <head> у нас хранится
# основная информация о страничке. Её название
# и инструкции по отображению в браузере.
title = tree.xpath('/html/head/title/text()')

print(title)  # выводим полученный заголовок страницы
# %%

# создадим объект ElementTree. Он возвращается функцией parse()
# попытаемся спарсить наш файл с помощью html-парсера.
# Сам html - это то, что мы скачали и поместили в папку из браузера.
tree = etree.parse('index.html', lxml.html.HTMLParser())
# помещаем в аргумент метода findall скопированный xpath.
# Здесь мы получим все элементы списка новостей. (Все заголовки и их даты)
ul = tree.findall('/body/div/div[3]/div/section/div[2]/div[1]/div/ul/li')

# создаём цикл, в котором мы будем выводить название каждого элемента из списка
for li in ul:
    # в каждом элементе находим, где хранится заголовок новости.
    # У нас это тег <a>. Т. е. гиперссылка, на которую нужно нажать,
    # чтобы перейти на страницу с новостью. (Гиперссылки в html это всегда тэг <a>)
    # print(etree.tostring(li, pretty_print=True))
    a = li.find('a')
    # из этого тега забираем текст, это и будет нашим названием
    print(a.text)
# %%

html_1 = """<html>
 <head> <title> Some title </title> </head>
 <body>
  <tag1> some text
     <tag2> MY TEXT </tag2>
   </tag1>
 </body>
</html>"""

tree = lxml.html.document_fromstring(html_1)
tag_text = tree.xpath('/html/body/tag1/tag2/text()')
print(tag_text[0])

# %%


# создадим объект ElementTree. Он возвращается функцией parse()
# попытаемся спарсить наш файл с помощью html-парсера.
# Сам html - это то, что мы скачали и поместили в папку из браузера.
tree = etree.parse('index.html', lxml.html.HTMLParser())
# помещаем в аргумент метода findall скопированный xpath.
# Здесь мы получим все элементы списка новостей. (Все заголовки и их даты)
ul = tree.findall('/body/div/div[3]/div/section/div[2]/div[1]/div/ul/li')

# создаём цикл, в котором мы будем выводить название каждого элемента из списка
for li in ul:
    # в каждом элементе находим, где хранится заголовок новости.
    # У нас это тег <a>. Т. е. гиперссылка, на которую нужно нажать,
    # чтобы перейти на страницу с новостью. (Гиперссылки в html это всегда тэг <a>)
    # print(etree.tostring(li, pretty_print=True))
    a = li.find('a')
    time = li.find('time')
    print(f'Дата добавления {time.get("datetime")}, новость: {a.text}')
    # из этого тега забираем текст, это и будет нашим названием
    #print(a.text)
# %%
