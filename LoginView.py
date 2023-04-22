# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LoginView.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from library import connection, messagebox
import resources


class Ui_MainWindow(object):
    def gotoRegister(self):
        from RegisterView import Ui_MainWindow
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def checkLogin(self):
        cur, con = connection()
        username = self.username.text()
        passsword = self.password.text()
        data = (username, passsword)

        if (username == '' or passsword == ''):
            return messagebox('Peringatan', 'Pastikan Mengisi Semua Kolom!')

        self.btnRegister.setEnabled(False)
        self.btnLogin.setEnabled(False)

        sql = "select * from user where username = %s and password = %s"
        cur.execute(sql, data)
        result = cur.fetchall()

        if (result):
            messagebox('Berhasil', 'Anda Berhasil Login!')
            from HomeView import Ui_HomeWindow
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_HomeWindow()
            self.ui.setupUi(self.window)
            self.window.show()
        else:
            messagebox('Gagal', 'Pastikan username dan password benar!')
            self.btnRegister.setEnabled(True)
            self.btnLogin.setEnabled(True)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 548)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, -10, 801, 571))
        self.label_2.setPixmap(QtGui.QPixmap(":/newPrefix/dipake.jpg"))
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(230, 70, 351, 401))
        self.label.setStyleSheet("background-color: rgba(255, 255, 255, 50%);\n"
"border-radius: 15px;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(360, 90, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(230, 130, 351, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(280, 200, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.username = QtWidgets.QLineEdit(self.centralwidget)
        self.username.setGeometry(QtCore.QRect(280, 220, 251, 31))
        self.username.setStyleSheet("border-radius: 5px;")
        self.username.setObjectName("username")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(280, 270, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_6.setObjectName("label_6")
        self.password = QtWidgets.QLineEdit(self.centralwidget)
        self.password.setGeometry(QtCore.QRect(280, 290, 251, 31))
        self.password.setStyleSheet("border-radius: 5px;")
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.btnLogin = QtWidgets.QPushButton(self.centralwidget)
        self.btnLogin.setGeometry(QtCore.QRect(340, 370, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.btnLogin.setFont(font)
        self.btnLogin.setStyleSheet("background-color: rgb(0, 0, 127);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.btnLogin.setObjectName("btnLogin")
        self.btnLogin.clicked.connect(self.checkLogin)
        self.btnRegister = QtWidgets.QPushButton(self.centralwidget)
        self.btnRegister.setGeometry(QtCore.QRect(320, 410, 171, 23))
        self.btnRegister.setStyleSheet("background-color: transparent;\n"
"color: rgb(255, 255, 255);")
        self.btnRegister.setObjectName("btnRegister")
        self.btnRegister.clicked.connect(self.gotoRegister)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/newPrefix/dipake.jpg\"/></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "SIGN IN"))
        self.label_4.setText(_translate("MainWindow", "Gunakan akun yang sudah didaftarkan!"))
        self.label_5.setText(_translate("MainWindow", "Username"))
        self.label_6.setText(_translate("MainWindow", "Password"))
        self.btnLogin.setText(_translate("MainWindow", "LOGIN"))
        self.btnRegister.setText(_translate("MainWindow", "Tidak punya akun? Daftar Disini"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
