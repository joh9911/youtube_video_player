from PyQt5 import QtWidgets, QtCore, QtGui
import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *
import LoginSignupPage
import SignupPageEvent
import PlaylistPageEvent
import Database


class LoginPageEvent:

    def __init__(self):
        self.loginSignupUi = LoginSignupPage.LoginSignupPage()
        self.loginSignupUi.stackedwidget.setCurrentIndex(0)
        self.signupPageEvent = None
        self.playlistPage = None
        self.loginSignupUi.loginPageInput[0].mousePressEvent = lambda event: self.idInputEvent(event)
        self.loginSignupUi.loginPageInput[1].mousePressEvent = lambda event: self.pwInputEvent(event)
        self.loginSignupUi.loginButton.clicked.connect(self.loginButtonEvent)
        self.loginSignupUi.signupButton.clicked.connect(self.signupButtonEvent)


    def idInputEvent(self, event):
        self.loginSignupUi.loginPageInput[0].setReadOnly(False)
        self.loginSignupUi.loginPageInput[0].setText("")

    def pwInputEvent(self,event):
        self.loginSignupUi.loginPageInput[1].setReadOnly(False)
        self.loginSignupUi.loginPageInput[1].setText("")
        self.loginSignupUi.loginPageInput[1].setEchoMode(QLineEdit.EchoMode.Password)
    
    def loginButtonEvent(self):
        database = Database.Database()
        id = self.loginSignupUi.loginPageInput[0].text()
        pw = self.loginSignupUi.loginPageInput[1].text()
        result = database.loginPage_loginCheck(id, pw)
        if len(result) == 1:
            QtWidgets.QMessageBox.about(self.loginSignupUi.centralwidget,'About Title','로그인에 성공하셨습니다.')
            self.loginSignupUi.mainWindow.close()
            self.playlistPage = PlaylistPageEvent.PlaylistPageEvent(id)
            self.eventDisconnect()
        else:
            QtWidgets.QMessageBox.about(self.loginSignupUi.centralwidget,'About Title','로그인에 실패하셨습니다.')
    
    def signupButtonEvent(self):
        QtWidgets.QMessageBox.about(self.loginSignupUi.centralwidget,'About Title','회원가입 페이지로 이동합니다.')
        self.signupPageEvent = SignupPageEvent.SignupPageEvent(self.loginSignupUi)
        self.loginSignupUi.loginPageInput[0].setText("")
        self.loginSignupUi.loginPageInput[1].setText("")
    
    def eventDisconnect(self):
        self.loginSignupUi.loginPageInput[0].mousePressEvent = None
        self.loginSignupUi.loginPageInput[1].mousePressEvent = None
        self.loginSignupUi.loginButton.clicked.disconnect()
        self.loginSignupUi.signupButton.clicked.disconnect()
    
    def eventConnect(self):
        self.loginSignupUi.loginPageInput[0].mousePressEvent = lambda event: self.idInputEvent(event)
        self.loginSignupUi.loginPageInput[1].mousePressEvent = lambda event: self.pwInputEvent(event)
        self.loginSignupUi.loginButton.clicked.connect(self.loginButtonEvent)
        self.loginSignupUi.signupButton.clicked.connect(self.signupButtonEvent)

