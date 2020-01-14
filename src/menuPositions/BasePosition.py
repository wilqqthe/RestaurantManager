from abc import ABC, abstractmethod

from src.db.DBConnector import DBConnector


class BasePosition(DBConnector, ABC):
    def __init__(self, name: str, price: float, tax_rate: int):
        super().__init__()
        self.name = self.setName(name)
        self.nettoPrice = self.setPrice(price)
        self.tax_rate = self.setTaxRate(tax_rate)

    def setPrice(Self, price):
        try:
            return float(format(price, '.2f'))
        except:
            print("Price must be numeric")

    def setName(self, name):
        return str(name).capitalize()

    def setTaxRate(self, value):
        if value > 100:
            return int(100)
        elif value < 0:
            return int(0)
        else:
            return round(value)

    def getNettoPrice(self):
        return self.nettoPrice

    def calculateBruttoPrice(self, amount=1):
        return format((self.nettoPrice + (self.nettoPrice * self.tax_rate )/ 100) * amount, '.2f')

    def printToOrder(self):
        return "Name: {:16}Price: {:>7}\n".format(self.name,
                                                  self.nettoPrice)

    def printToBill(self, ):
        return "Name: {:16}{:>7}{:>7}{:>7}\n".format(self.name,
                                                     self.getNettoPrice(),
                                                     self.tax_rate,
                                                     self.nettoPrice)

    @abstractmethod
    def __str__(self):
        pass
