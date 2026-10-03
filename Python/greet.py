class Greeter:
    def say_hello(self, name1, name2 = None):
        if name2 != None:
            print(f'Hello {name1} and {name2}')
        else:
            print(f'Hello {name1}')

name = Greeter()
name.say_hello('Someone1')
name.say_hello('Someone1', 'Someone2')