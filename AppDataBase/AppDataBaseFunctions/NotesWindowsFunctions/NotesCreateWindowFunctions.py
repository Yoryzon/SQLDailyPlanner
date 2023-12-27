from PyQt5.QtWidgets import QDialog, QMessageBox, QTableView
from PyQt5.QtGui import QStandardItemModel, QStandardItem

from sqlalchemy.exc import SQLAlchemyError

from AppDataBase.AppDataBaseUI.NotesWindowsUI.NotesCreateWindow import Ui_NotesCreateWindow
from DataBase.DataBaseClassesMethods.NotesMethods import NoteManager
from DataBase.DataBaseClassesMethods.TasksMethods import TaskManager


class NotesCreateDialog(QDialog, Ui_NotesCreateWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setup_connections()
        self.load_tasks_table()

    def setup_connections(self):
        self.CreateNoteButton.clicked.connect(self.confirm_create_note)
        self.CancelButton.clicked.connect(self.cancel_note)

    def load_tasks_table(self):
        try:
            tasks = TaskManager.get_all_tasks()

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

            self.TasksTableView.setModel(model)
            self.TasksTableView.setSelectionBehavior(QTableView.SelectRows)

        except SQLAlchemyError as e:
            QMessageBox.critical(self, 'Error', f'Error loading tasks: {str(e)}')

    def confirm_create_note(self):
        confirmation = QMessageBox.question(
            self, 'Confirmation', 'Are you sure you want to create the note?',
            QMessageBox.Yes | QMessageBox.No, QMessageBox.No
        )
        if confirmation == QMessageBox.Yes:
            self.create_note()
        else:
            pass

    def create_note(self):
        try:
            selected_row = self.TasksTableView.currentIndex().row()

            if selected_row >= 0:
                model = self.TasksTableView.model()
                task_id = model.index(selected_row, 0).data()

                title = self.TitlePlainTextEdit.toPlainText()
                content = self.ContentPlainTextEdit.toPlainText()
                created_date = self.CreatedDateEdit.date().toPyDate()

                new_note = NoteManager.create_note(title, content, created_date, task_id)

                if new_note:
                    QMessageBox.information(self, 'Success', 'Note created successfully.')
                    self.close()
                else:
                    QMessageBox.critical(self, 'Error', 'Failed to create note.')
            else:
                QMessageBox.warning(self, 'Warning', 'Please select a task to create a note.')

        except SQLAlchemyError as e:
            QMessageBox.critical(self, 'Error', f'Error creating note: {str(e)}')

    def cancel_note(self):
        self.close()
