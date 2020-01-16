import os

from src.bill.bill import Bill
from src.order.Order import Order


def takeAPayment():
    ordersToPay = list()
    while True:
        os.system('cls')
        for order in Order.orderList:
            if order not in ordersToPay:
                print("{}. {}".format(order.orderNo, order))
        print("Type number of order to pay.\nType 0 to Back")
        try:
            menu = int(input("Your choose: "))
            if menu == 0: break
        except:
            print('Must be number numeric')

        try:
            ordersToPay.append(Order.getOrderByOrderNo(menu))
        except:
            print('Failed!')

    while True:
        paymentMethod = str(input("Choose payment method or Quit(Type 0): "))
        if paymentMethod.capitalize() == 'Card' or paymentMethod.capitalize() == 'Cash':
            try:
                Bill.bills.append(Bill(ordersToPay, paymentMethod))
            except:
                print('Failed!')
            break
        elif paymentMethod == '0':
            return

    os.system('cls')
    Bill.bills[-1].printBill()
    while True:
        menu = str(input('Do you want to mark it as paid? 1 - Yes'))
        if menu == '1':
            Bill.bills[-1].makePayment()
            return

def paymentMenu():
    os.system('cls')
    print("1. Take a payment \n2. Show all orders \n3. Back")
    try:
        menu = int(input("Your choose: "))
    except:
        menu = 0
        print('Must be number 1-4')

    if menu == 1:
        takeAPayment()
    elif menu == 2:
        Order.printAllOrders()
    elif menu == 3:
        return
