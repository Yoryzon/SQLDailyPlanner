from typing import List, Optional

from sqlalchemy import Column, Date, ForeignKeyConstraint, Integer, PrimaryKeyConstraint, String, Text, Time, \
    UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.orm.base import Mapped

from DataBase.DataBaseConnection.DataBaseMeta import Base


class Tasks(Base):
    __tablename__ = 'Tasks'
    __table_args__ = (
        ForeignKeyConstraint(['EventID'], ['Events.EventID'], name='Tasks_EventID_fkey'),
        PrimaryKeyConstraint('TaskID', name='Tasks_pkey')
    )

    TaskID = mapped_column(Integer)
    TaskName = mapped_column(String(100))
    Description = mapped_column(Text)
    DueDate = mapped_column(Date)
    Priority = mapped_column(String(100))
    Status = mapped_column(String(20))
    EventID = mapped_column(Integer)

    Events_: Mapped[Optional['Events']] = relationship('Events', back_populates='Tasks')
    Notes: Mapped[List['Notes']] = relationship('Notes', uselist=True, back_populates='Tasks_')

    def __repr__(self):
        return f"<Task(TaskID={self.TaskID}, TaskName='{self.TaskName}', Description='{self.Description}', DueDate='{self.DueDate}', Priority={self.Priority}, Status='{self.Status}')>"
