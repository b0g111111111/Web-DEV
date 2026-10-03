class car :
    brand =''
    price =''

    def setValues(self, b, p):
        self.brand = b
        self.price = p

    def showValues(self):
        print('Brand:', self.brand)
        print('Price:', self.price)

my_car = car()
my_car.setValues('Toyota', 20000)
my_car.showValues()
