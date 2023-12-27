from typing import List, Optional

from sqlalchemy import Column, Date, ForeignKeyConstraint, Integer, PrimaryKeyConstraint, String, Text, Time, \
    UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.orm.base import Mapped

from DataBase.DataBaseConnection.DataBaseMeta import Base


class Events(Base):
    __tablename__ = 'Events'
    __table_args__ = (
        PrimaryKeyConstraint('EventID', name='Events_pkey'),
    )

    EventID = mapped_column(Integer)
    Title = mapped_column(String(100))
    Description = mapped_column(Text)
    EventDate = mapped_column(Date)
    StartTime = mapped_column(Time)
    EndTime = mapped_column(Time)

    Contacts: Mapped['Contacts'] = relationship('Contacts', uselist=False, back_populates='Events_')
    Tasks: Mapped[List['Tasks']] = relationship('Tasks', uselist=True, back_populates='Events_')

    def __repr__(self):
        return f"<Event(EventID={self.EventID}, Title='{self.Title}', Description='{self.Description}', EventDate='{self.EventDate}', StartTime='{self.StartTime}', EndTime='{self.EndTime}')>"
