class Light:
    def turn_on(self):
        return 'Light is now ON . Room is bright'

class Fan:
    def turn_on(self):
        return 'Fan is spinning at speed 3'

class AC:
    def turn_on(self):
        return 'AC is started . Temp set to 24c'

def activate(device):
    print (device.turn_on)

my_fan = Fan()
my_light = Light()
my_ac = AC()

print('Activation Smart Home Devices')
activate(my_fan)
activate(my_ac)
activate(my_light)