from pymongo import MongoClient
from dotenv import load_dotenv
import os
from pprint import pprint

# Завантажити .env
load_dotenv(dotenv_path=".env")

MONGODB_URI = os.getenv("MONGODB_URI", "mongodb://localhost:27017")
DB_NAME = os.getenv("DB_NAME", "cat_db")
COLLECTION_NAME = os.getenv("COLLECTION_NAME", "cats")

# Підключення до MongoDB
client = MongoClient(MONGODB_URI)
db = client[DB_NAME]
cats = db[COLLECTION_NAME]

# ---------- CREATE ----------
def create_cat(name, age, features):
    result = cats.insert_one({
        "name": name,
        "age": age,
        "features": features
    })
    print(f"✅ Cat added with id: {result.inserted_id}")

# ---------- READ ----------
def show_all_cats():
    for cat in cats.find():
        pprint(cat)

# ---------- UPDATE ----------
def update_cat_age(name, new_age):
    cats.update_one({"name": name}, {"$set": {"age": new_age}})
    print(f"🔄 Cat '{name}' age updated to {new_age}")

# ---------- DELETE ----------
def delete_cat(name):
    cats.delete_one({"name": name})
    print(f"🗑️ Cat '{name}' deleted")

# ---------- CLEAR COLLECTION ----------
def delete_all():
    cats.delete_many({})
    print("🧹 All cats deleted")

# ---------- DEMO ----------
if __name__ == "__main__":
    delete_all()
    create_cat("Barsik", 3, ["playful", "loves milk", "friendly"])
    create_cat("Murka", 5, ["lazy", "likes to sleep"])
    show_all_cats()
    update_cat_age("Barsik", 4)
    show_all_cats()
    delete_cat("Murka")
    show_all_cats()
