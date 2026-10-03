from abc import ABC , abstractmethod

class Payment (ABC):
    @abstractmethod
    def pay(self):
        pass

class Cashpayment (Payment):
    def pay(self):
        print(' Paid using cash. ')

class Cardpayment (Payment):
    def pay(self):
        print(' Paid using card. ')

cash = Cashpayment()
card = Cardpayment()
cash.pay()
card.pay()