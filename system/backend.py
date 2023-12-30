import math
import pymongo as pm

client = pm.MongoClient("mongodb://localhost:27017")
itemdb = client["itemdb"]
items = itemdb["Items"]

#test_item = {"id": 123456, "upc": 123456789012, "price": 12.34, "name": "test"}

#items.insert_one(test_item)
#query = {"name": "test"}
#results = items.find_one(query)
#print(results["id"])

class Item:
    def __init__(self):
        self.id = int()
        self.upc = int()
        self.price = int()
        self.name = str()
    def findItemById(self, id):
        query = {"id": id}
        item = items.find_one(query)
        if item is not None:
            self.id = item["id"]
            self.upc = item["upc"]
            self.price = item["price"]
            self.name = item["name"]
        else:
            self.id = -1
        return
    def findItemByUPC(self, upc):
        query = {"upc": upc}
        item = items.find_one(query)
        if item is not None:
            self.id = item["id"]
            self.upc = item["upc"]
            self.price = item["price"]
            self.name = item["name"]
        else:
            self.id = -1
        return
    def findItemByName(self, name):
        #TODO: connect to Mongodb to find item by name
        pass
    def isValidItem(self):
        return False if self.id == -1 else True

class Cart:
    def __init__(self):
        self.subtotal = int()
        self.tax = int()
        self.total = int()
        self.items = []
    def addItemToCart(self, num):
        newItem = Item()
        if len(str(num)) == 12:
            newItem.findItemByUPC(num)
            self.items.append(newItem) if newItem.isValidItem() else print("Invalid UPC")
        else:
            newItem.findItemById(num)
            self.items.append(newItem) if newItem.isValidItem() else print("Invalid ID")
    def displayCart(self):
        for item in self.items:
            print(item.id, item.name, ":", item.price)
    def calculateTotal(self):
        for item in self.items:
            self.subtotal += item.price
        self.tax = self.subtotal * 7.25
        self.total = self.subtotal + self.tax
        
            
cart = Cart()
cart.addItemToCart(123456)
cart.addItemToCart(123456789012)
cart.addItemToCart(111111)
cart.addItemToCart(123456789000)
cart.displayCart()
