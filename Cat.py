class Cat:
    def __init__(self, name, sex, age):
        self.name = name
        self.sex = sex
        self.age = age

    def get_name(self):
        return self.name

    def get_sex(self):
        return self.sex

    def get_age(self):
        return self.age


class Dog(Cat):
    def get_pet(self):
        return self.get_name(), self.get_age()  
