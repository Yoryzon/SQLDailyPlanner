from PyQt5.QtWidgets import QDialog, QMessageBox
from datetime import datetime

from sqlalchemy.exc import SQLAlchemyError

from AppDataBase.AppDataBaseUI.EventsWindowsUI.EventsCreateWindow import Ui_EventsCreateWindow
from DataBase.DataBaseClassesMethods.EventsMethods import EventManager


class EventsCreateDialog(QDialog, Ui_EventsCreateWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setup_connections()

    def setup_connections(self):
        self.EventCreateButton.clicked.connect(self.confirm_create)
        self.CancelButton.clicked.connect(self.cancel_event)

    def confirm_create(self):
        confirmation = QMessageBox.question(self, 'Confirmation', 'Are you sure you want to create a new event?',
                                            QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if confirmation == QMessageBox.Yes:
            self.create_event()
        else:
            pass

    def create_event(self):
        try:
            title = self.TitlePlainTextEdit.toPlainText()
            description = self.DescriptionPlainTextEdit.toPlainText()
            event_date = self.EventDateEdit.date().toPyDate()
            start_time = self.StartTimeEdit.time().toPyTime()
            end_time = self.EndTimeEdit.time().toPyTime()

            event_date = datetime.combine(event_date, datetime.min.time())
            start_time = datetime.combine(datetime.today(), start_time)
            end_time = datetime.combine(datetime.today(), end_time)

            new_event = EventManager.create_event(title, description, event_date, start_time, end_time)

            if new_event:
                QMessageBox.information(self, 'Success', 'Event created successfully.')
                self.close()
            else:
                QMessageBox.critical(self, 'Error', 'Failed to create event.')
        except SQLAlchemyError as e:
            QMessageBox.critical(self, 'Error', f'Failed to create event: {str(e)}')

    def cancel_event(self):
        self.close()
