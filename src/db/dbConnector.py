from abc import ABC

from tinydb import where, Query

from src.generator.globalIdGenerator import GlobalIdGenerator
from src.globalVariables import db, no


class dbConnector(ABC):
    def __init__(self):
        self.no = GlobalIdGenerator.getId()

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
        db.table(type(self).__name__).remove(where(no) == self.no)

