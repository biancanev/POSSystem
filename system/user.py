import pymongo as pm
from dotenv import load_dotenv
import os
import backend
import bcrypt

load_dotenv()
client = pm.MongoClient(os.getenv("MONGODB_STR"))
userdb = client["userdb"]
users = userdb["Users"]

class User:
    def __init__(self):
        self.username = str()  
        self.fname = str()
        self.lname = str()
        self.phone = int()
        self.email = str()
        self.address = str()
    def createUser(self):
        newUser = {"username": self.username, "fname": self.fname, "lname": self.lname, "phone": self.phone, "email": self.email}
        users.insert_one(newUser)
    def findAllUserOrders(self)->list:
        return [order for order in backend.orders.find({"username": self.username})]
    
class Employee(User):
    def __init__(self):
        pass
    
        