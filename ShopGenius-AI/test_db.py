# test_db.py
import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")

print("🔍 Checking MongoDB connection...")

if not MONGO_URI:
    print("❌ MONGO_URI is missing in .env file!")
    exit()

try:
    client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)
    client.server_info()  # Force connection check
    print("🟢 MongoDB Connected Successfully!")
except Exception as e:
    print("🔴 MongoDB Connection Failed!")
    print("Error:", e)
