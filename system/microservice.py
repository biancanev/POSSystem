import pymongo as pm
from dotenv import load_dotenv
import os

load_dotenv()
client = pm.MongoClient(os.getenv("MONGODB_STR"))
#Load database and columns
itemdb = client["itemdb"] #database for information related to items orders
items = itemdb["Items"] #collection of items

def calculateNewRevProfit(id:int, quantity:int):
    item = items.find_one({"id":id})
    rev = item["revenue"] + item["price"] * quantity
    profit = rev - item["costPerUnit"] * quantity
    items.update_one({"id":id}, {"$set": {"revenue": rev, "profit": profit}})
    