from PyQt5.QtWidgets import QDialog, QMessageBox, QTableView
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from sqlalchemy.exc import SQLAlchemyError

from DataBase.DataBaseClassesMethods.NotesMethods import NoteManager
from DataBase.DataBaseClassesMethods.TasksMethods import TaskManager
from AppDataBase.AppDataBaseUI.NotesWindowsUI.NotesWindow import Ui_NotesWindow
from AppDataBase.AppDataBaseFunctions.NotesWindowsFunctions.NotesCreateWindowFunctions import NotesCreateDialog
from AppDataBase.AppDataBaseFunctions.NotesWindowsFunctions.NotesUpdateWindowFunctions import NotesUpdateDialog
from AppDataBase.AppDataBaseFunctions.NotesWindowsFunctions.NotesDeleteWindowFunctions import NotesDeleteDialog


class NotesWindowDialog(QDialog, Ui_NotesWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setup_connections()
        self.load_tasks_table()
        self.load_notes_table(None)

    def setup_connections(self):
        self.CreateNoteButton.clicked.connect(self.open_create_note_dialog)
        self.UpdateNoteButton.clicked.connect(self.open_update_note_dialog)
        self.DeleteNoteButton.clicked.connect(self.open_delete_note_dialog)
        self.CancelButton.clicked.connect(self.cancel_action)
        self.TasksTableView.clicked.connect(self.load_notes_for_selected_task)

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

    def load_notes_for_selected_task(self):
        try:
            selected_row = self.TasksTableView.currentIndex().row()
            if selected_row >= 0:
                task_id = self.TasksTableView.model().index(selected_row, 0).data()
                self.load_notes_table(task_id)
        except SQLAlchemyError as e:
            QMessageBox.critical(self, 'Error', f'Error loading notes for selected task: {str(e)}')

    def load_notes_table(self, task_id):
        try:
            notes = NoteManager.search_notes_by_task_id(task_id) if task_id else []

            model = QStandardItemModel(len(notes), 4)
            model.setHorizontalHeaderLabels(
                ["Note ID", "Title", "Content", "Created Date"])

            for row, note in enumerate(notes):
                note_id_item = QStandardItem(str(note.NoteID))
                note_id_item.setEditable(False)
                model.setItem(row, 0, note_id_item)

                title_item = QStandardItem(note.Title)
                model.setItem(row, 1, title_item)

                content_item = QStandardItem(note.Content)
                model.setItem(row, 2, content_item)

                created_date_item = QStandardItem(str(note.CreatedDate))
                model.setItem(row, 3, created_date_item)

            self.NotesForTheTaskTableView.setModel(model)
            self.NotesForTheTaskTableView.setSelectionBehavior(QTableView.SelectRows)

        except SQLAlchemyError as e:
            QMessageBox.critical(self, 'Error', f'Error loading notes: {str(e)}')

    @staticmethod
    def open_create_note_dialog():
        create_note_dialog = NotesCreateDialog()
        create_note_dialog.exec_()

    @staticmethod
    def open_update_note_dialog():
        update_note_dialog = NotesUpdateDialog()
        update_note_dialog.exec_()

    @staticmethod
    def open_delete_note_dialog():
        delete_note_dialog = NotesDeleteDialog()
        delete_note_dialog.exec_()

    def cancel_action(self):
        self.close()
