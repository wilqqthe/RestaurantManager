from src.menuPositions.BasePosition import BasePosition


class Drink(BasePosition):
    def __init__(self, name, price, alcoholfree: bool = False):
        super().__init__(name, price)
        self.alcoholfree = alcoholfree

    def __str__(self):
        return "Name: {:10}\tAlkoholfree: {:<10}\tPrice: {}".format(self.name,
                                                                    self.alcoholfree,
                                                                    self.price)
