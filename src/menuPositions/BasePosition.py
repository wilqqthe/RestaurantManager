from abc import ABC, abstractmethod

from src.db.DBConnector import DBConnector


class BasePosition(DBConnector, ABC):
    def __init__(self, name: str, price: float):
        super().__init__()
        self.name = self.setName(name)
        self.price = self.setPrice(price)

    def setPrice(Self, price):
        try:
            return format(float(price), '.2f')
        except:
            print("Price must be numeric")

    def setName(self, name):
        return str(name).capitalize()

    # def __del__(self):
    #     super().deleteFromDB()

    def printToOrder(self):
        return "Name: {:16}Price: {:>7}\n".format(self.name,
                                               self.price)

    @abstractmethod
    def __str__(self):
        pass
