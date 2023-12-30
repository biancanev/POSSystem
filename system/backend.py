import math as m

class Item:
    def __init__(self):
        self.id = int()
        self.upc = int()
        self.price = int()
        self.name = str()
    
    def findItemById(id):
        # TODO: connect to Mongodb to find item by id
        pass
    
    def findItemByUPC(upc):
        # TODO: connect to Mongodb to find item by upc
        pass
    
    def findItemByName(name):
        # TODO: connect to Mongodb to find item by name
        pass
    
    def isValidItem(): return False if id == -1 else True

class Cart:
    def __init__(self):
        self.cartItems = dict()
        self.subtotal = float()
        self.tax = float()
        self.total = float()

    # -1: invalid item, 0: item added to cart
    def addItemToCart(self, num):
        newItem = Item()
        if m.log10(num) + 1 == 12:
            newItem.findItemByUPC(num)
            if newItem.isValidItem():
                if self.cartItems[newItem] == None:
                    self.cartItems[newItem] = 1
                else:
                    self.cartItems[newItem] += 1
                return 0
        else:
            newItem.findItemByUPC(num)
            if newItem.isValidItem():
                if self.cartItems[newItem] == None:
                    self.cartItems[newItem] = 1
                else:
                    self.cartItems[newItem] += 1
                return 0
        return -1

    def removeItemFromCart(self):
        delItem = Item()
        self.cartItems[delItem] -= 1
    
class Order(Cart):
    def __init__(self):
        self.orderNumber = int()
        self.orderName = str()
        
    def findOrderByUPC():
        pass