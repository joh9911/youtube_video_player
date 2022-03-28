from PyQt5 import QtWidgets, QtCore, QtGui
import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *
import Login_Signup_Page
import PlaylistPageEvent
import Database
class SignupPageEvent:
    def __init__(self,ui):
        self.loginSignupUi = ui
        self.loginSignupUi.stackedwidget.setCurrentIndex(1)
        for index in range(0,len(self.loginSignupUi.signupPage_input)):
            self.loginSignupUi.signupPage_input[index].mousePressEvent = lambda event, nowIndex = index: self.signupPage_signupInputEvent(event, nowIndex)
        self.loginSignupUi.signupPage_IDconfirmButton.clicked.connect(self.signupPage_IdconfirmEvent)
        self.loginSignupUi.signupPage_signupButton.clicked.connect(self.signupPage_signupButtonEvent)
        self.loginSignupUi.signupPage_backButton.clicked.connect(self.signupPagebackButton)
    
    def signupPage_signupInputEvent(self, evnet, index):
        self.loginSignupUi.signupPage_input[index].setReadOnly(False)
        self.loginSignupUi.signupPage_input[index].setText("")
        pw = self.loginSignupUi.signupPage_input[1].text()
        pwConfirm = self.loginSignupUi.signupPage_input[2].text()
        if pw == "":
            self.loginSignupUi.signupPage_input[1].setEchoMode(QLineEdit.EchoMode.Password)
        elif pwConfirm == "":
            self.loginSignupUi.signupPage_input[2].setEchoMode(QLineEdit.EchoMode.Password)

    def eventDisconnect(self):
        for index in range(0,len(self.loginSignupUi.signupPage_input)):
            self.loginSignupUi.signupPage_input[index].mousePressEvent = None
        self.loginSignupUi.signupPage_IDconfirmButton.clicked.disconnect()
        self.loginSignupUi.signupPage_signupButton.clicked.disconnect()
        self.loginSignupUi.signupPage_backButton.clicked.disconnect()

    def signupPage_IdconfirmEvent(self):
        database = Database.Database()
        id = self.loginSignupUi.signupPage_input[0].text()
        result = database.signupPage_idCheck(id)
        if len(id)<8 or len(id)>10:
            self.loginSignupUi.signupPage_Error[0].setText("8~10자 이내로 아이디를 설정해주세요.")
        else:
            if len(result) == 1:
                self.loginSignupUi.signupPage_Error[0].setText("중복된 아이디 입니다.")
            else:
                self.loginSignupUi.signupPage_Error[0].setText("사용 가능한 아이디 입니다.")
                self.loginSignupUi.signupPage_input[0].mousePressEvent = None
                self.loginSignupUi.signupPage_input[0].setReadOnly(True)


    def signupPage_signupButtonEvent(self):
        database = Database.Database()
        id = self.loginSignupUi.signupPage_input[0].text()
        pw = self.loginSignupUi.signupPage_input[1].text()
        name = self.loginSignupUi.signupPage_input[3].text()
        column = ["id","pw","name"]
        data = [id, pw, name]
        text = self.loginSignupUi.signupPage_Error[0].text()
        pwText = self.loginSignupUi.signupPage_input[1].text()
        pwConfirm = self.loginSignupUi.signupPage_input[2].text()
        if id == "" or pw == "" or name == "":
            QtWidgets.QMessageBox.about(self.loginSignupUi.centralwidget,'About Title','공백을 채워넣으세요.')
        else:
            if text == "사용 가능한 아이디 입니다.":
                if pwText == pwConfirm:
                    database.dataCreate("user",column,data)
                    QtWidgets.QMessageBox.about(self.loginSignupUi.centralwidget,'About Title','회원가입에 성공하였습니다. 로그인 페이지로 이동합니다.')
                    self.loginSignupUi.stackedwidget.setCurrentIndex(0)
                    for index in range(0,len(self.loginSignupUi.signupPage_input)):
                        self.loginSignupUi.signupPage_input[index].setText("")
                else:
                    QtWidgets.QMessageBox.about(self.loginSignupUi.centralwidget,'About Title','비밀번호확인이 일치하지 않습니다.')
            else:
                QtWidgets.QMessageBox.about(self.loginSignupUi.centralwidget,'About Title','아이디를 확인해주세요.')
                    
    def signupPagebackButton(self):
        self.loginSignupUi.stackedwidget.setCurrentIndex(0)
        self.eventDisconnect()

        