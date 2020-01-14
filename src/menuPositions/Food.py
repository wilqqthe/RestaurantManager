from src.menuPositions.BasePosition import BasePosition


class Food(BasePosition):
    def __init__(self, name, price, tax_rate: float, category: str, allergens: str = '---'):
        super().__init__(name, price, tax_rate)
        self.allergens = allergens
        self.category = category.capitalize()

    def __str__(self):
        return "Category: {:10}\tName: {:16}\tAllergens: {:16}\tPrice: {}".format(self.category,
                                                                                  self.name,
                                                                                  self.allergens,
                                                                                  self.nettoPrice)
