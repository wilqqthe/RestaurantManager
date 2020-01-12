from abc import ABC

from tinydb import Query

from globalVariables import db


class BasePosition(ABC):
    totalPositions = 0

    def __init__(self, name, price):
        self.no = self.generateID()
        self.name = self.setName(name)
        self.price = self.setPrice(price)

    def __str__(self):
        return "name: {} \tprice: {}".format(self.name,
                                             self.price)

    def setPrice(Self, price):
        try:
            return int(price)
        except:
            print("Price must be numeric")

    def setName(self, name):
        return str(name).capitalize()

    def getVariables(self):
        return [attr for attr in dir(self)
                if not callable(getattr(self, attr))
                and not attr.startswith("_")
                and not attr.__eq__('totalPositions')]

    def returnClassAttributes(self):
        attributes = {}
        for attrName in self.getVariables():
            attributes[attrName] = self.__getattribute__(attrName)
        return attributes

    def upsertInDB(self):
        db.table(type(self).__name__).upsert(self.returnClassAttributes(), Query().no == self.no)

    def deleteAllFromDB(self):
        db.purge_table(type(self).__name__)

    def deleteFromDB(self):
        db.remove(Query().where("no" == '1'))
        print("removed")

    @classmethod
    def generateID(cls):
        cls.totalPositions += 1
        return cls.totalPositions
