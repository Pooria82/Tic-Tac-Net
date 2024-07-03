from pathlib import Path
from pymongo import MongoClient
from datetime import datetime, timedelta
from dotenv import load_dotenv
import os
import jwt
import bcrypt

OUTPUT_PATH = Path(__file__).parent

load_dotenv(Path(OUTPUT_PATH, '..', 'SECRETKEY', 'SECRET_KEY.env'))
SECRET_KEY = os.getenv("SECRET_KEY")


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


def validate_login(username, password):
    collection = connect_to_db()
    user = collection.find_one({"username": username})

    if user and bcrypt.checkpw(password.encode('utf-8'), user["password"]):
        token = generate_jwt_token(username)
        return token
    return None


# Function to generate JWT token
def generate_jwt_token(username):
    payload = {
        'username': username,
        'exp': datetime.utcnow() + timedelta(days=1)  # Token expiry time
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    return token


# Function to verify JWT token
def verify_jwt_token(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        return payload['username']
    except jwt.ExpiredSignatureError:
        # Token expired
        return None
    except jwt.InvalidTokenError:
        # Invalid token
        return None
