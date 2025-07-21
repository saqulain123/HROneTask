from pymongo import MongoClient
from dotenv import load_dotenv
import os
import certifi

load_dotenv()

client = MongoClient(
    os.getenv("MONGODB_URL"),
    tls=True,
    tlsCAFile=certifi.where()
)

db = client["hrone_db"]
product_collection = db["products"]
order_collection = db["orders"]
