# %%
class Rectangle:
    def __init__(self,a,b):
        self.a = a
        self.b = b		  
    def get_area(self):		
        return self.a * self.b
        
    def __eq__(self,other):
        return self.a==other.a and self.b==other.b
		
class Square:
    def __init__(self,a):
        self.a = a
    def get_area_square(self):		
        return self.a ** 2 

rect_1 = Rectangle(3,4)
rect_2 = Rectangle(12,5)
rect_3 = Rectangle(3,4)
print(f'compare area r1 and r2: {rect_1 == rect_2}') 

print(f'compare area r1 and r3: {rect_1 == rect_3}') 
#вывод площади наших двух прямоугольников
print(rect_1.get_area())
print(rect_2.get_area())

square_1 = Square(5)
square_2 = Square(10)

print(square_1.get_area_square(),
      square_2.get_area_square())
	  
figures = [rect_1, rect_2, square_1, square_2]

for figure in figures:
    if isinstance (figure, Square):
        print(figure.get_area_square())
    else:
    	print(figure.get_area())

print('dot')

# %%
class Dot:
    def __init__(self,x,y):
       self.x=x
       self.y=y
    def __eq__(self,other):
        return self.x==other.x and self.y==other.y
    def __str__(self):
        return f'Dot: {self.x,self.y}'

p1=Dot(1,2)
p2=Dot(1,2)
print(p1==p2)
print(str(p1))
print(p2)


print('circle')




# %%
class Dot:
    def __init__(self,x,y):
       self.x=x
       self.y=y
    def __eq__(self,other):
        return self.x==other.x and self.y==other.y
    def __str__(self):
        return f'Dot: {self.x,self.y}'

p1=Dot(1,2)
p2=Dot(1,2)
print(p1==p2)
print(str(p1))
print(p2)

print('circle')

class Circle:
    def __init__(self,rad):
        self.rad = rad
    def get_area_circ(self):		
        return 3.14*self.rad ** 2 

cirk_1 = Circle(5)
print(cirk_1.get_area_circ())

