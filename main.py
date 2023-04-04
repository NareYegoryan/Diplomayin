from PyQt5.QtWidgets import QApplication, QTableWidget, QTableWidgetItem

import sys

from PyQt5 import QtWidgets,QtGui
from PyQt5.QtWidgets import QHeaderView, QLabel, QMainWindow, QLineEdit, QDateEdit, QRadioButton, QVBoxLayout, QTimeEdit, QScrollArea,QWidget,QTextEdit,QPushButton,QStackedWidget,QHBoxLayout,QStackedLayout
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import mysql.connector
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget
class Window(QMainWindow):
    def __init__(self):

        super(Window,self).__init__()

        self.setWindowTitle(" Your Pharmacy ")
        self.setGeometry(0, 0, 1320, 3590)

        self.setWindowIcon(QtGui.QIcon("icon.png"))
#
        self.scroll = QScrollArea()
        self.widget = QWidget()
        self.widget.resize(1350,3000)
        self.widget.setObjectName("WID")
        self.widget.setStyleSheet("#WID {background-color: #ACE1AF;}")
        self.scroll.setWidget(self.widget)
        self.setCentralWidget(self.scroll)

        self.button = QPushButton("Show Pharmacies in map", self.widget)
        self.button.setGeometry(1100, 250, 220, 30)
        self.button.clicked.connect(self.show_pharmacies)

        layout = QVBoxLayout(self)
        layout.addWidget(self.button)


######################################################
        self.buttonA = QPushButton("Alfa Pharm", self.widget)
        self.buttonA.setGeometry(10, 250, 120, 30)
        self.buttonA.clicked.connect(self.Alpha)

        self.buttonN = QPushButton("Natalie Pharm", self.widget)
        self.buttonN.setGeometry(140, 250, 120, 30)
        self.buttonN.clicked.connect(self.Natali)

        self.buttonV = QPushButton("Vaga Pharm", self.widget)
        self.buttonV.setGeometry(270, 250, 120, 30)
        self.buttonV.clicked.connect(self.Vaga)

        self.buttonAll = QPushButton(" All Pharmacies ", self.widget)
        self.buttonAll.setGeometry(400, 250, 120, 30)
        self.buttonAll.clicked.connect(self.populate_table)
########################################################
        self.nkar = QtWidgets.QLabel(self.widget)
        self.logo1 = QPixmap("logo.png")
        self.nkar.setPixmap(self.logo1)
        self.nkar.setGeometry(50, 50, 100, 100)
        self.nkar.adjustSize()

        self.nkar2 = QtWidgets.QLabel(self.widget)
        self.logo2 = QPixmap("logo.png")
        self.nkar2.setPixmap(self.logo2)
        self.nkar2.setGeometry(1200, 50, 100, 100)
        self.nkar2.adjustSize()


        self.header = QLabel(self.widget)
        self.header.setText("Your Pharmacy")
        self.header.move(400, 5)
        path_to_font_file = r'C:\Users\User\Downloads\relettered\Relettered.ttf'
        font_id = QFontDatabase.addApplicationFont(path_to_font_file)
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        self.header.setFont(QFont(font_family, 120))
        self.header.setStyleSheet("font-weight: bold;"
                                  "color: black")


        ################################################

        # create a QTableWidget with three columns
        self.table = QTableWidget(self.widget)

        self.table.move(10, 280)
        self.table.resize(1320, 3000)
        self.table.setColumnCount(5)

        self.table.setColumnWidth(0, 530)
        self.table.setColumnWidth(1, 125)
        self.table.setColumnWidth(2, 200)
        self.table.setColumnWidth(3, 200)
        self.table.setColumnWidth(4, 300)

        row = self.table.rowCount()
        col = self.table.columnCount()
        font = QFont()
        font.setPointSize(12)
        self.table.setFont(font)

        # set the headers for the QTableWidget
        headers = ["Picture", "Price", "Pharmacy Name", "Medicine Name",  "Pharmacy Adress"]
        self.table.setHorizontalHeaderLabels(headers)
        horizontal_header = self.table.horizontalHeader()
        font = QFont("Arial", 12)
        horizontal_header.setFont(font)

        #self.table.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)
        self.table.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.table.cellDoubleClicked.connect(self.open_website)


        # establish a connection to the MySQL database
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1111",
            database="pharmacy"
        )

            # create a cursor object
        self.cursor = self.conn.cursor()

        self.showMaximized()




    def Alpha(self):
        self.table.clearContents()
        self.table.setRowCount(0)
        self.table.setHorizontalHeaderLabels([])


        self.cursor.execute("SELECT PharmMed.MedicineName, PharmMed.Money, PharmMed.Picture, PharmMed.PharmacyName, PharmMed.PharmacyAdress FROM PharmMed WHERE PharmMed.PharmacyName='Alfa Pharm'")
        for MedicineName, Money, Picture, PharmacyName, PharmacyAdress in self.cursor:
            # create a QPixmap for the medicine picture
            pixmap = QPixmap()
            pixmap.loadFromData(Picture)

            # create a QTableWidgetItem for each column
            pictureItem = QTableWidgetItem()
            pictureItem.setData(Qt.DecorationRole, pixmap)
            moneyItem = QTableWidgetItem(Money)
            pharmacyNameItem = QTableWidgetItem(PharmacyName)
            MedicineNameItem = QTableWidgetItem(MedicineName)
            PharmacyAdressItem = QTableWidgetItem(PharmacyAdress)

            # add the QTableWidgetItem to the QTableWidget
            row = self.table.rowCount()
            self.table.insertRow(row)
            self.table.setItem(row, 0, pictureItem)
            self.table.setItem(row, 1, QTableWidgetItem(str(Money)))
            self.table.setItem(row, 2, pharmacyNameItem)
            self.table.setItem(row, 3, MedicineNameItem)
            self.table.setItem(row, 4, PharmacyAdressItem)

            for row in range(self.table.rowCount()):
                self.table.setRowHeight(row, 250)
    def Natali(self):
        self.table.clearContents()
        self.table.setRowCount(0)
        self.table.setHorizontalHeaderLabels([])

        self.cursor.execute("SELECT PharmMed.MedicineName, PharmMed.Money, PharmMed.Picture, PharmMed.PharmacyName, PharmMed.PharmacyAdress FROM PharmMed WHERE PharmMed.PharmacyName='Natali Pharm'")
        for MedicineName, Money, Picture, PharmacyName, PharmacyAdress in self.cursor:
            # create a QPixmap for the medicine picture
            pixmap = QPixmap()
            pixmap.loadFromData(Picture)

            # create a QTableWidgetItem for each column
            pictureItem = QTableWidgetItem()
            pictureItem.setData(Qt.DecorationRole, pixmap)
            moneyItem = QTableWidgetItem(Money)
            pharmacyNameItem = QTableWidgetItem(PharmacyName)
            MedicineNameItem = QTableWidgetItem(MedicineName)
            PharmacyAdressItem = QTableWidgetItem(PharmacyAdress)

            # add the QTableWidgetItem to the QTableWidget
            row = self.table.rowCount()
            self.table.insertRow(row)
            self.table.setItem(row, 0, pictureItem)
            self.table.setItem(row, 1, QTableWidgetItem(str(Money)))
            self.table.setItem(row, 2, pharmacyNameItem)
            self.table.setItem(row, 3, MedicineNameItem)
            self.table.setItem(row, 4, PharmacyAdressItem)

            for row in range(self.table.rowCount()):
                self.table.setRowHeight(row, 250)

    def Vaga(self):
        self.table.clearContents()
        self.table.setRowCount(0)
        self.table.setHorizontalHeaderLabels([])

        self.cursor.execute("SELECT PharmMed.MedicineName, PharmMed.Money, PharmMed.Picture, PharmMed.PharmacyName, PharmMed.PharmacyAdress FROM PharmMed WHERE PharmMed.PharmacyName='Vaga Pharm'")
        for MedicineName, Money, Picture, PharmacyName, PharmacyAdress in self.cursor:
            # create a QPixmap for the medicine picture
            pixmap = QPixmap()
            pixmap.loadFromData(Picture)

            # create a QTableWidgetItem for each column
            pictureItem = QTableWidgetItem()
            pictureItem.setData(Qt.DecorationRole, pixmap)
            moneyItem = QTableWidgetItem(Money)
            pharmacyNameItem = QTableWidgetItem(PharmacyName)
            MedicineNameItem = QTableWidgetItem(MedicineName)
            PharmacyAdressItem = QTableWidgetItem(PharmacyAdress)

            # add the QTableWidgetItem to the QTableWidget
            row = self.table.rowCount()
            self.table.insertRow(row)
            self.table.setItem(row, 0, pictureItem)
            self.table.setItem(row, 1, QTableWidgetItem(str(Money)))
            self.table.setItem(row, 2, pharmacyNameItem)
            self.table.setItem(row, 3, MedicineNameItem)
            self.table.setItem(row, 4, PharmacyAdressItem)

            for row in range(self.table.rowCount()):
                self.table.setRowHeight(row, 250)
    def populate_table(self):

        self.table.clearContents()
        self.table.setRowCount(0)
        self.table.setHorizontalHeaderLabels([])
        # execute a SELECT statement to retrieve the medicine pictures, descriptions, and pharmacy names
        self.cursor.execute("SELECT PharmMed.MedicineName, PharmMed.Money, PharmMed.Picture, PharmMed.pharmacyName, PharmMed.pharmacyAdress FROM PharmMed ")

        # iterate over the result set and add each medicine to the QTableWidget
        for MedicineName, Money, Picture, PharmacyName, PharmacyAdress in self.cursor:
            # create a QPixmap for the medicine picture
            pixmap = QPixmap()
            pixmap.loadFromData(Picture)

            # create a QTableWidgetItem for each column
            pictureItem = QTableWidgetItem()
            pictureItem.setData(Qt.DecorationRole, pixmap)
            moneyItem = QTableWidgetItem(Money)
            pharmacyNameItem = QTableWidgetItem(PharmacyName)
            MedicineNameItem = QTableWidgetItem(MedicineName)
            PharmacyAdressItem = QTableWidgetItem(PharmacyAdress)

            # add the QTableWidgetItem to the QTableWidget
            row = self.table.rowCount()
            self.table.insertRow(row)
            self.table.setItem(row, 0, pictureItem)
            self.table.setItem(row, 1, QTableWidgetItem(str(Money)))
            self.table.setItem(row, 2, pharmacyNameItem)
            self.table.setItem(row, 3, MedicineNameItem)
            self.table.setItem(row, 4, PharmacyAdressItem)

            for row in range(self.table.rowCount()):
                self.table.setRowHeight(row, 250)
    def search(self):
        search_query = self.search_edit.text()
        print(f"Searching for: {search_query}")

    def show_pharmacies(self):
        url = "https://www.google.com/maps/search/pharmacy"
        QDesktopServices.openUrl(QUrl(url))

    def open_website(self,row,col):


        if row == 0 and col == 3:
            url = QUrl("https://alfapharm.am/hy/products/details/1552/%D5%BA%D5%A1%D6%80%D5%A1%D6%81%D5%A5%D5%BF%D5%A1%D5%B4%D5%B8%D5%AC-%D5%A4%D5%B0%D5%BF-500%D5%B4%D5%A3-x-10")
            QDesktopServices.openUrl(url)
        elif row == 1 and col == 3:
            url = QUrl("https://alfapharm.am/hy/products/details/1552/%D5%BA%D5%A1%D6%80%D5%A1%D6%81%D5%A5%D5%BF%D5%A1%D5%B4%D5%B8%D5%AC-%D5%A4%D5%B0%D5%BF-500%D5%B4%D5%A3-x-10")
            QDesktopServices.openUrl(url)
        elif row == 2 and col == 3:
            url = QUrl("https://alfapharm.am/hy/products/details/1552/%D5%BA%D5%A1%D6%80%D5%A1%D6%81%D5%A5%D5%BF%D5%A1%D5%B4%D5%B8%D5%AC-%D5%A4%D5%B0%D5%BF-500%D5%B4%D5%A3-x-10")
            QDesktopServices.openUrl(url)
        elif row == 3 and col == 3:
            url = QUrl("https://alfapharm.am/hy/products/details/1552/%D5%BA%D5%A1%D6%80%D5%A1%D6%81%D5%A5%D5%BF%D5%A1%D5%B4%D5%B8%D5%AC-%D5%A4%D5%B0%D5%BF-500%D5%B4%D5%A3-x-10")
            QDesktopServices.openUrl(url)
        elif row == 4 and col == 3:
            url = QUrl("https://alfapharm.am/hy/products/details/1552/%D5%BA%D5%A1%D6%80%D5%A1%D6%81%D5%A5%D5%BF%D5%A1%D5%B4%D5%B8%D5%AC-%D5%A4%D5%B0%D5%BF-500%D5%B4%D5%A3-x-10")
            QDesktopServices.openUrl(url)
        elif row == 5 and col == 3:
            url = QUrl("https://natalipharm.am/hy/")
            QDesktopServices.openUrl(url)
        elif row == 6 and col == 3:
            url = QUrl("https://natalipharm.am/hy/")
            QDesktopServices.openUrl(url)
        elif row == 7 and col == 3:
            url = QUrl("https://natalipharm.am/hy/")
            QDesktopServices.openUrl(url)
        elif row == 8 and col == 3:
            url = QUrl("https://natalipharm.am/hy/")
            QDesktopServices.openUrl(url)
        elif row == 9 and col == 3:
            url = QUrl("https://natalipharm.am/hy/")
            QDesktopServices.openUrl(url)
        elif row == 10 and col == 3:
            url = QUrl("https://vagapharm.am/en/")
            QDesktopServices.openUrl(url)
        elif row == 11 and col == 3:
            url = QUrl("https://vagapharm.am/en/")
            QDesktopServices.openUrl(url)
        elif row == 12 and col == 3:
            url = QUrl("https://vagapharm.am/en/")
            QDesktopServices.openUrl(url)
        elif row == 13 and col == 3:
            url = QUrl("https://vagapharm.am/en/")
            QDesktopServices.openUrl(url)
        elif row == 14 and col == 3:
            url = QUrl("https://vagapharm.am/en/")
            QDesktopServices.openUrl(url)
        elif row == 15 and col == 3:
            url = QUrl("https://alfapharm.am/hy/products/details/2548/%D5%A1%D5%BD%D5%AF%D5%B8%D5%A5%D5%B6-%D5%A4%D5%B0%D5%BF-x-10")
            QDesktopServices.openUrl(url)
        elif row == 16 and col == 3:
            url = QUrl("https://alfapharm.am/hy/products/details/2548/%D5%A1%D5%BD%D5%AF%D5%B8%D5%A5%D5%B6-%D5%A4%D5%B0%D5%BF-x-10")
            QDesktopServices.openUrl(url)
        elif row == 17 and col == 3:
            url = QUrl("https://alfapharm.am/hy/products/details/2548/%D5%A1%D5%BD%D5%AF%D5%B8%D5%A5%D5%B6-%D5%A4%D5%B0%D5%BF-x-10")
            QDesktopServices.openUrl(url)
        elif row == 18 and col == 3:
            url = QUrl("https://alfapharm.am/hy/products/details/2548/%D5%A1%D5%BD%D5%AF%D5%B8%D5%A5%D5%B6-%D5%A4%D5%B0%D5%BF-x-10")
            QDesktopServices.openUrl(url)
        elif row == 19 and col == 3:
            url = QUrl("https://alfapharm.am/hy/products/details/2548/%D5%A1%D5%BD%D5%AF%D5%B8%D5%A5%D5%B6-%D5%A4%D5%B0%D5%BF-x-10")
            QDesktopServices.openUrl(url)
        elif row == 20 and col == 3:
            url = QUrl("https://natalipharm.am/hy/")
            QDesktopServices.openUrl(url)
        elif row == 21 and col == 3:
            url = QUrl("https://natalipharm.am/hy/")
            QDesktopServices.openUrl(url)
        elif row == 22 and col == 3:
            url = QUrl("https://natalipharm.am/hy/")
            QDesktopServices.openUrl(url)
        elif row == 23 and col == 3:
            url = QUrl("https://natalipharm.am/hy/")
            QDesktopServices.openUrl(url)
        elif row == 24 and col == 3:
            url = QUrl("https://natalipharm.am/hy/")
            QDesktopServices.openUrl(url)
        elif row == 25 and col == 3:
            url = QUrl("https://vagapharm.am/en/")
            QDesktopServices.openUrl(url)
        elif row == 26 and col == 3:
            url = QUrl("https://vagapharm.am/en/")
            QDesktopServices.openUrl(url)
        elif row == 27 and col == 3:
            url = QUrl("https://vagapharm.am/en/")
            QDesktopServices.openUrl(url)
        elif row == 28 and col == 3:
            url = QUrl("https://vagapharm.am/en/")
            QDesktopServices.openUrl(url)
        elif row == 29 and col == 3:
            url = QUrl("https://vagapharm.am/en/")
            QDesktopServices.openUrl(url)
        elif row == 30 and col == 3:
            url = QUrl("https://alfapharm.am/hy/products/details/1872/%D5%BF%D5%A5%D5%B4%D5%BA%D5%A1%D5%AC%D5%A3%D5%AB%D5%B6-%D5%A4%D5%B0%D5%BF-%D5%A9%D5%BA-x-20")
            QDesktopServices.openUrl(url)
        elif row == 31 and col == 3:
            url = QUrl("https://alfapharm.am/hy/products/details/1872/%D5%BF%D5%A5%D5%B4%D5%BA%D5%A1%D5%AC%D5%A3%D5%AB%D5%B6-%D5%A4%D5%B0%D5%BF-%D5%A9%D5%BA-x-20")
            QDesktopServices.openUrl(url)
        elif row == 32 and col == 3:
            url = QUrl("https://alfapharm.am/hy/products/details/1872/%D5%BF%D5%A5%D5%B4%D5%BA%D5%A1%D5%AC%D5%A3%D5%AB%D5%B6-%D5%A4%D5%B0%D5%BF-%D5%A9%D5%BA-x-20")
            QDesktopServices.openUrl(url)
        elif row == 33 and col == 3:
            url = QUrl("https://alfapharm.am/hy/products/details/1872/%D5%BF%D5%A5%D5%B4%D5%BA%D5%A1%D5%AC%D5%A3%D5%AB%D5%B6-%D5%A4%D5%B0%D5%BF-%D5%A9%D5%BA-x-20")
            QDesktopServices.openUrl(url)
        elif row == 34 and col == 3:
            url = QUrl("https://alfapharm.am/hy/products/details/1872/%D5%BF%D5%A5%D5%B4%D5%BA%D5%A1%D5%AC%D5%A3%D5%AB%D5%B6-%D5%A4%D5%B0%D5%BF-%D5%A9%D5%BA-x-20")
            QDesktopServices.openUrl(url)
        elif row == 35 and col == 3:
            url = QUrl("https://natalipharm.am/hy/")
            QDesktopServices.openUrl(url)
        elif row == 36 and col == 3:
            url = QUrl("https://natalipharm.am/hy/")
            QDesktopServices.openUrl(url)
        elif row == 37 and col == 3:
            url = QUrl("https://natalipharm.am/hy/")
            QDesktopServices.openUrl(url)
        elif row == 38 and col == 3:
            url = QUrl("https://natalipharm.am/hy/")
            QDesktopServices.openUrl(url)
        elif row == 39 and col == 3:
            url = QUrl("https://natalipharm.am/hy/")
            QDesktopServices.openUrl(url)
        elif row == 40 and col == 3:
            url = QUrl("https://vagapharm.am/en/")
            QDesktopServices.openUrl(url)
        elif row == 41 and col == 3:
            url = QUrl("https://vagapharm.am/en/")
            QDesktopServices.openUrl(url)
        elif row == 42 and col == 3:
            url = QUrl("https://vagapharm.am/en/")
            QDesktopServices.openUrl(url)
        elif row == 43 and col == 3:
            url = QUrl("https://vagapharm.am/en/")
            QDesktopServices.openUrl(url)
        elif row == 44 and col == 3:
            url = QUrl("https://vagapharm.am/en/")
            QDesktopServices.openUrl(url)
        elif row == 45 and col == 3:
            url = QUrl("https://alfapharm.am/hy/products/details/1424/%D5%B4%D5%A1%D5%A1%D5%AC%D5%B8%D6%84%D5%BD-%D5%AE%D5%A1%D5%B4-%D5%A4%D5%B0%D5%BF-x-40")
            QDesktopServices.openUrl(url)
        elif row == 46 and col == 3:
            url = QUrl("https://alfapharm.am/hy/products/details/1424/%D5%B4%D5%A1%D5%A1%D5%AC%D5%B8%D6%84%D5%BD-%D5%AE%D5%A1%D5%B4-%D5%A4%D5%B0%D5%BF-x-40")
            QDesktopServices.openUrl(url)
        elif row == 47 and col == 3:
            url = QUrl("https://alfapharm.am/hy/products/details/1424/%D5%B4%D5%A1%D5%A1%D5%AC%D5%B8%D6%84%D5%BD-%D5%AE%D5%A1%D5%B4-%D5%A4%D5%B0%D5%BF-x-40")
            QDesktopServices.openUrl(url)
        elif row == 48 and col == 3:
            url = QUrl("https://alfapharm.am/hy/products/details/1424/%D5%B4%D5%A1%D5%A1%D5%AC%D5%B8%D6%84%D5%BD-%D5%AE%D5%A1%D5%B4-%D5%A4%D5%B0%D5%BF-x-40")
            QDesktopServices.openUrl(url)
        elif row == 49 and col == 3:
            url = QUrl("https://alfapharm.am/hy/products/details/1424/%D5%B4%D5%A1%D5%A1%D5%AC%D5%B8%D6%84%D5%BD-%D5%AE%D5%A1%D5%B4-%D5%A4%D5%B0%D5%BF-x-40")
            QDesktopServices.openUrl(url)
        elif row == 50 and col == 3:
            url = QUrl("https://natalipharm.am/hy/")
            QDesktopServices.openUrl(url)
        elif row == 51 and col == 3:
            url = QUrl("https://natalipharm.am/hy/")
            QDesktopServices.openUrl(url)
        elif row == 52 and col == 3:
            url = QUrl("https://natalipharm.am/hy/")
            QDesktopServices.openUrl(url)
        elif row == 53 and col == 3:
            url = QUrl("https://natalipharm.am/hy/")
            QDesktopServices.openUrl(url)
        elif row == 54 and col == 3:
            url = QUrl("https://natalipharm.am/hy/")
            QDesktopServices.openUrl(url)
        elif row == 55 and col == 3:
            url = QUrl("https://vagapharm.am/en/")
            QDesktopServices.openUrl(url)
        elif row == 56 and col == 3:
            url = QUrl("https://vagapharm.am/en/")
            QDesktopServices.openUrl(url)
        elif row == 57 and col == 3:
            url = QUrl("https://vagapharm.am/en/")
            QDesktopServices.openUrl(url)
        elif row == 58 and col == 3:
            url = QUrl("https://vagapharm.am/en/")
            QDesktopServices.openUrl(url)
        elif row == 59 and col == 3:
            url = QUrl("https://vagapharm.am/en/")
            QDesktopServices.openUrl(url)
        elif row == 60 and col == 3:
            url = QUrl("https://alfapharm.am/hy/products/details/1941/%D5%A1%D5%B6%D5%A1%D5%AC%D5%A3%D5%AB%D5%B6-%D5%BD%D6%80%D5%BE-50-2%D5%B4%D5%AC-x-10")
            QDesktopServices.openUrl(url)
        elif row == 61 and col == 3:
            url = QUrl("https://alfapharm.am/hy/products/details/1941/%D5%A1%D5%B6%D5%A1%D5%AC%D5%A3%D5%AB%D5%B6-%D5%BD%D6%80%D5%BE-50-2%D5%B4%D5%AC-x-10")
            QDesktopServices.openUrl(url)
        elif row == 62 and col == 3:
            url = QUrl("https://alfapharm.am/hy/products/details/1941/%D5%A1%D5%B6%D5%A1%D5%AC%D5%A3%D5%AB%D5%B6-%D5%BD%D6%80%D5%BE-50-2%D5%B4%D5%AC-x-10")
            QDesktopServices.openUrl(url)
        elif row == 63 and col == 3:
            url = QUrl("https://alfapharm.am/hy/products/details/1941/%D5%A1%D5%B6%D5%A1%D5%AC%D5%A3%D5%AB%D5%B6-%D5%BD%D6%80%D5%BE-50-2%D5%B4%D5%AC-x-10")
            QDesktopServices.openUrl(url)
        elif row == 64 and col == 3:
            url = QUrl("https://alfapharm.am/hy/products/details/1941/%D5%A1%D5%B6%D5%A1%D5%AC%D5%A3%D5%AB%D5%B6-%D5%BD%D6%80%D5%BE-50-2%D5%B4%D5%AC-x-10")
            QDesktopServices.openUrl(url)
        elif row == 65 and col == 3:
            url = QUrl("https://natalipharm.am/hy/")
            QDesktopServices.openUrl(url)
        elif row == 66 and col == 3:
            url = QUrl("https://natalipharm.am/hy/")
            QDesktopServices.openUrl(url)
        elif row == 67 and col == 3:
            url = QUrl("https://natalipharm.am/hy/")
            QDesktopServices.openUrl(url)
        elif row == 68 and col == 3:
            url = QUrl("https://natalipharm.am/hy/")
            QDesktopServices.openUrl(url)
        elif row == 69 and col == 3:
            url = QUrl("https://natalipharm.am/hy/")
            QDesktopServices.openUrl(url)
        elif row == 70 and col == 3:
            url = QUrl("https://vagapharm.am/en/")
            QDesktopServices.openUrl(url)
        elif row == 71 and col == 3:
            url = QUrl("https://vagapharm.am/en/")
            QDesktopServices.openUrl(url)
        elif row == 72 and col == 3:
            url = QUrl("https://vagapharm.am/en/")
            QDesktopServices.openUrl(url)
        elif row == 73 and col == 3:
            url = QUrl("https://vagapharm.am/en/")
            QDesktopServices.openUrl(url)
        elif row == 74 and col == 3:
            url = QUrl("https://vagapharm.am/en/")
            QDesktopServices.openUrl(url)

        if row == 0 and col == 4:
            url = QUrl("https://www.google.com/maps/place/6+Samvel+Safaryani+poxoc,+Yerevan/@40.1979634,44.5634224,17z/data=!3m1!4b1!4m6!3m5!1s0x406aa330a72aa399:0xd3a084ad1619388d!8m2!3d40.1979593!4d44.5656111!16s%2Fg%2F11t142bg4x")
            QDesktopServices.openUrl(url)
        elif row == 1 and col == 4:
            url = QUrl("https://www.google.com/maps/place/51+Karakhanyan+St,+Yerevan+0092/@40.175261,44.5641856,17z/data=!3m1!4b1!4m6!3m5!1s0x406abca65d2d53d3:0x36b7cb0a82d800e2!8m2!3d40.1752569!4d44.5663743!16s%2Fg%2F11pckm_gjk")
            QDesktopServices.openUrl(url)
        elif row == 2 and col == 4:
            url = QUrl("https://www.google.com/maps/place/8,+Yeritsyan+Supermarket,+2+Gai+Ave,+Yerevan+0056/@40.1998151,44.5639763,17z/data=!3m1!4b1!4m6!3m5!1s0x406aa33a57efddc7:0xd23b343fefb270d!8m2!3d40.199811!4d44.566165!16s%2Fg%2F11r63j0vm3")
            QDesktopServices.openUrl(url)
        elif row == 3 and col == 4:
            url = QUrl("https://www.google.com/maps/place/2+Bakunts+St,+Yerevan+0076/@40.1922488,44.5701601,17z/data=!3m1!4b1!4m6!3m5!1s0x406aa34902eb717f:0x2a671344ce65716b!8m2!3d40.1922447!4d44.5723488!16s%2Fg%2F11cp7ygcmd")
            QDesktopServices.openUrl(url)
        elif row == 4 and col == 4:
            url = QUrl("https://www.google.com/maps/place/4+Moldovakan+St,+Yerevan+0062/@40.2059188,44.5669872,17z/data=!3m1!4b1!4m6!3m5!1s0x406aa3228fe74251:0x648e66c406b23399!8m2!3d40.2059147!4d44.5691759!16s%2Fg%2F11h0t6m20r")
            QDesktopServices.openUrl(url)
        elif row == 5 and col == 4:
            url = QUrl("https://www.google.com/maps/place/55+Raffi+St,+Yerevan/@40.1740784,44.4455331,17.57z/data=!4m5!3m4!1s0x406abde8043ffbf5:0x862e14823299000c!8m2!3d40.1741174!4d44.4470146")
            QDesktopServices.openUrl(url)
        elif row == 6 and col == 4:
            url = QUrl("https://www.google.com/maps/place/Natali+Pharm/@40.1712626,44.4860039,14z/data=!4m10!1m2!2m1!1snatali+pharm!3m6!1s0x406abd36b6d6d747:0xfcc8bbca7fc33d7!8m2!3d40.1712626!4d44.5189629!15sCgxuYXRhbGkgcGhhcm1aDiIMbmF0YWxpIHBoYXJtkgEIcGhhcm1hY3ngAQA!16s%2Fg%2F11g18tpbxf")
            QDesktopServices.openUrl(url)
        elif row == 7 and col == 4:
            url = QUrl("https://www.google.com/maps/place/33+Abovyan+poxoc,+Yerevan+0009/@40.1877682,44.5210342,17z/data=!3m1!4b1!4m6!3m5!1s0x406abce09c329a4b:0x190558989842c3c2!8m2!3d40.1877641!4d44.5232229!16s%2Fg%2F1tl7m60h")
            QDesktopServices.openUrl(url)
        elif row == 8 and col == 4:
            url = QUrl("https://www.google.com/maps/place/24+Tumanyan+St,+Yerevan+0001/@40.1818338,44.5164513,17z/data=!3m1!4b1!4m6!3m5!1s0x406abce4e5477817:0x2c20ed9c97bd6c5!8m2!3d40.1818297!4d44.51864!16s%2Fg%2F1vmq_wgh")
            QDesktopServices.openUrl(url)
        elif row == 9 and col == 4:
            url = QUrl("https://www.google.com/maps/place/Natali+Pharm+PHARMACY/@40.2010788,44.4770028,15z/data=!4m10!1m2!2m1!1sNatali+Pharm!3m6!1s0x406abd6a412a48d3:0x77502653562eabde!8m2!3d40.2010788!4d44.4934823!15sCgxOYXRhbGkgUGhhcm1aDiIMbmF0YWxpIHBoYXJtkgEIcGhhcm1hY3ngAQA!16s%2Fg%2F11g6vl789s")
            QDesktopServices.openUrl(url)
        elif row == 10 and col == 4:
            url = QUrl("https://www.google.com/maps/place/20+Acharyan+St,+Yerevan+0040/@40.2153655,44.5605928,17z/data=!3m1!4b1!4m6!3m5!1s0x406aa2e3e5c9b7d9:0xb2b5c0d32ebffa2!8m2!3d40.2153614!4d44.5627815!16s%2Fg%2F11lqm9llj_")
            QDesktopServices.openUrl(url)
        elif row == 11 and col == 4:
            url = QUrl("https://www.google.com/maps/place/5+Andranik+Zoravar+St,+Yerevan+0064/@40.1790695,44.4447396,17z/data=!3m1!4b1!4m6!3m5!1s0x406abdec01023e0d:0x96fe98df9a9db657!8m2!3d40.1790654!4d44.4469283!16s%2Fg%2F11cpb74wcy")
            QDesktopServices.openUrl(url)
        elif row == 12 and col == 4:
            url = QUrl("https://www.google.com/maps/place/4th,+17+Mikoyan+St,+Yerevan+0090/@40.1827248,44.5660781,17z/data=!3m1!4b1!4m5!3m4!1s0x406abcadf4de7723:0x1c6c93cd4bda2376!8m2!3d40.1827207!4d44.5682668")
            QDesktopServices.openUrl(url)
        elif row == 13 and col == 4:
            url = QUrl("https://www.google.com/maps/place/8+Moskovyan+pokhoc,+Yerevan/@40.1884219,44.5157268,17z/data=!3m1!4b1!4m6!3m5!1s0x406abce029004929:0x1eb0b9f9e1e81713!8m2!3d40.1884178!4d44.5179155!16s%2Fg%2F11bw42gcd4")
            QDesktopServices.openUrl(url)
        elif row == 14 and col == 4:
            url = QUrl("https://www.google.com/maps/place/17%2F8+Tigran+Petrosyan+St,+Yerevan+0054/@40.2182195,44.4874528,17z/data=!3m1!4b1!4m6!3m5!1s0x406a97fdca62b4c9:0x697446759049ca54!8m2!3d40.2182154!4d44.4896415!16s%2Fg%2F11bw49k7sc")
            QDesktopServices.openUrl(url)
        elif row == 15 and col == 4:
            url = QUrl("https://www.google.com/maps/place/6+Samvel+Safaryani+poxoc,+Yerevan/@40.1979634,44.5634224,17z/data=!3m1!4b1!4m6!3m5!1s0x406aa330a72aa399:0xd3a084ad1619388d!8m2!3d40.1979593!4d44.5656111!16s%2Fg%2F11t142bg4x")
            QDesktopServices.openUrl(url)
        elif row == 16 and col == 4:
            url = QUrl("https://www.google.com/maps/place/51+Karakhanyan+St,+Yerevan+0092/@40.175261,44.5641856,17z/data=!3m1!4b1!4m6!3m5!1s0x406abca65d2d53d3:0x36b7cb0a82d800e2!8m2!3d40.1752569!4d44.5663743!16s%2Fg%2F11pckm_gjk")
            QDesktopServices.openUrl(url)
        elif row == 17 and col == 4:
            url = QUrl("https://www.google.com/maps/place/8,+Yeritsyan+Supermarket,+2+Gai+Ave,+Yerevan+0056/@40.1998151,44.5639763,17z/data=!3m1!4b1!4m6!3m5!1s0x406aa33a57efddc7:0xd23b343fefb270d!8m2!3d40.199811!4d44.566165!16s%2Fg%2F11r63j0vm3")
            QDesktopServices.openUrl(url)
        elif row == 18 and col == 4:
            url = QUrl("https://www.google.com/maps/place/2+Bakunts+St,+Yerevan+0076/@40.1922488,44.5701601,17z/data=!3m1!4b1!4m6!3m5!1s0x406aa34902eb717f:0x2a671344ce65716b!8m2!3d40.1922447!4d44.5723488!16s%2Fg%2F11cp7ygcmd")
            QDesktopServices.openUrl(url)
        elif row == 19 and col == 4:
            url = QUrl("https://www.google.com/maps/place/4+Moldovakan+St,+Yerevan+0062/@40.2059188,44.5669872,17z/data=!3m1!4b1!4m6!3m5!1s0x406aa3228fe74251:0x648e66c406b23399!8m2!3d40.2059147!4d44.5691759!16s%2Fg%2F11h0t6m20r")
            QDesktopServices.openUrl(url)
        elif row == 20 and col == 4:
            url = QUrl("https://www.google.com/maps/place/55+Raffi+St,+Yerevan/@40.1740784,44.4455331,17.57z/data=!4m5!3m4!1s0x406abde8043ffbf5:0x862e14823299000c!8m2!3d40.1741174!4d44.4470146")
            QDesktopServices.openUrl(url)
        elif row == 21 and col == 4:
            url = QUrl("https://www.google.com/maps/place/Natali+Pharm/@40.1712626,44.4860039,14z/data=!4m10!1m2!2m1!1snatali+pharm!3m6!1s0x406abd36b6d6d747:0xfcc8bbca7fc33d7!8m2!3d40.1712626!4d44.5189629!15sCgxuYXRhbGkgcGhhcm1aDiIMbmF0YWxpIHBoYXJtkgEIcGhhcm1hY3ngAQA!16s%2Fg%2F11g18tpbxf")
            QDesktopServices.openUrl(url)
        elif row == 22 and col == 4:
            url = QUrl("https://www.google.com/maps/place/33+Abovyan+poxoc,+Yerevan+0009/@40.1877682,44.5210342,17z/data=!3m1!4b1!4m6!3m5!1s0x406abce09c329a4b:0x190558989842c3c2!8m2!3d40.1877641!4d44.5232229!16s%2Fg%2F1tl7m60h")
            QDesktopServices.openUrl(url)
        elif row == 23 and col == 4:
            url = QUrl("https://www.google.com/maps/place/24+Tumanyan+St,+Yerevan+0001/@40.1818338,44.5164513,17z/data=!3m1!4b1!4m6!3m5!1s0x406abce4e5477817:0x2c20ed9c97bd6c5!8m2!3d40.1818297!4d44.51864!16s%2Fg%2F1vmq_wgh")
            QDesktopServices.openUrl(url)
        elif row == 24 and col == 4:
            url = QUrl("https://www.google.com/maps/place/Natali+Pharm+PHARMACY/@40.2010788,44.4770028,15z/data=!4m10!1m2!2m1!1sNatali+Pharm!3m6!1s0x406abd6a412a48d3:0x77502653562eabde!8m2!3d40.2010788!4d44.4934823!15sCgxOYXRhbGkgUGhhcm1aDiIMbmF0YWxpIHBoYXJtkgEIcGhhcm1hY3ngAQA!16s%2Fg%2F11g6vl789s")
            QDesktopServices.openUrl(url)
        elif row == 25 and col == 4:
            url = QUrl("https://www.google.com/maps/place/20+Acharyan+St,+Yerevan+0040/@40.2153655,44.5605928,17z/data=!3m1!4b1!4m6!3m5!1s0x406aa2e3e5c9b7d9:0xb2b5c0d32ebffa2!8m2!3d40.2153614!4d44.5627815!16s%2Fg%2F11lqm9llj_")
            QDesktopServices.openUrl(url)
        elif row == 26 and col == 4:
            url = QUrl("https://www.google.com/maps/place/5+Andranik+Zoravar+St,+Yerevan+0064/@40.1790695,44.4447396,17z/data=!3m1!4b1!4m6!3m5!1s0x406abdec01023e0d:0x96fe98df9a9db657!8m2!3d40.1790654!4d44.4469283!16s%2Fg%2F11cpb74wcy")
            QDesktopServices.openUrl(url)
        elif row == 27 and col == 4:
            url = QUrl("https://www.google.com/maps/place/4th,+17+Mikoyan+St,+Yerevan+0090/@40.1827248,44.5660781,17z/data=!3m1!4b1!4m5!3m4!1s0x406abcadf4de7723:0x1c6c93cd4bda2376!8m2!3d40.1827207!4d44.5682668")
            QDesktopServices.openUrl(url)
        elif row == 28 and col == 4:
            url = QUrl("https://www.google.com/maps/place/8+Moskovyan+pokhoc,+Yerevan/@40.1884219,44.5157268,17z/data=!3m1!4b1!4m6!3m5!1s0x406abce029004929:0x1eb0b9f9e1e81713!8m2!3d40.1884178!4d44.5179155!16s%2Fg%2F11bw42gcd4")
            QDesktopServices.openUrl(url)
        elif row == 29 and col == 4:
            url = QUrl("https://www.google.com/maps/place/17%2F8+Tigran+Petrosyan+St,+Yerevan+0054/@40.2182195,44.4874528,17z/data=!3m1!4b1!4m6!3m5!1s0x406a97fdca62b4c9:0x697446759049ca54!8m2!3d40.2182154!4d44.4896415!16s%2Fg%2F11bw49k7sc")
            QDesktopServices.openUrl(url)
        elif row == 30 and col == 4:
            url = QUrl("https://www.google.com/maps/place/6+Samvel+Safaryani+poxoc,+Yerevan/@40.1979634,44.5634224,17z/data=!3m1!4b1!4m6!3m5!1s0x406aa330a72aa399:0xd3a084ad1619388d!8m2!3d40.1979593!4d44.5656111!16s%2Fg%2F11t142bg4x")
            QDesktopServices.openUrl(url)
        elif row == 31 and col == 4:
            url = QUrl("https://www.google.com/maps/place/51+Karakhanyan+St,+Yerevan+0092/@40.175261,44.5641856,17z/data=!3m1!4b1!4m6!3m5!1s0x406abca65d2d53d3:0x36b7cb0a82d800e2!8m2!3d40.1752569!4d44.5663743!16s%2Fg%2F11pckm_gjk")
            QDesktopServices.openUrl(url)
        elif row == 32 and col == 4:
            url = QUrl("https://www.google.com/maps/place/8,+Yeritsyan+Supermarket,+2+Gai+Ave,+Yerevan+0056/@40.1998151,44.5639763,17z/data=!3m1!4b1!4m6!3m5!1s0x406aa33a57efddc7:0xd23b343fefb270d!8m2!3d40.199811!4d44.566165!16s%2Fg%2F11r63j0vm3")
            QDesktopServices.openUrl(url)
        elif row == 33 and col == 4:
            url = QUrl("https://www.google.com/maps/place/2+Bakunts+St,+Yerevan+0076/@40.1922488,44.5701601,17z/data=!3m1!4b1!4m6!3m5!1s0x406aa34902eb717f:0x2a671344ce65716b!8m2!3d40.1922447!4d44.5723488!16s%2Fg%2F11cp7ygcmd")
            QDesktopServices.openUrl(url)
        elif row == 34 and col == 4:
            url = QUrl("https://www.google.com/maps/place/4+Moldovakan+St,+Yerevan+0062/@40.2059188,44.5669872,17z/data=!3m1!4b1!4m6!3m5!1s0x406aa3228fe74251:0x648e66c406b23399!8m2!3d40.2059147!4d44.5691759!16s%2Fg%2F11h0t6m20r")
            QDesktopServices.openUrl(url)
        elif row == 35 and col == 4:
            url = QUrl("https://www.google.com/maps/place/55+Raffi+St,+Yerevan/@40.1740784,44.4455331,17.57z/data=!4m5!3m4!1s0x406abde8043ffbf5:0x862e14823299000c!8m2!3d40.1741174!4d44.4470146")
            QDesktopServices.openUrl(url)
        elif row == 36 and col == 4:
            url = QUrl("https://www.google.com/maps/place/Natali+Pharm/@40.1712626,44.4860039,14z/data=!4m10!1m2!2m1!1snatali+pharm!3m6!1s0x406abd36b6d6d747:0xfcc8bbca7fc33d7!8m2!3d40.1712626!4d44.5189629!15sCgxuYXRhbGkgcGhhcm1aDiIMbmF0YWxpIHBoYXJtkgEIcGhhcm1hY3ngAQA!16s%2Fg%2F11g18tpbxf")
            QDesktopServices.openUrl(url)
        elif row == 37 and col == 4:
            url = QUrl("https://www.google.com/maps/place/33+Abovyan+poxoc,+Yerevan+0009/@40.1877682,44.5210342,17z/data=!3m1!4b1!4m6!3m5!1s0x406abce09c329a4b:0x190558989842c3c2!8m2!3d40.1877641!4d44.5232229!16s%2Fg%2F1tl7m60h")
            QDesktopServices.openUrl(url)
        elif row == 38 and col == 4:
            url = QUrl("https://www.google.com/maps/place/24+Tumanyan+St,+Yerevan+0001/@40.1818338,44.5164513,17z/data=!3m1!4b1!4m6!3m5!1s0x406abce4e5477817:0x2c20ed9c97bd6c5!8m2!3d40.1818297!4d44.51864!16s%2Fg%2F1vmq_wgh")
            QDesktopServices.openUrl(url)
        elif row == 39 and col == 4:
            url = QUrl("https://www.google.com/maps/place/Natali+Pharm+PHARMACY/@40.2010788,44.4770028,15z/data=!4m10!1m2!2m1!1sNatali+Pharm!3m6!1s0x406abd6a412a48d3:0x77502653562eabde!8m2!3d40.2010788!4d44.4934823!15sCgxOYXRhbGkgUGhhcm1aDiIMbmF0YWxpIHBoYXJtkgEIcGhhcm1hY3ngAQA!16s%2Fg%2F11g6vl789s")
            QDesktopServices.openUrl(url)
        elif row == 40 and col == 4:
            url = QUrl("https://www.google.com/maps/place/20+Acharyan+St,+Yerevan+0040/@40.2153655,44.5605928,17z/data=!3m1!4b1!4m6!3m5!1s0x406aa2e3e5c9b7d9:0xb2b5c0d32ebffa2!8m2!3d40.2153614!4d44.5627815!16s%2Fg%2F11lqm9llj_")
            QDesktopServices.openUrl(url)
        elif row == 41 and col == 4:
            url = QUrl("https://www.google.com/maps/place/5+Andranik+Zoravar+St,+Yerevan+0064/@40.1790695,44.4447396,17z/data=!3m1!4b1!4m6!3m5!1s0x406abdec01023e0d:0x96fe98df9a9db657!8m2!3d40.1790654!4d44.4469283!16s%2Fg%2F11cpb74wcy")
            QDesktopServices.openUrl(url)
        elif row == 42 and col == 4:
            url = QUrl("https://www.google.com/maps/place/4th,+17+Mikoyan+St,+Yerevan+0090/@40.1827248,44.5660781,17z/data=!3m1!4b1!4m5!3m4!1s0x406abcadf4de7723:0x1c6c93cd4bda2376!8m2!3d40.1827207!4d44.5682668")
            QDesktopServices.openUrl(url)
        elif row == 43 and col == 4:
            url = QUrl("https://www.google.com/maps/place/8+Moskovyan+pokhoc,+Yerevan/@40.1884219,44.5157268,17z/data=!3m1!4b1!4m6!3m5!1s0x406abce029004929:0x1eb0b9f9e1e81713!8m2!3d40.1884178!4d44.5179155!16s%2Fg%2F11bw42gcd4")
            QDesktopServices.openUrl(url)
        elif row == 44 and col == 4:
            url = QUrl("https://www.google.com/maps/place/17%2F8+Tigran+Petrosyan+St,+Yerevan+0054/@40.2182195,44.4874528,17z/data=!3m1!4b1!4m6!3m5!1s0x406a97fdca62b4c9:0x697446759049ca54!8m2!3d40.2182154!4d44.4896415!16s%2Fg%2F11bw49k7sc")
            QDesktopServices.openUrl(url)
        elif row == 45 and col == 4:
            url = QUrl("https://www.google.com/maps/place/6+Samvel+Safaryani+poxoc,+Yerevan/@40.1979634,44.5634224,17z/data=!3m1!4b1!4m6!3m5!1s0x406aa330a72aa399:0xd3a084ad1619388d!8m2!3d40.1979593!4d44.5656111!16s%2Fg%2F11t142bg4x")
            QDesktopServices.openUrl(url)
        elif row == 46 and col == 4:
            url = QUrl("https://www.google.com/maps/place/51+Karakhanyan+St,+Yerevan+0092/@40.175261,44.5641856,17z/data=!3m1!4b1!4m6!3m5!1s0x406abca65d2d53d3:0x36b7cb0a82d800e2!8m2!3d40.1752569!4d44.5663743!16s%2Fg%2F11pckm_gjk")
            QDesktopServices.openUrl(url)
        elif row == 47 and col == 4:
            url = QUrl("https://www.google.com/maps/place/8,+Yeritsyan+Supermarket,+2+Gai+Ave,+Yerevan+0056/@40.1998151,44.5639763,17z/data=!3m1!4b1!4m6!3m5!1s0x406aa33a57efddc7:0xd23b343fefb270d!8m2!3d40.199811!4d44.566165!16s%2Fg%2F11r63j0vm3")
            QDesktopServices.openUrl(url)
        elif row == 48 and col == 4:
            url = QUrl("https://www.google.com/maps/place/2+Bakunts+St,+Yerevan+0076/@40.1922488,44.5701601,17z/data=!3m1!4b1!4m6!3m5!1s0x406aa34902eb717f:0x2a671344ce65716b!8m2!3d40.1922447!4d44.5723488!16s%2Fg%2F11cp7ygcmd")
            QDesktopServices.openUrl(url)
        elif row == 49 and col == 4:
            url = QUrl("https://www.google.com/maps/place/4+Moldovakan+St,+Yerevan+0062/@40.2059188,44.5669872,17z/data=!3m1!4b1!4m6!3m5!1s0x406aa3228fe74251:0x648e66c406b23399!8m2!3d40.2059147!4d44.5691759!16s%2Fg%2F11h0t6m20r")
            QDesktopServices.openUrl(url)
        elif row == 50 and col == 4:
            url = QUrl("https://www.google.com/maps/place/55+Raffi+St,+Yerevan/@40.1740784,44.4455331,17.57z/data=!4m5!3m4!1s0x406abde8043ffbf5:0x862e14823299000c!8m2!3d40.1741174!4d44.4470146")
            QDesktopServices.openUrl(url)
        elif row == 51 and col == 4:
            url = QUrl("https://www.google.com/maps/place/Natali+Pharm/@40.1712626,44.4860039,14z/data=!4m10!1m2!2m1!1snatali+pharm!3m6!1s0x406abd36b6d6d747:0xfcc8bbca7fc33d7!8m2!3d40.1712626!4d44.5189629!15sCgxuYXRhbGkgcGhhcm1aDiIMbmF0YWxpIHBoYXJtkgEIcGhhcm1hY3ngAQA!16s%2Fg%2F11g18tpbxf")
            QDesktopServices.openUrl(url)
        elif row == 52 and col == 4:
            url = QUrl("https://www.google.com/maps/place/33+Abovyan+poxoc,+Yerevan+0009/@40.1877682,44.5210342,17z/data=!3m1!4b1!4m6!3m5!1s0x406abce09c329a4b:0x190558989842c3c2!8m2!3d40.1877641!4d44.5232229!16s%2Fg%2F1tl7m60h")
            QDesktopServices.openUrl(url)
        elif row == 53 and col == 4:
            url = QUrl("https://www.google.com/maps/place/24+Tumanyan+St,+Yerevan+0001/@40.1818338,44.5164513,17z/data=!3m1!4b1!4m6!3m5!1s0x406abce4e5477817:0x2c20ed9c97bd6c5!8m2!3d40.1818297!4d44.51864!16s%2Fg%2F1vmq_wgh")
            QDesktopServices.openUrl(url)
        elif row == 54 and col == 4:
            url = QUrl("https://www.google.com/maps/place/Natali+Pharm+PHARMACY/@40.2010788,44.4770028,15z/data=!4m10!1m2!2m1!1sNatali+Pharm!3m6!1s0x406abd6a412a48d3:0x77502653562eabde!8m2!3d40.2010788!4d44.4934823!15sCgxOYXRhbGkgUGhhcm1aDiIMbmF0YWxpIHBoYXJtkgEIcGhhcm1hY3ngAQA!16s%2Fg%2F11g6vl789s")
            QDesktopServices.openUrl(url)
        elif row == 55 and col == 4:
            url = QUrl("https://www.google.com/maps/place/20+Acharyan+St,+Yerevan+0040/@40.2153655,44.5605928,17z/data=!3m1!4b1!4m6!3m5!1s0x406aa2e3e5c9b7d9:0xb2b5c0d32ebffa2!8m2!3d40.2153614!4d44.5627815!16s%2Fg%2F11lqm9llj_")
            QDesktopServices.openUrl(url)
        elif row == 56 and col == 4:
            url = QUrl("https://www.google.com/maps/place/5+Andranik+Zoravar+St,+Yerevan+0064/@40.1790695,44.4447396,17z/data=!3m1!4b1!4m6!3m5!1s0x406abdec01023e0d:0x96fe98df9a9db657!8m2!3d40.1790654!4d44.4469283!16s%2Fg%2F11cpb74wcy/")
            QDesktopServices.openUrl(url)
        elif row == 57 and col == 4:
            url = QUrl("https://www.google.com/maps/place/4th,+17+Mikoyan+St,+Yerevan+0090/@40.1827248,44.5660781,17z/data=!3m1!4b1!4m5!3m4!1s0x406abcadf4de7723:0x1c6c93cd4bda2376!8m2!3d40.1827207!4d44.5682668")
            QDesktopServices.openUrl(url)
        elif row == 58 and col == 4:
            url = QUrl("https://www.google.com/maps/place/8+Moskovyan+pokhoc,+Yerevan/@40.1884219,44.5157268,17z/data=!3m1!4b1!4m6!3m5!1s0x406abce029004929:0x1eb0b9f9e1e81713!8m2!3d40.1884178!4d44.5179155!16s%2Fg%2F11bw42gcd4")
            QDesktopServices.openUrl(url)
        elif row == 59 and col == 4:
            url = QUrl("https://www.google.com/maps/place/17%2F8+Tigran+Petrosyan+St,+Yerevan+0054/@40.2182195,44.4874528,17z/data=!3m1!4b1!4m6!3m5!1s0x406a97fdca62b4c9:0x697446759049ca54!8m2!3d40.2182154!4d44.4896415!16s%2Fg%2F11bw49k7sc")
            QDesktopServices.openUrl(url)
        elif row == 60 and col == 4:
            url = QUrl("https://www.google.com/maps/place/6+Samvel+Safaryani+poxoc,+Yerevan/@40.1979634,44.5634224,17z/data=!3m1!4b1!4m6!3m5!1s0x406aa330a72aa399:0xd3a084ad1619388d!8m2!3d40.1979593!4d44.5656111!16s%2Fg%2F11t142bg4x")
            QDesktopServices.openUrl(url)
        elif row == 61 and col == 4:
            url = QUrl("https://www.google.com/maps/place/8,+Yeritsyan+Supermarket,+2+Gai+Ave,+Yerevan+0056/@40.1998151,44.5639763,17z/data=!3m1!4b1!4m6!3m5!1s0x406aa33a57efddc7:0xd23b343fefb270d!8m2!3d40.199811!4d44.566165!16s%2Fg%2F11r63j0vm3")
            QDesktopServices.openUrl(url)
        elif row == 62 and col == 4:
            url = QUrl("https://www.google.com/maps/place/8,+Yeritsyan+Supermarket,+2+Gai+Ave,+Yerevan+0056/@40.1998151,44.5639763,17z/data=!3m1!4b1!4m6!3m5!1s0x406aa33a57efddc7:0xd23b343fefb270d!8m2!3d40.199811!4d44.566165!16s%2Fg%2F11r63j0vm3")
            QDesktopServices.openUrl(url)
        elif row == 63 and col == 4:
            url = QUrl("https://www.google.com/maps/place/2+Bakunts+St,+Yerevan+0076/@40.1922488,44.5701601,17z/data=!3m1!4b1!4m6!3m5!1s0x406aa34902eb717f:0x2a671344ce65716b!8m2!3d40.1922447!4d44.5723488!16s%2Fg%2F11cp7ygcmd")
            QDesktopServices.openUrl(url)
        elif row == 64 and col == 4:
            url = QUrl("https://www.google.com/maps/place/4+Moldovakan+St,+Yerevan+0062/@40.2059188,44.5669872,17z/data=!3m1!4b1!4m6!3m5!1s0x406aa3228fe74251:0x648e66c406b23399!8m2!3d40.2059147!4d44.5691759!16s%2Fg%2F11h0t6m20r")
            QDesktopServices.openUrl(url)
        elif row == 65 and col == 4:
            url = QUrl("https://www.google.com/maps/place/55+Raffi+St,+Yerevan/@40.1740784,44.4455331,17.57z/data=!4m5!3m4!1s0x406abde8043ffbf5:0x862e14823299000c!8m2!3d40.1741174!4d44.4470146")
            QDesktopServices.openUrl(url)
        elif row == 66 and col == 4:
            url = QUrl("https://www.google.com/maps/place/Natali+Pharm/@40.1712626,44.4860039,14z/data=!4m10!1m2!2m1!1snatali+pharm!3m6!1s0x406abd36b6d6d747:0xfcc8bbca7fc33d7!8m2!3d40.1712626!4d44.5189629!15sCgxuYXRhbGkgcGhhcm1aDiIMbmF0YWxpIHBoYXJtkgEIcGhhcm1hY3ngAQA!16s%2Fg%2F11g18tpbxf")
            QDesktopServices.openUrl(url)
        elif row == 67 and col == 4:
            url = QUrl("https://www.google.com/maps/place/33+Abovyan+poxoc,+Yerevan+0009/@40.1877682,44.5210342,17z/data=!3m1!4b1!4m6!3m5!1s0x406abce09c329a4b:0x190558989842c3c2!8m2!3d40.1877641!4d44.5232229!16s%2Fg%2F1tl7m60h")
            QDesktopServices.openUrl(url)
        elif row == 68 and col == 4:
            url = QUrl("https://www.google.com/maps/place/24+Tumanyan+St,+Yerevan+0001/@40.1818338,44.5164513,17z/data=!3m1!4b1!4m6!3m5!1s0x406abce4e5477817:0x2c20ed9c97bd6c5!8m2!3d40.1818297!4d44.51864!16s%2Fg%2F1vmq_wgh")
            QDesktopServices.openUrl(url)
        elif row == 69 and col == 4:
            url = QUrl("https://www.google.com/maps/place/Natali+Pharm+PHARMACY/@40.2010788,44.4770028,15z/data=!4m10!1m2!2m1!1sNatali+Pharm!3m6!1s0x406abd6a412a48d3:0x77502653562eabde!8m2!3d40.2010788!4d44.4934823!15sCgxOYXRhbGkgUGhhcm1aDiIMbmF0YWxpIHBoYXJtkgEIcGhhcm1hY3ngAQA!16s%2Fg%2F11g6vl789s")
            QDesktopServices.openUrl(url)
        elif row == 70 and col == 4:
            url = QUrl("https://www.google.com/maps/place/20+Acharyan+St,+Yerevan+0040/@40.2153655,44.5605928,17z/data=!3m1!4b1!4m6!3m5!1s0x406aa2e3e5c9b7d9:0xb2b5c0d32ebffa2!8m2!3d40.2153614!4d44.5627815!16s%2Fg%2F11lqm9llj_")
            QDesktopServices.openUrl(url)
        elif row == 71 and col == 4:
            url = QUrl("https://www.google.com/maps/place/5+Andranik+Zoravar+St,+Yerevan+0064/@40.1790695,44.4447396,17z/data=!3m1!4b1!4m6!3m5!1s0x406abdec01023e0d:0x96fe98df9a9db657!8m2!3d40.1790654!4d44.4469283!16s%2Fg%2F11cpb74wcy")
            QDesktopServices.openUrl(url)
        elif row == 72 and col == 4:
            url = QUrl("https://www.google.com/maps/place/4th,+17+Mikoyan+St,+Yerevan+0090/@40.1827248,44.5660781,17z/data=!3m1!4b1!4m5!3m4!1s0x406abcadf4de7723:0x1c6c93cd4bda2376!8m2!3d40.1827207!4d44.5682668")
            QDesktopServices.openUrl(url)
        elif row == 73 and col == 4:
            url = QUrl("https://www.google.com/maps/place/8+Moskovyan+pokhoc,+Yerevan/@40.1884219,44.5157268,17z/data=!3m1!4b1!4m6!3m5!1s0x406abce029004929:0x1eb0b9f9e1e81713!8m2!3d40.1884178!4d44.5179155!16s%2Fg%2F11bw42gcd4")
            QDesktopServices.openUrl(url)
        elif row == 74 and col == 4:
            url = QUrl("https://www.google.com/maps/place/17%2F8+Tigran+Petrosyan+St,+Yerevan+0054/@40.2182195,44.4874528,17z/data=!3m1!4b1!4m6!3m5!1s0x406a97fdca62b4c9:0x697446759049ca54!8m2!3d40.2182154!4d44.4896415!16s%2Fg%2F11bw49k7sc")
            QDesktopServices.openUrl(url)

if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = Window()
    window.setObjectName("window")
    window.setStyleSheet("#window {background-color: #ACE1AF;}")
    window.show()
    sys.exit(app.exec())






