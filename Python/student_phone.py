class Smartphone:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def display_info (self):
        print(f'Smartphone Details - Brand : {self.brand} Price : {self.price} BDT')

class GamingPhone(Smartphone):
        def __init__(self, brand, price, cooling_system):
            super().__init__(brand, price)
            self.cooling_system = cooling_system

        def display_gamingphone_info(self):
            print(f'Cooling System : {self.cooling_system}')


student_gamingPhone = GamingPhone('ASUS ROG', 100000, 'GameCool 9')
student_gamingPhone.display_info()
student_gamingPhone.display_gamingphone_info()