class Smartphone:
    brand = ''
    price = ''
    def setDetails(self, brand, price):
        self.brand = brand
        self.price = price

    def showDetails(self):
        print(f'Smartphone Details - Brand: {self.brand} , Price : {self.price} BDT')

phone1 = Smartphone()
phone2 = Smartphone()

phone1.setDetails('Samsung', 85000)
phone2.setDetails('Apple', 120000)

phone1.showDetails()
phone2.showDetails()

