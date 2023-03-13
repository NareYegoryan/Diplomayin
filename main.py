import sys
# from ipregistry import IpregistryClient
#
# import googlemaps

import json
from urllib.request import urlopen

# url = 'http://ipinfo.io/json'
# response = urlopen(url)
# data = json.load(response)
#
# print(data)

from PyQt5 import QtWidgets,QtGui
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QLineEdit, QDateEdit, QRadioButton, QVBoxLayout, QTimeEdit, QScrollArea,QWidget,QTextEdit,QPushButton,QStackedWidget,QHBoxLayout,QStackedLayout
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class Window(QMainWindow):
    def __init__(self):

        super(Window,self).__init__()


        self.setWindowTitle(" Your Pharmacy ")
        self.setGeometry(0, 0, 1920, 1890)

        self.setWindowIcon(QtGui.QIcon("icon.png"))

        self.scroll = QScrollArea()
        self.widget = QWidget()
        self.widget.resize(1920,3000)
        self.widget.setObjectName("WID")
        self.widget.setStyleSheet("#WID {background-color: #ACE1AF;}")
        self.scroll.setWidget(self.widget)
        self.setCentralWidget(self.scroll)

        self.button = QPushButton("Տեսնել դեղատները", self.widget)
        self.button.setGeometry(1160, 250, 120, 30)
        self.button.clicked.connect(self.show_pharmacies)

        layout = QVBoxLayout(self)
        layout.addWidget(self.button)

        # Create a search button

        self.search_button = QPushButton('Փնտրել', self.widget)
        self.search_button.setGeometry(1050, 250, 100, 30)

        # Create a line edit for entering search query
        self.search_edit = QLineEdit(self.widget)
        self.search_edit.setStyleSheet("QLineEdit {border:2px solid gray; border-radius: 10px; }")
        self.search_edit.setGeometry(QRect(40, 250, 1000, 30))
        # Connect the search button to the search function
        self.search_button.clicked.connect(self.search)


        self.nkar = QtWidgets.QLabel(self.widget)
        self.logo1 = QPixmap("logo.png")
        self.nkar.setPixmap(self.logo1)
        self.nkar.setGeometry(50,50,100,100)
        self.nkar.adjustSize()

        self.nkar2 = QtWidgets.QLabel(self.widget)
        self.logo2 = QPixmap("logo.png")
        self.nkar2.setPixmap(self.logo2)
        self.nkar2.setGeometry(1200,50,100,100)
        self.nkar2.adjustSize()


        self.header = QLabel(self.widget)
        self.header.setText("Your Pharmacy")
        self.header.move(400,5)
        path_to_font_file = r'C:\Users\User\Downloads\relettered\Relettered.ttf'
        font_id = QFontDatabase.addApplicationFont(path_to_font_file)
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        self.header.setFont(QFont(font_family, 120))
        self.header.setStyleSheet("font-weight: bold;"
                                  "color: black")

        self.bucket = QPushButton(self.widget)
        self.bucket.setIcon(QIcon("bucket.png"))
        self.bucket.setGeometry(1290,250,30,30)




        self.setLayout(layout)
        self.showMaximized()


    def search(self):
        search_query = self.search_edit.text()
        print(f"Searching for: {search_query}")

    def show_pharmacies(self):
        url = "https://www.google.com/maps/search/pharmacy"
        QDesktopServices.openUrl(QUrl(url))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.setObjectName("window")
    window.setStyleSheet("#window {background-color: #ACE1AF;}")
    window.show()
    sys.exit(app.exec())





