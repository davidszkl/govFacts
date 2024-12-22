from dotenv import load_dotenv
from fastapi import FastAPI

from base.DataSource import DataSource
from database.Database import Database


class State:
    def __init__(self):
        self.app = FastAPI()
        self.db = Database()
        self.db.init_database()
        load_dotenv()
        
    def loadDataSources(self):
        for dataSource in DataSource.__subclasses__():
            instance = dataSource()
            data = instance.getData()
            self.db.create(data)