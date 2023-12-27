from typing import List, Optional

from sqlalchemy import Column, Date, ForeignKeyConstraint, Integer, PrimaryKeyConstraint, String, Text, Time, \
    UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from DataBase.DataBaseConnection.DataBaseMeta import Base


class Notes(Base):
    __tablename__ = 'Notes'
    __table_args__ = (
        ForeignKeyConstraint(['TaskID'], ['Tasks.TaskID'], name='Notes_TaskID_fkey'),
        PrimaryKeyConstraint('NoteID', name='Notes_pkey')
    )

    NoteID = mapped_column(Integer)
    Title = mapped_column(String(100))
    Content = mapped_column(Text)
    CreatedDate = mapped_column(Date)
    TaskID = mapped_column(Integer)

    Tasks_: Mapped[Optional['Tasks']] = relationship('Tasks', back_populates='Notes')

    def __repr__(self):
        return f"<Note(NoteID={self.NoteID}, Title='{self.Title}', Content='{self.Content}', CreatedDate='{self.CreatedDate}')>"
