from PyQt5.QtWidgets import QMainWindow, QMessageBox, QApplication, QTableView
from PyQt5.QtGui import QStandardItemModel, QStandardItem

from AppDataBase.AppDataBase import Ui_DailyPlanner
from AppDataBase.AppDataBaseFunctions.ContactsWindowsFunctions.ContactsCreateWindowFunctions import ContactsCreateDialog
from AppDataBase.AppDataBaseFunctions.ContactsWindowsFunctions.ContactsDeleteWindowFunctions import ContactsDeleteDialog
from AppDataBase.AppDataBaseFunctions.ContactsWindowsFunctions.ContactsUpdateWindowFunctions import ContactsUpdateDialog
from AppDataBase.AppDataBaseFunctions.ContactsWindowsFunctions.ContactsWindowFunctions import ContactsWindowDialog
from AppDataBase.AppDataBaseFunctions.EventsWindowsFunctions.EventsCreateWindowFunctions import EventsCreateDialog
from AppDataBase.AppDataBaseFunctions.EventsWindowsFunctions.EventsDeleteWindowFunctions import EventsDeleteDialog
from AppDataBase.AppDataBaseFunctions.EventsWindowsFunctions.EventsUpdateWindowFunctions import EventsUpdateDialog
from AppDataBase.AppDataBaseFunctions.EventsWindowsFunctions.EventsWindowFunctions import EventsWindowDialog
from AppDataBase.AppDataBaseFunctions.NotesWindowsFunctions.NotesCreateWindowFunctions import NotesCreateDialog
from AppDataBase.AppDataBaseFunctions.NotesWindowsFunctions.NotesDeleteWindowFunctions import NotesDeleteDialog
from AppDataBase.AppDataBaseFunctions.NotesWindowsFunctions.NotesUpdateWindowFunctions import NotesUpdateDialog
from AppDataBase.AppDataBaseFunctions.NotesWindowsFunctions.NotesWindowFunctions import NotesWindowDialog
from AppDataBase.AppDataBaseFunctions.TasksWindowsFunctions.TasksCreateWindowFunctions import TasksCreateDialog
from AppDataBase.AppDataBaseFunctions.TasksWindowsFunctions.TasksDeleteWindowFunctions import TasksDeleteDialog
from AppDataBase.AppDataBaseFunctions.TasksWindowsFunctions.TasksUpdateWindowFunctions import TasksUpdateDialog
from AppDataBase.AppDataBaseFunctions.TasksWindowsFunctions.TasksWindowFunctions import TasksWindowDialog
from DataBase.DataBaseClassesMethods.EventsMethods import EventManager
from DataBase.DataBaseClassesMethods.TasksMethods import TaskManager
from DataBase.DataBaseClassesMethods.NotesMethods import NoteManager
from DataBase.DataBaseClassesMethods.ContactsMethods import ContactManager


class DailyPlannerFunctions(QMainWindow, Ui_DailyPlanner):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setup_connections()
        self.load_events()

        self.EventsTableView.clicked.connect(self.load_tasks)
        self.EventsTableView.clicked.connect(self.load_contacts)
        self.TasksForTheEventsTableView.clicked.connect(self.load_notes)

        self.ActionCreateEvent.triggered.connect(self.open_create_event_dialog)
        self.ActionCreateTask.triggered.connect(self.open_create_task_dialog)
        self.ActionCreateContact.triggered.connect(self.open_create_contact_dialog)
        self.ActionCreateNote.triggered.connect(self.open_create_note_dialog)

        self.ActionUpdateEvent.triggered.connect(self.open_update_event_dialog)
        self.ActionUpdateTask.triggered.connect(self.open_update_task_dialog)
        self.ActionUpdateContact.triggered.connect(self.open_update_contact_dialog)
        self.ActionUpdateNote.triggered.connect(self.open_update_note_dialog)

        self.ActionDeleteEvent.triggered.connect(self.open_delete_event_dialog)
        self.ActionDeleteTask.triggered.connect(self.open_delete_task_dialog)
        self.ActionDeleteContact.triggered.connect(self.open_delete_contact_dialog)
        self.ActionDeleteNote.triggered.connect(self.open_delete_note_dialog)

    def setup_connections(self):
        self.EventsButton.clicked.connect(self.open_events_dialog)
        self.TasksButton.clicked.connect(self.open_tasks_dialog)
        self.ContactsButton.clicked.connect(self.open_contacts_dialog)
        self.NotesButton.clicked.connect(self.open_notes_dialog)
        self.CancelButton.clicked.connect(self.close)
        self.UpdateTheTablesButton.clicked.connect(self.update_the_tables)

    def load_events(self):
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
        except Exception as e:
            QMessageBox.critical(self, 'Error', f'Error loading events: {str(e)}')

    def load_tasks(self):
        try:
            selected_row = self.EventsTableView.currentIndex().row()
            if selected_row >= 0:
                event_id = self.EventsTableView.model().index(selected_row, 0).data()
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

                    priority_item = QStandardItem(str(task.Priority))
                    model.setItem(row, 4, priority_item)

                    status_item = QStandardItem(task.Status)
                    model.setItem(row, 5, status_item)

                self.TasksForTheEventsTableView.setModel(model)
                self.TasksForTheEventsTableView.setSelectionBehavior(QTableView.SelectRows)
        except Exception as e:
            QMessageBox.critical(self, 'Error', f'Error loading tasks: {str(e)}')

    def load_contacts(self):
        try:
            selected_row = self.EventsTableView.currentIndex().row()
            if selected_row >= 0:
                event_id = self.EventsTableView.model().index(selected_row, 0).data()
                contacts = ContactManager.search_contacts_by_event_id(event_id) if event_id else []

                model = QStandardItemModel(len(contacts), 5)
                model.setHorizontalHeaderLabels(["Contact ID", "Full Name", "Phone", "Email", "Address"])

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

                self.ContactForTheEventTableView.setModel(model)
                self.ContactForTheEventTableView.setSelectionBehavior(QTableView.SelectRows)
        except Exception as e:
            QMessageBox.critical(self, 'Error', f'Error loading contacts: {str(e)}')

    def load_notes(self):
        try:
            selected_row = self.TasksForTheEventsTableView.currentIndex().row()
            if selected_row >= 0:
                task_id = self.TasksForTheEventsTableView.model().index(selected_row, 0).data()
                notes = NoteManager.search_notes_by_task_id(task_id) if task_id else []

                model = QStandardItemModel(len(notes), 4)
                model.setHorizontalHeaderLabels(["Note ID", "Title", "Content", "Created Date"])

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
        except Exception as e:
            QMessageBox.critical(self, 'Error', f'Error loading notes: {str(e)}')

    def update_the_tables(self):
        self.load_events()
        self.load_tasks()
        self.load_contacts()
        self.load_notes()

    @staticmethod
    def open_events_dialog():
        events_window = EventsWindowDialog()
        events_window.exec_()

    @staticmethod
    def open_tasks_dialog():
        tasks_window = TasksWindowDialog()
        tasks_window.exec_()

    @staticmethod
    def open_contacts_dialog():
        contacts_window = ContactsWindowDialog()
        contacts_window.exec_()

    @staticmethod
    def open_notes_dialog():
        notes_window = NotesWindowDialog()
        notes_window.exec_()

    @staticmethod
    def open_create_event_dialog():
        create_event_dialog = EventsCreateDialog()
        create_event_dialog.exec_()

    @staticmethod
    def open_create_task_dialog():
        create_task_dialog = TasksCreateDialog()
        create_task_dialog.exec_()

    @staticmethod
    def open_create_contact_dialog():
        create_contact_dialog = ContactsCreateDialog()
        create_contact_dialog.exec_()

    @staticmethod
    def open_create_note_dialog():
        create_note_dialog = NotesCreateDialog()
        create_note_dialog.exec_()

    @staticmethod
    def open_update_event_dialog():
        update_event_dialog = EventsUpdateDialog()
        update_event_dialog.exec_()

    @staticmethod
    def open_update_task_dialog():
        update_task_dialog = TasksUpdateDialog()
        update_task_dialog.exec_()

    @staticmethod
    def open_update_contact_dialog():
        update_contact_dialog = ContactsUpdateDialog()
        update_contact_dialog.exec_()

    @staticmethod
    def open_update_note_dialog():
        update_note_dialog = NotesUpdateDialog()
        update_note_dialog.exec_()

    @staticmethod
    def open_delete_event_dialog():
        delete_event_dialog = EventsDeleteDialog()
        delete_event_dialog.exec_()

    @staticmethod
    def open_delete_task_dialog():
        delete_task_dialog = TasksDeleteDialog()
        delete_task_dialog.exec_()

    @staticmethod
    def open_delete_contact_dialog():
        delete_contact_dialog = ContactsDeleteDialog()
        delete_contact_dialog.exec_()

    @staticmethod
    def open_delete_note_dialog():
        delete_note_dialog = NotesDeleteDialog()
        delete_note_dialog.exec_()


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = DailyPlannerFunctions()
    window.show()
    sys.exit(app.exec_())
