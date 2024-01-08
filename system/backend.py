import pymongo as pm
from dotenv import load_dotenv
import os
import user

#Load environment variables
load_dotenv()
client = pm.MongoClient(os.getenv("MONGODB_STR"))
#Load database and columns
itemdb = client["itemdb"]
items = itemdb["Items"]
orders = itemdb["Orders"]

class Item:
    def __init__(self):
        self.id = int()
        self.upc = int()
        self.price = int()
        self.name = str()
        self.quantity = int()
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
    def saveItemToDB(self):
        newItem = {"id": self.id, "upc": self.upc, "price": self.price, "name": self.name, "quantity": 0}
        items.insert_one(newItem)
        
    def addItemToDB(self, quantity):
        query = {"id": self.id}
        item = items.find_one(query)
        if item is not None:
            self.quantity = item["quantity"] + quantity
            items.update_one(query, {"$set": {"quantity": self.quantity}})
        else:
            self.quantity = quantity
            self.saveItemToDB()
        return
    def removeItemFromDB(self, quantity):
        query = {"id": self.id}
        item = items.find_one(query)
        if item is not None:
            self.quantity = item["quantity"] - quantity if self.quantity >= quantity else print("Invalid removal amount")
            items.update_one(query, {"$set": {"quantity": self.quantity}})
        return
    def deleteItemFromDB(self):
        query = {"id": self.id}
        items.delete_one(query)           
        return
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
        self.subtotal += newItem.price
    def displayCartItems(self):
        cart = ""
        for item in self.items:
            cart += str(item.id) + item.name + ":" + str(item.price), "\n"
        return cart
    def displayCartTotals(self):
        totals = ""
        totals += "Subtotal: " + str(self.subtotal) + "\nTax: " + str(self.tax) + "\nTotal: " + str(self.total)
        return totals
    def calculateTotal(self):
        checkSub = 0
        for item in self.items:
            checkSub += item.price
        self.total = self.subtotal + self.tax
        
            
class Order(Cart):
    def __init__(self):
        self.ordernumber = str()
        self.user = user.User()
        self.deliveryAddress = self.user.address # default delivery address is to user's address
        Cart.__init__(self)
        
    def findOrderByNumber(self, num:int)->int:
        order = orders.find_one({"orderNumber": num})
        if order is not None:
            self.orderNumber = order["orderNumber"]
            self.cart = order["cart"]
            return 1
        self.orderNumber = None
        return -1
        
    def generateOrderNumber(self):
        cursor = orders.find().limit(1).sort({"$natural":-1})
        lastGeneratedNumber = cursor[0]["orderNumber"]
        print(lastGeneratedNumber)
        
    def changeDeliveryAddress(self, newAddr:str)->str:
        self.deliveryAddress = newAddr
        return newAddr

    def isValidOrder(self)->bool:
        return True if self.orderNumber is not None and self.deliveryAddress is not None else False
    
    def saveOrder(self)->int:
        if self.isValidOrder():
            newOrder = {"orderNumber": self.orderNumber, "cart": {"subtotal": self.subtotal, "tax": self.tax, "total": self.total, "items": self.items}, "user": self.user}
            orders.insert_one(newOrder)
            return 0
        print("Cannot save invalid order. Reason: Order field is none")
        return -1
    
    def voidOrder(self):
        pass
    
def keyEvents(event):
    match event.char:
        case '1':
            pass
        

#exampleOrder = {"orderNumber": "ABC123", "cart": {"subtotal": 12.34, "tax": 0.01025, "total": 13.61, "items": [{"id": 123456, "upc": 123456789012, "price": 12.34, "name": "test"}]}}
#orders.insert_one(exampleOrder)
#test_item = {"id": 123456, "upc": 123456789012, "price": 12.34, "name": "test"}

#items.insert_one(test_item)
#query = {"name": "test"}
#results = items.find_one(query)
#print(results["id"])