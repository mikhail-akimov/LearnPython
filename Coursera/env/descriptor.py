class Value:

    def __init__(self):
        self.total = None

    @staticmethod
    def __set_commission(value, commission):
        return value - (value * commission)

    def __set__(self, instance, value):
        self.total = self.__set_commission(value, instance.commission)

    def __get__(self, instance, owner):
        return self.total


class Account:
    amount = Value()

    def __init__(self, commission):
        self.commission = commission


boris = Account(0.1)
boris.amount = 100
print(boris.amount)
# petr = Account(0.5)
# petr.amount = 200
# print(petr.amount)
