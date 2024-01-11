import pymongo as pm
from dotenv import load_dotenv
import os

load_dotenv()
client = pm.MongoClient(os.getenv("MONGODB_STR"))
#Load database and columns
itemdb = client["itemdb"] #database for information related to items orders
items = itemdb["Items"] #collection of items

def getTopSellingItems(num:int)->list:
    cur = items.find({}).limit(num).sort({"sold": -1})
    return [doc["name"] for doc in cur]

def getTopRevenueItems():
    pass
    