import os

from src.Table.Table import Table
from src.globalVariables.globalVariables import SimplyException
from src.menuPositions.Drink import Drink
from src.menuPositions.Food import Food
from src.order.Order import Order

drinkList, tablesList, foodList = list(), list(), list()


def orderFood():
    while True:
        print("Type 0 to exit")
        for i, food in enumerate(Food.loadElementsFromDB()):
            print("{}. {}".format(i + 1, food))
        try:
            menu = int(input("Your choose: ")) - 1
            if menu > len(Food.loadElementsFromDB()) - 1 or menu < 0: raise SimplyException("Value out of range")
            if menu < 0: return
        except SimplyException as ExceptionInfo:
            print(ExceptionInfo)
            return
        except:
            menu = 0
            print('Must be number 1-4')

        foodList.append(Food.loadElementsFromDB()[menu])


def orderDrinks():
    while True:
        print("Type 0 to exit")
        for i, drink in enumerate(Drink.loadElementsFromDB()):
            print("{}. {}".format(i + 1, drink))
        try:
            menu = int(input("Your choose: ")) - 1
            if menu > len(Drink.loadElementsFromDB()) - 1 or menu < 0: raise SimplyException("Value out of range")
            if menu < 0: return
        except SimplyException as ExceptionInfo:
            print(ExceptionInfo)
            return
        except:
            menu = 0
            print('Must be number 1-4')
        drinkList.append(Drink.loadElementsFromDB()[menu])

def chooseTable():
    while True:
        print("Type 0 to exit")
        for i, table in enumerate(Table.loadElementsFromDB()):
            print("{}. {}".format(i + 1, table))
        try:
            menu = int(input("Your choose: ")) - 1
            if menu > len(Table.loadElementsFromDB()) - 1 or menu < 0: raise SimplyException("Value out of range")
            if menu < 0: return
        except SimplyException as ExceptionInfo:
            print(ExceptionInfo)
            return
        except:
            menu = 0
            print('Must be number 1-4')

        tablesList.append(Table.loadElementsFromDB()[menu])

def takeAOrder():
    while True:
        os.system('cls')
        print("1. Food \n2. Drinks \n3. Table \n4. Save order\n5. Back")
        try:
            menu = int(input("Your choose: "))
        except:
            menu = 0
            print('Must be number 1-5')

        if menu == 1:
            orderFood()
        elif menu == 2:
            orderDrinks()
        elif menu == 3:
            chooseTable()
        elif menu == 4:
            break
        elif menu == 5:
            return
    try:
        Order.addToOrderList(Order(tablesList, foodList, drinkList))
        foodList.clear()
        drinkList.clear()
        tablesList.clear()
    except:
        print("Creating a new order failed!")


def removeOrder():
    if len(Drink.loadElementsFromDB()) == 0:
        print('There is no orders')
        return
    Order.printAllOrders()
    try:
        menu = int(input("Your choose: ")) - 1
        if menu > len(Drink.loadElementsFromDB()) - 1 or menu < 0: raise SimplyException("Value out of range")
    except SimplyException as ExceptionInfo:
        print(ExceptionInfo)
        return
    except:
        menu = 0
        print('Must be number')

    Order.removeFromOrderList(menu)


def orderMenu():
    while True:
        os.system('cls')
        print("1. Take a order \n2. Remove order\n3. Show all orders \n4. Back")
        try:
            menu = int(input("Your choose: "))
        except:
            menu = 0
            print('Must be number 1-4')

        if menu == 1:
            takeAOrder()
        elif menu == 2:
            removeOrder()
        elif menu == 3:
            Order.printAllOrders()
        elif menu == 4:
            return
