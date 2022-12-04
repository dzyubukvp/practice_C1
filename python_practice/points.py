# class Dot:
#    def __init__(self,x,y):
#        self.x=x
#        self.y=y
#
#    def __eq__(self, other):
#        return self.x == other.x and self.y == other.y
#
#    def __str__(self):
#        return f'Dot: {self.x, self.y}'
#
# p1=Dot(1,2)
# p2=Dot(1,2)
# print(p1==p2)
# print(str(p1))
# print(p2)

class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_area(self):
        return self.a * self.b

    # Добавьте в класс Rectangle
    # перегрузку оператора == и
    # сравните несколько экземпляров одного класса.

    def __eq__(self, other):
        return self.a == other.a and self.b == other.b


class Square:
    def __init__(self, a):
        self.a = a

    def get_area_square(self):
        return self.a ** 2


class Circle:
    def __init__(self, a):
        self.a = a

    def get_area_circle(self):
        return (self.a ** 2) * 3.14


rect_1 = Rectangle(3, 4)
rect_2 = Rectangle(12, 5)
square_1 = Square(5)
square_2 = Square(10)
circle_1 = Circle(1)
circle_2 = Circle(2)

figures = [rect_1, rect_2, square_1, square_2, circle_1, circle_2]
for figure in figures:
    if isinstance(figure, Square):
        print(figure.get_area_square())
    elif isinstance(figure, Rectangle):
        print(figure.get_area())
    else:
        print(figure.get_area_circle())


print(rect_1==rect_2)
