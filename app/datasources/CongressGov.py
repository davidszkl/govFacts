import os
import requests

from main import state
from base.DataSource import DataSource
from base.RawData import RawData
from models.EventType import EventType
from models.PoliticalEvent import PoliticalEvent

class CongressGov(DataSource):
    def __init__(self) -> None:
        super().__init__()

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
        entity_id = state.db.static_data["entity"]["USA"].id
        new_bill_types = set(bill["type"] for bill in jsonData["bills"] if bill["type"] not in state.db.static_data["event_type"])
        state.db.create([EventType(name=type_name) for type_name in new_bill_types])
        return [
            PoliticalEvent(
                name=bill["title"],
                entity_id=entity_id,
                type_id=state.db.static_data["event_type"][bill["type"]].id,
                external_id=bill["number"]
            ) for bill in jsonData["bills"]
        ]
