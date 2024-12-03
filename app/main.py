from base.DataSource import DataSource
from datasources import *
from dotenv import load_dotenv
from fastapi import FastAPI
import os

app = FastAPI()
data = []

@app.get("/")
def home():
    return data

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

def loadDataSources():
    global data
    for dataSource in DataSource.__subclasses__():
        instance = dataSource()
        data = instance.getData()

if __name__ == "main":
    load_dotenv()
    loadDataSources()