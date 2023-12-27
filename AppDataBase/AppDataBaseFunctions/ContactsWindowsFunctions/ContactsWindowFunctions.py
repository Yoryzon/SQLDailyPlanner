from PyQt5.QtWidgets import QDialog, QMessageBox, QTableView
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from sqlalchemy.exc import SQLAlchemyError

from DataBase.DataBaseClassesMethods.ContactsMethods import ContactManager
from DataBase.DataBaseClassesMethods.EventsMethods import EventManager
from AppDataBase.AppDataBaseUI.ContactsWindowsUI.ContactsWindow import Ui_ContactsWindow
from AppDataBase.AppDataBaseFunctions.ContactsWindowsFunctions.ContactsCreateWindowFunctions import ContactsCreateDialog
from AppDataBase.AppDataBaseFunctions.ContactsWindowsFunctions.ContactsUpdateWindowFunctions import ContactsUpdateDialog
from AppDataBase.AppDataBaseFunctions.ContactsWindowsFunctions.ContactsDeleteWindowFunctions import ContactsDeleteDialog


class ContactsWindowDialog(QDialog, Ui_ContactsWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setup_connections()
        self.load_events_table()
        self.load_contacts_table(None)

    def setup_connections(self):
        self.CreateContactButton.clicked.connect(self.open_create_contact_dialog)
        self.UpdateContactButton.clicked.connect(self.open_update_contact_dialog)
        self.DeleteContactButton.clicked.connect(self.open_delete_contact_dialog)
        self.CancelButton.clicked.connect(self.cancel_action)
        self.EventsTableView.clicked.connect(self.load_contacts_for_selected_event)

    def load_events_table(self):
        try:
            events = EventManager.get_all_events()

            model = QStandardItemModel(len(events), 6)
            model.setHorizontalHeaderLabels(
                ["Event ID", "Title", "Description", "Event Date", "Start Time", "End Time"])

            for row, event in enumerate(events):
                event_id_item = QStandardItem(str(event.EventID))
                event_id_item.setEditable(False)
                model.setItem(row, 0, event_id_item)

                title_item = QStandardItem(event.Title)
                model.setItem(row, 1, title_item)

                description_item = QStandardItem(event.Description)
                model.setItem(row, 2, description_item)

                event_date_item = QStandardItem(str(event.EventDate))
                model.setItem(row, 3, event_date_item)

                start_time_item = QStandardItem(str(event.StartTime))
                model.setItem(row, 4, start_time_item)

                end_time_item = QStandardItem(str(event.EndTime))
                model.setItem(row, 5, end_time_item)

            self.EventsTableView.setModel(model)
            self.EventsTableView.setSelectionBehavior(QTableView.SelectRows)
        except SQLAlchemyError as e:
            QMessageBox.critical(self, 'Error', f'Error loading events: {str(e)}')

    def load_contacts_for_selected_event(self):
        try:
            selected_row = self.EventsTableView.currentIndex().row()
            if selected_row >= 0:
                event_id = self.EventsTableView.model().index(selected_row, 0).data()
                self.load_contacts_table(event_id)
        except SQLAlchemyError as e:
            QMessageBox.critical(self, 'Error', f'Error loading contacts for selected event: {str(e)}')

    def load_contacts_table(self, event_id):
        try:
            contacts = ContactManager.search_contacts_by_event_id(event_id) if event_id else []

            model = QStandardItemModel(len(contacts), 6)
            model.setHorizontalHeaderLabels(
                ["Contact ID", "Full Name", "Phone", "Email", "Address", "Event ID"])

            for row, contact in enumerate(contacts):
                contact_id_item = QStandardItem(str(contact.ContactID))
                contact_id_item.setEditable(False)
                model.setItem(row, 0, contact_id_item)

                full_name_item = QStandardItem(contact.FullName)
                model.setItem(row, 1, full_name_item)

                phone_item = QStandardItem(contact.Phone)
                model.setItem(row, 2, phone_item)

                email_item = QStandardItem(contact.Email)
                model.setItem(row, 3, email_item)

                address_item = QStandardItem(contact.Address)
                model.setItem(row, 4, address_item)

                event_id_item = QStandardItem(str(contact.EventID))
                model.setItem(row, 5, event_id_item)

            self.ContactsForTheEventTableView.setModel(model)
            self.ContactsForTheEventTableView.setSelectionBehavior(QTableView.SelectRows)
        except SQLAlchemyError as e:
            QMessageBox.critical(self, 'Error', f'Error loading contacts: {str(e)}')

    @staticmethod
    def open_create_contact_dialog():
        create_contact_dialog = ContactsCreateDialog()
        create_contact_dialog.exec_()

    @staticmethod
    def open_update_contact_dialog():
        update_contact_dialog = ContactsUpdateDialog()
        update_contact_dialog.exec_()

    @staticmethod
    def open_delete_contact_dialog():
        delete_contact_dialog = ContactsDeleteDialog()
        delete_contact_dialog.exec_()

    def cancel_action(self):
        self.close()
