from sqlalchemy import ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column
from models.Base import Base

class PoliticalEvent(Base):
    '''Event related to an Entity, can be a new bill being introduced,
        a new vote, a law being passed, etc..
    '''
    __tablename__ = "political_event"

    name: Mapped[str] = mapped_column(Text)    
    entity_id: Mapped[int] = mapped_column(ForeignKey("entity.id"))
    type_id: Mapped[int] = mapped_column(ForeignKey("event_type.id"))
    external_id : Mapped[int] = mapped_column() # unique identifier from an external source
