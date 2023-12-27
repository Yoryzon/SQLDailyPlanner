# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AppDataBase\AppDataBaseUI\EventsWindowsUI\EventsCreateWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_EventsCreateWindow(object):
    def setupUi(self, EventsCreateWindow):
        EventsCreateWindow.setObjectName("EventsCreateWindow")
        EventsCreateWindow.resize(450, 330)
        EventsCreateWindow.setMinimumSize(QtCore.QSize(450, 330))
        EventsCreateWindow.setMaximumSize(QtCore.QSize(450, 330))
        self.CreateEventBox = QtWidgets.QGroupBox(EventsCreateWindow)
        self.CreateEventBox.setGeometry(QtCore.QRect(10, 10, 430, 310))
        self.CreateEventBox.setObjectName("CreateEventBox")
        self.TitleBox = QtWidgets.QGroupBox(self.CreateEventBox)
        self.TitleBox.setGeometry(QtCore.QRect(20, 20, 120, 50))
        self.TitleBox.setObjectName("TitleBox")
        self.TitlePlainTextEdit = QtWidgets.QPlainTextEdit(self.TitleBox)
        self.TitlePlainTextEdit.setGeometry(QtCore.QRect(10, 20, 100, 20))
        self.TitlePlainTextEdit.setObjectName("TitlePlainTextEdit")
        self.DescriptionBox = QtWidgets.QGroupBox(self.CreateEventBox)
        self.DescriptionBox.setGeometry(QtCore.QRect(150, 20, 260, 230))
        self.DescriptionBox.setObjectName("DescriptionBox")
        self.DescriptionPlainTextEdit = QtWidgets.QPlainTextEdit(self.DescriptionBox)
        self.DescriptionPlainTextEdit.setGeometry(QtCore.QRect(10, 20, 240, 200))
        self.DescriptionPlainTextEdit.setObjectName("DescriptionPlainTextEdit")
        self.EventDateBox = QtWidgets.QGroupBox(self.CreateEventBox)
        self.EventDateBox.setGeometry(QtCore.QRect(20, 80, 120, 50))
        self.EventDateBox.setObjectName("EventDateBox")
        self.EventDateEdit = QtWidgets.QDateEdit(self.EventDateBox)
        self.EventDateEdit.setGeometry(QtCore.QRect(10, 20, 100, 20))
        self.EventDateEdit.setObjectName("EventDateEdit")
        self.StartTimeBox = QtWidgets.QGroupBox(self.CreateEventBox)
        self.StartTimeBox.setGeometry(QtCore.QRect(20, 140, 120, 50))
        self.StartTimeBox.setObjectName("StartTimeBox")
        self.StartTimeEdit = QtWidgets.QTimeEdit(self.StartTimeBox)
        self.StartTimeEdit.setGeometry(QtCore.QRect(10, 20, 100, 20))
        self.StartTimeEdit.setObjectName("StartTimeEdit")
        self.EndTimeBox = QtWidgets.QGroupBox(self.CreateEventBox)
        self.EndTimeBox.setGeometry(QtCore.QRect(20, 200, 120, 50))
        self.EndTimeBox.setObjectName("EndTimeBox")
        self.EndTimeEdit = QtWidgets.QTimeEdit(self.EndTimeBox)
        self.EndTimeEdit.setGeometry(QtCore.QRect(10, 20, 100, 20))
        self.EndTimeEdit.setObjectName("EndTimeEdit")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.CreateEventBox)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 260, 390, 40))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.HorizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.HorizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.HorizontalLayout.setObjectName("HorizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.HorizontalLayout.addItem(spacerItem)
        self.EventCreateButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.EventCreateButton.setObjectName("EventCreateButton")
        self.HorizontalLayout.addWidget(self.EventCreateButton)
        self.CancelButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.CancelButton.setObjectName("CancelButton")
        self.HorizontalLayout.addWidget(self.CancelButton)

        self.retranslateUi(EventsCreateWindow)
        QtCore.QMetaObject.connectSlotsByName(EventsCreateWindow)

    def retranslateUi(self, EventsCreateWindow):
        _translate = QtCore.QCoreApplication.translate
        EventsCreateWindow.setWindowTitle(_translate("EventsCreateWindow", "Dialog"))
        self.CreateEventBox.setTitle(_translate("EventsCreateWindow", "Create Event"))
        self.TitleBox.setTitle(_translate("EventsCreateWindow", "Title"))
        self.DescriptionBox.setTitle(_translate("EventsCreateWindow", "Description"))
        self.EventDateBox.setTitle(_translate("EventsCreateWindow", "Event Date"))
        self.StartTimeBox.setTitle(_translate("EventsCreateWindow", "Start Time"))
        self.EndTimeBox.setTitle(_translate("EventsCreateWindow", "End Time"))
        self.EventCreateButton.setText(_translate("EventsCreateWindow", "Create Event"))
        self.CancelButton.setText(_translate("EventsCreateWindow", "Cancel"))