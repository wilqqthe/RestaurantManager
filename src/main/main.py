import os
import sys

from src.Table.tableMenuOperations import tableMenu
from src.menuPositions.menuOperations import editMenuPositions

menuCategories = "1. Add tables\n2. Edit menu positions\n3. Work day\n4. EXIT"

while True:
    os.system('cls')
    print(menuCategories)
    try:
        menu = int(input("Your choose: "))
    except:
        menu = 0
        print('Must be number 1-4')

    if menu == 1:
        tableMenu()
    elif menu == 2:
        editMenuPositions()
    elif menu == 3:
        pass
    elif menu == 4:
        sys.exit()
