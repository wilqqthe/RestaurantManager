from src.globalVariables.globalVariables import db
from src.menuPositions.BasePosition import BasePosition


class Drink(BasePosition):
    def __init__(self, name, price, tax_rate: int, alcoholfree: bool = False, no: int = 0):
        super().__init__(name, price, tax_rate, no)
        self.alcoholfree = alcoholfree

    def __str__(self):
        return "Name: {:10}\tAlkoholfree: {:<10}\tPrice: {}".format(self.name,
                                                                    self.alcoholfree,
                                                                    self.nettoPrice)

    @classmethod
    def loadElementsFromDB(cls):
        positions = []
        if len(db.table("Drink")) == 0:
            print("No entries for food positions in Database")
        else:
            for position in db.table("Drink"):
                positions.append(Drink(position["name"],
                                       position["nettoPrice"],
                                       position["tax_rate"],
                                       position["alcoholfree"],
                                       position["no"]))
        return positions

    @classmethod
    def prepareAndCreateNew(cls, no: int = 0):
        name = input('Name: ')
        try:
            nettoPrice = float(input('Price netto: '))
            tax_rate = int(input('Tax rate: '))
        except:
            print('Value must be numeric')
            return
        if input('Alkoholfree True/False: ') == 'True':
            alcoholfree = True
        else:
            alcoholfree = False

        return Drink(name, nettoPrice, tax_rate, alcoholfree, no)
