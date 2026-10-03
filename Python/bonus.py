class Manager:
    def get_bonus(self):
        return 'Manager bonus is 5000 tk'

class Developer:
    def get_bonus(self):
        return 'Developer bonus is 3000 tk'

def show_bonus(employee_bonus):
    print(employee_bonus.get_bonus())

manager = Manager()
developer = Developer()

print('Bonus:')
show_bonus(manager)
show_bonus(developer)