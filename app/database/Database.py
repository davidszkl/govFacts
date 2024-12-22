from typing import List
from sqlalchemy import URL, create_engine, select
from sqlalchemy.orm import Session
from os import getenv

from models.Entity import Entity
from models.EventType import EventType
from base.utils import read_secret
from models.Base import Base

class Database():
    def __init__(self):
        self.name = getenv('POSTGRES_DB')
        self.user = getenv('POSTGRES_USER')
        self.password = read_secret('db_password')
        self.host = getenv('POSTGRES_HOST', 'localhost')
        self.port = '5432'
        self.engine = create_engine(self.__database_url(), echo=True)
        self.static_data = {"entity": {}, "event_type": {}}

    def __database_url(self):
        url = URL.create(
            drivername="postgresql+psycopg2",
            database=self.name,
            host=self.host,
            port=self.port,
            username=self.user,
            password=self.password
        )
        return url
    
    def init_database(self):
        if not self.engine:
            print("Database engine not initialised")
            return
        Base.metadata.create_all(self.engine)
        self.init_static_data()

    def init_static_data(self):
        '''initialise static data that does not change often, it will be cached in the db instance'''
        self.static_data["entity"] = {entity.name: entity for entity in self.search(Entity)}
        self.static_data["event_type"] = {event_type.name: event_type for event_type in self.search(EventType)}

    def _before_create(self, entity):
        pass

    def _after_create(self, entity):
        if (isinstance(entity, list) and any(ent.__tablename__ in self.static_data.keys() for ent in entity))\
            or (not isinstance(entity, list) and entity.__tablename__ in self.static_data.keys()):
            self.init_static_data()

    def create(self, entity: Base | List[Base]):
        if not entity:
            return None
        if isinstance(entity, list):
            self._create_many(entity)
        else:
            self._create_one(entity)

    def _create_one(self, entity):
        with Session(self.engine) as session:
            self._before_create(entity)
            session.add(entity)
            session.commit()
            self._after_create(entity)

    def _create_many(self, entity_list):
        with Session(self.engine) as session:
            self._before_create(entity_list)
            session.add_all(entity_list)
            session.commit()
            self._after_create(entity_list)

    def search(self, entity, where_clause=False, throw_error=False):
        with Session(self.engine) as session:
            stmt = select(entity)
            if where_clause:
                stmt = stmt.where(where_clause)
            res = session.scalars(stmt)
            if not res and throw_error:
                raise Exception(f"no entity found for query {stmt}")
            return res.all()
