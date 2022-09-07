# %%

import redis # импортируем библиотеку
import json

red = redis.Redis(
    host="localhost",     port=6379,)


# %%

red.set('key1', 'uuuuu')

# %%
red.get('key1')

# %%


dict1 = {'key1': 'value1', 'key2': 'value2'}  # создаём словарь для записи
# с помощью функции dumps() из модуля json превратим наш словарь в строчку
red.set('dict1', json.dumps(dict1))
# с помощью знакомой нам функции превращаем данные,
# полученные из кэша обратно в словарь
converted_dict = json.loads(red.get('dict1'))
print(type(converted_dict))  # убеждаемся, что мы получили действительно словарь
print(converted_dict)  # ну и выводим его содержание

# %%

red.delete('dict1')  # удаляются ключи с помощью метода .delete()
print(red.get('dict1'))

# %%


cont = True

while cont:
    action = input('action:\t')
    if action == 'write':
        name = input('name:\t')
        phone = input('phone:\t')
        red.set(name, phone)
    elif action == 'read':
        name = input('name:\t')
        phone = red.get(name)
        if phone:
            print(f'{name}\'s phone is {str(phone)}')
    elif action == 'delete':
        name = input('name:\t')
        phone = red.delete(name)
        if phone:
            print(f"{name}'s phone is deleted")
        else:
            print(f"Not found {name}")
    elif action == 'stop':
        break

# %%
