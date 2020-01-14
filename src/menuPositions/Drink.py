from src.menuPositions.BasePosition import BasePosition


class Drink(BasePosition):
    def __init__(self, name, price, tax_rate: float, alcoholfree: bool = False):
        super().__init__(name, price, tax_rate)
        self.alcoholfree = alcoholfree

    def __str__(self):
        return "Name: {:10}\tAlkoholfree: {:<10}\tPrice: {}".format(self.name,
                                                                    self.alcoholfree,
                                                                    self.nettoPrice)
