# %%
from Cat import Cat

sam = Cat("Сэм", "мальчик", 2)
print(f"Имя: {sam.get_name()}, Пол: {sam.get_sex()}, Возраст: {sam.get_age()} года")
# %%
from Cat import Dog

dog_1 = Dog("Мухтар", "мальчик", 0)
print(dog_1.get_pet())
# %%
