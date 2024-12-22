from models.Base import Base
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

class EventType(Base):
    '''Type to categorize a political event'''
    __tablename__ = "event_type"

    name: Mapped[str] = mapped_column(String(255))        
        
