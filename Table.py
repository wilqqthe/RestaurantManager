tableArray = []


class Table:
    tableCounter = 0

    def __init__(self):
        self.tableNo = self.generateTableNo()
        tableArray.append(self)
        self.occupied = False

    def setOccupation(self):
        self.occupied = not self.occupied

    def getOccupation(self):
        return self.occupied

    @classmethod
    def generateTableNo(cls):
        cls.tableCounter += 1
        return cls.tableCounter

    @classmethod
    def listTables(cls):
        for x in tableArray:
            print("Table no. {}".format(x.tableNo))

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


table1 = Table()
table2 = Table()
table3 = Table()
table4 = Table()
table5 = Table()
table6 = Table()

table4.occupied = True
table6.occupied = True

print("All tables")
Table.listTables()
print("All free tables")
Table.listFreeTables()


# test 