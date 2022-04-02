from PyQt5 import QtWidgets, QtCore, QtGui
import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

class PlayPage:
    def __init__(self):
        self.mainWindow = QtWidgets.QMainWindow()
        self.mainWindow.resize(1600, 900)
        
        self.centralwidget = QtWidgets.QWidget(self.mainWindow)
        self.centralwidget.setStyleSheet(
            "background-color: white;"
        )

        self.stackedwidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedwidget.setGeometry(0, 0, 1600, 900)
        self.stackedwidget.setStyleSheet(
            "background-color: white;"
        )
       
        self.playListPage = QtWidgets.QWidget()

        self.playListPageUpbar = QtWidgets.QLineEdit(self.playListPage)
        self.playListPageUpbar.setGeometry(0, 0, 1600 ,40)
        self.playListPageUpbar.setStyleSheet(
            "border-radius: 1px;"
            "border: 1px solid black;"
            "border-top-style: none;"
            "font: 12pt Arial;"
            "color: gray;"
        )
        self.playListPageUpbar.setReadOnly(True)

        self.playListPageUpbarButton = []
        for index in (0,2):
            button = QtWidgets.QPushButton(self.playListPage)
            button.setGeometry(1100+index*130, 0, 200, 40)
            button.setStyleSheet(
            "background-color: rgb(80, 130, 255 );"
            "border-radius: 1px;"
            "color: white;"
            "font: 12pt Arial;"
            )
            button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
            self.playListPageUpbarButton.append(button)
        self.playListPageUpbarButton[0].setText("추가")
        self.playListPageUpbarButton[1].setText("뒤로가기")
        
        self.playListPageGroupBox = QtWidgets.QGroupBox("재생목록")
        self.playListPageForm = QtWidgets.QFormLayout()
        
        self.playListPagePlayList = []
        self.playListPageDeleteButton = []
        self.playListPagePlayListNumber = []
        
        self.playListPageGroupBox.setLayout(self.playListPageForm)

        self.playListPageScrollArea = QtWidgets.QScrollArea(self.playListPage)
        self.playListPageScrollArea.setWidget(self.playListPageGroupBox)
        self.playListPageScrollArea.setGeometry(0, 40, 1600, 860)
        self.playListPageScrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.playListPageScrollArea.setWidgetResizable(True)

        self.stackedwidget.addWidget(self.playListPage)

        self.playerPage = QtWidgets.QWidget()

        self.playerPageUpBar = QtWidgets.QLineEdit(self.playerPage)
        self.playerPageUpBar.setGeometry(0, 0, 1600 ,40)
        self.playerPageUpBar.setStyleSheet(
            "border-radius: 1px;"
            "border: 1px solid black;"
            "border-top-style: none;"
            "font: 12pt 맑은 고딕;"
            "color: gray;"
        )
        self.playerPageUpBar.setText("      사용자의 이름이 들어갈 자리")
        self.playerPageUpBar.setReadOnly(True)
        

        self.playerPageUpBarButton = []
        for index in (0,2):
            button = QtWidgets.QPushButton(self.playerPage)
            button.setGeometry(1100+index*130, 0, 200, 40)
            button.setStyleSheet(
            "background-color: rgb(80, 130, 255 );"
            "border-radius: 1px;"
            "color: white;"
            "font: 12pt Arial;"
            )
            button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
            self.playerPageUpBarButton.append(button)
        self.playerPageUpBarButton[0].setText("추가")
        self.playerPageUpBarButton[1].setText("뒤로가기")

        self.playerPagePlayer = QtWidgets.QFrame(self.playerPage)
        self.playerPagePlayer.setGeometry(0,40,1100,800)

        self.progressbar = QtWidgets.QSlider(QtCore.Qt.Orientation.Horizontal,self.playerPage)
        self.progressbar.setGeometry(0,800,1100,50)
        self.progressbar.setMaximum(1100)        

        self.playerPagePlayButton = []
        for index in range(0,4):
            button = QtWidgets.QPushButton(self.playerPage)
            button.setGeometry(10+index*120,850,100,50)
            self.playerPagePlayButton.append(button)
        self.playerPagePlayButton[0].setText("ㅣ◀")
        self.playerPagePlayButton[1].setText("⏸")
        self.playerPagePlayButton[2].setText("▶ㅣ")
        self.playerPagePlayButton[3].setText("■")

        self.playerPageMediaName = QtWidgets.QLineEdit(self.playerPage)
        self.playerPageMediaName.setGeometry(500,850,500, 50)
        
        self.playerPageGroupBox = QtWidgets.QGroupBox("재생목록")
        self.playerPageForm = QtWidgets.QFormLayout()

        self.playerPagePlayerList= []
        self.playerPageDeleteButton = []
        self.playerPageThumnail = []
        self.playerPageTitle = []
        self.playerPagePlayerNumber = []
        
        self.playerPageGroupBox.setLayout(self.playerPageForm)

        self.playerPageScrollArea = QtWidgets.QScrollArea(self.playerPage)
        self.playerPageScrollArea.setWidget(self.playerPageGroupBox)
        self.playerPageScrollArea.setGeometry(1100, 40, 500, 860)
        self.playerPageScrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.playerPageScrollArea.setWidgetResizable(True)

        self.stackedwidget.addWidget(self.playerPage)

        self.mainWindow.setCentralWidget(self.centralwidget)
        self.stackedwidget.setCurrentIndex(0)
        self.mainWindow.show()

