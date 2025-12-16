from dotenv import load_dotenv
import os

# Load variables from .env file
load_dotenv()

# Read the keys
main_key = os.getenv("MAIN_KEY")
secret_key = os.getenv("SECRET_KEY")

# Use the keys
print("Main Key:", main_key)
print("Secret Key:", secret_key)

api_key = main_key
if main_key and secret_key:
    print("Keys loaded successfully")
else:
    print("Keys missing")
