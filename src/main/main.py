import os
import sys

from src.Table.tableMenuOperations import tableMenu
from src.main.workDay import workDay
from src.menuPositions.menuOperations import editMenuPositions
from src.payment.cash import Cash

categories = "1. Add tables\n2. Edit menu positions\n3. Orders Menu\n4. Sum and close this day\n5. EXIT"

def closeDay():
    print("Today's cash: {}\nToday's card paymets: {}".format(Cash.cash_state,
                                                              Cash.card_state))
    input("Press Enter to continue...")


while True:
    os.system('cls')
    print(categories)
    try:
        menu = int(input("Your choose: "))
    except:
        menu = 0
        print('Must be number 1-5')

    if menu == 1:
        tableMenu()
    elif menu == 2:
        editMenuPositions()
    elif menu == 3:
        workDay()
    elif menu == 4:
        closeDay()
    elif menu == 5:
        sys.exit()