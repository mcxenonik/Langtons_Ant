# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'app_gui.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(378, 424)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(10, 170, 361, 91))
        self.saveImageToFileCB = QCheckBox(self.groupBox_2)
        self.saveImageToFileCB.setObjectName(u"saveImageToFileCB")
        self.saveImageToFileCB.setGeometry(QRect(10, 20, 121, 17))
        self.allIterationsRB = QRadioButton(self.groupBox_2)
        self.allIterationsRB.setObjectName(u"allIterationsRB")
        self.allIterationsRB.setEnabled(False)
        self.allIterationsRB.setGeometry(QRect(30, 40, 101, 17))
        self.everyNIterationsRB = QRadioButton(self.groupBox_2)
        self.everyNIterationsRB.setObjectName(u"everyNIterationsRB")
        self.everyNIterationsRB.setEnabled(False)
        self.everyNIterationsRB.setGeometry(QRect(30, 60, 51, 17))
        self.saveIterationsLE = QLineEdit(self.groupBox_2)
        self.saveIterationsLE.setObjectName(u"saveIterationsLE")
        self.saveIterationsLE.setEnabled(False)
        self.saveIterationsLE.setGeometry(QRect(80, 60, 31, 20))
        self.label_5 = QLabel(self.groupBox_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setEnabled(False)
        self.label_5.setGeometry(QRect(120, 60, 51, 16))
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 0, 361, 171))
        self.showImagePB = QPushButton(self.groupBox)
        self.showImagePB.setObjectName(u"showImagePB")
        self.showImagePB.setEnabled(False)
        self.showImagePB.setGeometry(QRect(260, 130, 91, 23))
        self.randomImageRB = QRadioButton(self.groupBox)
        self.randomImageRB.setObjectName(u"randomImageRB")
        self.randomImageRB.setGeometry(QRect(10, 130, 91, 17))
        self.imageFromFileRB = QRadioButton(self.groupBox)
        self.imageFromFileRB.setObjectName(u"imageFromFileRB")
        self.imageFromFileRB.setGeometry(QRect(10, 80, 91, 17))
        self.whiteImageRB = QRadioButton(self.groupBox)
        self.whiteImageRB.setObjectName(u"whiteImageRB")
        self.whiteImageRB.setGeometry(QRect(10, 30, 91, 17))
        self.whiteImageRB.setChecked(True)
        self.heightLE = QLineEdit(self.groupBox)
        self.heightLE.setObjectName(u"heightLE")
        self.heightLE.setGeometry(QRect(230, 30, 113, 20))
        self.probabilityLE = QLineEdit(self.groupBox)
        self.probabilityLE.setObjectName(u"probabilityLE")
        self.probabilityLE.setEnabled(False)
        self.probabilityLE.setGeometry(QRect(110, 130, 113, 20))
        self.widthLE = QLineEdit(self.groupBox)
        self.widthLE.setObjectName(u"widthLE")
        self.widthLE.setGeometry(QRect(110, 30, 113, 20))
        self.widthLE.setInputMethodHints(Qt.ImhNone)
        self.pathLE = QLineEdit(self.groupBox)
        self.pathLE.setObjectName(u"pathLE")
        self.pathLE.setEnabled(False)
        self.pathLE.setGeometry(QRect(110, 80, 113, 20))
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(270, 10, 47, 13))
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(130, 60, 81, 16))
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(150, 10, 47, 13))
        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(110, 110, 121, 16))
        self.generateImagePB = QPushButton(self.groupBox)
        self.generateImagePB.setObjectName(u"generateImagePB")
        self.generateImagePB.setGeometry(QRect(260, 100, 91, 23))
        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(10, 260, 361, 121))
        self.label_6 = QLabel(self.groupBox_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 20, 101, 16))
        self.numberOfIterationsLE = QLineEdit(self.groupBox_3)
        self.numberOfIterationsLE.setObjectName(u"numberOfIterationsLE")
        self.numberOfIterationsLE.setGeometry(QRect(10, 40, 101, 20))
        self.runPB = QPushButton(self.groupBox_3)
        self.runPB.setObjectName(u"runPB")
        self.runPB.setEnabled(False)
        self.runPB.setGeometry(QRect(10, 80, 75, 23))
        MainWindow.setCentralWidget(self.centralwidget)
        self.groupBox_3.raise_()
        self.groupBox_2.raise_()
        self.groupBox.raise_()
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 378, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Output", None))
        self.saveImageToFileCB.setText(QCoreApplication.translate("MainWindow", u"Save images to files", None))
        self.allIterationsRB.setText(QCoreApplication.translate("MainWindow", u"All iterations", None))
        self.everyNIterationsRB.setText(QCoreApplication.translate("MainWindow", u"Every ", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"iterations", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Image", None))
        self.showImagePB.setText(QCoreApplication.translate("MainWindow", u"Show image", None))
        self.randomImageRB.setText(QCoreApplication.translate("MainWindow", u"Random image", None))
        self.imageFromFileRB.setText(QCoreApplication.translate("MainWindow", u"Image from file", None))
        self.whiteImageRB.setText(QCoreApplication.translate("MainWindow", u"White image", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Height", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Path to image", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Width", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Probability (Black pixels)", None))
        self.generateImagePB.setText(QCoreApplication.translate("MainWindow", u"Generate image", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Algorithm", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Number of iterations", None))
        self.runPB.setText(QCoreApplication.translate("MainWindow", u"RUN", None))
    # retranslateUi

