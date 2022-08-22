# %%

class ParentException(Exception):  # создаём пустой класс – исключения потомка, наследуемся от exception
    pass

 
class ChildException(ParentException):  # создаём пустой класс – исключение наследника, наследуемся от ParentException
    pass

 
try:
    raise ChildException("message")  # поднимаем исключение-наследник
except ParentException as e:  # ловим его родителя
    print(e)  # выводим информацию об исключении

# %%
# 3.2.5
class Square():
    def __init__(self, side):
        if side <= 0:
            raise NonPositiveDigitException
        self.side = side


class SquareFactory():
    @staticmethod
    def side_square(side):
        return Square(side)

class NonPositiveDigitException(ValueError):
    pass


# sq = SquareFactory.side_square(7)
sq = Square(-5)
print(sq)
print(sq.side)

# %%
