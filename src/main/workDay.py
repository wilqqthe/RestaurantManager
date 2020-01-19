import os

from src.Table.Table import Table
from src.order.OrderMenu import orderMenu
from src.payment.paymentMenu import paymentMenu


def occupyOrResloveTable():
    tableList = Table.loadElementsFromDB('ALL')
    for i, table in enumerate(tableList):
        print("{}. {}".format(i + 1, table))
    print("Type number of table: ")
    try:
        menu = int(input("Your choose: ")) - 1
    except:
        menu = 0
        print('Must be number: ')

    try:
        tableList[menu].setOccupation()
        print(tableList[menu])
        tableList[menu].upsertInDB()
    except:
        print("Out of range")


def workDay():
    while True:
        os.system('cls')
        print("1. Occupy/Reslove table \n2. Take a order\n3. Payment\n4. Back")
        try:
            menu = int(input("Your choose: "))
        except:
            menu = 0
            print('Must be number 1-4')

        if menu == 1:
            occupyOrResloveTable()
        elif menu == 2:
            orderMenu()
        elif menu == 3:
            paymentMenu()
        elif menu == 4:
            return
