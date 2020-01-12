from menuPositions.BasePosition import BasePosition


class Food(BasePosition):
    def __init__(self, name, price, newValue):
        super().__init__(name, price)
        self.newValue = newValue



x = Food('Ma', 1, 'neewValue')
y = Food('te', 1, 'neewValue')
z = Food('usz', 1, 'neewValue')
x.upsertInDB()
y.upsertInDB()
z.upsertInDB()

# y.name = 'dupsko'
# y.upsertInDB()
# x.deleteFromDB()

x.deleteFromDB()