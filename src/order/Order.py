import copy

from src.generator.IdGenerator import IdGenerator


class Order:
    def __init__(self, tables: list, ordered_food=[], ordered_drinks=[], notes: str = ''):
        self.orderNo = IdGenerator.getOrderID()
        self.tables = copy.deepcopy(tables)
        self.ordered_food = copy.deepcopy(ordered_food)
        self.ordered_drinks = copy.deepcopy(ordered_drinks)
        self.notes = notes
        self.paid = False

    def __str__(self):
        return ''.join(['' + el.printToOrder() for el in self.tables + self.ordered_food + self.ordered_drinks])

    def setTableOccupied(self):
        for table in self.tables:
            if not table.occupied:
                table.setOccupation()

    def setPaidStatus(self):
        self.paid = True

    def sumUpOrder(self):
        return format(sum(float(food.calculateBruttoPrice()) for food in self.ordered_food + self.ordered_drinks), '.2f')

    def sumUpNettoOrder(self):
        return format(sum(float(food.getNettoPrice()) for food in self.ordered_food + self.ordered_drinks), '.2f')

    def printToBill(self):
        return ''.join(['' + el.printToBill() for el in self.ordered_food + self.ordered_drinks])

    def positionCounter(self):
        positions = {}
        for el in self.ordered_drinks + self.ordered_food:
            if el.name in positions.keys():
                positions[el.name] += 1
            else:
                positions[el.name] = 1
        return positions