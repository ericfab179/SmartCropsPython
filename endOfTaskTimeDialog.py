# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'endOfTaskTimeDialog.ui'
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(400, 81)
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.frame = QtGui.QFrame(Dialog)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.gridLayout_4 = QtGui.QGridLayout(self.frame)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.notCompletedTaskPushButton = QtGui.QPushButton(self.frame)
        self.notCompletedTaskPushButton.setObjectName(_fromUtf8("notCompletedTaskPushButton"))
        self.gridLayout_4.addWidget(self.notCompletedTaskPushButton, 0, 1, 1, 1)
        self.notDoneTaskPushButton = QtGui.QPushButton(self.frame)
        self.notDoneTaskPushButton.setObjectName(_fromUtf8("notDoneTaskPushButton"))
        self.gridLayout_4.addWidget(self.notDoneTaskPushButton, 0, 2, 1, 1)
        self.completedTaskPushButton = QtGui.QPushButton(self.frame)
        self.completedTaskPushButton.setObjectName(_fromUtf8("completedTaskPushButton"))
        self.gridLayout_4.addWidget(self.completedTaskPushButton, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.notCompletedTaskPushButton.setText(_translate("Dialog", "Not completed", None))
        self.notDoneTaskPushButton.setText(_translate("Dialog", "Not done", None))
        self.completedTaskPushButton.setText(_translate("Dialog", "Completed", None))

