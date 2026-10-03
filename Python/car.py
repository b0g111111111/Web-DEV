class Vehicle :
    def speed_limit(self):
        print('A normal vehicle has a max speed of 100 km/h.')

class SportCar(Vehicle):
    def speed_limit(self):
        print('A sports car has a max speed of 350 km/h.')

my_car = SportCar()
my_car.speed_limit()