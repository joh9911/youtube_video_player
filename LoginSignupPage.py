from PyQt5 import QtWidgets, QtCore, QtGui
import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *

class LoginSignupPage:
    
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
       
        self.youtubeLogo = QtWidgets.QLabel(self.loginPage)
        self.youtubeLogo.setGeometry(150, 80, 200, 60)
        self.youtubeLogo.setStyleSheet(
            "border: 1px solid white;"
        )
        pixmap = QPixmap("youtube.png")
        pixmap = pixmap.scaled(200,140,Qt.AspectRatioMode.KeepAspectRatio)  
        self.youtubeLogo.setPixmap(pixmap)
        self.youtubeLogo.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        self.loginPageInput = []

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
            self.loginPageInput.append(input)
        self.loginPageInput[0].setPlaceholderText("ID")
        self.loginPageInput[1].setPlaceholderText("PW")
        
        
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

        self.signupPageInput = []

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
            self.signupPageInput.append(input)
        self.signupPageInput[0].setPlaceholderText("ID")
        self.signupPageInput[1].setPlaceholderText("Password")
        self.signupPageInput[2].setPlaceholderText("Password confirm")
        self.signupPageInput[3].setPlaceholderText("Name")

        
        self.signupPageErrorText = []
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
            self.signupPageErrorText.append(Error)
            
        
        self.signupPageIDconfirmButton = QtWidgets.QPushButton(self.signupPage)
        self.signupPageIDconfirmButton.setGeometry(400, 30, 60, 30)
        self.signupPageIDconfirmButton.setStyleSheet(
            "background-color: rgb(80, 130, 255 );"
            "border-radius: 1px;"
            "color: white;"
            
        )
        self.signupPageIDconfirmButton.setText("결정")
        self.signupPageIDconfirmButton.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

        self.signupPageSignupButton = QtWidgets.QPushButton(self.signupPage)
        self.signupPageSignupButton.setGeometry(140, 370, 220, 60)
        self.signupPageSignupButton.setStyleSheet(
            "background-color: rgb(80, 130, 255 );"
            "border-radius: 10px;"
            "color: white;"
            "font: 12pt Arial;"
        )
        self.signupPageSignupButton.setText("회원가입")
        self.signupPageSignupButton.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

        self.signupPageBackButton = QtWidgets.QPushButton(self.signupPage)
        self.signupPageBackButton.setGeometry(390, 430, 80, 20)
        self.signupPageBackButton.setStyleSheet(
            "border: 1px solid white;"
            "text-decoration: underline;"
        )
        self.signupPageBackButton.setText("뒤로가기")
        self.signupPageBackButton.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

        
        self.stackedwidget.addWidget(self.signupPage)
        

        self.stackedwidget.setCurrentIndex(0)
        self.mainWindow.setCentralWidget(self.centralwidget)
        self.mainWindow.show()
    


