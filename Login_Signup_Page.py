from PyQt5 import QtWidgets, QtCore, QtGui
import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *

class Login_Signup_Page:
    
    def __init__(self):
        self.mainWindow = QtWidgets.QMainWindow()
        self.mainWindow.resize(500, 550)
        
        self.centralwidget = QtWidgets.QWidget(self.mainWindow)
        
        self.stackedwidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedwidget.setGeometry(0, 0, 500, 550)
        self.stackedwidget.setStyleSheet(
            "background-color: white;"
        )
       
        self.loginPage = QtWidgets.QWidget()
       
        self.Youtube_logo = QtWidgets.QLabel(self.loginPage)
        self.Youtube_logo.setGeometry(150, 80, 200, 60)
        self.Youtube_logo.setStyleSheet(
            "border: 1px solid white;"
        )
        pixmap = QPixmap("youtube.png")
        pixmap = pixmap.scaled(200,140,Qt.AspectRatioMode.KeepAspectRatio)  
        self.Youtube_logo.setPixmap(pixmap)
        self.Youtube_logo.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        self.loginPage_input = []

        for index in range(0,2):
            input = QtWidgets.QLineEdit(self.loginPage)
            input.setGeometry(125, 190+100*index, 250, 20)
            input.setStyleSheet(
            "border-radius: 1px;"
            "border: 1px solid black;"
            "border-top-style: none;"
            "border-left-style: none;"
            "border-right-style: none;"
            "font: 12pt Arial;"
            "color: gray;"
            )
            input.setReadOnly(True)
            input.setCursor(QCursor(QtCore.Qt.CursorShape.IBeamCursor))
            self.loginPage_input.append(input)
        self.loginPage_input[0].setText("ID")
        self.loginPage_input[1].setText("PW")
        
        
        self.loginButton = QtWidgets.QPushButton(self.loginPage)
        self.loginButton.setGeometry(140, 370, 220, 60)
        self.loginButton.setStyleSheet(
            "background-color: blue;"
            "border-radius: 10px;"
            "color: white;"
        )
        self.loginButton.setText("로그인")
        self.loginButton.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

        self.signupButton = QtWidgets.QPushButton(self.loginPage)
        self.signupButton.setGeometry(390, 430, 80, 20)
        self.signupButton.setStyleSheet(
            "border: 1px solid white;"
            "text-decoration: underline;"
        )
        self.signupButton.setText("회원가입")
        self.signupButton.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        
        self.stackedwidget.addWidget(self.loginPage)

        self.signupPage = QtWidgets.QWidget()

        self.signupPage_input = []

        for index in range(0,4):

            input = QtWidgets.QLineEdit(self.signupPage)
            input.setGeometry(QtCore.QRect(100, 40+90*index, 300, 20))
            input.setStyleSheet(
            "border-radius: 1px;"
            "border: 1px solid black;"
            "border-top-style: none;"
            "border-left-style: none;"
            "border-right-style: none;"
            "font: 12pt Arial;"
            "color: gray;"
            )
            input.setReadOnly(True)

            input.setCursor(QCursor(QtCore.Qt.CursorShape.IBeamCursor))
            self.signupPage_input.append(input)
        self.signupPage_input[0].setText("ID")
        self.signupPage_input[1].setText("Password")
        self.signupPage_input[2].setText("Password confirm")
        self.signupPage_input[3].setText("Name")

        
        self.signupPage_Error = []
        for index in range(0,2):
            Error = QtWidgets.QLineEdit(self.signupPage)
            Error.setGeometry(100,60+180*index,300,20)
            Error.setStyleSheet(
            "border-radius: 1px;"
            "border: 1px solid white;"
            "font: 10pt Arial;"
            "color: red;"
            )
            Error.setReadOnly(True)
            Error.keyPressEvent
            self.signupPage_Error.append(Error)
            
        
        self.signupPage_IDconfirmButton = QtWidgets.QPushButton(self.signupPage)
        self.signupPage_IDconfirmButton.setGeometry(400, 30, 60, 30)
        self.signupPage_IDconfirmButton.setStyleSheet(
            "background-color: rgb(80, 130, 255 );"
            "border-radius: 1px;"
            "color: white;"
            
        )
        self.signupPage_IDconfirmButton.setText("결정")
        self.signupPage_IDconfirmButton.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

        self.signupPage_signupButton = QtWidgets.QPushButton(self.signupPage)
        self.signupPage_signupButton.setGeometry(140, 370, 220, 60)
        self.signupPage_signupButton.setStyleSheet(
            "background-color: rgb(80, 130, 255 );"
            "border-radius: 10px;"
            "color: white;"
            "font: 12pt Arial;"
        )
        self.signupPage_signupButton.setText("회원가입")
        self.signupPage_signupButton.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

        self.signupPage_backButton = QtWidgets.QPushButton(self.signupPage)
        self.signupPage_backButton.setGeometry(390, 430, 80, 20)
        self.signupPage_backButton.setStyleSheet(
            "border: 1px solid white;"
            "text-decoration: underline;"
        )
        self.signupPage_backButton.setText("뒤로가기")
        self.signupPage_backButton.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

        
        self.stackedwidget.addWidget(self.signupPage)
        

        self.stackedwidget.setCurrentIndex(0)
        self.mainWindow.setCentralWidget(self.centralwidget)
        self.mainWindow.show()
    


