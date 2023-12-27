from PyQt5.QtWidgets import QDialog, QMessageBox, QTableView
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from sqlalchemy.exc import SQLAlchemyError

from DataBase.DataBaseClassesMethods.ContactsMethods import ContactManager
from DataBase.DataBaseClassesMethods.EventsMethods import EventManager
from AppDataBase.AppDataBaseUI.ContactsWindowsUI.ContactsCreateWindow import Ui_ContactsCreateWindow


class ContactsCreateDialog(QDialog, Ui_ContactsCreateWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setup_connections()
        self.load_events_table()

    def setup_connections(self):
        self.CreateContactButton.clicked.connect(self.confirm_create_contact)
        self.CancelButton.clicked.connect(self.cancel_contact)

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

    def confirm_create_contact(self):
        confirmation = QMessageBox.question(
            self, 'Confirmation', 'Are you sure you want to create the contact?',
            QMessageBox.Yes | QMessageBox.No, QMessageBox.No
        )
        if confirmation == QMessageBox.Yes:
            self.create_contact()
        else:
            pass

    def create_contact(self):
        try:
            selected_row = self.EventsTableView.currentIndex().row()

            if selected_row >= 0:
                model = self.EventsTableView.model()
                event_id = model.index(selected_row, 0).data()

                existing_contact = ContactManager.search_contacts_by_event_id(event_id)
                if existing_contact:
                    QMessageBox.warning(self, 'Warning', 'Contact already exists for this event.')
                    return

                full_name = self.FullNamePlainTextEdit.toPlainText()
                phone = self.PhonePlainTextEdit.toPlainText()
                email = self.EmailPlainTextEdit.toPlainText()
                address = self.AddressPlainTextEdit.toPlainText()

                new_contact = ContactManager.create_contact(full_name, phone, email, address, event_id)

                if new_contact:
                    QMessageBox.information(self, 'Success', 'Contact created successfully.')
                    self.close()
                else:
                    QMessageBox.critical(self, 'Error', 'Failed to create contact.')
            else:
                QMessageBox.warning(self, 'Warning', 'Please select an event to create a contact.')

        except SQLAlchemyError as e:
            QMessageBox.critical(self, 'Error', f'Error creating contact: {str(e)}')

    def cancel_contact(self):
        self.close()
