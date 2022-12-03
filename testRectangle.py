from oop1 import Cat
from oop1 import Dog

r1 = Cat('Вася', 'Мальчик', '3')
r2 = Cat('Дуся', 'сучка', '2')
dog1 = Dog('Bob','boy', 2)
#print("r1.width =", r1.width)
#print("r1.height =", r1.height)
#print("r1.get_width =", r1.get_width())
#print("r1.get_height =", r1.get_height())
#print("r1.get_area =", r1.get_area())

#print("r2.width =", r2.width)
#print("r2.height =", r2.height)
#print("r2.get_width =", r2.get_width())
#print("r2.get_height =", r2.get_height())
#print("r2.get_area =", r2.get_area())

print(f'Кот {r1.get_age()} годичного возраста {r1.get_gender()} зовут {r1.get_name()}')
print(f'Кот {r2.get_age()} годичного возраста {r2.get_gender()} зовут {r2.get_name()}')
print(dog1.get_pet())
