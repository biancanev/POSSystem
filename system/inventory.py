from backend import *

def addItemtoDB(newItem:dict):
    items.insert_one(newItem)