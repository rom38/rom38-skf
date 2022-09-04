# %%
from pprint import pprint


G = {"Адмиралтейская":
     ["Садовая"],
     "Садовая":
         ["Сенная площадь",
          "Спасская",
          "Адмиралтейская",
          "Звенигородская"],
     "Сенная площадь":
         ["Садовая",
          "Спасская"],
     "Спасская":
         ["Садовая",
          "Сенная площадь",
          "Достоевская"],
     "Звенигородская":
         ["Пушкинская",
          "Садовая"],
     "Пушкинская":
         ["Звенигородская",
          "Владимирская"],
     "Владимирская":
         ["Достоевская",
          "Пушкинская"],
     "Достоевская":
         ["Владимирская",
          "Спасская"]}

G = {"Адмиралтейская":
      {"Садовая": 4},
      "Садовая":
      {"Сенная площадь": 4,
          "Спасская": 3,
          "Адмиралтейская": 4,
          "Звенигородская": 5},
      "Сенная площадь":
      {"Садовая": 4,
          "Спасская": 4},
      "Спасская":
      {"Садовая": 3,
          "Сенная площадь": 4,
          "Достоевская": 6},
      "Звенигородская":
      {"Пушкинская": 3,
          "Садовая": 5},
      "Пушкинская":
      {"Звенигородская": 3,
          "Владимирская": 4},
      "Владимирская":
      {"Достоевская": 3,
          "Пушкинская": 4},
      "Достоевская":
      {"Владимирская": 3,
          "Спасская": 6}}

# %%

D = {k : 100 for k in G.keys()}  # расстояния
P = {k : None for k in G.keys()}

start_k = 'Адмиралтейская'  # стартовая вершина
D[start_k] = 0  # расстояние от нее до самой себя равно нулю
U = {k : False for k in G.keys()}  # флаги просмотра вершин

for _ in range(len(D)):
    # выбираем среди непросмотренных наименьшее по расстоянию
    min_k = min([k for k in U.keys() if not U[k]], key=lambda x: D[x])

    for v in G[min_k].keys():  # проходимся по всем смежным вершинам
        if D[v] > D[min_k] + G[min_k][v]:  # если расстояние от текущей вершины меньше
            D[v] = D[min_k] + G[min_k][v]  # то фиксируем его
            P[v] = min_k  # и записываем как предок
        U[min_k]=True

pprint(D)
pprint(P)
# %%
pointer = 'Владимирская'  # куда должны прийти
path = [] # список с вершинами пути
while pointer is not None:  # перемещаемся, пока не придём в стартовую точку
    path.append(pointer)
    pointer = P[pointer]

path.reverse()  # разворачиваем путь
for v in path:
    print(v)
# %%


class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

    def insert_left(self, next_value):
        if self.left_child is None:
            self.left_child = BinaryTree(next_value)
        else:
            new_child = BinaryTree(next_value)
            new_child.left_child = self.left_child
            self.left_child = new_child
        return self

    def insert_right(self, next_value):
        if self.right_child is None:
            self.right_child = BinaryTree(next_value)
        else:
            new_child = BinaryTree(next_value)
            new_child.right_child = self.right_child
            self.right_child = new_child
        return self

    def pre_order(self):
        print(self.value)  # процедура обработки

        if self.left_child is not None:  # если левый потомок существует
            self.left_child.pre_order()  # рекурсивно вызываем функцию

        if self.right_child is not None:  # если правый потомок существует
            self.right_child.pre_order()  # рекурсивно вызываем функцию

    def post_order(self):
        if self.left_child is not None:  # если левый потомок существует
            self.left_child.post_order()  # рекурсивно вызываем функцию

        if self.right_child is not None:  # если правый потомок существует
            self.right_child.post_order()  # рекурсивно вызываем функцию

        print(self.value)  # процедура обработки

    def in_order(self):
        if self.left_child is not None:  # если левый потомок существует
            self.left_child.in_order()  # рекурсивно вызываем функцию

        print(self.value)  # процедура обработки

        if self.right_child is not None:  # если правый потомок существует
            self.right_child.in_order()  # рекурсивно вызываем функцию
# %%
two_node = BinaryTree('2').insert_left('7').insert_right('5')
seven_node = two_node.left_child.insert_left('2').insert_right('6')
six_node = seven_node.right_child.insert_left('5').insert_right('11')
five_node = two_node.right_child.insert_right('9').right_child.insert_left('4')

two_node.pre_order()
print()
two_node.post_order()
print()
two_node.in_order()

#  print(two_node)
# %%
