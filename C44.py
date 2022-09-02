# %%
def p(n):
    n -=1
    if n == 0:
        return n
    return n+p(n)

p(11)

# %%
print(54)

# %%

def p(n):
    if n == 0:
        return
    else:
        p(n-1)
        print(n)
p(5)
# %%

def par_checker(string):
    stack = []  # инициализируем стек

    for s in string:  # читаем строку посимвольно
        if s == "(":  # если открывающая скобка,
            stack.append(s)  # добавляем ее в стек
        elif s == ")":
            # если встретилась закрывающая скобка, то проверяем
            # пуст ли стек и является ли верхний элемент - открывающей скобкой
            if len(stack) > 0 and stack[-1] == "(":
                stack.pop()  # удаляем из стека
            else:  # иначе завершаем функцию с False
                return False
    # если стек пустой, то незакрытых скобок не осталось
    # значит возвращаем True, иначе - False
    return len(stack) == 0
# %%
par_checker("(5+6)*(7+8)/(4+3))")
# %%
def par_checker(string):
    stack = {}  # инициализируем стек

    for s in string:  # читаем строку посимвольно
        if s == "("  # если открывающая скобка,
            stac[")"] = s  # добавляем ее в стек
        elif s == ")":
            # если встретилась закрывающая скобка, то проверяем
            # пуст ли стек и является ли верхний элемент - открывающей скобкой
            if len(stack)  and stack[-1] == "(":
                stack.pop()  # удаляем из стека
            else:  # иначе завершаем функцию с False
                return False
    # если стек пустой, то незакрытых скобок не осталось
    # значит возвращаем True, иначе - False
    return len(stack) == 0
# %%
pars = {")" : "(", "]" : "["}

def par_checker_mod(string):
    stack = []

    for s in string:
        if s in "([":
            stack.append(s)
        elif s in ")]":
            if len(stack) > 0 and stack[-1] == pars[s]:
                stack.pop()
            else:
                return False
    return len(stack) == 0

par_checker_mod("[(5+6)*[7+8]]/(4+3)")


# %%
from typing import Union
# Создадим класс Queue - нужная нам очередь
class Queue:
    tasks: list[Union[str, None]]
    # Конструктор нашего класса, в нём происходит нужная инициализация объекта
    def __init__(self, max_size):
        self.max_size = max_size  # размер очереди
        self.task_num = 0  # будем хранить сквозной номер задачи

        self.tasks = [0 for _ in range(self.max_size)]  # инициализируем список с нулевыми элементами
        self.head = 0  # указатель на начало очереди
        self.tail = 0  # указатель на элемент следующий за концом очереди

    # !!! Класс далее нужно дополнить методами !!!
    def is_empty(self):
        return self.head == self.tail and self.tasks[self.head] == 0

    def size(self):
        if self.head == self.tail and self.tasks[self.head] == 0:
            return 0
        elif self.head == self.tail and self.tasks[self.head] != 0:
            return self.max_size
        elif self.head < self.tail:
            return self.tail - self.head
        elif self.head > self.tail:
            return self.tail + self.max_size - self.head

    def add(self):
        self.task_num += 1
        self.tasks[self.tail] = f"Задача №{self.task_num}"
        self.tail += 1
        if self.tail >= self.max_size:
            self.tail = 0
        print(f'Задача №{self.task_num} добавлена')

    def show(self):
        print(f'{self.tasks[self.head]} в приоритете')

    def do(self):
        print(f'{self.tasks[self.head]} выполнена')
        self.tasks[self.head] = 0
        self.head = (self.head + 1) % self.max_size


# Используем класс
size = int(input("Определите размер очереди: "))
q = Queue(size)

while True:
    cmd = input("Введите команду:")
    if cmd == "empty":
        if q.is_empty():
            print("Очередь пустая")
        else:
            print("В очереди есть задачи")
    elif cmd == "size":
        print("Количество задач в очереди:", q.size())
    elif cmd == "add":
        if q.size() != q.max_size:
            q.add()
        else:
            print("Очередь переполнена")
    elif cmd == "show":
        if q.is_empty():
            print("Очередь пустая")
        else:
            q.show()
    elif cmd == "do":
        if q.is_empty():
            print("Очередь пустая")
        else:
            q.do()
    elif cmd == "exit":
        for _ in range(q.size()):
            q.do()
        print("Очередь пустая. Завершение работы")
        break
    else:
        print("Введена неверная команда")

# %%
