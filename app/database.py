from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

client = MongoClient(
    os.getenv("MONGODB_URL"),
    tls=True,
    tlsAllowInvalidCertificates=False
)

db = client['hrone_db']

product_collection = db['products']
order_collection = db['orders']
