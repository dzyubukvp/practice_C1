class First:
    parametr_first = 'Статический аттрибут Принадлежит классу FIRST'

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

First.parametr_first = '+Переинициализировали+'
print(f"Обращение к {First.parametr_first}")

xyz = First(10, 20, 30)
xyz1 = First(3,2,1)
print(f"Обращение к классу First \n{xyz.__class__}\nполучаем динамические \nатрибуты X={xyz.x}, Y={xyz.y}, Z={xyz.z}")
print(f"Обращение к классу First \n{xyz1.__class__}\nполучаем динамические \nатрибуты X={xyz1.x}, Y={xyz1.y}, Z={xyz1.z}")