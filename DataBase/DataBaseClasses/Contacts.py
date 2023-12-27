from typing import List, Optional

from sqlalchemy import Column, Date, ForeignKeyConstraint, Integer, PrimaryKeyConstraint, String, Text, Time, \
    UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.orm.base import Mapped

from DataBase.DataBaseConnection.DataBaseMeta import Base


class Contacts(Base):
    __tablename__ = 'Contacts'
    __table_args__ = (
        ForeignKeyConstraint(['EventID'], ['Events.EventID'], name='Contacts_EventID_fkey'),
        PrimaryKeyConstraint('ContactID', name='Contacts_pkey'),
        UniqueConstraint('EventID', name='Contacts_EventID_key')
    )

    ContactID = mapped_column(Integer)
    FullName = mapped_column(String(100))
    Phone = mapped_column(String(20))
    Email = mapped_column(String(100))
    Address = mapped_column(Text)
    EventID = mapped_column(Integer)

    Events_: Mapped[Optional['Events']] = relationship('Events', back_populates='Contacts')

    def __repr__(self):
        return f"<Contact(ContactID={self.ContactID}, FullName='{self.FullName}', Phone='{self.Phone}', Email='{self.Email}', Address='{self.Address}')>"
