from tinydb import TinyDB, where

db = TinyDB('db.json')

tables = db.table("Tables")

tableArray = []

class Table:

    tableCounter = 0

    def __init__(self, seats, mode="manual"):
        self.tableNo = self.generateTableNo()
        self.occupied = False
        self.seats = seats
        self.insertToDB()
        if mode == "manual":
            tableArray.append(self)

    def setOccupation(self):
        self.occupied = not self.occupied

    def getOccupation(self):
        return self.occupied

    def insertToDB(self):
        if tables.contains(where('No') == self.tableNo):
            print("Table with that number - {} exists in database.".format(self.tableNo))
        else:
            tables.insert({"No": self.tableNo, "Seats": self.seats})
            print("Table no. {} has been created.".format(self.tableNo))

    # def deleteFromDB(self):
    #     tables.insert({"No": self.tableNo, "Seats": self.seats})

    @classmethod
    def generateTableNo(cls):
        cls.tableCounter += 1
        return cls.tableCounter

    @classmethod
    def listOccupiedTables(cls):
        for x in tableArray:
            if x.occupied:
                print("Table no. {}".format(x.tableNo))

    @classmethod
    def listFreeTables(cls):
        for x in tableArray:
            if not x.occupied:
                print("Table no. {}".format(x.tableNo))

    @classmethod
    def loadTablesFromDB(cls):
        if len(tables) == 0:
            print("No entries for tables in Database")
        else:
            if len(tableArray) == 0:
                for x in tables:
                    tableArray.append(Table(x["Seats"], "db"))

                print("{} tables has been loaded".format(len(tables)))

    @classmethod
    def printTables(cls):
        for x in tableArray:
            print("Table No: " + str(x.tableNo) + "  Number of seats: " + str(x.seats) + "  Occupied? : " + str(
                x.occupied))
