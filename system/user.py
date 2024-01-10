import pymongo as pm
from dotenv import load_dotenv
import os

load_dotenv()
client = pm.MongoClient(os.getenv("MONGODB_STR"))
userdb = client["userdb"]
users = userdb["Users"]

class User:
    def __init__(self):
        self.username = str()
        self.password = bytes()
        self.fname = str()
        self.lname = str()
        self.phone = int()
        self.email = str()
        self.address = str()
        self.memberInfo = dict()
    def createUser(self):
        newUser = {"username": self.username, "password": self.password, "fname": self.fname, "lname": self.lname, "phone": self.phone, "email": self.email}
        users.insert_one(newUser)
    def editUserInfo(self):
        pass
    def getUserInfo(self, username:str)->dict:
        user = users.find_one({"username":username})
        return user
    def deleteUser(self, username:str):
        users.delete_one({"username": username})
    def displayUser(self):
        user = "Name: " + self.fname + " " + self.lname + "\nPhone #: " + str(self.phone) + "\nEmail: " + self.email + "\nAddress: " + self.address + "\nBest Buy Membership: " + self.memberInfo["type"]
        return user
    def getUserByPhoneNumber(self, phone):
        user = users.find_one({"phone": phone})
        self.username = user["username"]
        self.fname = user["fname"]
        self.lname = user["lname"]
        self.phone = user["phone"]
        self.email = user["email"]
        self.address = user["address"]
        self.memberInfo = user["memberInfo"]
        return self.displayUser()
    
class Employee(User):
    def __init__(self):
        self.id = int()
        self.permissions = int()
        User.__init__(self)
        
    def hasPermissions(self, req:int)->bool:
        return True if self.permissions >= req else False
    
        