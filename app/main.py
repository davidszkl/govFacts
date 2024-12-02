from dotenv import load_dotenv
from fastapi import FastAPI
import os
import requests

app = FastAPI()

@app.get("/")
def home():
    api_key = os.getenv('API_KEY')
    url = f"https://api.congress.gov/v3/bill?format=json&api_key={api_key}"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        return {'error': 'Failed to fetch data from the external API'}

def read_secret(secret_name):
    secret_path = f"/run/secrets/{secret_name}"
    try:
        with open(secret_path) as f:
            return f.read().strip()
    except FileNotFoundError:
        return None

DATABASE = {
    'NAME': os.getenv('POSTGRES_DB'),
    'USER': os.getenv('POSTGRES_USER'),
    'PASSWORD': read_secret('db_password'),
    'HOST': os.getenv('POSTGRES_HOST', 'localhost'),
    'PORT': '5432'
}

if __name__ == "main":
    load_dotenv()