# Form implementation generated from reading ui file '.\addEditCoffeeForm.ui'
#
# Created by: PyQt6 UI code generator 6.8.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(473, 433)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.edit_name = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.edit_name.setGeometry(QtCore.QRect(150, 10, 291, 31))
        self.edit_name.setObjectName("edit_name")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 141, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 60, 141, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 110, 141, 31))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 170, 141, 31))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 220, 141, 31))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 270, 141, 31))
        self.label_6.setObjectName("label_6")
        self.edit_roasted = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.edit_roasted.setGeometry(QtCore.QRect(150, 60, 291, 31))
        self.edit_roasted.setObjectName("edit_roasted")
        self.edit_type = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.edit_type.setGeometry(QtCore.QRect(150, 110, 291, 31))
        self.edit_type.setObjectName("edit_type")
        self.edit_taste = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.edit_taste.setGeometry(QtCore.QRect(150, 160, 291, 31))
        self.edit_taste.setObjectName("edit_taste")
        self.edit_cost = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.edit_cost.setGeometry(QtCore.QRect(150, 210, 291, 31))
        self.edit_cost.setObjectName("edit_cost")
        self.edit_amount = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.edit_amount.setGeometry(QtCore.QRect(150, 260, 291, 31))
        self.edit_amount.setObjectName("edit_amount")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(120, 320, 231, 81))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Название"))
        self.label_2.setText(_translate("MainWindow", "Степень обжарки"))
        self.label_3.setText(_translate("MainWindow", "Тип зерен"))
        self.label_4.setText(_translate("MainWindow", "Описание вкуса"))
        self.label_5.setText(_translate("MainWindow", "Цена"))
        self.label_6.setText(_translate("MainWindow", "Объем упаковки"))
        self.pushButton.setText(_translate("MainWindow", "Добавить"))