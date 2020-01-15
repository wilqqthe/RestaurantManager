import os

from src.globalVariables.globalVariables import SimplyException
from src.menuPositions.Drink import Drink
from src.menuPositions.Food import Food


def editFoodPositions():
    os.system('cls')
    print("1. Add new\n2. Edit existing\n3. Delete\n4. EXIT")
    try:
        menu = int(input("Your choose: "))
    except:
        menu = 0
        print('Must be number 1-4')

    if menu == 1:
        try:
            Food.prepareAndCreateNew().upsertInDB()
            print("Successful!")
        except:
            print("Creating new food position failed")
    elif menu == 2:
        for i, position in enumerate(Food.loadElementsFromDB()):
            print("{}. {}".format(i + 1, position))
        try:
            positionNumber = int(input("Type position number to edit: "))
            if positionNumber > len(Food.loadElementsFromDB()) or positionNumber < 0: raise print("Value out of range")
        except:
            print('Value must be numeric')
            print('Editing failed')
            return
        try:
            Food.prepareAndCreateNew(Food.loadElementsFromDB()[positionNumber - 1].no).upsertInDB()
            print("Successful!")
        except:
            print("Editing new food position failed")
    elif menu == 3:
        foodList = Food.loadElementsFromDB()
        for i, position in enumerate(foodList):
            print("{}. {}".format(i + 1, position))
        try:
            positionNumber = int(input("Type position number to delete: "))
            if positionNumber > len(foodList) or positionNumber < 0: raise print("Value out of range")
        except:
            print('Value must be numeric')
            print('Editing failed')
            return
        foodList[positionNumber - 1].deleteFromDB()
    elif menu == 4:
        return 0


def editDrinkPositions():
    os.system('cls')
    print("1. Add new\n2. Edit existing\n3. Delete\n4. EXIT")
    try:
        menu = int(input("Your choose: "))
    except:
        menu = 0
        print('Must be number 1-4')

    if menu == 1:
        try:
            Drink.prepareAndCreateNew().upsertInDB()
            print("Successful!")
        except:
            print("Creating new food position failed")
    elif menu == 2:
        for i, position in enumerate(Drink.loadElementsFromDB()):
            print("{}. {}".format(i + 1, position))
        try:
            positionNumber = int(input("Type position number to edit: "))
            if positionNumber > len(Drink.loadElementsFromDB()) or positionNumber < 0: raise SimplyException(
                "Value out of range")
        except SimplyException as ExceptionInfo:
            print(ExceptionInfo)
            return
        except:
            print('Value must be numeric')
            print('Editing failed')
            return
        try:
            Drink.prepareAndCreateNew(Drink.loadElementsFromDB()[positionNumber - 1].no).upsertInDB()
            print("Successful!")
        except:
            print("Editing new food position failed")
    elif menu == 3:
        drinkList = Drink.loadElementsFromDB()
        for i, position in enumerate(drinkList):
            print("{}. {}".format(i + 1, position))
        try:
            positionNumber = int(input("Type position number to delete: "))
            if positionNumber > len(drinkList) or positionNumber < 0: raise SimplyException("Value out of range")
        except SimplyException as ExceptionInfo:
            print(ExceptionInfo)
            return
        except:
            print('Value must be numeric')
            print('Editing failed')
            return
        drinkList[positionNumber - 1].deleteFromDB()
    elif menu == 4:
        return 0


def showAllPositions():
    for position in Food.loadElementsFromDB() + Drink.loadElementsFromDB():
        print(position)


def editMenuPositions():
    while True:
        os.system('cls')
        print("1. Edit/delete food\n2. Edit/delete drinks\n3. Show all\n4. EXIT")
        try:
            menu = int(input("Your choose: "))
        except:
            menu = 0
            print('Must be number 1-4')

        if menu == 1:
            editFoodPositions()
        elif menu == 2:
            editDrinkPositions()
        elif menu == 3:
            showAllPositions()
        elif menu == 4:
            return 0
