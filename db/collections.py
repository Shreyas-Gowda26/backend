from db.mongodb import db

def users_collection():
    return db["users"]

def messages_collection():
    return db["messages"]

def rooms_collectio():
    return db["rooms"]