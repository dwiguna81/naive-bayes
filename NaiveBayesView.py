# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NaiveBayesView.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from library import connection, messagebox
import matplotlib.pyplot as plt
import numpy as np
saveDataChart = []


class Ui_NaiveBayesWindow(object):
    def homeView(self):
        from HomeView import Ui_HomeWindow
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_HomeWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def datasetView(self):
        from DatasetView import Ui_DatasetWindow
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_DatasetWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def preprocessingView(self):
        from preprocessingView import Ui_PreprocessingWindow
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_PreprocessingWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def show_algoritma(self):
        try:
            cur, con = connection()
            cur.execute("SELECT sentimen, komentar FROM naive_bayes")
            result = cur.fetchall()
            self.tbAlgoritma.setRowCount(0)
            self.tbAlgoritma.setHorizontalHeaderLabels(['sentimen', 'komentar'])

            for row_number, row_data in enumerate(result):
                self.tbAlgoritma.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.tbAlgoritma.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

            sql = "select sentimen from naive_bayes where sentimen = %s"
            cur.execute(sql, 'Positive')
            positive = cur.fetchall()

            sql = "select sentimen from naive_bayes where sentimen = %s"
            cur.execute(sql, 'Negative')
            negative = cur.fetchall()

            sql = "select sentimen from naive_bayes where sentimen = %s"
            cur.execute(sql, 'Neutral')
            neutral = cur.fetchall()

            cur.execute("select * from link")
            link = cur.fetchall()

            cur.execute("select * from komentar")
            komentar = cur.fetchall()

            persentase_positive = (len(positive) / len(result)) * 100
            persentase_negative = (len(negative) / len(result)) * 100
            persentase_neutral = (len(neutral) / len(result)) * 100

            self.lbPositive.setText(str("%.2f" % persentase_positive + ' %'))
            self.lbNegative.setText(str("%.2f" % persentase_negative + ' %'))
            self.lbNeutral.setText(str("%.2f" % persentase_neutral + ' %'))
            self.lbLink.setText(str(len(link)))
            self.lbKomentar.setText(str(len(komentar)))
            dataChart = [['positif', "%.2f" % persentase_positive], ['negatif', "%.2f" % persentase_negative], ['netral', "%.2f" % persentase_neutral]]

            saveDataChart.append(dataChart)
        except Exception as e:
            print(e)

    def piechart(self):
        y = np.array([saveDataChart[0][0][1], saveDataChart[0][1][1], saveDataChart[0][2][1]])
        mylabels = [saveDataChart[0][0][0] + ' (' + saveDataChart[0][0][1] + '%)', saveDataChart[0][1][0] + ' (' + saveDataChart[0][1][1] + '%)', saveDataChart[0][2][0] + ' (' + saveDataChart[0][2][1] + '%)']
        if (saveDataChart[0][0][1] > saveDataChart[0][1][1] > saveDataChart[0][2][1]):
                myexplode = [0.1, 0, 0]
        elif (saveDataChart[0][1][1] > saveDataChart[0][0][1] > saveDataChart[0][2][1]):
                myexplode = [0, 0.1, 0]
        else:
                myexplode = [0, 0, 0.1]

        plt.title('Grafik Hasil Perhitungan Algoritma Naive Bayes')
        plt.pie(y, labels=mylabels, explode=myexplode)
        plt.savefig('pieChart.png')
        plt.show()

    def setupUi(self, NaiveBayesWindow):
        NaiveBayesWindow.setObjectName("NaiveBayesWindow")
        NaiveBayesWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(NaiveBayesWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(0, 30, 801, 61))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("background-color: rgb(0, 143, 241);\n"
"color: rgb(255, 255, 255);")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.lbLink = QtWidgets.QLabel(self.centralwidget)
        self.lbLink.setGeometry(QtCore.QRect(20, 530, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lbLink.setFont(font)
        self.lbLink.setAutoFillBackground(False)
        self.lbLink.setStyleSheet("background-color: rgb(255, 255, 255); border-radius: 5px; padding-right: 8px;")
        self.lbLink.setText("")
        self.lbLink.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbLink.setObjectName("lbLink")
        self.lbKomentar = QtWidgets.QLabel(self.centralwidget)
        self.lbKomentar.setGeometry(QtCore.QRect(170, 530, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lbKomentar.setFont(font)
        self.lbKomentar.setStyleSheet("background-color: rgb(255, 255, 255); border-radius: 5px; padding-right: 8px;")
        self.lbKomentar.setText("")
        self.lbKomentar.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbKomentar.setObjectName("lbKomentar")
        self.lbPositive = QtWidgets.QLabel(self.centralwidget)
        self.lbPositive.setGeometry(QtCore.QRect(330, 530, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lbPositive.setFont(font)
        self.lbPositive.setStyleSheet("background-color: rgb(255, 255, 255); border-radius: 5px; padding-right: 8px;")
        self.lbPositive.setText("")
        self.lbPositive.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.lbPositive.setObjectName("lbPositive")
        self.lbNegative = QtWidgets.QLabel(self.centralwidget)
        self.lbNegative.setGeometry(QtCore.QRect(500, 530, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lbNegative.setFont(font)
        self.lbNegative.setStyleSheet("background-color: rgb(255, 255, 255); border-radius: 5px; padding-right: 8px;")
        self.lbNegative.setText("")
        self.lbNegative.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.lbNegative.setObjectName("lbNegative")
        self.lbNeutral = QtWidgets.QLabel(self.centralwidget)
        self.lbNeutral.setGeometry(QtCore.QRect(650, 530, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lbNeutral.setFont(font)
        self.lbNeutral.setStyleSheet("background-color: rgb(255, 255, 255); border-radius: 5px; padding-right: 8px;")
        self.lbNeutral.setText("")
        self.lbNeutral.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbNeutral.setObjectName("lbNeutral")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(30, 110, 751, 16))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(20, 510, 120, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(170, 510, 120, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(330, 510, 120, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(500, 510, 120, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(650, 510, 120, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.tbAlgoritma = QtWidgets.QTableWidget(self.centralwidget)
        self.tbAlgoritma.setGeometry(QtCore.QRect(20, 140, 761, 351))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(10)
        self.tbAlgoritma.setFont(font)
        self.tbAlgoritma.setObjectName("tbAlgoritma")
        self.tbAlgoritma.setColumnCount(2)
        self.tbAlgoritma.setRowCount(0)
        self.show_algoritma()
        header = self.tbAlgoritma.horizontalHeader()
        header.setStretchLastSection(True)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-4, 0, 811, 31))
        self.label.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.btnHome = QtWidgets.QPushButton(self.centralwidget)
        self.btnHome.setGeometry(QtCore.QRect(0, 0, 101, 30))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(9)
        self.btnHome.setFont(font)
        self.btnHome.setStyleSheet("border: 1px solid;\n"
"border-color: rgb(35,178,254);")
        self.btnHome.setObjectName("btnHome")
        self.btnHome.clicked.connect(self.homeView)
        self.btnDataset = QtWidgets.QPushButton(self.centralwidget)
        self.btnDataset.setGeometry(QtCore.QRect(100, 0, 101, 30))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(9)
        self.btnDataset.setFont(font)
        self.btnDataset.setStyleSheet("border: 1px solid;\n"
"border-color: rgb(35,178,254);")
        self.btnDataset.setObjectName("btnDataset")
        self.btnDataset.clicked.connect(self.datasetView)
        self.btnPreprocessing = QtWidgets.QPushButton(self.centralwidget)
        self.btnPreprocessing.setGeometry(QtCore.QRect(200, 0, 101, 30))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(9)
        self.btnPreprocessing.setFont(font)
        self.btnPreprocessing.setStyleSheet("border: 1px solid;\n"
"border-color: rgb(35,178,254);")
        self.btnPreprocessing.setObjectName("btnPreprocessing")
        self.btnPreprocessing.clicked.connect(self.preprocessingView)
        self.btnAlgoritma = QtWidgets.QPushButton(self.centralwidget)
        self.btnAlgoritma.setGeometry(QtCore.QRect(300, 0, 141, 30))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.btnAlgoritma.setFont(font)
        self.btnAlgoritma.setStyleSheet("background-color: rgb(35,178,254);\n"
"color: rgb(255, 255, 255);\n"
"border: none;")
        self.btnAlgoritma.setObjectName("btnAlgoritma")
        self.btnAlgoritma.clicked.connect(self.piechart)
        self.label.raise_()
        self.label_6.raise_()
        self.lbLink.raise_()
        self.lbKomentar.raise_()
        self.lbPositive.raise_()
        self.lbNegative.raise_()
        self.lbNeutral.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.label_9.raise_()
        self.label_10.raise_()
        self.label_11.raise_()
        self.label_12.raise_()
        self.tbAlgoritma.raise_()
        self.btnHome.raise_()
        self.btnDataset.raise_()
        self.btnPreprocessing.raise_()
        self.btnAlgoritma.raise_()
        NaiveBayesWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(NaiveBayesWindow)
        QtCore.QMetaObject.connectSlotsByName(NaiveBayesWindow)

    def retranslateUi(self, NaiveBayesWindow):
        _translate = QtCore.QCoreApplication.translate
        NaiveBayesWindow.setWindowTitle(_translate("NaiveBayesWindow", "Naive Bayes View"))
        self.label_6.setText(_translate("NaiveBayesWindow", "Algoritma Naive Bayes"))
        self.label_7.setText(_translate("NaiveBayesWindow", "Hasil Algoritma Naive Bayes"))
        self.label_8.setText(_translate("NaiveBayesWindow", "Jumlah Link"))
        self.label_9.setText(_translate("NaiveBayesWindow", "Jumlah Komentar"))
        self.label_10.setText(_translate("NaiveBayesWindow", "Persentase Positive"))
        self.label_11.setText(_translate("NaiveBayesWindow", "Persentase Negative"))
        self.label_12.setText(_translate("NaiveBayesWindow", "Persentase Neutral"))
        self.btnHome.setText(_translate("NaiveBayesWindow", "Home"))
        self.btnDataset.setText(_translate("NaiveBayesWindow", "Dataset"))
        self.btnPreprocessing.setText(_translate("NaiveBayesWindow", "Preprocessing"))
        self.btnAlgoritma.setText(_translate("NaiveBayesWindow", "Algoritma Naive Bayes"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    NaiveBayesWindow = QtWidgets.QMainWindow()
    ui = Ui_NaiveBayesWindow()
    ui.setupUi(NaiveBayesWindow)
    NaiveBayesWindow.show()
    sys.exit(app.exec_())