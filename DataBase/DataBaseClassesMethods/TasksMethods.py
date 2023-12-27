from sqlalchemy.exc import SQLAlchemyError

from DataBase.DataBaseConnection.DataBaseMeta import Base, Engine, SessionFactory
from DataBase.DataBaseClasses.Tasks import Tasks

Base.metadata.create_all(Engine)
session = SessionFactory()


class TaskManager:
    @staticmethod
    def create_task(task_name, description, due_date, priority, status, event_id):
        try:
            new_task = Tasks(TaskName=task_name, Description=description, DueDate=due_date, Priority=priority,
                             Status=status, EventID=event_id)
            session.add(new_task)
            session.commit()
            return new_task
        except SQLAlchemyError as e:
            session.rollback()
            print(f"Error creating task: {e}")
            return None

    @staticmethod
    def get_all_tasks():
        try:
            return session.query(Tasks).all()
        except SQLAlchemyError as e:
            print(f"Error getting all tasks: {e}")
            return []

    @staticmethod
    def update_task(task_id, new_task_name=None, new_description=None, new_due_date=None, new_priority=None,
                    new_status=None, new_event_id=None):
        try:
            task = session.query(Tasks).filter_by(TaskID=task_id).first()
            if task:
                if new_task_name:
                    task.TaskName = new_task_name
                if new_description:
                    task.Description = new_description
                if new_due_date:
                    task.DueDate = new_due_date
                if new_priority:
                    task.Priority = new_priority
                if new_status:
                    task.Status = new_status
                if new_event_id:
                    task.EventID = new_event_id
                session.commit()
                return task
            return None
        except SQLAlchemyError as e:
            session.rollback()
            print(f"Error updating task: {e}")
            return None

    @staticmethod
    def delete_task(task_id):
        try:
            task = session.query(Tasks).filter_by(TaskID=task_id).first()
            if task:
                session.delete(task)
                session.commit()
                return True
            return False
        except SQLAlchemyError as e:
            session.rollback()
            print(f"Error deleting task: {e}")
            return False

    @staticmethod
    def get_task_by_id(task_id):
        try:
            return session.query(Tasks).filter_by(TaskID=task_id).first()
        except SQLAlchemyError as e:
            print(f"Error getting task by ID: {e}")
            return None

    @staticmethod
    def search_tasks_by_name(task_name):
        try:
            return session.query(Tasks).filter(Tasks.TaskName.ilike(f"%{task_name}%")).all()
        except SQLAlchemyError as e:
            print(f"Error searching tasks by name: {e}")
            return []

    @staticmethod
    def search_tasks_by_description(description):
        try:
            return session.query(Tasks).filter(Tasks.Description.ilike(f"%{description}%")).all()
        except SQLAlchemyError as e:
            print(f"Error searching tasks by description: {e}")
            return []

    @staticmethod
    def search_tasks_by_event_id(event_id):
        try:
            return session.query(Tasks).filter(Tasks.EventID == event_id).all()
        except SQLAlchemyError as e:
            print(f"Error searching tasks by event ID: {e}")
            return []
