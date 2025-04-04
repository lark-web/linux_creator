# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/lark/PycharmProjects/linux_creator/linux_creator.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit_Work_Directory = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_Work_Directory.setGeometry(QtCore.QRect(50, 60, 201, 27))
        self.lineEdit_Work_Directory.setObjectName("lineEdit_Work_Directory")
        self.pushButton_Create_Work_Space = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Create_Work_Space.setGeometry(QtCore.QRect(330, 60, 181, 27))
        self.pushButton_Create_Work_Space.setObjectName("pushButton_Create_Work_Space")
        self.pushButton_Select_Work_Directory = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Select_Work_Directory.setGeometry(QtCore.QRect(50, 30, 201, 27))
        self.pushButton_Select_Work_Directory.setObjectName("pushButton_Select_Work_Directory")
        self.pushButton_br_config = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_br_config.setGeometry(QtCore.QRect(70, 160, 161, 27))
        self.pushButton_br_config.setObjectName("pushButton_br_config")
        self.pushButton_br_build = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_br_build.setGeometry(QtCore.QRect(70, 200, 161, 27))
        self.pushButton_br_build.setObjectName("pushButton_br_build")
        self.pushButton_kernel_build = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_kernel_build.setGeometry(QtCore.QRect(290, 160, 141, 27))
        self.pushButton_kernel_build.setObjectName("pushButton_kernel_build")
        self.pushButton_uboot_build = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_uboot_build.setGeometry(QtCore.QRect(500, 160, 141, 27))
        self.pushButton_uboot_build.setObjectName("pushButton_uboot_build")
        self.pushButton_image_build = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_image_build.setGeometry(QtCore.QRect(70, 320, 161, 27))
        self.pushButton_image_build.setObjectName("pushButton_image_build")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 24))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.menuFile.addSeparator()
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_Create_Work_Space.setText(_translate("MainWindow", "Create Work Space"))
        self.pushButton_Select_Work_Directory.setText(_translate("MainWindow", "Select Work Directory"))
        self.pushButton_br_config.setText(_translate("MainWindow", "br-config"))
        self.pushButton_br_build.setText(_translate("MainWindow", "br-build"))
        self.pushButton_kernel_build.setText(_translate("MainWindow", "kernel-build"))
        self.pushButton_uboot_build.setText(_translate("MainWindow", "Uboot-build"))
        self.pushButton_image_build.setText(_translate("MainWindow", "image-build"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
