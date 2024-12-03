from base.DataSource import DataSource
from base.RawData import RawData
from models.PoliticalEvent import PoliticalEvent
import json
import os
import requests

class CongressGov(DataSource):
    def __init__(self) -> None:
        super().__init__()
        self.entity = "USA"

    def fetch(self):
        api_key = os.getenv('CONGRESS_GOV_API_KEY')
        url = f"https://api.congress.gov/v3/bill?format=json&api_key={api_key}"
        
        response = requests.get(url)
        
        if response.status_code == 200:
            return RawData("json", response.json())
        else:
            return RawData("error", {'message': 'Failed to fetch data from the external API'})
        
    def transform(self, rawData: RawData):
        if not rawData:
            return None
        if rawData.error:
            return rawData.error
        jsonData = rawData.data
        return [PoliticalEvent(bill["title"], "USA", bill["type"]) for bill in jsonData["bills"]]
