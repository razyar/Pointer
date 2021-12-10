# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_main.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(750, 500)
        MainWindow.setMinimumSize(QtCore.QSize(750, 500))
        MainWindow.setMaximumSize(QtCore.QSize(750, 500))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ico.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: rgb(160, 169, 179);\n"
"\n"
"border: 0px solid;\n"
"border-radius: 10px;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Big John PRO Light")
        font.setBold(True)
        font.setWeight(75)
        self.frame.setFont(font)
        self.frame.setStyleSheet("color: rgb(0, 0, 0);\n"
"\n"
"background-image: url(:/1/bg.jpg);\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(230, 250, 201, 21))
        self.lineEdit_2.setStyleSheet("QLineEdit {\n"
"    border: 0px solid;\n"
"        border-radius: 10px;\n"
"    \n"
"    color: rgb(170, 0, 0);\n"
"    font: 8pt \"Big John PRO Light\";\n"
"    \n"
"    background-image: url(:/1/icons/btn.png);\n"
"\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    \n"
"\n"
"\n"
"\n"
"}")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 430, 51, 43))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"    border: 0px solid;\n"
"        border-radius: 10px;\n"
"    color: rgb(0, 0, 0);\n"
"    image: url(:/1/icons/github.png);\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"\n"
"\n"
"\n"
"}")
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(190, 250, 31, 21))
        font = QtGui.QFont()
        font.setFamily("Big John PRO Light")
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(0, 0, 0);")
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(280, 460, 181, 21))
        font = QtGui.QFont()
        font.setFamily("Big John PRO")
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.pushButton_6 = QtWidgets.QPushButton(self.frame)
        self.pushButton_6.setGeometry(QtCore.QRect(440, 250, 24, 21))
        self.pushButton_6.setStyleSheet("QPushButton{\n"
"    border: 0px solid;\n"
"        border-radius: 10px;\n"
"    color: rgb(0, 0, 0);\n"
"    background-image: url(:/1/icons/cil-check-alt.png);\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"\n"
"\n"
"\n"
"}")
        self.pushButton_6.setText("")
        self.pushButton_6.setObjectName("pushButton_6")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(190, 280, 31, 21))
        font = QtGui.QFont()
        font.setFamily("Big John PRO Light")
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_2.setObjectName("label_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_3.setGeometry(QtCore.QRect(230, 280, 201, 21))
        self.lineEdit_3.setStyleSheet("QLineEdit {\n"
"    border: 0px solid;\n"
"        border-radius: 10px;\n"
"    \n"
"    color: rgb(170, 0, 0);\n"
"    font: 8pt \"Big John PRO Light\";\n"
"    \n"
"    background-image: url(:/1/icons/btn.png);\n"
"\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    \n"
"\n"
"\n"
"\n"
"}")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton_7 = QtWidgets.QPushButton(self.frame)
        self.pushButton_7.setGeometry(QtCore.QRect(440, 280, 24, 21))
        self.pushButton_7.setStyleSheet("QPushButton{\n"
"    border: 0px solid;\n"
"        border-radius: 10px;\n"
"    color: rgb(0, 0, 0);\n"
"    background-image: url(:/1/icons/cil-check-alt.png);\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"\n"
"\n"
"\n"
"}")
        self.pushButton_7.setText("")
        self.pushButton_7.setObjectName("pushButton_7")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(190, 310, 31, 21))
        font = QtGui.QFont()
        font.setFamily("Big John PRO Light")
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_4.setObjectName("label_4")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_4.setGeometry(QtCore.QRect(230, 310, 201, 21))
        self.lineEdit_4.setStyleSheet("QLineEdit {\n"
"    border: 0px solid;\n"
"        border-radius: 10px;\n"
"    \n"
"    color: rgb(170, 0, 0);\n"
"    font: 8pt \"Big John PRO Light\";\n"
"    \n"
"    background-image: url(:/1/icons/btn.png);\n"
"\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    \n"
"\n"
"\n"
"\n"
"}")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.pushButton_8 = QtWidgets.QPushButton(self.frame)
        self.pushButton_8.setGeometry(QtCore.QRect(440, 310, 24, 21))
        self.pushButton_8.setStyleSheet("QPushButton{\n"
"    border: 0px solid;\n"
"        border-radius: 10px;\n"
"    color: rgb(0, 0, 0);\n"
"    background-image: url(:/1/icons/cil-check-alt.png);\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"\n"
"\n"
"\n"
"}")
        self.pushButton_8.setText("")
        self.pushButton_8.setObjectName("pushButton_8")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(200, 170, 201, 61))
        font = QtGui.QFont()
        font.setFamily("Big John PRO Bold")
        font.setPointSize(32)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(400, 170, 111, 61))
        font = QtGui.QFont()
        font.setFamily("Big John PRO Bold")
        font.setPointSize(32)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(170, 0, 0);")
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Pointer"))
        self.label.setText(_translate("MainWindow", "Point"))
        self.label_3.setText(_translate("MainWindow", "Say everything, Fuck everyone."))
        self.label_2.setText(_translate("MainWindow", "Time"))
        self.label_4.setText(_translate("MainWindow", "Gift"))
        self.label_5.setText(_translate("MainWindow", "P O I N T"))
        self.label_6.setText(_translate("MainWindow", "E R"))
import qrc_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

import qrc_rc