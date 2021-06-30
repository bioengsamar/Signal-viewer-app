# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'des1.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 555)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        MainWindow.setFocusPolicy(QtCore.Qt.NoFocus)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("pictures/google-wave-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(480, 320))
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.MplWid1 = MplWid1(self.centralwidget)
        self.MplWid1.setObjectName("MplWid1")
        self.play = QtWidgets.QPushButton(self.MplWid1)
        self.play.setGeometry(QtCore.QRect(400, 0, 75, 23))
        self.play.setObjectName("play")
        self.stop = QtWidgets.QPushButton(self.MplWid1)
        self.stop.setGeometry(QtCore.QRect(320, 0, 75, 23))
        self.stop.setObjectName("stop")
        self.gridLayout.addWidget(self.MplWid1, 0, 0, 1, 1)
        self.MplWid2 = MplWid2(self.centralwidget)
        self.MplWid2.setObjectName("MplWid2")
        self.play2 = QtWidgets.QPushButton(self.MplWid2)
        self.play2.setGeometry(QtCore.QRect(400, 0, 75, 23))
        self.play2.setObjectName("play2")
        self.stop2 = QtWidgets.QPushButton(self.MplWid2)
        self.stop2.setGeometry(QtCore.QRect(320, 0, 75, 23))
        self.stop2.setObjectName("stop2")
        self.gridLayout.addWidget(self.MplWid2, 1, 0, 1, 1)
        self.MplWid3 = MplWid3(self.centralwidget)
        self.MplWid3.setObjectName("MplWid3")
        self.play3 = QtWidgets.QPushButton(self.MplWid3)
        self.play3.setGeometry(QtCore.QRect(400, 0, 75, 23))
        self.play3.setObjectName("play3")
        self.stop3 = QtWidgets.QPushButton(self.MplWid3)
        self.stop3.setGeometry(QtCore.QRect(320, 0, 75, 23))
        self.stop3.setObjectName("stop3")
        self.gridLayout.addWidget(self.MplWid3, 2, 0, 1, 1)
        self.MplWid4 = MplWid4(self.centralwidget)
        self.MplWid4.setObjectName("MplWid4")
        self.pushButton = QtWidgets.QPushButton(self.MplWid4)
        self.pushButton.setGeometry(QtCore.QRect(400, 0, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_5 = QtWidgets.QPushButton(self.MplWid4)
        self.pushButton_5.setGeometry(QtCore.QRect(320, 0, 75, 23))
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.MplWid4, 3, 0, 1, 1)
        self.MplWid5 = MplWid5(self.centralwidget)
        self.MplWid5.setObjectName("MplWid5")
        self.pushButton_4 = QtWidgets.QPushButton(self.MplWid5)
        self.pushButton_4.setGeometry(QtCore.QRect(400, 0, 75, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_6 = QtWidgets.QPushButton(self.MplWid5)
        self.pushButton_6.setGeometry(QtCore.QRect(320, 0, 75, 23))
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout.addWidget(self.MplWid5, 4, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 21))
        self.menubar.setObjectName("menubar")
        self.menufile = QtWidgets.QMenu(self.menubar)
        self.menufile.setObjectName("menufile")
        self.menuedit = QtWidgets.QMenu(self.menubar)
        self.menuedit.setObjectName("menuedit")
        self.menuchannel_1 = QtWidgets.QMenu(self.menubar)
        self.menuchannel_1.setObjectName("menuchannel_1")
        self.menuchannel_2 = QtWidgets.QMenu(self.menubar)
        self.menuchannel_2.setObjectName("menuchannel_2")
        self.menuchannel_3 = QtWidgets.QMenu(self.menubar)
        self.menuchannel_3.setObjectName("menuchannel_3")
        self.menuchannel_4 = QtWidgets.QMenu(self.menubar)
        self.menuchannel_4.setObjectName("menuchannel_4")
        self.menuchannel_5 = QtWidgets.QMenu(self.menubar)
        self.menuchannel_5.setObjectName("menuchannel_5")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionexit = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("pictures/Button-Close-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionexit.setIcon(icon1)
        self.actionexit.setObjectName("actionexit")
        self.actionopen = QtWidgets.QAction(MainWindow)
        self.actionopen.setObjectName("actionopen")
        self.actionopen_file_csv = QtWidgets.QAction(MainWindow)
        self.actionopen_file_csv.setObjectName("actionopen_file_csv")
        self.actionload_data = QtWidgets.QAction(MainWindow)
        self.actionload_data.setObjectName("actionload_data")
        self.actionclose = QtWidgets.QAction(MainWindow)
        self.actionclose.setObjectName("actionclose")
        self.actionopen_2 = QtWidgets.QAction(MainWindow)
        self.actionopen_2.setObjectName("actionopen_2")
        self.actionopen_file_xls_2 = QtWidgets.QAction(MainWindow)
        self.actionopen_file_xls_2.setObjectName("actionopen_file_xls_2")
        self.actionclose_2 = QtWidgets.QAction(MainWindow)
        self.actionclose_2.setObjectName("actionclose_2")
        self.actionload_data_2 = QtWidgets.QAction(MainWindow)
        self.actionload_data_2.setObjectName("actionload_data_2")
        self.actionopen_3 = QtWidgets.QAction(MainWindow)
        self.actionopen_3.setObjectName("actionopen_3")
        self.actionopen_file_txt = QtWidgets.QAction(MainWindow)
        self.actionopen_file_txt.setObjectName("actionopen_file_txt")
        self.actionload_data_3 = QtWidgets.QAction(MainWindow)
        self.actionload_data_3.setObjectName("actionload_data_3")
        self.actionclose_3 = QtWidgets.QAction(MainWindow)
        self.actionclose_3.setObjectName("actionclose_3")
        self.actionopen_4 = QtWidgets.QAction(MainWindow)
        self.actionopen_4.setObjectName("actionopen_4")
        self.actionopen_file = QtWidgets.QAction(MainWindow)
        self.actionopen_file.setObjectName("actionopen_file")
        self.actionload_data_4 = QtWidgets.QAction(MainWindow)
        self.actionload_data_4.setObjectName("actionload_data_4")
        self.actionclose_4 = QtWidgets.QAction(MainWindow)
        self.actionclose_4.setObjectName("actionclose_4")
        self.actionopen_5 = QtWidgets.QAction(MainWindow)
        self.actionopen_5.setObjectName("actionopen_5")
        self.actionopen_file_4 = QtWidgets.QAction(MainWindow)
        self.actionopen_file_4.setObjectName("actionopen_file_4")
        self.actionload_data_5 = QtWidgets.QAction(MainWindow)
        self.actionload_data_5.setObjectName("actionload_data_5")
        self.actionclose_5 = QtWidgets.QAction(MainWindow)
        self.actionclose_5.setObjectName("actionclose_5")
        self.actionplay = QtWidgets.QAction(MainWindow)
        self.actionplay.setObjectName("actionplay")
        self.actionopen_file_txt_2 = QtWidgets.QAction(MainWindow)
        self.actionopen_file_txt_2.setObjectName("actionopen_file_txt_2")
        self.actionopen_file_xls = QtWidgets.QAction(MainWindow)
        self.actionopen_file_xls.setObjectName("actionopen_file_xls")
        self.actionopen_file_txt_3 = QtWidgets.QAction(MainWindow)
        self.actionopen_file_txt_3.setObjectName("actionopen_file_txt_3")
        self.actionopen_file_csv_2 = QtWidgets.QAction(MainWindow)
        self.actionopen_file_csv_2.setObjectName("actionopen_file_csv_2")
        self.actionopen_file_csv_3 = QtWidgets.QAction(MainWindow)
        self.actionopen_file_csv_3.setObjectName("actionopen_file_csv_3")
        self.actionopen_file_xls_3 = QtWidgets.QAction(MainWindow)
        self.actionopen_file_xls_3.setObjectName("actionopen_file_xls_3")
        self.actionopen_file_1 = QtWidgets.QAction(MainWindow)
        self.actionopen_file_1.setObjectName("actionopen_file_1")
        self.actionopen_file_2 = QtWidgets.QAction(MainWindow)
        self.actionopen_file_2.setObjectName("actionopen_file_2")
        self.actionopen_file_3 = QtWidgets.QAction(MainWindow)
        self.actionopen_file_3.setObjectName("actionopen_file_3")
        self.actionopen_file_44 = QtWidgets.QAction(MainWindow)
        self.actionopen_file_44.setObjectName("actionopen_file_44")
        self.actionopen_file_5 = QtWidgets.QAction(MainWindow)
        self.actionopen_file_5.setObjectName("actionopen_file_5")
        self.menufile.addAction(self.actionexit)
        self.menuchannel_1.addAction(self.actionopen)
        self.menuchannel_1.addAction(self.actionopen_file_1)
        self.menuchannel_1.addAction(self.actionclose)
        self.menuchannel_2.addAction(self.actionopen_2)
        self.menuchannel_2.addAction(self.actionopen_file_2)
        self.menuchannel_2.addAction(self.actionclose_2)
        self.menuchannel_3.addAction(self.actionopen_3)
        self.menuchannel_3.addAction(self.actionopen_file_3)
        self.menuchannel_3.addAction(self.actionclose_3)
        self.menuchannel_4.addAction(self.actionopen_4)
        self.menuchannel_4.addAction(self.actionopen_file_44)
        self.menuchannel_4.addAction(self.actionclose_4)
        self.menuchannel_5.addAction(self.actionopen_5)
        self.menuchannel_5.addAction(self.actionopen_file_5)
        self.menuchannel_5.addAction(self.actionclose_5)
        self.menubar.addAction(self.menufile.menuAction())
        self.menubar.addAction(self.menuedit.menuAction())
        self.menubar.addAction(self.menuchannel_1.menuAction())
        self.menubar.addAction(self.menuchannel_2.menuAction())
        self.menubar.addAction(self.menuchannel_3.menuAction())
        self.menubar.addAction(self.menuchannel_4.menuAction())
        self.menubar.addAction(self.menuchannel_5.menuAction())

        self.retranslateUi(MainWindow)
        self.actionclose.triggered.connect(self.MplWid1.hide)
        self.actionopen.triggered.connect(self.MplWid1.show)
        self.actionopen_2.triggered.connect(self.MplWid2.show)
        self.actionclose_2.triggered.connect(self.MplWid2.hide)
        self.actionexit.triggered.connect(MainWindow.close)
        self.actionopen_3.triggered.connect(self.MplWid3.show)
        self.actionclose_3.triggered.connect(self.MplWid3.close)
        self.actionopen_4.triggered.connect(self.MplWid4.show)
        self.actionopen_5.triggered.connect(self.MplWid5.show)
        self.actionclose_4.triggered.connect(self.MplWid4.close)
        self.actionclose_5.triggered.connect(self.MplWid5.close)
        self.play.clicked.connect(MainWindow.play1)
        self.stop.clicked.connect(MainWindow.stop)
        self.play3.clicked.connect(MainWindow.play3)
        self.stop3.clicked.connect(MainWindow.stop3)
        self.play2.clicked.connect(MainWindow.play2)
        self.stop2.clicked.connect(MainWindow.stop2)
        self.actionopen_file_1.triggered.connect(MainWindow.openFile)
        self.actionopen_file_2.triggered.connect(MainWindow.open2)
        self.actionopen_file_3.triggered.connect(MainWindow.openn)
        self.actionopen_file_44.triggered.connect(MainWindow.open4)
        self.actionopen_file_5.triggered.connect(MainWindow.open5)
        self.pushButton.clicked.connect(MainWindow.play4)
        self.pushButton_5.clicked.connect(MainWindow.stop4)
        self.pushButton_4.clicked.connect(MainWindow.play5)
        self.pushButton_6.clicked.connect(MainWindow.stop5)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "signal viewer"))
        self.play.setText(_translate("MainWindow", "play"))
        self.stop.setText(_translate("MainWindow", "pause"))
        self.play2.setText(_translate("MainWindow", "play"))
        self.stop2.setText(_translate("MainWindow", "pause"))
        self.play3.setText(_translate("MainWindow", "play"))
        self.stop3.setText(_translate("MainWindow", "pause"))
        self.pushButton.setText(_translate("MainWindow", "play"))
        self.pushButton_5.setText(_translate("MainWindow", "pause"))
        self.pushButton_4.setText(_translate("MainWindow", "play"))
        self.pushButton_6.setText(_translate("MainWindow", "pause"))
        self.menufile.setTitle(_translate("MainWindow", "file"))
        self.menuedit.setTitle(_translate("MainWindow", "edit"))
        self.menuchannel_1.setTitle(_translate("MainWindow", "channel 1"))
        self.menuchannel_2.setTitle(_translate("MainWindow", "channel 2"))
        self.menuchannel_3.setTitle(_translate("MainWindow", "channel 3"))
        self.menuchannel_4.setTitle(_translate("MainWindow", "channel 4"))
        self.menuchannel_5.setTitle(_translate("MainWindow", "channel 5"))
        self.actionexit.setText(_translate("MainWindow", "exit"))
        self.actionopen.setText(_translate("MainWindow", "open"))
        self.actionopen_file_csv.setText(_translate("MainWindow", "open file_csv"))
        self.actionload_data.setText(_translate("MainWindow", "load data"))
        self.actionclose.setText(_translate("MainWindow", "close"))
        self.actionopen_2.setText(_translate("MainWindow", "open"))
        self.actionopen_file_xls_2.setText(_translate("MainWindow", "open file_xls"))
        self.actionclose_2.setText(_translate("MainWindow", "close"))
        self.actionload_data_2.setText(_translate("MainWindow", "load data"))
        self.actionopen_3.setText(_translate("MainWindow", "open"))
        self.actionopen_file_txt.setText(_translate("MainWindow", "open file_txt"))
        self.actionload_data_3.setText(_translate("MainWindow", "load data"))
        self.actionclose_3.setText(_translate("MainWindow", "close"))
        self.actionopen_4.setText(_translate("MainWindow", "open"))
        self.actionopen_file.setText(_translate("MainWindow", "open file"))
        self.actionload_data_4.setText(_translate("MainWindow", "load data"))
        self.actionclose_4.setText(_translate("MainWindow", "close"))
        self.actionopen_5.setText(_translate("MainWindow", "open"))
        self.actionopen_file_4.setText(_translate("MainWindow", "open file"))
        self.actionload_data_5.setText(_translate("MainWindow", "load data"))
        self.actionclose_5.setText(_translate("MainWindow", "close"))
        self.actionplay.setText(_translate("MainWindow", "play"))
        self.actionopen_file_txt_2.setText(_translate("MainWindow", "open file_txt"))
        self.actionopen_file_xls.setText(_translate("MainWindow", "open file_xls"))
        self.actionopen_file_txt_3.setText(_translate("MainWindow", "open file_txt"))
        self.actionopen_file_csv_2.setText(_translate("MainWindow", "open file_csv"))
        self.actionopen_file_csv_3.setText(_translate("MainWindow", "open file_csv"))
        self.actionopen_file_xls_3.setText(_translate("MainWindow", "open file_xls"))
        self.actionopen_file_1.setText(_translate("MainWindow", "open file"))
        self.actionopen_file_2.setText(_translate("MainWindow", "open file"))
        self.actionopen_file_3.setText(_translate("MainWindow", "open file"))
        self.actionopen_file_44.setText(_translate("MainWindow", "open file"))
        self.actionopen_file_5.setText(_translate("MainWindow", "open file"))

from mplwid1 import MplWid1
from mplwid2 import MplWid2
from mplwid3 import MplWid3
from mplwid4 import MplWid4
from mplwid5 import MplWid5

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
