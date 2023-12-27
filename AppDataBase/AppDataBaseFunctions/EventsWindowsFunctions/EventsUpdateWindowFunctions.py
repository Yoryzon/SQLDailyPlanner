from PyQt5.QtWidgets import QDialog, QMessageBox, QTableView
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from sqlalchemy.exc import SQLAlchemyError

from AppDataBase.AppDataBaseUI.EventsWindowsUI.EventsUpdateWindow import Ui_EventsUpdateWindow
from DataBase.DataBaseClassesMethods.EventsMethods import EventManager


class EventsUpdateDialog(QDialog, Ui_EventsUpdateWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.load_events_table()
        self.setup_connections()

    def setup_connections(self):
        self.UpdateEventButton.clicked.connect(self.confirm_update)
        self.CancelButton.clicked.connect(self.cancel_event)

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

    def confirm_update(self):
        confirmation = QMessageBox.question(self, 'Confirmation', 'Are you sure you want to update the selected event?',
                                            QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if confirmation == QMessageBox.Yes:
            self.update_selected_event()
        else:
            pass

    def update_selected_event(self):
        selected_row = self.EventsTableView.currentIndex().row()

        if selected_row >= 0:
            try:
                model = self.EventsTableView.model()
                event_id = model.index(selected_row, 0).data()

                updated_title = self.TitlePlainTextEdit.toPlainText()
                updated_description = self.DescriptionPlainTextEdit.toPlainText()
                updated_event_date = self.EventDateEdit.date().toString(Qt.ISODate)
                updated_start_time = self.StartTimeEdit.time().toString(Qt.ISODate)
                updated_end_time = self.EndTimeEdit.time().toString(Qt.ISODate)

                EventManager.update_event(event_id, updated_title, updated_description,
                                          updated_event_date, updated_start_time, updated_end_time)

                self.load_events_table()

                QMessageBox.information(self, 'Success', 'Event updated successfully.')
                self.close()

            except SQLAlchemyError as e:
                QMessageBox.critical(self, 'Error', f'Error updating event: {str(e)}')

        else:
            QMessageBox.warning(self, 'Warning', 'Please select an event to update.')

    def cancel_event(self):
        self.close()
