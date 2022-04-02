from PyQt5 import QtWidgets, QtCore, QtGui
import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *
import LoginSignupPage
import PlaylistPageEvent
import Database
class SignupPageEvent:
    def __init__(self,ui):
        self.loginSignupUi = ui
        self.loginSignupUi.stackedwidget.setCurrentIndex(1)
        for index in range(0,len(self.loginSignupUi.signupPageInput)):
            self.loginSignupUi.signupPageInput[index].mousePressEvent = lambda event, nowIndex = index: self.signupInputEvent(event, nowIndex)
        self.loginSignupUi.signupPageIDconfirmButton.clicked.connect(self.idConfirmEvent)
        self.loginSignupUi.signupPageSignupButton.clicked.connect(self.signupPageSignupButtonEvent)
        self.loginSignupUi.signupPageBackButton.clicked.connect(self.signupPagebackButton)
    
    def signupInputEvent(self, evnet, index):
        self.loginSignupUi.signupPageInput[index].setReadOnly(False)
        # self.loginSignupUi.signupPageInput[index].setText("")
        pw = self.loginSignupUi.signupPageInput[1].text()
        pwConfirm = self.loginSignupUi.signupPageInput[2].text()
        if pw == "":
            self.loginSignupUi.signupPageInput[1].setEchoMode(QLineEdit.EchoMode.Password)
        elif pwConfirm == "":
            self.loginSignupUi.signupPageInput[2].setEchoMode(QLineEdit.EchoMode.Password)

    def eventDisconnect(self):
        for index in range(0,len(self.loginSignupUi.signupPageInput)):
            self.loginSignupUi.signupPageInput[index].mousePressEvent = None
        self.loginSignupUi.signupPageIDconfirmButton.clicked.disconnect()
        self.loginSignupUi.signupPageSignupButton.clicked.disconnect()
        self.loginSignupUi.signupPageBackButton.clicked.disconnect()

    def idConfirmEvent(self):
        database = Database.Database()
        id = self.loginSignupUi.signupPageInput[0].text()
        result = database.signupPage_idCheck(id)
        if len(id)<8 or len(id)>10:
            self.setFontColor(self.loginSignupUi.signupPageErrorText[0],"red")
            self.loginSignupUi.signupPageErrorText[0].setText("8~10자 이내로 아이디를 설정해주세요.")
        else:
            if len(result) == 1:
                self.setFontColor(self.loginSignupUi.signupPageErrorText[0],"red")
                self.loginSignupUi.signupPageErrorText[0].setText("중복된 아이디 입니다.")
            else:
                self.setFontColor(self.loginSignupUi.signupPageErrorText[0],"green")
                self.loginSignupUi.signupPageErrorText[0].setText("사용 가능한 아이디 입니다.")
                self.loginSignupUi.signupPageInput[0].mousePressEvent = None
                self.loginSignupUi.signupPageInput[0].setReadOnly(True)


    def signupPageSignupButtonEvent(self):
        database = Database.Database()
        id = self.loginSignupUi.signupPageInput[0].text()
        pw = self.loginSignupUi.signupPageInput[1].text()
        name = self.loginSignupUi.signupPageInput[3].text()
        column = ["id","pw","name"]
        data = [id, pw, name]
        text = self.loginSignupUi.signupPageErrorText[0].text()
        pwText = self.loginSignupUi.signupPageInput[1].text()
        pwConfirm = self.loginSignupUi.signupPageInput[2].text()
        if id == "" or pw == "" or name == "":
            QtWidgets.QMessageBox.about(self.loginSignupUi.centralwidget,'About Title','공백을 채워넣으세요.')
        else:
            if text == "사용 가능한 아이디 입니다.":
                if pwText == pwConfirm:
                    database.dataCreate("user",column,data)
                    QtWidgets.QMessageBox.about(self.loginSignupUi.centralwidget,'About Title','회원가입에 성공하였습니다. 로그인 페이지로 이동합니다.')
                    self.loginSignupUi.stackedwidget.setCurrentIndex(0)
                    for index in range(0,len(self.loginSignupUi.signupPageInput)):
                        self.loginSignupUi.signupPageInput[index].setText("")
                else:
                    QtWidgets.QMessageBox.about(self.loginSignupUi.centralwidget,'About Title','비밀번호확인이 일치하지 않습니다.')
            else:
                QtWidgets.QMessageBox.about(self.loginSignupUi.centralwidget,'About Title','아이디를 확인해주세요.')
                    
    def signupPagebackButton(self):
        self.loginSignupUi.stackedwidget.setCurrentIndex(0)
        self.eventDisconnect()
        self.loginSignupUi.signupPageInput[0].setText("")
        self.loginSignupUi.signupPageInput[1].setText("")
        self.loginSignupUi.signupPageInput[2].setText("")
        self.loginSignupUi.signupPageInput[3].setText("")

    def setFontColor(self, widget, color):
        style = widget.styleSheet()
        style += "color: "+color+";"
        style = widget.setStyleSheet(style)