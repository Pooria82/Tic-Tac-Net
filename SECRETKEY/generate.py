import secrets
from dotenv import set_key, load_dotenv
import os

# Generate a secret key
secret_key = secrets.token_hex(32)
print(secret_key)

# Define the path to the .env file
env_file = "SECRET_KEY.env"

# Check if the .env file exists, if not create it
if not os.path.exists(env_file):
    open(env_file, 'a').close()

# Load the .env file
load_dotenv(env_file)

# Set the SECRET_KEY in the .env file
set_key(env_file, "SECRET_KEY", secret_key)

print(f'SECRET_KEY has been written to {env_file}')
