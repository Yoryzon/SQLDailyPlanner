from sqlalchemy.exc import SQLAlchemyError

from DataBase.DataBaseConnection.DataBaseMeta import Base, Engine, SessionFactory
from DataBase.DataBaseClasses.Events import Events

Base.metadata.create_all(Engine)
session = SessionFactory()


class EventManager:
    @staticmethod
    def create_event(title, description, event_date, start_time, end_time):
        try:
            new_event = Events(Title=title, Description=description, EventDate=event_date, StartTime=start_time,
                               EndTime=end_time)
            session.add(new_event)
            session.commit()
            return new_event
        except SQLAlchemyError as e:
            session.rollback()
            print(f"Error creating event: {e}")
            return None

    @staticmethod
    def get_all_events():
        try:
            return session.query(Events).all()
        except SQLAlchemyError as e:
            print(f"Error getting all events: {e}")
            return []

    @staticmethod
    def update_event(event_id, new_title=None, new_description=None, new_event_date=None, new_start_time=None,
                     new_end_time=None):
        try:
            event = session.query(Events).filter_by(EventID=event_id).first()
            if event:
                if new_title:
                    event.Title = new_title
                if new_description:
                    event.Description = new_description
                if new_event_date:
                    event.EventDate = new_event_date
                if new_start_time:
                    event.StartTime = new_start_time
                if new_end_time:
                    event.EndTime = new_end_time
                session.commit()
                return event
        except SQLAlchemyError as e:
            session.rollback()
            print(f"Error updating event: {e}")
            return None

        return None

    @staticmethod
    def delete_event(event_id):
        try:
            event = session.query(Events).filter_by(EventID=event_id).first()
            if event:
                session.delete(event)
                session.commit()
                return True
            return False
        except SQLAlchemyError as e:
            session.rollback()
            print(f"Error deleting event: {e}")
            return False

    @staticmethod
    def get_event_by_id(event_id):
        try:
            return session.query(Events).filter_by(EventID=event_id).first()
        except SQLAlchemyError as e:
            print(f"Error getting event by ID: {e}")
            return None

    @staticmethod
    def search_events_by_title(title):
        try:
            return session.query(Events).filter(Events.Title.ilike(f"%{title}%")).all()
        except SQLAlchemyError as e:
            print(f"Error searching events by title: {e}")
            return []

    @staticmethod
    def search_events_by_date(event_date):
        try:
            return session.query(Events).filter(Events.EventDate == event_date).all()
        except SQLAlchemyError as e:
            print(f"Error searching events by date: {e}")
            return []

    @staticmethod
    def search_events_by_description(description):
        try:
            return session.query(Events).filter(Events.Description.ilike(f"%{description}%")).all()
        except SQLAlchemyError as e:
            print(f"Error searching events by description: {e}")
            return []
