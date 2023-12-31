# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AppDataBase\AppDataBaseUI\TasksWindowsUI\TasksCreateWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TasksCreateWindow(object):
    def setupUi(self, TasksCreateWindow):
        TasksCreateWindow.setObjectName("TasksCreateWindow")
        TasksCreateWindow.resize(580, 510)
        TasksCreateWindow.setMinimumSize(QtCore.QSize(580, 510))
        TasksCreateWindow.setMaximumSize(QtCore.QSize(580, 510))
        self.CreateTaskGroupBox = QtWidgets.QGroupBox(TasksCreateWindow)
        self.CreateTaskGroupBox.setGeometry(QtCore.QRect(20, 10, 540, 480))
        self.CreateTaskGroupBox.setObjectName("CreateTaskGroupBox")
        self.TaskName = QtWidgets.QGroupBox(self.CreateTaskGroupBox)
        self.TaskName.setGeometry(QtCore.QRect(20, 20, 120, 110))
        self.TaskName.setObjectName("TaskName")
        self.TaskNamePlainTextEdit = QtWidgets.QPlainTextEdit(self.TaskName)
        self.TaskNamePlainTextEdit.setGeometry(QtCore.QRect(10, 20, 100, 80))
        self.TaskNamePlainTextEdit.setObjectName("TaskNamePlainTextEdit")
        self.DescriptionGroupBox = QtWidgets.QGroupBox(self.CreateTaskGroupBox)
        self.DescriptionGroupBox.setGeometry(QtCore.QRect(280, 20, 240, 170))
        self.DescriptionGroupBox.setObjectName("DescriptionGroupBox")
        self.DescriptionPlainTextEdit = QtWidgets.QPlainTextEdit(self.DescriptionGroupBox)
        self.DescriptionPlainTextEdit.setGeometry(QtCore.QRect(10, 20, 220, 140))
        self.DescriptionPlainTextEdit.setObjectName("DescriptionPlainTextEdit")
        self.DueDateGroupBox = QtWidgets.QGroupBox(self.CreateTaskGroupBox)
        self.DueDateGroupBox.setGeometry(QtCore.QRect(150, 80, 120, 50))
        self.DueDateGroupBox.setObjectName("DueDateGroupBox")
        self.DueDateDateEdit = QtWidgets.QDateEdit(self.DueDateGroupBox)
        self.DueDateDateEdit.setGeometry(QtCore.QRect(10, 20, 100, 20))
        self.DueDateDateEdit.setObjectName("DueDateDateEdit")
        self.PriorityGroupBox = QtWidgets.QGroupBox(self.CreateTaskGroupBox)
        self.PriorityGroupBox.setGeometry(QtCore.QRect(20, 140, 250, 50))
        self.PriorityGroupBox.setObjectName("PriorityGroupBox")
        self.PriorityComboBox = QtWidgets.QComboBox(self.PriorityGroupBox)
        self.PriorityComboBox.setGeometry(QtCore.QRect(10, 20, 230, 20))
        self.PriorityComboBox.setObjectName("PriorityComboBox")
        self.PriorityComboBox.addItem("")
        self.PriorityComboBox.addItem("")
        self.PriorityComboBox.addItem("")
        self.PriorityComboBox.addItem("")
        self.StatusGroupBox = QtWidgets.QGroupBox(self.CreateTaskGroupBox)
        self.StatusGroupBox.setGeometry(QtCore.QRect(150, 20, 120, 50))
        self.StatusGroupBox.setObjectName("StatusGroupBox")
        self.StatusComboBox = QtWidgets.QComboBox(self.StatusGroupBox)
        self.StatusComboBox.setGeometry(QtCore.QRect(10, 20, 100, 20))
        self.StatusComboBox.setObjectName("StatusComboBox")
        self.StatusComboBox.addItem("")
        self.StatusComboBox.addItem("")
        self.StatusComboBox.addItem("")
        self.EventsGroupBox = QtWidgets.QGroupBox(self.CreateTaskGroupBox)
        self.EventsGroupBox.setGeometry(QtCore.QRect(20, 200, 500, 210))
        self.EventsGroupBox.setObjectName("EventsGroupBox")
        self.EventsTableView = QtWidgets.QTableView(self.EventsGroupBox)
        self.EventsTableView.setGeometry(QtCore.QRect(10, 20, 480, 180))
        self.EventsTableView.setObjectName("EventsTableView")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.CreateTaskGroupBox)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 420, 500, 40))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.HorizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.HorizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.HorizontalLayout.setObjectName("HorizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.HorizontalLayout.addItem(spacerItem)
        self.CreateTaskButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.CreateTaskButton.setObjectName("CreateTaskButton")
        self.HorizontalLayout.addWidget(self.CreateTaskButton)
        self.CancelButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.CancelButton.setObjectName("CancelButton")
        self.HorizontalLayout.addWidget(self.CancelButton)

        self.retranslateUi(TasksCreateWindow)
        QtCore.QMetaObject.connectSlotsByName(TasksCreateWindow)

    def retranslateUi(self, TasksCreateWindow):
        _translate = QtCore.QCoreApplication.translate
        TasksCreateWindow.setWindowTitle(_translate("TasksCreateWindow", "Dialog"))
        self.CreateTaskGroupBox.setTitle(_translate("TasksCreateWindow", "Create Task"))
        self.TaskName.setTitle(_translate("TasksCreateWindow", "Task Name"))
        self.DescriptionGroupBox.setTitle(_translate("TasksCreateWindow", "Description"))
        self.DueDateGroupBox.setTitle(_translate("TasksCreateWindow", "Due Date"))
        self.PriorityGroupBox.setTitle(_translate("TasksCreateWindow", "Priority"))
        self.PriorityComboBox.setItemText(0, _translate("TasksCreateWindow", "Urgent and important"))
        self.PriorityComboBox.setItemText(1, _translate("TasksCreateWindow", "Not urgent, but important"))
        self.PriorityComboBox.setItemText(2, _translate("TasksCreateWindow", "Urgent, but not important"))
        self.PriorityComboBox.setItemText(3, _translate("TasksCreateWindow", "Not urgent and not important"))
        self.StatusGroupBox.setTitle(_translate("TasksCreateWindow", "Status"))
        self.StatusComboBox.setItemText(0, _translate("TasksCreateWindow", "Done"))
        self.StatusComboBox.setItemText(1, _translate("TasksCreateWindow", "In process"))
        self.StatusComboBox.setItemText(2, _translate("TasksCreateWindow", "Waiting"))
        self.EventsGroupBox.setTitle(_translate("TasksCreateWindow", "Events"))
        self.CreateTaskButton.setText(_translate("TasksCreateWindow", "Create Task"))
        self.CancelButton.setText(_translate("TasksCreateWindow", "Cancel"))
