# %%


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # создадим свойство human_age,
    # которое будет переводить возраст животного в человеческий
    # тот самый магический декоратор
    @property
    def human_age(self):
        return self.age * 7.3


jane = Dog("jane", 4)
# т.к. метод помечен декоратором property,
# то нам не надо вызывать этот метод чтобы получить результат
print(jane.human_age)
# %%


class Dog:
    _happiness = 10

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def human_age(self):
        return self.age * 7.3

    # добавим новое поле - шкала счастья
    @property
    def happiness(self):
        return self._happiness

    # с помощью декоратора setter мы можем неявно передать во второй 
    # аргумент значение, находящееся справа от равно, а не закидывать это 
    # значение в скобки, как мы это делали в модуле C1, когда не знали о 
    # декораторах класса 
    @happiness.setter
    # допустим, мы хотим, чтобы счастье питомца измерялось шкалой от 0 до 100
    def happiness(self, value):
        if value <= 100 and value >= 0:
            self._happiness = value
        else:
            raise ValueError("Happiness must be between 0 ... 100")


jane = Dog("jane", 4)
jane.happiness = 101  # осчастливим нашу собаку < :
print(jane.happiness)
# %%
# 2.3.4


class Square():
    _side = None

    def __init__(self, side):
        self.side = side

    @property
    def area(self):
        return self.side ** 2

    @property
    def side(self):
        return self._side

    @side.setter
    def side(self, side_1):
        if side_1 >= 0:
            self._side = side_1
        else:
            raise ValueError("Side must be >= 0")


class SquareFactory():
    @staticmethod
    def side_square(side):
        return Square(side)


# sq = SquareFactory.side_square(7)
sq = Square(9)

print(sq)
print(sq.area)
sq.side = 3
print(sq.side, sq.area)
# %%
