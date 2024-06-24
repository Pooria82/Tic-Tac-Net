from pymongo import MongoClient
import bcrypt


def connect_to_db():
    client = MongoClient('mongodb://localhost:27017/')
    db = client['user_database']
    collection = db['users']
    return collection


def is_unique_username(username):
    collection = connect_to_db()
    if collection.find_one({"username": username}):
        return False
    return True


def is_unique_email(email):
    collection = connect_to_db()
    if collection.find_one({"email": email}):
        return False
    return True


def save_user_to_db(username, email, password):
    collection = connect_to_db()

    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    user = {
        "username": username,
        "email": email,
        "password": hashed_password,
        "role": "player"
    }
    collection.insert_one(user)
