# В проекте «Дом питомца» добавим новую услугу — электронный кошелек.
# Необходимо создать класс «Клиент», который будет содержать данные о
# клиентах и их финансовых операциях. О клиенте известна следующая
# информация: имя, фамилия, город, баланс.
# «Иван Петров. Москва. Баланс: 50 руб.»

class Customers:
    def __init__(self, first_name, second_name, city, balance):
        self.first_name = first_name
        self.second_name = second_name
        self.balance = balance
        self.city = city

    def __str__(self):
        return f'''"{self.first_name} {self.second_name}". {self.city}. Баланс: {self.balance} руб.'''

    # создайте список, в который будут добавлены все клиенты, и выведете его в консоль.
    def get_guest(self):
        return f'{self.first_name} {self.second_name},г. {self.city}'


customer_1 = Customers('Иван', 'Петров', 'Москва', 50)
customer_2 = Customers('Сидор', 'Захаров', 'Урюпинск', 5590)
customer_3 = Customers('Иосиф', 'Плейшнер', 'Задрищинск', 1540)

guest_list = [customer_1, customer_2, customer_3]
for guest in guest_list:
    print(guest.get_guest())

for guest in guest_list:
    print(guest)