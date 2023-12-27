from PyQt5.QtWidgets import QDialog
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QMessageBox, QTableView
from sqlalchemy.exc import SQLAlchemyError

from DataBase.DataBaseClassesMethods.EventsMethods import EventManager
from AppDataBase.AppDataBaseUI.EventsWindowsUI.EventsWindow import Ui_EventsWindow
from AppDataBase.AppDataBaseFunctions.EventsWindowsFunctions.EventsCreateWindowFunctions import EventsCreateDialog
from AppDataBase.AppDataBaseFunctions.EventsWindowsFunctions.EventsDeleteWindowFunctions import EventsDeleteDialog
from AppDataBase.AppDataBaseFunctions.EventsWindowsFunctions.EventsUpdateWindowFunctions import EventsUpdateDialog


class EventsWindowDialog(QDialog, Ui_EventsWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setup_connections()
        self.load_events_table()

    def setup_connections(self):
        self.CreateEventButton.clicked.connect(self.create_event)
        self.DeleteEventButton.clicked.connect(self.delete_event)
        self.UpdateEventButton.clicked.connect(self.update_event)
        self.CancelButton.clicked.connect(self.close)
        self.UpdateTheTableButton.clicked.connect(self.load_events_table)

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

            self.ViewingEventsTableView.setModel(model)
            self.ViewingEventsTableView.setSelectionBehavior(QTableView.SelectRows)
        except SQLAlchemyError as e:
            QMessageBox.critical(self, 'Error', f'Error loading events: {str(e)}')

    @staticmethod
    def create_event():
        create_dialog = EventsCreateDialog()
        create_dialog.exec_()

    @staticmethod
    def delete_event():
        delete_dialog = EventsDeleteDialog()
        delete_dialog.exec_()

    @staticmethod
    def update_event():
        update_dialog = EventsUpdateDialog()
        update_dialog.exec_()
