import copy

from src.Table import Table
from src.generator.IdGenerator import IdGenerator
from src.menuPositions.Drink import Drink
from src.menuPositions.Food import Food


class Order:
    def __init__(self, tables: list, ordered_food=[], ordered_drinks=[], notes: str = ''):
        self.orderNo = IdGenerator.getOrderID()
        self.tables = copy.deepcopy(tables)
        self.ordered_food = copy.deepcopy(ordered_food)
        self.ordered_drinks = copy.deepcopy(ordered_drinks)
        self.notes = notes

    def __str__(self):
        return ''.join(['' + el.printToOrder() for el in self.tables + self.ordered_food + self.ordered_drinks])

    def setTableOccupied(self):
        for table in self.tables:
            if not table.occupied:
                table.setOccupation()

    def summaryOrder(self):
        return sum(float(food.price) for food in self.ordered_food + self.ordered_drinks)


table = []
foods = []
drink = []
table.append(Table(4))
foods.append(Food('Margetira', 12.00, 'Pizza'))
foods.append(Food('Carbonara', 8.00, 'Pasta'))
foods.append(Food('Donner kebab', 3.50, 'Kebab'))

drink.append(Drink('Tequila', 4.12))
drink.append(Drink('Coke', 3))

x = Order(table, foods, drink)

print(x)
