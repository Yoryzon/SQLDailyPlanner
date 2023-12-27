from PyQt5.QtWidgets import QDialog, QMessageBox, QTableView
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from sqlalchemy.exc import SQLAlchemyError

from AppDataBase.AppDataBaseUI.TasksWindowsUI.TasksCreateWindow import Ui_TasksCreateWindow
from DataBase.DataBaseClassesMethods.TasksMethods import TaskManager
from DataBase.DataBaseClassesMethods.EventsMethods import EventManager


class TasksCreateDialog(QDialog, Ui_TasksCreateWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setup_connections()
        self.load_events_table()

    def setup_connections(self):
        self.CreateTaskButton.clicked.connect(self.confirm_create_task)
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

    def confirm_create_task(self):
        confirmation = QMessageBox.question(
            self, 'Confirmation', 'Are you sure you want to create the task?',
            QMessageBox.Yes | QMessageBox.No, QMessageBox.No
        )
        if confirmation == QMessageBox.Yes:
            self.create_task()
        else:
            pass

    def create_task(self):
        try:
            selected_row = self.EventsTableView.currentIndex().row()

            if selected_row >= 0:
                model = self.EventsTableView.model()
                event_id = model.index(selected_row, 0).data()

                task_name = self.TaskNamePlainTextEdit.toPlainText()
                description = self.DescriptionPlainTextEdit.toPlainText()
                due_date = self.DueDateDateEdit.date().toPyDate()
                priority = self.PriorityComboBox.currentText()
                status = self.StatusComboBox.currentText()

                new_task = TaskManager.create_task(task_name, description, due_date, priority, status, event_id)

                if new_task:
                    QMessageBox.information(self, 'Success', 'Task created successfully.')
                    self.close()
                else:
                    QMessageBox.critical(self, 'Error', 'Failed to create task.')
            else:
                QMessageBox.warning(self, 'Warning', 'Please select an event to create a task.')

        except SQLAlchemyError as e:
            QMessageBox.critical(self, 'Error', f'Error creating task: {str(e)}')

    def cancel_event(self):
        self.close()
