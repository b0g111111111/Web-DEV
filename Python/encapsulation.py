class BankAcc:
    def __init__(self, owner, pin, balance):
        self.owner = owner
        self._pin = pin 
        self.__balance = balance 

    def get_balance(self):
        return self.__balance

my_account = BankAcc('Rahim', '122334', '2222222')

print(f'Account owner:{my_account.owner}')
print(f'Pin : {my_account._pin}')
print(f'Balance : {my_account.get_balance()}TK')