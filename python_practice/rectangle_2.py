# Создайте метод, который возвращает атрибуты прямоугольника
# как строку ( постарайтесь применить магический метод __str__).
# Для объекта прямоугольника со значениями атрибута
# x = 5, y = 10, width = 50, height = 100 метод должен вернуть строку
# Rectangle : 5, 10, 50, 100.

class Rectangle:
    def __init__(self, x,y, width,heigth):
        self.x = x
        self.y = y
        self.width=width
        self.heigth=heigth

    # Создаем метод, который возвращает атрибуты прямоугольника как строку
    def __str__(self):
        return f'В квадрате: \nХ = {self.x} У = {self.y} \nШирина {self.width} Высота {self.heigth}'

    # Метод расчета площади фигуры
    def get_area(self):
        return self.width*self.heigth


r1 = Rectangle(5,10,50,100)
print(r1)
print(f'Площадь фигуры = {r1.get_area()} кв. ед.')