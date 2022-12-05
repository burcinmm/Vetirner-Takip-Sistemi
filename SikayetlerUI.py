# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Sikayetler.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Sikayet(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1100, 917)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(90, 20, 891, 771))
        self.groupBox.setStyleSheet("gridline-color: rgb(193, 187, 168);\n"
"\n"
"")
        self.groupBox.setObjectName("groupBox")
        self.Tedavi_Tavsiyeler = QtWidgets.QLineEdit(self.groupBox)
        self.Tedavi_Tavsiyeler.setGeometry(QtCore.QRect(460, 360, 371, 121))
        self.Tedavi_Tavsiyeler.setStyleSheet("QLineEdit{\n"
"    border:2px solid rgb(221, 221, 221);\n"
"    border-radius:16px;\n"
"    color: rgb(0, 0, 0);\n"
"    padding-left: 20px;\n"
"    padding-right: 20px;\n"
"    background-color: rgb(239, 231, 204);\n"
"}\n"
"QLineEdit:hover{\n"
"    border: 2px solid rgb(79, 83, 102);\n"
"}\n"
"QLineEdit:focus{\n"
"    border: 2px solid rgb(85, 85, 127);\n"
"    background-color: rgb(251, 197, 123);\n"
"}")
        self.Tedavi_Tavsiyeler.setText("")
        self.Tedavi_Tavsiyeler.setObjectName("Tedavi_Tavsiyeler")
        self.Diger_Sikayetler = QtWidgets.QLineEdit(self.groupBox)
        self.Diger_Sikayetler.setGeometry(QtCore.QRect(460, 510, 371, 121))
        self.Diger_Sikayetler.setStyleSheet("QLineEdit{\n"
"    border:2px solid rgb(221, 221, 221);\n"
"    border-radius:16px;\n"
"    color: rgb(0, 0, 0);\n"
"    padding-left: 20px;\n"
"    padding-right: 20px;\n"
"    background-color: rgb(239, 231, 204);\n"
"}\n"
"QLineEdit:hover{\n"
"    border: 2px solid rgb(79, 83, 102);\n"
"}\n"
"QLineEdit:focus{\n"
"    border: 2px solid rgb(85, 85, 127);\n"
"    background-color: rgb(251, 197, 123);\n"
"}")
        self.Diger_Sikayetler.setText("")
        self.Diger_Sikayetler.setObjectName("Diger_Sikayetler")
        self.label_20 = QtWidgets.QLabel(self.groupBox)
        self.label_20.setGeometry(QtCore.QRect(470, 490, 181, 16))
        self.label_20.setObjectName("label_20")
        self.label_50 = QtWidgets.QLabel(self.groupBox)
        self.label_50.setGeometry(QtCore.QRect(460, 340, 221, 16))
        self.label_50.setObjectName("label_50")
        self.Degerlendirme = QtWidgets.QLineEdit(self.groupBox)
        self.Degerlendirme.setGeometry(QtCore.QRect(460, 50, 371, 121))
        self.Degerlendirme.setStyleSheet("QLineEdit{\n"
"    border:2px solid rgb(221, 221, 221);\n"
"    border-radius:16px;\n"
"    color: rgb(0, 0, 0);\n"
"    padding-left: 20px;\n"
"    padding-right: 20px;\n"
"    background-color: rgb(239, 231, 204);\n"
"}\n"
"QLineEdit:hover{\n"
"    border: 2px solid rgb(79, 83, 102);\n"
"}\n"
"QLineEdit:focus{\n"
"    border: 2px solid rgb(85, 85, 127);\n"
"    background-color: rgb(251, 197, 123);\n"
"}")
        self.Degerlendirme.setObjectName("Degerlendirme")
        self.label_48 = QtWidgets.QLabel(self.groupBox)
        self.label_48.setGeometry(QtCore.QRect(470, 20, 141, 16))
        self.label_48.setObjectName("label_48")
        self.Gecmis = QtWidgets.QLineEdit(self.groupBox)
        self.Gecmis.setGeometry(QtCore.QRect(460, 210, 371, 121))
        self.Gecmis.setStyleSheet("QLineEdit{\n"
"    border:2px solid rgb(221, 221, 221);\n"
"    border-radius:16px;\n"
"    color: rgb(0, 0, 0);\n"
"    padding-left: 20px;\n"
"    padding-right: 20px;\n"
"    background-color: rgb(239, 231, 204);\n"
"}\n"
"QLineEdit:hover{\n"
"    border: 2px solid rgb(79, 83, 102);\n"
"}\n"
"QLineEdit:focus{\n"
"    border: 2px solid rgb(85, 85, 127);\n"
"    background-color: rgb(251, 197, 123);\n"
"}")
        self.Gecmis.setText("")
        self.Gecmis.setObjectName("Gecmis")
        self.label_21 = QtWidgets.QLabel(self.groupBox)
        self.label_21.setGeometry(QtCore.QRect(470, 180, 111, 16))
        self.label_21.setObjectName("label_21")
        self.label_51 = QtWidgets.QLabel(self.groupBox)
        self.label_51.setGeometry(QtCore.QRect(480, 690, 101, 16))
        self.label_51.setObjectName("label_51")
        self.fiyat = QtWidgets.QLineEdit(self.groupBox)
        self.fiyat.setEnabled(False)
        self.fiyat.setGeometry(QtCore.QRect(580, 690, 71, 22))
        self.fiyat.setStyleSheet("QLineEdit{\n"
"    border:2px solid rgb(221, 221, 221);\n"
"    border-radius:6px;\n"
"    color: rgb(0, 0, 0);\n"
"    padding-left: 20px;\n"
"    padding-right: 20px;\n"
"    background-color: rgb(239, 231, 204);\n"
"}\n"
"QLineEdit:hover{\n"
"    border: 2px solid rgb(79, 83, 102);\n"
"}\n"
"QLineEdit:focus{\n"
"    border: 2px solid rgb(85, 85, 127);\n"
"    background-color: rgb(251, 197, 123);\n"
"}")
        self.fiyat.setInputMethodHints(QtCore.Qt.ImhPreferNumbers)
        self.fiyat.setObjectName("fiyat")
        self.tableWidget = QtWidgets.QTableWidget(self.groupBox)
        self.tableWidget.setGeometry(QtCore.QRect(30, 170, 301, 591))
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setRowCount(19)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(3, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(4, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(4, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(5, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(5, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(6, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(6, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(7, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(7, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(8, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(8, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(9, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(9, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(10, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(10, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(11, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(11, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(12, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(12, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(13, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(13, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(14, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(14, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(15, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(15, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(16, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(16, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(17, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(17, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(18, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(18, 1, item)
        self.label_49 = QtWidgets.QLabel(self.groupBox)
        self.label_49.setGeometry(QtCore.QRect(30, 150, 81, 16))
        self.label_49.setObjectName("label_49")
        self.Sahip_Adi1 = QtWidgets.QLineEdit(self.groupBox)
        self.Sahip_Adi1.setGeometry(QtCore.QRect(150, 20, 201, 22))
        self.Sahip_Adi1.setStyleSheet("QLineEdit{\n"
"    border:2px solid rgb(221, 221, 221);\n"
"    border-radius:6px;\n"
"    color: rgb(0, 0, 0);\n"
"    padding-left: 20px;\n"
"    padding-right: 20px;\n"
"    background-color: rgb(239, 231, 204);\n"
"}\n"
"QLineEdit:hover{\n"
"    border: 2px solid rgb(79, 83, 102);\n"
"}\n"
"QLineEdit:focus{\n"
"    border: 2px solid rgb(85, 85, 127);\n"
"    background-color: rgb(251, 197, 123);\n"
"}")
        self.Sahip_Adi1.setText("")
        self.Sahip_Adi1.setObjectName("Sahip_Adi1")
        self.label_14 = QtWidgets.QLabel(self.groupBox)
        self.label_14.setGeometry(QtCore.QRect(30, 20, 121, 20))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.groupBox)
        self.label_15.setGeometry(QtCore.QRect(30, 60, 121, 20))
        self.label_15.setObjectName("label_15")
        self.Hasta_Ismi1 = QtWidgets.QLineEdit(self.groupBox)
        self.Hasta_Ismi1.setGeometry(QtCore.QRect(150, 60, 201, 22))
        self.Hasta_Ismi1.setStyleSheet("QLineEdit{\n"
"    border:2px solid rgb(221, 221, 221);\n"
"    border-radius:6px;\n"
"    color: rgb(0, 0, 0);\n"
"    padding-left: 20px;\n"
"    padding-right: 20px;\n"
"    background-color: rgb(239, 231, 204);\n"
"}\n"
"QLineEdit:hover{\n"
"    border: 2px solid rgb(79, 83, 102);\n"
"}\n"
"QLineEdit:focus{\n"
"    border: 2px solid rgb(85, 85, 127);\n"
"    background-color: rgb(251, 197, 123);\n"
"}")
        self.Hasta_Ismi1.setText("")
        self.Hasta_Ismi1.setObjectName("Hasta_Ismi1")
        self.label_16 = QtWidgets.QLabel(self.groupBox)
        self.label_16.setGeometry(QtCore.QRect(30, 100, 121, 20))
        self.label_16.setObjectName("label_16")
        self.cmb_Cins1 = QtWidgets.QComboBox(self.groupBox)
        self.cmb_Cins1.setGeometry(QtCore.QRect(150, 100, 201, 31))
        self.cmb_Cins1.setStyleSheet("QComboBox{\n"
"border-radius:6px;\n"
"background-color: rgb(239, 231, 204);\n"
"border:2px solid rgb(221, 221, 221);\n"
"color: rgb(0, 0, 0);\n"
"}\n"
"QComboBox:hover{\n"
"border: 2px solid rgb(79, 83, 102);\n"
"}")
        self.cmb_Cins1.setObjectName("cmb_Cins1")
        self.cmb_Cins1.addItem("")
        self.cmb_Cins1.addItem("")
        self.cmb_Cins1.addItem("")
        self.cmb_Cins1.addItem("")
        self.cmb_Cins1.addItem("")
        self.cmb_Cins1.addItem("")
        self.cmb_Cins1.addItem("")
        self.cmb_Cins1.addItem("")
        self.cmb_Cins1.addItem("")
        self.btn_Kayit_Ol = QtWidgets.QPushButton(self.centralwidget)
        self.btn_Kayit_Ol.setGeometry(QtCore.QRect(390, 800, 93, 41))
        font = QtGui.QFont()
        font.setFamily("Wingdings")
        font.setPointSize(20)
        self.btn_Kayit_Ol.setFont(font)
        self.btn_Kayit_Ol.setStyleSheet("QPushButton{\n"
"    color: black;\n"
"    border-style: outset;\n"
"    border-radius: 10px;\n"
"    background-color: rgb(239, 231, 204);\n"
"}\n"
"QPushButton:pressed{\n"
"    border-style: inset;\n"
"    background-color: rgb(251, 197, 123);\n"
"}")
        self.btn_Kayit_Ol.setObjectName("btn_Kayit_Ol")
        self.btnara = QtWidgets.QPushButton(self.centralwidget)
        self.btnara.setGeometry(QtCore.QRect(520, 800, 93, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Symbol")
        font.setPointSize(22)
        self.btnara.setFont(font)
        self.btnara.setStyleSheet("QPushButton{\n"
"    color: black;\n"
"    border-style: outset;\n"
"    border-radius: 10px;\n"
"    background-color: rgb(239, 231, 204);\n"
"}\n"
"QPushButton:pressed{\n"
"    border-style: inset;\n"
"    background-color: rgb(251, 197, 123);\n"
"}")
        self.btnara.setObjectName("btnara")
        self.btn_guncelle = QtWidgets.QPushButton(self.centralwidget)
        self.btn_guncelle.setGeometry(QtCore.QRect(640, 800, 93, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Symbol")
        font.setPointSize(16)
        self.btn_guncelle.setFont(font)
        self.btn_guncelle.setStyleSheet("QPushButton{\n"
"    color: black;\n"
"    border-style: outset;\n"
"    border-radius: 10px;\n"
"    background-color: rgb(239, 231, 204);\n"
"}\n"
"QPushButton:pressed{\n"
"    border-style: inset;\n"
"    background-color: rgb(251, 197, 123);\n"
"}")
        self.btn_guncelle.setObjectName("btn_guncelle")
        self.btn_ileri1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_ileri1.setGeometry(QtCore.QRect(960, 800, 93, 41))
        font = QtGui.QFont()
        font.setFamily("Wingdings 3")
        font.setPointSize(36)
        font.setBold(False)
        font.setWeight(50)
        self.btn_ileri1.setFont(font)
        self.btn_ileri1.setStyleSheet("QPushButton{\n"
"    color: black;\n"
"    border-style: outset;\n"
"    border-radius: 10px;\n"
"    background-color: rgb(239, 231, 204);\n"
"}\n"
"QPushButton:pressed{\n"
"    border-style: inset;\n"
"    background-color: rgb(251, 197, 123);\n"
"}")
        self.btn_ileri1.setObjectName("btn_ileri1")
        self.btn_geri1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_geri1.setGeometry(QtCore.QRect(30, 800, 93, 41))
        font = QtGui.QFont()
        font.setFamily("Wingdings 3")
        font.setPointSize(36)
        self.btn_geri1.setFont(font)
        self.btn_geri1.setStyleSheet("QPushButton{\n"
"    color: black;\n"
"    border-style: outset;\n"
"    border-radius: 10px;\n"
"    background-color: rgb(239, 231, 204);\n"
"}\n"
"QPushButton:pressed{\n"
"    border-style: inset;\n"
"    background-color: rgb(251, 197, 123);\n"
"}")
        self.btn_geri1.setObjectName("btn_geri1")
        self.label_22 = QtWidgets.QLabel(self.centralwidget)
        self.label_22.setGeometry(QtCore.QRect(10, 10, 1081, 861))
        self.label_22.setStyleSheet("background-color: rgb(193, 187, 168);\n"
"border-radius: 50px;")
        self.label_22.setText("")
        self.label_22.setObjectName("label_22")
        self.label_22.raise_()
        self.btn_Kayit_Ol.raise_()
        self.btnara.raise_()
        self.btn_guncelle.raise_()
        self.btn_ileri1.raise_()
        self.btn_geri1.raise_()
        self.groupBox.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1100, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Reçete"))
        self.label_20.setText(_translate("MainWindow", "DİĞER ŞİKAYETLER:"))
        self.label_50.setText(_translate("MainWindow", "TEDAVİ VE TAVSİYELER"))
        self.label_48.setText(_translate("MainWindow", "DEĞERLENDİRME"))
        self.label_21.setText(_translate("MainWindow", "GEÇMİŞ:"))
        self.label_51.setText(_translate("MainWindow", "Ödenecek Tutar:"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("MainWindow", "Teşhisler"))
        item = self.tableWidget.item(0, 1)
        item.setText(_translate("MainWindow", "Fiyat"))
        item = self.tableWidget.item(1, 0)
        item.setText(_translate("MainWindow", "CBC"))
        item = self.tableWidget.item(1, 1)
        item.setText(_translate("MainWindow", " 50 ₺"))
        item = self.tableWidget.item(2, 0)
        item.setText(_translate("MainWindow", "T4"))
        item = self.tableWidget.item(2, 1)
        item.setText(_translate("MainWindow", "55 ₺"))
        item = self.tableWidget.item(3, 0)
        item.setText(_translate("MainWindow", "ECG"))
        item = self.tableWidget.item(3, 1)
        item.setText(_translate("MainWindow", "60 ₺"))
        item = self.tableWidget.item(4, 0)
        item.setText(_translate("MainWindow", "Deri Testi"))
        item = self.tableWidget.item(4, 1)
        item.setText(_translate("MainWindow", "65 ₺"))
        item = self.tableWidget.item(5, 0)
        item.setText(_translate("MainWindow", "FELV/FIV"))
        item = self.tableWidget.item(5, 1)
        item.setText(_translate("MainWindow", "70 ₺"))
        item = self.tableWidget.item(6, 0)
        item.setText(_translate("MainWindow", "Dışkı"))
        item = self.tableWidget.item(6, 1)
        item.setText(_translate("MainWindow", "75 ₺"))
        item = self.tableWidget.item(7, 0)
        item.setText(_translate("MainWindow", "Biyopsi"))
        item = self.tableWidget.item(7, 1)
        item.setText(_translate("MainWindow", "80 ₺"))
        item = self.tableWidget.item(8, 0)
        item.setText(_translate("MainWindow", "Chem"))
        item = self.tableWidget.item(8, 1)
        item.setText(_translate("MainWindow", "85 ₺"))
        item = self.tableWidget.item(9, 0)
        item.setText(_translate("MainWindow", "Radyografi"))
        item = self.tableWidget.item(9, 1)
        item.setText(_translate("MainWindow", "90 ₺"))
        item = self.tableWidget.item(10, 0)
        item.setText(_translate("MainWindow", "Karın Ultrasonu"))
        item = self.tableWidget.item(10, 1)
        item.setText(_translate("MainWindow", "95 ₺"))
        item = self.tableWidget.item(11, 0)
        item.setText(_translate("MainWindow", "Aerobic C ve S"))
        item = self.tableWidget.item(11, 1)
        item.setText(_translate("MainWindow", "100 ₺"))
        item = self.tableWidget.item(12, 0)
        item.setText(_translate("MainWindow", "Kalp Kurdu Testi"))
        item = self.tableWidget.item(12, 1)
        item.setText(_translate("MainWindow", "105 ₺"))
        item = self.tableWidget.item(13, 0)
        item.setText(_translate("MainWindow", "Laym Titre"))
        item = self.tableWidget.item(13, 1)
        item.setText(_translate("MainWindow", "110 ₺"))
        item = self.tableWidget.item(14, 0)
        item.setText(_translate("MainWindow", "Ameliyat Öncesi Kan Tahlili"))
        item = self.tableWidget.item(14, 1)
        item.setText(_translate("MainWindow", "115 ₺"))
        item = self.tableWidget.item(15, 0)
        item.setText(_translate("MainWindow", "İdarar Tahlili"))
        item = self.tableWidget.item(15, 1)
        item.setText(_translate("MainWindow", "120 ₺"))
        item = self.tableWidget.item(16, 0)
        item.setText(_translate("MainWindow", "Yankılı Yürek Gösterimi"))
        item = self.tableWidget.item(16, 1)
        item.setText(_translate("MainWindow", "125 ₺"))
        item = self.tableWidget.item(17, 0)
        item.setText(_translate("MainWindow", "İdrar Gösterimi"))
        item = self.tableWidget.item(17, 1)
        item.setText(_translate("MainWindow", "130 ₺"))
        item = self.tableWidget.item(18, 0)
        item.setText(_translate("MainWindow", "Diğer"))
        item = self.tableWidget.item(18, 1)
        item.setText(_translate("MainWindow", "40 ₺"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.label_49.setText(_translate("MainWindow", "Fiyat Listesi:"))
        self.label_14.setText(_translate("MainWindow", "SAHİP ADI:"))
        self.label_15.setText(_translate("MainWindow", "HASTA İSMİ:"))
        self.label_16.setText(_translate("MainWindow", "HASTA CİNSİ:"))
        self.cmb_Cins1.setItemText(0, _translate("MainWindow", "Seçiniz"))
        self.cmb_Cins1.setItemText(1, _translate("MainWindow", "Kedi"))
        self.cmb_Cins1.setItemText(2, _translate("MainWindow", "Köpek"))
        self.cmb_Cins1.setItemText(3, _translate("MainWindow", "At"))
        self.cmb_Cins1.setItemText(4, _translate("MainWindow", "Büyükbaş"))
        self.cmb_Cins1.setItemText(5, _translate("MainWindow", "Küçükbaş"))
        self.cmb_Cins1.setItemText(6, _translate("MainWindow", "Kuş"))
        self.cmb_Cins1.setItemText(7, _translate("MainWindow", "Sürüngen"))
        self.cmb_Cins1.setItemText(8, _translate("MainWindow", "Diğer"))
        self.btn_Kayit_Ol.setText(_translate("MainWindow", "<"))
        self.btnara.setText(_translate("MainWindow", ""))
        self.btn_guncelle.setText(_translate("MainWindow", ""))
        self.btn_ileri1.setText(_translate("MainWindow", ""))
        self.btn_geri1.setText(_translate("MainWindow", ""))
