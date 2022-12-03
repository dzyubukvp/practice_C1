class Rectangle:
    def __init__(self, width, heigth):
        self.width = width
        self.height = heigth

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    # Метод, рассчитывающий площадь
    def get_area(self):
        return self.width * self.height
class Cat:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self. age = age
    def get_name(self):
        return self.name

    def get_gender(self):
        return self.gender

    def get_age(self):
        return self.age
class Dog(Cat):
    def get_pet(self):
        return f'{self.get_name()}   {self.get_age()}'