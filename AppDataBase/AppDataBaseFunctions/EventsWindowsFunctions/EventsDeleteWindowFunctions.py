from PyQt5.QtWidgets import QDialog, QMessageBox, QTableView
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from sqlalchemy.exc import SQLAlchemyError

from AppDataBase.AppDataBaseUI.EventsWindowsUI.EventsDeleteWindow import Ui_EventsDeleteWindow
from DataBase.DataBaseClassesMethods.EventsMethods import EventManager


class EventsDeleteDialog(QDialog, Ui_EventsDeleteWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setup_connections()
        self.load_events_table()

    def setup_connections(self):
        self.EventDeleteButton.clicked.connect(self.confirm_delete)
        self.CancelButton.clicked.connect(self.cancel_event)

    def load_events_table(self):
        try:
            events = EventManager.get_all_events()

            model = QStandardItemModel(len(events), 6)

            model.setHorizontalHeaderLabels(["Event ID", "Title", "Description", "Event Date", "Start Time", "End Time"])

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

    def confirm_delete(self):
        confirmation = QMessageBox.question(self, 'Confirmation', 'Are you sure you want to delete the selected event?',
                                            QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if confirmation == QMessageBox.Yes:
            self.delete_selected_event()
        else:
            pass

    def delete_selected_event(self):
        selected_row = self.EventsTableView.currentIndex().row()

        if selected_row >= 0:
            try:
                model = self.EventsTableView.model()
                event_id_index = model.index(selected_row, 0)
                event_id = model.data(event_id_index, Qt.DisplayRole)

                deleted = EventManager.delete_event(event_id)

                if deleted:
                    QMessageBox.information(self, 'Success', 'Event deleted successfully.')
                    self.load_events_table()
                    self.close()
                else:
                    QMessageBox.warning(self, 'Error', 'Error deleting event.')
            except SQLAlchemyError as e:
                QMessageBox.critical(self, 'Error', f'Error deleting event: {str(e)}')
        else:
            QMessageBox.warning(self, 'Warning', 'Please select an event to delete.')

    def cancel_event(self):
        self.close()
