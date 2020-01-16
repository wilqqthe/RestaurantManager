import copy
from collections import Counter
from datetime import date

from src.payment.cash import Cash


class Bill:
    bills = list()

    def __init__(self, order: list, payment_method: str):
        self.orders = copy.deepcopy(order)
        self.today = date.today()
        self.payment_method = payment_method
        self.positionsWithAmount = self.positionsCounter()

    def positionsCounter(self):
        positionsWithAmount = {}
        for order in self.orders:
            positionsWithAmount = dict(Counter(order.positionCounter()) + Counter(positionsWithAmount))
        return positionsWithAmount

    def printBill(self):
        no = 0
        totalBill = position = ''
        payment_method = "Payment method: {:>50}".format(self.payment_method)
        header = '{:4}{:25}{:8}{:8}{:6}{:9}{}\n'.format('No.',
                                                        'Product name',
                                                        'Piece',
                                                        'Amount',
                                                        'Netto',
                                                        'Tax rate',
                                                        'Brutto')
        for product, amount in self.positionsWithAmount.items():
            no += 1
            position += "{}.  {:15}{:>15}{:>8}{:>8}{:>8}{:>8}\n".format(no,
                                                                        product,
                                                                        self.getDetails('netto', product, 1),
                                                                        amount,
                                                                        self.getDetails('netto', product, amount),
                                                                        self.getDetails('tax', product, amount),
                                                                        self.getDetails('brutto', product, amount))

            totalBill = "Total amount: {:>36}{:>16}\n".format(format(self.getNettoBill(), '.2f'),
                                                              format(self.getBruttoBill(), '.2f'))

        print(header + position + totalBill + payment_method)

    def getDetails(self, detail, product, amount: int):
        for order in self.orders:
            for position in order.ordered_food + order.ordered_drinks:
                if position.name == product:
                    if detail == 'netto':
                        return format(position.nettoPrice * amount, '.2f')
                    elif detail == 'tax':
                        return str(position.tax_rate) + '%'
                    elif detail == 'brutto':
                        return position.calculateBruttoPrice(amount)

    def getNettoBill(self):
        return sum(float(order.sumUpNettoOrder()) for order in self.orders)

    def getBruttoBill(self):
        return sum(float(order.sumUpOrder()) for order in self.orders)

    def makePayment(self):
        if self.payment_method == 'Cash':
            Cash.addCardPayment(self.getBruttoBill())
        elif self.payment_method == 'Card':
            Cash.addCardPayment(self.getBruttoBill())
        for order in self.orders:
            order.paid = True
            for table in order.tables:
                if table.occupied:
                    table.setOccupation()


