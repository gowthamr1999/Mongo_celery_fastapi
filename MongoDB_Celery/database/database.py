from pymongo import MongoClient
from dotenv import dotenv_values

config = dotenv_values(".env")

def connection():
    mongodb_client = MongoClient("mongodb://localhost:27017/")
    database = mongodb_client['mychatdb']
    return database,mongodb_client