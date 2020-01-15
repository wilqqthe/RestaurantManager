from abc import ABC, abstractmethod

from tinydb import where, Query

from src.generator.IdGenerator import IdGenerator
from src.globalVariables.globalVariables import db


class DBConnector(ABC):
    def __init__(self, no: int):
        if no == 0:
            self.no = IdGenerator.getGlobalId()
        else:
            self.no = no


    def getVariables(self):
        return [attr for attr in dir(self)
                if not callable(getattr(self, attr))
                and not attr.startswith("_")]

    def returnClassAttributes(self):
        attributes = {}
        for attrName in self.getVariables():
            attributes[attrName] = self.__getattribute__(attrName)
        return attributes

    def upsertInDB(self):
        db.table(type(self).__name__).upsert(self.returnClassAttributes(), Query().no == self.no)

    def deleteOwnTableFromDB(self):
        db.purge_table(type(self).__name__)

    def deleteFromDB(self):
        db.table(type(self).__name__).remove(where('no') == self.no)

    @classmethod
    @abstractmethod
    def loadElementsFromDB(cls):
        pass
