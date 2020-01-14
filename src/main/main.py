from src.Table import *
from src.bill.bill import Bill
from src.menuPositions.Drink import Drink
from src.menuPositions.Food import Food
from src.order.Order import Order

table = []
foods = []
drink = []
table.append(Table(4))
foods.append(Food('Margetira', 12.00, 23, 'Pizza'))
foods.append(Food('Carbonara', 8.00, 23, 'Pasta'))
foods.append(Food('Donner kebab', 3.50, 23, 'Kebab'))

drink.append(Drink('Tequila', 4.12, 23))
drink.append(Drink('Coke', 3, 23))


x = []

x.append(Order(table, foods, drink))
x.append(Order(table, foods, drink))


bill = Bill(x, 'card')
bill.printBill()