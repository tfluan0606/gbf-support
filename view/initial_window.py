# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'initial_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_initial_window(object):
    def setupUi(self, initial_window):
        initial_window.setObjectName("initial_window")
        initial_window.resize(400, 500)
        self.centralwidget = QtWidgets.QWidget(initial_window)
        self.centralwidget.setObjectName("centralwidget")
        self.start = QtWidgets.QPushButton(self.centralwidget)
        self.start.setGeometry(QtCore.QRect(135, 300, 130, 60))
        self.start.setObjectName("start")
        self.windowlist = QtWidgets.QComboBox(self.centralwidget)
        self.windowlist.setGeometry(QtCore.QRect(30, 160, 201, 50))
        self.windowlist.setObjectName("windowlist")
        self.refresh = QtWidgets.QPushButton(self.centralwidget)
        self.refresh.setGeometry(QtCore.QRect(270, 170, 111, 41))
        self.refresh.setObjectName("refresh")
        initial_window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(initial_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 21))
        self.menubar.setObjectName("menubar")
        initial_window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(initial_window)
        self.statusbar.setObjectName("statusbar")
        initial_window.setStatusBar(self.statusbar)

        self.retranslateUi(initial_window)
        QtCore.QMetaObject.connectSlotsByName(initial_window)

    def retranslateUi(self, initial_window):
        _translate = QtCore.QCoreApplication.translate
        initial_window.setWindowTitle(_translate("initial_window", "MainWindow"))
        self.start.setText(_translate("initial_window", "開始"))
        self.refresh.setText(_translate("initial_window", "刷新視窗"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    initial_window = QtWidgets.QMainWindow()
    ui = Ui_initial_window()
    ui.setupUi(initial_window)
    initial_window.show()
    sys.exit(app.exec_())
