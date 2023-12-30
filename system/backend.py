import pymongo as pm
from dotenv import load_dotenv
import os

load_dotenv()
client = pm.MongoClient(os.getenv("MONGODB_STR"))
itemdb = client["itemdb"]
items = itemdb["Items"]
orderdb = client["orderdb"]
orders = orderdb["Orders"]

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
        query = {"name": name}
        item = items.find_one(query)
        if item is not None:
            self.id = item["id"]
            self.upc = item["upc"]
            self.price = item["price"]
            self.name = item["name"]
        else:
            self.id = -1
        return
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
        if type(num) is int:
            if len(str(num)) == 12:
                newItem.findItemByUPC(num)
                self.items.append(newItem) if newItem.isValidItem() else print("Invalid UPC")
            else:
                newItem.findItemById(num)
                self.items.append(newItem) if newItem.isValidItem() else print("Invalid ID")
        else:
            newItem.findItemByName(num)
            self.items.append(newItem) if newItem.isValidItem() else print("Invalid Name")
    def displayCart(self):
        for item in self.items:
            print(item.id, item.name, ":", item.price, "\n")
        print("Subtotal: ", self.subtotal, "\n")
        print("Tax: ", self.tax, "\n")
        print("Total: ", self.total, "\n")
    def calculateTotal(self):
        for item in self.items:
            subtotal += item.price
        self.subtotal = subtotal
        self.tax = self.subtotal * 7.25
        self.total = self.subtotal + self.tax
        
            
class Order(Cart):
    def __init__(self):
        self.orderNumber = str()
        self.orderName = str()
    # tentative naming (not sure how the query thing works)
    def findOrderByName(self, name):
        query = {"name": name}
        order = orders.find_one(query)
        if order is not None:
            self.orderNumber = order["number"]
            self.orderName = order["name"]
            self.items = order["items"]
        else:
            self.orderNumber = -1
        return
    def findOrderByNumber(self, num):
        query = {"number": num}
        order = orders.find_one(query)
        if order is not None:
            self.orderNumber = order["number"]
            self.orderName = order["name"]
            self.items = order["items"]
        else:
            self.orderNumber = -1
        return
    def isValidOrder(self):
        return False if self.orderNumber == -1 else True
    def returnOrder(self):
        pass
            
cart = Cart()
cart.addItemToCart(123456)
cart.addItemToCart(123456789012)
cart.addItemToCart(111111)
cart.addItemToCart(123456789000)
cart.displayCart()
