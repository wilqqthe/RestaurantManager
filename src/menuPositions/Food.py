from src.globalVariables.globalVariables import db
from src.menuPositions.BasePosition import BasePosition


class Food(BasePosition):
    def __init__(self, name, price, tax_rate: int, category: str, allergens: str = '---', no: int = 0):
        super().__init__(name, price, tax_rate, no)
        self.allergens = allergens
        self.category = category.capitalize()

    def __str__(self):
        return "Name: {:10}\tCategory: {:16}\tAllergens: {:16}\tPrice: {}".format(self.name,
                                                                                  self.category,
                                                                                  self.allergens,
                                                                                  self.calculateBruttoPrice())

    @classmethod
    def loadElementsFromDB(cls):
        positions = []
        if len(db.table("Food")) == 0:
            print("No entries for food positions in Database")
        else:
            for position in db.table("Food"):
                positions.append(Food(position["name"],
                                      position["nettoPrice"],
                                      position["tax_rate"],
                                      position["category"],
                                      position["allergens"],
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
        category = input('Category: ')
        allergens = input('Allergens: ')

        return Food(name, nettoPrice, tax_rate, category, allergens, no)
