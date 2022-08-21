class ParentException(Exception):  # создаём пустой класс – исключения потомка, наследуемся от exception
    pass

 
class ChildException(ParentException):  # создаём пустой класс – исключение наследника, наследуемся от ParentException
    pass

 
try:
    raise ChildException("message")  # поднимаем исключение-наследник
except ParentException as e:  # ловим его родителя
    print(e)  # выводим информацию об исключении
