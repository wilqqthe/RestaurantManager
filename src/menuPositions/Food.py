from src.menuPositions.BasePosition import BasePosition


class Food(BasePosition):
    def __init__(self, name, price, allergens: str):
        super().__init__(name, price)
        self.allergens = allergens

    def __str__(self):
        return "Name: {:10}\tAllergens: {:16}\tPrice: {}".format(self.name,
                                                                 self.allergens,
                                                                 self.price)