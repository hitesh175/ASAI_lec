import math

# prac.py - simple square root calculator

def sqrt_of_number(x):
    if x < 0:
        raise ValueError("Cannot compute square root of a negative number")
    return math.sqrt(x)

def main():
    try:
        n = float(input("Enter a non-negative number: ").strip())
        print(f"Square root: {sqrt_of_number(n)}")
    except ValueError as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
    
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
