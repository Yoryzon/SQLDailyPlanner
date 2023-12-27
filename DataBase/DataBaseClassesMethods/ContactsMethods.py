from sqlalchemy.exc import SQLAlchemyError

from DataBase.DataBaseConnection.DataBaseMeta import Base, Engine, SessionFactory
from DataBase.DataBaseClasses.Contacts import Contacts

Base.metadata.create_all(Engine)
session = SessionFactory()


class ContactManager:
    @staticmethod
    def create_contact(full_name, phone, email, address, event_id):
        try:
            new_contact = Contacts(FullName=full_name, Phone=phone, Email=email, Address=address, EventID=event_id)
            session.add(new_contact)
            session.commit()
            return new_contact
        except SQLAlchemyError as e:
            session.rollback()
            print(f"Error creating contact: {e}")
            return None

    @staticmethod
    def get_all_contacts():
        try:
            return session.query(Contacts).all()
        except SQLAlchemyError as e:
            print(f"Error getting all contacts: {e}")
            return []

    @staticmethod
    def update_contact(contact_id, new_full_name=None, new_phone=None, new_email=None, new_address=None,
                       new_event_id=None):
        try:
            contact = session.query(Contacts).filter_by(ContactID=contact_id).first()
            if contact:
                if new_full_name:
                    contact.FullName = new_full_name
                if new_phone:
                    contact.Phone = new_phone
                if new_email:
                    contact.Email = new_email
                if new_address:
                    contact.Address = new_address
                if new_event_id:
                    contact.EventID = new_event_id
                session.commit()
                return contact
            return None
        except SQLAlchemyError as e:
            session.rollback()
            print(f"Error updating contact: {e}")
            return None

    @staticmethod
    def delete_contact(contact_id):
        try:
            contact = session.query(Contacts).filter_by(ContactID=contact_id).first()
            if contact:
                session.delete(contact)
                session.commit()
                return True
            return False
        except SQLAlchemyError as e:
            session.rollback()
            print(f"Error deleting contact: {e}")
            return False

    @staticmethod
    def get_contact_by_id(contact_id):
        try:
            return session.query(Contacts).filter_by(ContactID=contact_id).first()
        except SQLAlchemyError as e:
            print(f"Error getting contact by ID: {e}")
            return None

    @staticmethod
    def search_contacts_by_full_name(full_name):
        try:
            return session.query(Contacts).filter(Contacts.FullName.ilike(f"%{full_name}%")).all()
        except SQLAlchemyError as e:
            print(f"Error searching contacts by full name: {e}")
            return []

    @staticmethod
    def search_contacts_by_email(email):
        try:
            return session.query(Contacts).filter(Contacts.Email.ilike(f"%{email}%")).all()
        except SQLAlchemyError as e:
            print(f"Error searching contacts by email: {e}")
            return []

    @staticmethod
    def search_contacts_by_event_id(event_id):
        try:
            return session.query(Contacts).filter(Contacts.EventID == event_id).all()
        except SQLAlchemyError as e:
            print(f"Error searching tasks by event ID: {e}")
            return []
