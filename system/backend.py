import math

class Item:
    def __init__(self):
        self.id = int()
        self.upc = int()
        self.price = int()
        self.name = str()
    def findItemById(id):
        #TODO: connect to Mongodb to find item by id
        pass
    def findItemByUPC(self, upc):
        #TODO: connect to Mongodb to find item by upc
        return self
    def findItemByName(self, name):
        #TODO: connect to Mongodb to find item by name
        pass
    def isValidItem():
        return False if id == -1 else True

class Cart:
    def __init__(self):
        self.subtotal = int()
        self.tax = int()
        self.total = int()
        self.items = dict()
    def addItemToCart(self, num):
        newItem = Item()
        if math.log10(num) + 1 == 12:
            newItem.findItemByUPC(num)
            if self.items[newItem] == None:
                self.items[newItem] = 1
            else:
                self.items[newItem] += 1
            

cart = Cart()
cart.addItemToCart(123456789012)
print(cart.items)