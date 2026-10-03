class Calculator:
    def add (self, a, b, c = None):
        if c != None:
            print(f'Sum of 3 numbers : {a + b + c}')
        else:
            print(f'Sum of 2 numbers : {a + b}')

my_cal = Calculator()
my_cal.add(10, 20)
my_cal.add(10, 20, 50)