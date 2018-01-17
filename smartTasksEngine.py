# -*- coding: utf-8 -*-

import sys
import threading


#GUI
from smartTasksMainWindow import Ui_MainWindow
from endOfTaskTimeDialog import Ui_Dialog


from collections import OrderedDict
from PyQt4 import QtCore,QtGui
from PyQt4.Qt import QTableWidgetItem


import pickle

from random import shuffle
from random import randint

from PyQt4.phonon import Phonon

SECS_TO_MINS = 60

class EndTaskDialog(QtGui.QDialog):
    
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.dialog = Ui_Dialog()
        self.dialog.setupUi(self)
        
#        self.finishedTask = None


class mainWindowAppEngine(QtGui.QMainWindow):

    #Constructor
    def __init__(self):

        QtGui.QMainWindow.__init__(self)
        
        self.appMainWindow = Ui_MainWindow()
        self.appMainWindow.setupUi(self)
        #self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.tasksList = []
        try:
            tasksListFile = open('tasks.pickle')
            self.tasksList = pickle.load(tasksListFile)
        except Exception as e:
            print e
            
        
        self.schedTasksIndicesList = []
        self.notSchedTaskIndicesList = []
        self.currentTaskIndex = None
        
        self.endTaskDialog = EndTaskDialog()
        self.connect(self.endTaskDialog.dialog.completedTaskPushButton, QtCore.SIGNAL('clicked()'), self.completedTask)
        self.connect(self.endTaskDialog.dialog.notCompletedTaskPushButton, QtCore.SIGNAL('clicked()'), self.notCompletedTask)
        self.connect(self.endTaskDialog.dialog.notDoneTaskPushButton, QtCore.SIGNAL('clicked()'), self.notDoneTask)
        
        self.connect(self.appMainWindow.addTaskPushButton, QtCore.SIGNAL('clicked()'), self.addTask)
        self.connect(self.appMainWindow.scheduleTasksPushButton, QtCore.SIGNAL('clicked()'), self.scheduleTasks)
        
        self.setFocusOnMainWindowSignal = QtCore.SIGNAL("doOnFinishedCurrentTaskTime")
        self.connect(self,self.setFocusOnMainWindowSignal,self.doOnFinishedCurrentTaskTime)
        
        self.updateTaskLabelSignal = QtCore.SIGNAL("updateTaskLabelSignal")
        self.connect(self,self.updateTaskLabelSignal, self.updateTaskLabel )
        
        self.mediaObject = Phonon.MediaObject(self)
        self.audioOutput = Phonon.AudioOutput(Phonon.MusicCategory, self)
        Phonon.createPath(self.mediaObject, self.audioOutput)
        self.mediaObject.setCurrentSource(Phonon.MediaSource('/home/ericfab17/Spyder Workspace/SmartTasks/alarm.mp3'))
        
        self.updateTasksTableWidget()
        
        for task in self.tasksList:
            print task
        
        #Reset priority
        for task in self.tasksList:
            task.priority = 0


    def closeEvent(self, evnt):
        for index in self.schedTasksIndicesList:
            self.tasksList[index].priority = self.tasksList[index].priority + 2
        for index in self.notSchedTaskIndicesList:
            self.tasksList[index].priority = self.tasksList[index].priority +2
        if self.currentTaskIndex > -1:
            self.tasksList[self.currentTaskIndex].priority = self.tasksList[self.currentTaskIndex].priority +2
        self.saveTasksList()
    
    def updateTaskLabel(self):
        if self.currentTaskIndex == -1:
            self.appMainWindow.currentTaskLabel.setText("No current task")
        else:
            self.appMainWindow.currentTaskLabel.setText(self.tasksList[self.currentTaskIndex].name)
            
        
    def doOnFinishedCurrentTaskTime(self):
        self.mediaObject.play()
        self.endTaskDialog.show()
        #self.setWindowState(self.windowState() & ~QtCore.Qt.WindowMinimized | QtCore.Qt.WindowActive)
#        if self.windowState() == QtCore.Qt.WindowMinimized:
#            # Window is minimised. Restore it.
#            self.setWindowState(QtCore.Qt.WindowNoState)
#        self.setFocus(True)
#        self.activateWindow()
#        self.raise_()
#        self.show()
        #self.appMainWindow.currentTaskLabel.setText( self.tasksList[self.currentTaskIndex].name)

        
    def acknowledgeFinishedTimeTask(self):
        if self.mediaObject.state() == Phonon.PlayingState:
            self.mediaObject.stop()
            
        if len(self.schedTasksIndicesList) > 0:
                self.currentTaskIndex = self.schedTasksIndicesList.pop(0)
                finalTaskTime = (self.tasksList[self.currentTaskIndex].timeDuration)*SECS_TO_MINS
                def requestNextTask(tasksList, schedTasksIndicesList):
                    self.emit(self.setFocusOnMainWindowSignal, "")
                taskTimer = threading.Timer(finalTaskTime, requestNextTask, [self.tasksList, self.schedTasksIndicesList])
                taskTimer.start()
        else:
            self.currentTaskIndex = -1
        self.emit(self.updateTaskLabelSignal)
        self.endTaskDialog.hide()
        
        self.saveTasksList()

    def completedTask(self):
        self.tasksList[self.currentTaskIndex].priority = self.tasksList[self.currentTaskIndex].priority
        self.acknowledgeFinishedTimeTask()
    def notCompletedTask(self):
        self.tasksList[self.currentTaskIndex].priority = self.tasksList[self.currentTaskIndex].priority + 1
        self.acknowledgeFinishedTimeTask()
    def notDoneTask(self):
        self.tasksList[self.currentTaskIndex].priority = self.tasksList[self.currentTaskIndex].priority +2
        self.acknowledgeFinishedTimeTask()
        
    def addTask(self):
        if self.appMainWindow.taskTimeDurationSpinBox.value() > 0 and self.appMainWindow.taskNameLineEdit.text() is not "":
            self.tasksList.append(Task(self.appMainWindow.taskNameLineEdit.text(), self.appMainWindow.taskTimeDurationSpinBox.value()))
            self.updateTasksTableWidget()
        
        print self.tasksList
        self.saveTasksList()
        
    def saveTasksList(self):
        tasksFile = open("tasks.pickle","w+")
        pickle.dump(self.tasksList, tasksFile)
        tasksFile.close()
        
    def scheduleTasks(self):
        
        shuffle(self.tasksList)
        
        def taskSortKey(task):
            return task.priority
        self.tasksList.sort( key = taskSortKey, reverse = True)
        
        
        
        availableTime = self.appMainWindow.startSchedulingtimeEdit.time().secsTo(self.appMainWindow.endSchedulingTimeEdit.time())/60
        overallTime = 0
        for task in self.tasksList:
            overallTime = overallTime + task.timeDuration
            if overallTime < availableTime:
                self.schedTasksIndicesList.append(self.tasksList.index(task))
            else:
                self.notSchedTaskIndicesList.append(self.tasksList.index(task))
        self.updateScheduledTasksTableWidget()
        self.currentTaskIndex = self.schedTasksIndicesList.pop(0)
        self.appMainWindow.currentTaskLabel.setText( self.tasksList[self.currentTaskIndex].name)
        finalTaskTime = (self.tasksList[self.currentTaskIndex].timeDuration)*SECS_TO_MINS
        
        def requestNextTask(tasksList, schedTasksIndicesList):

            
            
            
#            finishedTask = self.currentTaskIndex
#            if len(schedTasksIndicesList) > 0:
#                self.currentTaskIndex = self.schedTasksIndicesList.pop(0)
#                finalTaskTime = (self.tasksList[self.currentTaskIndex].timeDuration)*SECS_TO_MINS
#                requestTaskTimer = threading.Timer(finalTaskTime, requestNextTask, [tasksList, schedTasksIndicesList])
#                requestTaskTimer.start()
#            else:
#                self.currentTaskIndex = "No current task"
            self.emit(self.setFocusOnMainWindowSignal, "")

        taskTimer = threading.Timer(finalTaskTime, requestNextTask, [self.tasksList, self.schedTasksIndicesList])
        taskTimer.start()
        
        print self.tasksList
        
    def updateTableWidget(self, tableWidget, tableDictionary):
        tableWidget.clear()
        horHeaders = []
        tableWidget.setColumnCount(len(tableDictionary))
        tableWidget.setRowCount(len(tableDictionary[tableDictionary.keys()[0]]))
        for n, key in enumerate(tableDictionary.keys()):
            horHeaders.append(key)
            for m, item in enumerate(tableDictionary[key]):
                newItem = QTableWidgetItem(item)

                tableWidget.setItem(m, n, newItem)
        tableWidget.setHorizontalHeaderLabels(horHeaders)
        tableWidget.horizontalHeader().setResizeMode(QtGui.QHeaderView.Stretch)


    def updateTasksTableWidget(self):
        tasksDict = OrderedDict([('Name',[]),( 'Time Duration',[])])
        for task in self.tasksList:
            tasksDict['Name'].append(task.name)
            tasksDict['Time Duration'].append(str(task.timeDuration))
        self.updateTableWidget(self.appMainWindow.tasksTableWidget, tasksDict)

    def updateScheduledTasksTableWidget(self):
        scheduledTaksDict = OrderedDict([('Name',[]),( 'Time Duration',[])])
        for index in self.schedTasksIndicesList:
            scheduledTaksDict['Name'].append(self.tasksList[index].name)
            scheduledTaksDict['Time Duration'].append(str(self.tasksList[index].timeDuration))
        self.updateTableWidget(self.appMainWindow.schedluedTasksTableWidget, scheduledTaksDict)
#==============================================================================
#  MODEL CLASSES
#==============================================================================


class Task():

    def __init__(self, name, timeDuration):
        self.name = name
        self.timeDuration = timeDuration
        self.priority = 0
        
        #self.priority = randint(1, 10)
        
    def __repr__(self):
        return self.name.encode('utf-8') + "," +str(self.timeDuration)+","+str(self.priority)
    


def main():
    app = QtGui.QApplication(sys.argv)
    app.setApplicationName('SmartTasks')
    appWindow = mainWindowAppEngine()
    appWindow.show()
    sys.exit(app.exec_())
if __name__=="__main__":
    main()
