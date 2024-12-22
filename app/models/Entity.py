from models.Base import Base
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

class Entity(Base):
    '''Country, State, Federation, etc.'''
    __tablename__ = "entity"

    name: Mapped[str] = mapped_column(String(255))        
