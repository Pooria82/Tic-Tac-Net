from pymongo import MongoClient


def connect_to_db():
    client = MongoClient('mongodb://localhost:27017/')
    db = client['user_database']
    collection = db['users']
    return collection


def save_user_to_db(username, email, password):
    collection = connect_to_db()
    user = {
        "username": username,
        "email": email,
        "password": password
    }
    collection.insert_one(user)
