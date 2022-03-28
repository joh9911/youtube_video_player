from PyQt5 import QtWidgets, QtCore, QtGui
import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

class Play_Page:
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
       
        self.playList_Page = QtWidgets.QWidget()

        self.list_upBar = QtWidgets.QLineEdit(self.playList_Page)
        self.list_upBar.setGeometry(0, 0, 1600 ,40)
        self.list_upBar.setStyleSheet(
            "border-radius: 1px;"
            "border: 1px solid black;"
            "border-top-style: none;"
            "font: 12pt Arial;"
            "color: gray;"
        )
        self.list_upBar.setReadOnly(True)

        self.list_upBar_button = []
        for index in (0,2):
            button = QtWidgets.QPushButton(self.playList_Page)
            button.setGeometry(1100+index*130, 0, 200, 40)
            button.setStyleSheet(
            "background-color: rgb(80, 130, 255 );"
            "border-radius: 1px;"
            "color: white;"
            "font: 12pt Arial;"
            )
            button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
            self.list_upBar_button.append(button)
        self.list_upBar_button[0].setText("추가")
        self.list_upBar_button[1].setText("뒤로가기")
        
        self.list_groupbox = QtWidgets.QGroupBox("재생목록")
        self.list_form = QtWidgets.QFormLayout()
        
        self.list_list = []
        self.list_deleteButton = []
        self.list_playlist_number = []
        
        self.list_groupbox.setLayout(self.list_form)

        self.list_scrollArea = QtWidgets.QScrollArea(self.playList_Page)
        self.list_scrollArea.setWidget(self.list_groupbox)
        self.list_scrollArea.setGeometry(0, 40, 1600, 860)
        self.list_scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.list_scrollArea.setWidgetResizable(True)

        self.stackedwidget.addWidget(self.playList_Page)

        self.player_page = QtWidgets.QWidget()

        self.player_upBar = QtWidgets.QLineEdit(self.player_page)
        self.player_upBar.setGeometry(0, 0, 1600 ,40)
        self.player_upBar.setStyleSheet(
            "border-radius: 1px;"
            "border: 1px solid black;"
            "border-top-style: none;"
            "font: 12pt 맑은 고딕;"
            "color: gray;"
        )
        self.player_upBar.setText("      사용자의 이름이 들어갈 자리")
        self.player_upBar.setReadOnly(True)
        

        self.player_upBar_button = []
        for index in (0,2):
            button = QtWidgets.QPushButton(self.player_page)
            button.setGeometry(1100+index*130, 0, 200, 40)
            button.setStyleSheet(
            "background-color: rgb(80, 130, 255 );"
            "border-radius: 1px;"
            "color: white;"
            "font: 12pt Arial;"
            )
            button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
            self.player_upBar_button.append(button)
        self.player_upBar_button[0].setText("추가")
        self.player_upBar_button[1].setText("뒤로가기")

        self.player_player = QtWidgets.QFrame(self.player_page)
        self.player_player.setGeometry(0,40,1100,800)

        self.progressbar = QtWidgets.QSlider(QtCore.Qt.Orientation.Horizontal,self.player_page)
        self.progressbar.setGeometry(0,800,1100,50)
        self.progressbar.setMaximum(1100)        

        self.player_playbutton = []
        for index in range(0,4):
            button = QtWidgets.QPushButton(self.player_page)
            button.setGeometry(10+index*120,850,100,50)
            self.player_playbutton.append(button)
        self.player_playbutton[0].setText("◀◀")
        self.player_playbutton[1].setText("⏸")
        self.player_playbutton[2].setText("▶▶")
        self.player_playbutton[3].setText("■")

        self.player_medianame = QtWidgets.QLineEdit(self.player_page)
        self.player_medianame.setGeometry(500,850,500, 50)
        
        self.player_groupBox = QtWidgets.QGroupBox("재생목록")
        self.player_form = QtWidgets.QFormLayout()

        self.player_list= []
        self.player_deleteButton = []
        self.player_listImage = []
        self.player_listName = []
        self.player_player_number = []
        
        self.player_groupBox.setLayout(self.player_form)

        self.player_scrollArea = QtWidgets.QScrollArea(self.player_page)
        self.player_scrollArea.setWidget(self.player_groupBox)
        self.player_scrollArea.setGeometry(1100, 40, 500, 860)
        self.player_scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.player_scrollArea.setWidgetResizable(True)

        self.stackedwidget.addWidget(self.player_page)

        self.mainWindow.setCentralWidget(self.centralwidget)
        self.stackedwidget.setCurrentIndex(0)
        self.mainWindow.show()

