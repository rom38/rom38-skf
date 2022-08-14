# %%

class Rectangle:
    def __init__(self, x, y, width, heigth):
        self.x = x
        self.y = y
        self.width = width
        self.height = heigth

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    # Метод, рассчитывающий площадь
    def get_area(self):
        return self.width * self.height

    def __str__(self):
        return (f'Rectangle: x = {self.x}, y = {self.y},'
                f' width = {self.width}, height = {self.height}')
# %%


rec_1 = Rectangle(2, 3, 10, 20)
print(rec_1)
print(f'area = {rec_1.get_area()}')
# %%


class Client:
    def __init__(self, name, family, town, balance: int):
        self.name = name
        self.family = family
        self.town = town
        self.balance = balance

    def get_name(self):
        return self.name

    def get_family(self):
        return self.family

    def get_town(self):
        return self.town

    def get_balance(self):
        return self.balance

    def __str__(self):
        return (f'{self.name}, {self.family}. '
                f'{self.town}. Баланс: {self.balance} руб.')

    def get_client_corp(self):
        return (f'{self.name}, {self.family}. '
                f'{self.town}.')


cl_1 = Client('Ivan', 'Petrov', 'Moskva', 50)
cl_2 = Client('Sergey', 'Egorov', 'Irkutsk', 150)

print(cl_1)
print(cl_1.get_client_corp())

list_cust = [cl_1, cl_2]
print()
print([cust.get_client_corp() for cust in list_cust])


# %%
