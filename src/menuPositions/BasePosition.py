from abc import ABC, abstractmethod

from src.db.dbConnector import dbConnector


class BasePosition(dbConnector, ABC):
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

    def __del__(self):
        super().deleteFromDB()

    @abstractmethod
    def __str__(self):
        pass
