from abc import ABC

from src.db.DBConnector import DBConnector
from src.generator.IdGenerator import IdGenerator
from src.globalVariables.globalVariables import db, SimplyException


class Table(DBConnector, ABC):
    def __init__(self, seats: int, tableNo: int = 0,  no: int = 0):
        super().__init__(no)
        if tableNo == 0 : self.tableNo = IdGenerator.getTableNo()
        else: self.tableNo = tableNo
        self.occupied = False
        self.seats = seats

    def setOccupation(self):
        self.occupied = not self.occupied

    def __str__(self):
        return "Table No: {:<5} Number of seats {:<5} Occupied?{:2}".format(self.tableNo,
                                                                            self.seats,
                                                                            self.occupied)

    @classmethod
    def loadElementsFromDB(cls):
        tables = []
        if len(db.table("Table")) == 0:
            print("No entries for food positions in Database")
        else:
            for position in db.table("Table"):
                tables.append(Table(position["seats"],
                                    position["tableNo"],
                                    position["no"]))
        return tables

    @classmethod
    def listFreeTables(cls):
        for table in Table.loadElementsFromDB():
            if not table.occupied:
                print(table)

    @classmethod
    def listOccupiedTables(cls):
        for table in Table.loadElementsFromDB():
            if table.occupied:
                print(table)

    @classmethod
    def prepareAndCreateNew(cls):
        try:
            seats = int(input('Seats 1 - 12: '))
            if seats < 0 or seats > 12: raise SimplyException("Value out of range")
        except SimplyException as ExceptionInfo:
            print(ExceptionInfo)
            return
        except:
            print('Value must be numeric')
            print('Between 1 - 12')
            return
        return Table(seats)
