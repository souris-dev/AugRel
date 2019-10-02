# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'control_win.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

import threading as th
from queue import Queue
from PyQt5 import QtCore, QtGui, QtWidgets
import sys


# Sorry for the globals, but I found this to be the easiest
filter_l = ["one_devil_horn", "unihorn", "two_horns1", "two_horns2", "bunny_ears1", "bunny_ears2", "bunny_ears3", "puppy"]

event_snp = th.Event()  # take snapshot
event_size = th.Event()  # resize cam feed
event_filter_change = th.Event()  # change filter

event_quit = th.Event()  # the quit button

# Used to pass file folder to save into, for now
pass_q = Queue()


class Ui_MainWindow(QtWidgets.QMainWindow):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(586, 708)
        MainWindow.setMinimumSize(QtCore.QSize(586, 666))
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.groupBox_2)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(0, 20, 551, 165))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.filter_sel_box = QtWidgets.QComboBox(self.verticalLayoutWidget_2)
        self.filter_sel_box.setMinimumSize(QtCore.QSize(230, 0))
        self.filter_sel_box.setObjectName("filter_sel_box")
        self.horizontalLayout_4.addWidget(self.filter_sel_box)
        self.add_filter_btn = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.add_filter_btn.setObjectName("add_filter_btn")
        self.horizontalLayout_4.addWidget(self.add_filter_btn)
        self.remove_filt_btn = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.remove_filt_btn.setObjectName("remove_filt_btn")
        self.horizontalLayout_4.addWidget(self.remove_filt_btn)
        #self.spinBox = QtWidgets.QSpinBox(self.verticalLayoutWidget_2)
        #self.spinBox.setObjectName("spinBox")
        #self.horizontalLayout_4.addWidget(self.spinBox)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.listWidget = QtWidgets.QListWidget(self.verticalLayoutWidget_2)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout_2.addWidget(self.listWidget)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.filter_change_btn = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.filter_change_btn.setObjectName("filter_change_btn")
        self.horizontalLayout_3.addWidget(self.filter_change_btn)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.verticalLayout_5.addWidget(self.groupBox_2)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 30, 551, 141))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit.setMinimumSize(QtCore.QSize(360, 0))
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.folder_sel_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.folder_sel_btn.setObjectName("folder_sel_btn")
        self.horizontalLayout.addWidget(self.folder_sel_btn)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem6)
        self.snap_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.snap_btn.setObjectName("snap_btn")
        self.horizontalLayout_2.addWidget(self.snap_btn)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem7)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_5.addWidget(self.groupBox)
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.groupBox_3)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(0, 20, 551, 171))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem8)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_2.setMinimumSize(QtCore.QSize(500, 0))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_7.addWidget(self.label_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem9)
        self.horizontalSlider = QtWidgets.QSlider(self.verticalLayoutWidget_3)
        self.horizontalSlider.setMinimumSize(QtCore.QSize(300, 0))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setInvertedAppearance(False)
        self.horizontalSlider.setInvertedControls(False)
        self.horizontalSlider.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalLayout_5.addWidget(self.horizontalSlider)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem10)
        self.lcdNumber = QtWidgets.QLCDNumber(self.verticalLayoutWidget_3)
        self.lcdNumber.setProperty("intValue", 100)
        self.lcdNumber.setObjectName("lcdNumber")
        self.horizontalLayout_5.addWidget(self.lcdNumber)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_5.addWidget(self.label_3)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem11)
        self.camsize_change_btn = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.camsize_change_btn.setObjectName("camsize_change_btn")
        self.horizontalLayout_5.addWidget(self.camsize_change_btn)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem12)
        self.quit_btn = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.quit_btn.setObjectName("quit_btn")
        self.horizontalLayout_6.addWidget(self.quit_btn)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem13)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.verticalLayout_5.addWidget(self.groupBox_3)
        self.verticalLayout_6.addLayout(self.verticalLayout_5)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 586, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # addendum
        self.snap_btn.clicked.connect(self.snapBtnClicked)
        self.folder_sel_btn.clicked.connect(self.show_foldersel)
        self.camsize_change_btn.clicked.connect(self.cam_size_change)
        self.horizontalSlider.valueChanged.connect(self.slider_change)
        self.quit_btn.clicked.connect(self.send_quit_signal)
        self.add_filter_btn.clicked.connect(self.add_filter)
        self.remove_filt_btn.clicked.connect(self.remove_filter)

        # populate the filter selection combobox
        self.filter_sel_box.addItems(filter_l)
        self.filter_change_btn.clicked.connect(self.filter_change_evt)

        # be default, scale is 150%
        # recall that the slider provides value from 0 to 99
        self.horizontalSlider.setValue(50)

        MainWindow.setWindowIcon(QtGui.QIcon("icons8_camera_64_uVa_icon.ico"))

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Controls"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Overlay"))
        self.add_filter_btn.setText(_translate("MainWindow", "Add"))
        self.remove_filt_btn.setText(_translate("MainWindow", "Remove"))
        self.filter_change_btn.setText(_translate("MainWindow", "Use"))
        self.groupBox.setTitle(_translate("MainWindow", "Take a Snap"))
        self.folder_sel_btn.setText(_translate("MainWindow", "Select folder..."))
        self.snap_btn.setText(_translate("MainWindow", "Take Snap (or press Enter)"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Others"))
        self.label_2.setText(_translate("MainWindow", "Change camera window size: "))
        self.label_3.setText(_translate("MainWindow", "percent"))
        self.camsize_change_btn.setText(_translate("MainWindow", "Change"))
        self.quit_btn.setText(_translate("MainWindow", "Quit"))

    def add_filter(self, e):
        self.listWidget.addItem(self.filter_sel_box.currentText())

    def remove_filter(self, e):
        """
        if self.spinBox.value() > self.listWidget.count():
            emsg = QtWidgets.QErrorMessage()
            emsg.setWindowTitle("Please!")
            emsg.showMessage("I can't remove that from the list! Cut me some slack, will you?")
            emsg.exec_()
            return
        self.listWidget.removeItemWidget(self.listWidget.item(self.spinBox.value() - 1))
        """
        list_items_sel = self.listWidget.selectedItems()

        if not list_items_sel:
            return
        for item in list_items_sel:
            self.listWidget.takeItem(self.listWidget.row(item))

    def slider_change(self, e):
        self.lcdNumber.setProperty("intValue", str(100 + self.horizontalSlider.value()))

    def filter_change_evt(self, e):
        # pass_q.put(self.filter_sel_box.currentText())
        list_sel_fil = []

        for i in range(0, self.listWidget.count()):
            list_sel_fil.append(self.listWidget.item(i).text())

        pass_q.put(list_sel_fil)
        event_filter_change.set()

    def send_quit_signal(self, e):
        event_quit.set()
        emsg = QtWidgets.QErrorMessage()
        emsg.setWindowTitle("Arigatou Gozaimasu")
        emsg.showMessage("Thank you for previewing this project, O sentient being!")
        emsg.exec_()
        sys.exit()

    def cam_size_change(self, e):
        # pass the main thread the size to scale to
        pass_q.put(100 + int(self.horizontalSlider.value()))
        # set the event
        event_size.set()

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
        file_dlg = QtWidgets.QFileDialog()
        file = str(file_dlg.getExistingDirectory(self, "Select Directory"))
        self.lineEdit.setText(file)


class AppWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
