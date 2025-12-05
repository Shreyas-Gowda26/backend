from motor.motor_asyncio import AsyncIOMotorClient
from fastapi import FastAPI
from dotenv import load_dotenv
import os

load_dotenv()

MONGODB_URI = os.getenv("MONGODB_URI","mongodb://localhost:27017")
DATABASE_NAME = os.getenv("DATABASE_NAME","chat_app")

client = None
db = None

async def connet_to_mongo():
    global client , db
    client = AsyncIOMotorClient(MONGODB_URI)
    db = client(DATABASE_NAME)
    print("🚀 Connected to MongoDB")

async def close_mongo_connection():
    global client
    if client:
        client.close()
        print("🛑 MongoDB connection closed")
        