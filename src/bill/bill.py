import copy
from collections import Counter
from datetime import date


class Bill():
    def __init__(self, order: list, payment_method: str):
        super().__init__()
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
        position = ''
        no = 0
        for product, amount in self.positionsWithAmount.items():
            no += 1
            position += "{}.  {:15}{:>15}{:>8}{:>8}{:>8}{:>8}\n".format(no,
                                                                        product,
                                                                        self.getDetails('netto', product, 1),
                                                                        amount,
                                                                        self.getDetails('netto', product, amount),
                                                                        self.getDetails('tax', product, amount),
                                                                        self.getDetails('brutto', product, amount))

            totalBill = "{}{:>16}".format(format(sum(float(order.sumUpNettoOrder()) for order in self.orders), '.2f'),
                                          format(sum(float(order.sumUpOrder()) for order in self.orders)), '.2f')

        print('No\tProduct Name\t\t\tPiece\tAmount\t Netto\tTax rate\tBrutto')
        print(position)
        print(totalBill)

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
