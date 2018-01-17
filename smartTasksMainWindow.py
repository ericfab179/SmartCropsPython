# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'smartTaksMainWindow.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.tasksGroupBox = QtGui.QGroupBox(self.centralwidget)
        self.tasksGroupBox.setObjectName(_fromUtf8("tasksGroupBox"))
        self.gridLayout_3 = QtGui.QGridLayout(self.tasksGroupBox)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.taskNameLineEdit = QtGui.QLineEdit(self.tasksGroupBox)
        self.taskNameLineEdit.setObjectName(_fromUtf8("taskNameLineEdit"))
        self.gridLayout_3.addWidget(self.taskNameLineEdit, 0, 0, 1, 1)
        self.taskTimeDurationSpinBox = QtGui.QSpinBox(self.tasksGroupBox)
        self.taskTimeDurationSpinBox.setObjectName(_fromUtf8("taskTimeDurationSpinBox"))
        self.gridLayout_3.addWidget(self.taskTimeDurationSpinBox, 1, 0, 1, 1)
        self.addTaskPushButton = QtGui.QPushButton(self.tasksGroupBox)
        self.addTaskPushButton.setObjectName(_fromUtf8("addTaskPushButton"))
        self.gridLayout_3.addWidget(self.addTaskPushButton, 2, 0, 1, 1)
        self.tasksTableWidget = QtGui.QTableWidget(self.tasksGroupBox)
        self.tasksTableWidget.setObjectName(_fromUtf8("tasksTableWidget"))
        self.tasksTableWidget.setColumnCount(0)
        self.tasksTableWidget.setRowCount(0)
        self.gridLayout_3.addWidget(self.tasksTableWidget, 3, 0, 1, 1)
        self.gridLayout.addWidget(self.tasksGroupBox, 0, 0, 1, 1)
        self.schedulingGroupBox = QtGui.QGroupBox(self.centralwidget)
        self.schedulingGroupBox.setObjectName(_fromUtf8("schedulingGroupBox"))
        self.gridLayout_2 = QtGui.QGridLayout(self.schedulingGroupBox)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.endSchedulingTimeEdit = QtGui.QTimeEdit(self.schedulingGroupBox)
        self.endSchedulingTimeEdit.setObjectName(_fromUtf8("endSchedulingTimeEdit"))
        self.gridLayout_2.addWidget(self.endSchedulingTimeEdit, 2, 0, 1, 1)
        self.startSchedulingtimeEdit = QtGui.QTimeEdit(self.schedulingGroupBox)
        self.startSchedulingtimeEdit.setObjectName(_fromUtf8("startSchedulingtimeEdit"))
        self.gridLayout_2.addWidget(self.startSchedulingtimeEdit, 1, 0, 1, 1)
        self.schedluedTasksTableWidget = QtGui.QTableWidget(self.schedulingGroupBox)
        self.schedluedTasksTableWidget.setObjectName(_fromUtf8("schedluedTasksTableWidget"))
        self.schedluedTasksTableWidget.setColumnCount(0)
        self.schedluedTasksTableWidget.setRowCount(0)
        self.gridLayout_2.addWidget(self.schedluedTasksTableWidget, 3, 0, 1, 1)
        self.scheduleTasksPushButton = QtGui.QPushButton(self.schedulingGroupBox)
        self.scheduleTasksPushButton.setObjectName(_fromUtf8("scheduleTasksPushButton"))
        self.gridLayout_2.addWidget(self.scheduleTasksPushButton, 4, 0, 1, 1)
        self.currentTaskLabel = QtGui.QLabel(self.schedulingGroupBox)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Tlwg Mono"))
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.currentTaskLabel.setFont(font)
        self.currentTaskLabel.setObjectName(_fromUtf8("currentTaskLabel"))
        self.gridLayout_2.addWidget(self.currentTaskLabel, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.schedulingGroupBox, 4, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.tasksGroupBox.setTitle(_translate("MainWindow", "Tareas", None))
        self.addTaskPushButton.setText(_translate("MainWindow", "Add task", None))
        self.schedulingGroupBox.setTitle(_translate("MainWindow", "Programación", None))
        self.scheduleTasksPushButton.setText(_translate("MainWindow", "Schedule tasks", None))
        self.currentTaskLabel.setText(_translate("MainWindow", "No current task", None))

