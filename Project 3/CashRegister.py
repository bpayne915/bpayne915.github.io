# Name: Barbara Payne
# Assignment 11.1
# Purpose: Cash register to display total items and total price from user's input

import locale
locale.setlocale(locale.LC_ALL, 'en_US')

class CashRegister:
    def __init__(self):
        self.count = 0
        self.total = 0
        self.price = 0
        print('Welcome to Cash Register!')
    def addItem(self, price):
        self.price = price
        self.count = self.count+1
        self.total = self.total + price
    def getTotal(self):
        print("The total price is:", locale.currency(self.total,'$'))
    def getCount(self):
        print("You have entered", self.count, "items into the cash register.")

register = CashRegister()

while True:
    priceAnswer = register.addItem(float(input('Enter price of the item ')))
    response = input('Want to add another price? Type any key to continue or type q to quit. ')
    if response == 'q':
        print("\n")
        break
register.getCount()
register.getTotal()
