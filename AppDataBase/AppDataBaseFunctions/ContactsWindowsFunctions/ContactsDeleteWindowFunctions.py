from PyQt5.QtWidgets import QDialog, QMessageBox, QTableView
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from sqlalchemy.exc import SQLAlchemyError
from DataBase.DataBaseClassesMethods.ContactsMethods import ContactManager
from DataBase.DataBaseClassesMethods.EventsMethods import EventManager
from AppDataBase.AppDataBaseUI.ContactsWindowsUI.ContactsDeleteWindow import Ui_ContactsDeleteWindow


class ContactsDeleteDialog(QDialog, Ui_ContactsDeleteWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setup_connections()
        self.load_events_table()
        self.load_contacts_table(None)

    def setup_connections(self):
        self.DeleteContactButton.clicked.connect(self.confirm_delete)
        self.CancelButton.clicked.connect(self.cancel_deletion)
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

            model = QStandardItemModel(len(contacts), 5)
            model.setHorizontalHeaderLabels(
                ["Contact ID", "Full Name", "Phone", "Email", "Address"])

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

            self.ContactsForTheEventTableView.setModel(model)
            self.ContactsForTheEventTableView.setSelectionBehavior(QTableView.SelectRows)
        except SQLAlchemyError as e:
            QMessageBox.critical(self, 'Error', f'Error loading contacts: {str(e)}')

    def confirm_delete(self):
        try:
            selected_row = self.ContactsForTheEventTableView.currentIndex().row()
            if selected_row >= 0:
                contact_id = self.ContactsForTheEventTableView.model().index(selected_row, 0).data()

                confirmation = QMessageBox.question(
                    self, 'Confirmation', 'Are you sure you want to delete the selected contact?',
                    QMessageBox.Yes | QMessageBox.No, QMessageBox.No
                )
                if confirmation == QMessageBox.Yes:
                    deleted = ContactManager.delete_contact(contact_id)
                    if deleted:
                        QMessageBox.information(self, 'Success', 'Contact deleted successfully.')
                        self.load_contacts_for_selected_event()
                        self.close()
                    else:
                        QMessageBox.critical(self, 'Error', 'Error deleting contact.')
                else:
                    pass
            else:
                QMessageBox.warning(self, 'Warning', 'Please select a contact to delete.')
        except SQLAlchemyError as e:
            QMessageBox.critical(self, 'Error', f'Error confirming contact deletion: {str(e)}')

    def cancel_deletion(self):
        self.close()
