from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import json

file = "creds.json"
fp = open(file)
data = json.load(fp)
uri = data["mongodb"]
client = MongoClient(uri, server_api=ServerApi('1'))
mydb = client["HTL_Billing"]


def add_items(item, price, image):
    mycoll = mydb["items"]
    query = {"item": item, "price": price, "image": image}
    insert = mycoll.insert_one(query)
    return insert


adding = add_items("briyani", "120",
                   "https://restaurantindia.s3.ap-south-1.amazonaws.com/s3fs-public/2019-10/biryani.jpg")
