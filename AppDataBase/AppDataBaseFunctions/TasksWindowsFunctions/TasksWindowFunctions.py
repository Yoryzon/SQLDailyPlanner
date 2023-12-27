from PyQt5.QtWidgets import QDialog, QMessageBox, QApplication, QTableView
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from sqlalchemy.exc import SQLAlchemyError

from DataBase.DataBaseClassesMethods.TasksMethods import TaskManager
from DataBase.DataBaseClassesMethods.EventsMethods import EventManager
from AppDataBase.AppDataBaseUI.TasksWindowsUI.TasksWindow import Ui_TasksWindow
from AppDataBase.AppDataBaseFunctions.TasksWindowsFunctions.TasksCreateWindowFunctions import TasksCreateDialog
from AppDataBase.AppDataBaseFunctions.TasksWindowsFunctions.TasksUpdateWindowFunctions import TasksUpdateDialog
from AppDataBase.AppDataBaseFunctions.TasksWindowsFunctions.TasksDeleteWindowFunctions import TasksDeleteDialog


class TasksWindowDialog(QDialog, Ui_TasksWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setup_connections()
        self.load_events_table()
        self.load_tasks_table(None)

    def setup_connections(self):
        self.CreateTaskButton.clicked.connect(self.open_create_task_dialog)
        self.UpdateTaskButton.clicked.connect(self.open_update_task_dialog)
        self.DeleteTaskButton.clicked.connect(self.open_delete_task_dialog)
        self.CancelButton.clicked.connect(self.cancel_action)
        self.EventsTableView.clicked.connect(self.load_tasks_for_selected_event)

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

    def load_tasks_for_selected_event(self):
        try:
            selected_row = self.EventsTableView.currentIndex().row()
            if selected_row >= 0:
                event_id = self.EventsTableView.model().index(selected_row, 0).data()
                self.load_tasks_table(event_id)
        except SQLAlchemyError as e:
            QMessageBox.critical(self, 'Error', f'Error loading tasks for selected event: {str(e)}')

    def load_tasks_table(self, event_id):
        try:
            tasks = TaskManager.search_tasks_by_event_id(event_id) if event_id else []

            model = QStandardItemModel(len(tasks), 6)
            model.setHorizontalHeaderLabels(
                ["Task ID", "Task Name", "Description", "Due Date", "Priority", "Status"])

            for row, task in enumerate(tasks):
                task_id_item = QStandardItem(str(task.TaskID))
                task_id_item.setEditable(False)
                model.setItem(row, 0, task_id_item)

                task_name_item = QStandardItem(task.TaskName)
                model.setItem(row, 1, task_name_item)

                description_item = QStandardItem(task.Description)
                model.setItem(row, 2, description_item)

                due_date_item = QStandardItem(str(task.DueDate))
                model.setItem(row, 3, due_date_item)

                priority_item = QStandardItem(task.Priority)
                model.setItem(row, 4, priority_item)

                status_item = QStandardItem(task.Status)
                model.setItem(row, 5, status_item)

            self.TasksForTheEventTableView.setModel(model)
            self.TasksForTheEventTableView.setSelectionBehavior(QTableView.SelectRows)
        except SQLAlchemyError as e:
            QMessageBox.critical(self, 'Error', f'Error loading tasks: {str(e)}')

    @staticmethod
    def open_create_task_dialog():
        create_task_dialog = TasksCreateDialog()
        create_task_dialog.exec_()

    @staticmethod
    def open_update_task_dialog():
        update_task_dialog = TasksUpdateDialog()
        update_task_dialog.exec_()

    @staticmethod
    def open_delete_task_dialog():
        delete_task_dialog = TasksDeleteDialog()
        delete_task_dialog.exec_()

    def cancel_action(self):
        self.close()


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = TasksWindowDialog()
    window.show()
    sys.exit(app.exec_())
