from abc import ABC, abstractmethod
from base import RawData
from models.PoliticalEvent import PoliticalEvent
from typing import List

class DataSource(ABC):
	'''Data source linked to a certain Entity, every data source declares at least a
		fetch method, which explains how to get data, and a transform method, which
		transforms the raw data into a PoliticalEvent'''
	entity = "USA"

	def __init__(self, *args, **kwargs):
		pass
	
	@abstractmethod
	def fetch(self) -> RawData:
		'''Fetches data from the DataSource'''
		return None
	
	@abstractmethod
	def transform(self, data: RawData) -> List[PoliticalEvent]:
		'''Transforms RawData returned from fetch() into a PoliticalEvent'''
		if not data:
			return None
		return PoliticalEvent("event", self.entity, "general")
	
	def getData(self) -> List[PoliticalEvent]:
		return self.transform(self.fetch())