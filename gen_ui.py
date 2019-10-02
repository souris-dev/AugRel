# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Documents\Projects (Py)\AugRel\control_win.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

import threading as th
from queue import Queue
from PyQt5 import QtCore, QtGui, QtWidgets

global event_snp
global pass_q

# This event lets know when the take snapshot is taken to the opencv thread
event_snp = th.Event()

# Used to pass file folder to save into, for now
pass_q = Queue()


class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.snap_folder = ""

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(614, 404)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 10, 581, 331))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.snap_btn = QtWidgets.QPushButton(self.frame)
        self.snap_btn.setGeometry(QtCore.QRect(210, 260, 141, 41))
        self.snap_btn.setObjectName("snap_btn")

        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(100, 211, 271, 31))
        self.lineEdit.setObjectName("lineEdit")

        self.folder_sel_btn = QtWidgets.QPushButton(self.frame)
        self.folder_sel_btn.setGeometry(QtCore.QRect(380, 210, 101, 31))
        self.folder_sel_btn.setObjectName("folder_sel_btn")

        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(240, 10, 91, 31))

        font = QtGui.QFont()
        font.setPointSize(14)

        self.label.setFont(font)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 614, 26))
        self.menubar.setObjectName("menubar")

        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # addendum
        MainWindow.setWindowTitle("Controls")
        self.snap_btn.clicked.connect(self.snapBtnClicked)
        self.folder_sel_btn.clicked.connect(self.show_foldersel)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

        self.snap_btn.setText(_translate("MainWindow", "Take Snap"))
        self.folder_sel_btn.setText(_translate("MainWindow", "Select folder..."))
        self.label.setText(_translate("MainWindow", "Controls"))

    def snapBtnClicked(self, e):
        if self.lineEdit.text() == "":
            print("Please select a folder to save the snapshots to!")
            emsg = QtWidgets.QErrorMessage()
            emsg.setWindowTitle("Error")
            emsg.showMessage("Please select a folder to save the snapshots to!")
            emsg.exec_()
            return

        pass_q.put(self.lineEdit.text())
        event_snp.set()

    def show_foldersel(self, e):
        file = str(QtWidgets.QFileDialog.getExistingDirectory(self, "Select Directory"))
        self.lineEdit.setText(file)


class AppWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)