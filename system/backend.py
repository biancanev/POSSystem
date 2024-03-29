import pymongo as pm
from datetime import date
from dotenv import load_dotenv
import os
import user
import gridfs

#Load environment variables
load_dotenv()
client = pm.MongoClient(os.getenv("MONGODB_STR"))
#Load database and columns
itemdb = client["itemdb"] #database for information related to items orders
items = itemdb["Items"] #collection of items
orders = itemdb["Orders"] #collection of orders
fsdb = client["filesystem"] #database for filesystem(images)
fs = gridfs.GridFS(fsdb) #filesystem using GridFS

class Item:
    def __init__(self):
        self.id = int()
        self.upc = int()
        self.price = int()
        self.name = str()
        self.quantity = int()
        self.imageFilePath = str()
        self.addons = {"plans": list(), "services": list, "accessories": list()}
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
    def uploadPicture(self, path:str):
        with open(path, 'rb') as f:
            contents = f.read()
        fs.put(contents, filename=path)
        self.imageFilePath = path
    def displayImage(self):
        file = fs.find_one({"filename": self.imageFilePath})
        image = file.read()
        return image
    def displayItem(self):
        item = "Name: " + self.name + "\nID: " + str(self.id) + "\nUPC: " + str(self.upc)
        return item
    
class ProtectionPlan(Item):
    def __init__(self):
        self.childID = int()
        self.associatedSerial = int()
        self.expDate = str()
        Item.__init__(self)
    def isPlanStillValid(self)->bool:
        return True if date.today() >= self.expDate else False
class Cart:
    def __init__(self):
        self.subtotal = float()
        self.tax = float()
        self.total = float()
        self.items = []
    def addItemToCart(self, num):
        try:
            num = int(num)
        except:
            pass
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
        self.tax = 0.1025 * self.subtotal
        self.total = self.subtotal + self.tax
        return
    def displayCartItems(self):
        cart = ""
        for item in self.items:
            cart += f'{str(item.id):12}' + "   " + f'{item.name:18}' + "  " + "$" + f'{item.price:8.2f}' + "\n"
        return cart
    def displayCartTotals(self):
        totals = ""
        totals += "Subtotal: " + f'{self.subtotal:.2f}' + "\nTax: " + f'{self.tax:.2f}' + "\nTotal: " + f'{self.total:.2f}'
        return totals
                   
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
    
    
        

#exampleOrder = {"orderNumber": "ABC123", "cart": {"subtotal": 12.34, "tax": 0.01025, "total": 13.61, "items": [{"id": 123456, "upc": 123456789012, "price": 12.34, "name": "test"}]}}
#orders.insert_one(exampleOrder)
#test_item = {"id": 123456, "upc": 123456789012, "price": 12.34, "name": "test"}

#items.insert_one(test_item)
#query = {"name": "test"}
#results = items.find_one(query)
#print(results["id"])