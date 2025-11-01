from pymongo import MongoClient
from dotenv import load_dotenv
import os
from pprint import pprint

# ------------------ CONFIG ------------------
load_dotenv(dotenv_path=".env")

MONGODB_URI = os.getenv("MONGODB_URI", "mongodb://localhost:27017")
DB_NAME = os.getenv("DB_NAME", "cat_db")
COLLECTION_NAME = os.getenv("COLLECTION_NAME", "cats")

# ------------------ CONNECTION ------------------
try:
    client = MongoClient(MONGODB_URI)
    db = client[DB_NAME]
    cats = db[COLLECTION_NAME]
    print("✅ Connected to MongoDB successfully.")
except Exception as e:
    print("❌ Connection error:", e)
    exit(1)

# ------------------ CREATE ------------------
def create_cat(name, age, features):
    """Створює нового кота."""
    try:
        result = cats.insert_one({
            "name": name,
            "age": age,
            "features": features
        })
        print(f"✅ Cat added with id: {result.inserted_id}")
    except Exception as e:
        print("❌ Error creating cat:", e)

# ------------------ READ ------------------
def show_all_cats():
    """Виводить усіх котів."""
    try:
        for cat in cats.find():
            pprint(cat)
    except Exception as e:
        print("❌ Error reading cats:", e)

def find_cat_by_name(name: str):
    """Знаходить кота за ім’ям."""
    try:
        doc = cats.find_one({"name": name})
        if doc:
            pprint(doc)
        else:
            print(f"ℹ️ Cat '{name}' not found.")
    except Exception as e:
        print("❌ Error in find_cat_by_name:", e)

# ------------------ UPDATE ------------------
def update_cat_age(name, new_age):
    """Оновлює вік кота."""
    try:
        res = cats.update_one({"name": name}, {"$set": {"age": new_age}})
        if res.matched_count:
            print(f"🔄 Cat '{name}' age updated to {new_age}")
        else:
            print(f"ℹ️ Cat '{name}' not found.")
    except Exception as e:
        print("❌ Error updating cat age:", e)

def add_feature(name: str, feature: str):
    """Додає нову характеристику коту (уникає дублікатів)."""
    try:
        res = cats.update_one({"name": name}, {"$addToSet": {"features": feature}})
        if res.matched_count == 0:
            print(f"ℹ️ Cat '{name}' not found.")
        else:
            print(f"➕ Feature added to '{name}': {feature}")
    except Exception as e:
        print("❌ Error in add_feature:", e)

# ------------------ DELETE ------------------
def delete_cat(name):
    """Видаляє кота за ім’ям."""
    try:
        res = cats.delete_one({"name": name})
        if res.deleted_count:
            print(f"🗑️ Cat '{name}' deleted.")
        else:
            print(f"ℹ️ Cat '{name}' not found.")
    except Exception as e:
        print("❌ Error deleting cat:", e)

def delete_all():
    """Видаляє всіх котів."""
    try:
        cats.delete_many({})
        print("🧹 All cats deleted.")
    except Exception as e:
        print("❌ Error clearing collection:", e)

# ------------------ DEMO ------------------
if __name__ == "__main__":
    delete_all()

    create_cat("Barsik", 3, ["playful", "loves milk", "friendly"])
    create_cat("Murka", 5, ["lazy", "likes to sleep"])
    show_all_cats()

    print("\n🔍 Find 'Barsik':")
    find_cat_by_name("Barsik")

    print("\n➕ Add new feature to 'Barsik':")
    add_feature("Barsik", "loves to climb trees")

    print("\n🔄 Update 'Barsik' age:")
    update_cat_age("Barsik", 4)

    print("\n📋 Show all cats:")
    show_all_cats()

    print("\n🗑️ Delete 'Murka':")
    delete_cat("Murka")

    print("\n📋 Final cats list:")
    show_all_cats()
