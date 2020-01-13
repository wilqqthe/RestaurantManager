from src.menuPositions.BasePosition import BasePosition


class Drink(BasePosition):
    def __init__(self, name, price, alkoholfree: bool):
        super().__init__(name, price)
        self.alkoholfree = alkoholfree

    def __str__(self):
        return "Name: {:10}\tAlkoholfree: {:<10}\tPrice: {}".format(self.name,
                                                                    self.alkoholfree,
                                                                    self.price)
