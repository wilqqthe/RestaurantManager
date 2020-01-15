import os

from src.Table.Table import Table
from src.globalVariables.globalVariables import SimplyException


def deleteTable():
    tableList = Table.loadElementsFromDB()
    for i, table in enumerate(tableList):
        print("{}. {}".format(i + 1, table))
    try:
        positionNumber = int(input("Type position number to delete: "))
        if positionNumber > len(tableList) or positionNumber < 0: raise SimplyException("Value out of range")
    except SimplyException as ExceptionInfo:
        print(ExceptionInfo)
        return
    except:
        print('Value must be numeric')
        print('Editing failed')
        return
    tableList[positionNumber - 1].deleteFromDB()


def tableMenu():
    while True:
        os.system('cls')
        print("1. Add new table\n2. Delete table\n3. Show all\n4. EXIT")
        try:
            menu = int(input("Your choose: "))
        except:
            menu = 0
            print('Must be number 1-4')

        if menu == 1:
            try:
                Table.prepareAndCreateNew().upsertInDB()
                print("Successful!")
            except:
                print("Creating new table failed")
        elif menu == 2:
            deleteTable()
        elif menu == 3:
            Table.listOccupiedTables()
            Table.listFreeTables()
        elif menu == 4:
            return 0

