from PyQt5 import QtWidgets, QtCore, QtGui
import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *
import Login_Signup_Page
import Play_PageEvent
import Database

class LoginSignup_Event:

    def __init__(self):
        self.loginSignupUi = Login_Signup_Page.Login_Signup_Page()
        self.PlayPage = None
       #로그인 페이지 이벤트
        self.loginSignupUi.loginPage_input[0].mousePressEvent = lambda event: self.loginPage_idInputEvent(event)
        self.loginSignupUi.loginPage_input[1].mousePressEvent = lambda event: self.loginPage_pwInputEvent(event)
        self.loginSignupUi.loginButton.clicked.connect(self.loginPage_loginButtonEvent)
        self.loginSignupUi.signupButton.clicked.connect(self.loginPage_signupButtonEvent)
        #회원가입 페이지 이벤트
        for index in range(0,len(self.loginSignupUi.signupPage_input)):
            self.loginSignupUi.signupPage_input[index].mousePressEvent = lambda event, nowIndex = index: self.signupPage_signupInputEvent(event, nowIndex)
        # self.loginSignupUi.signupPage_input[0].keyPressEvent = lambda event: self.signupPage_IdErrorText(event)
        self.loginSignupUi.signupPage_IDconfirmButton.clicked.connect(self.signupPage_IdconfirmEvent)
        self.loginSignupUi.signupPage_signupButton.clicked.connect(self.signupPage_signupButtonEvent)

    
    def loginPage_idInputEvent(self, event):
        self.loginSignupUi.loginPage_input[0].setReadOnly(False)
        self.loginSignupUi.loginPage_input[0].setText("")

    def loginPage_pwInputEvent(self,event):
        self.loginSignupUi.loginPage_input[1].setReadOnly(False)
        self.loginSignupUi.loginPage_input[1].setText("")
        self.loginSignupUi.loginPage_input[1].setEchoMode(QLineEdit.EchoMode.Password)
    
    def loginPage_loginButtonEvent(self):
        database = Database.Database()
        id = self.loginSignupUi.loginPage_input[0].text()
        pw = self.loginSignupUi.loginPage_input[1].text()
        result = database.loginPage_loginCheck(id, pw)
        if len(result) == 1:
            QtWidgets.QMessageBox.about(self.loginSignupUi.centralwidget,'About Title','로그인에 성공하셨습니다.')
            self.loginSignupUi.mainWindow.close()
            self.PlayPage = Play_PageEvent.Play_PageEvent()
        else:
            QtWidgets.QMessageBox.about(self.loginSignupUi.centralwidget,'About Title','로그인에 실패하셨습니다.')
    
    def loginPage_signupButtonEvent(self):
        QtWidgets.QMessageBox.about(self.loginSignupUi.centralwidget,'About Title','회원가입 페이지로 이동합니다.')
        self.loginSignupUi.stackedwidget.setCurrentIndex(1)
    #회원가입 페이지 이벤트 함수
    def signupPage_signupInputEvent(self, evnet, index):
        self.loginSignupUi.signupPage_input[index].setReadOnly(False)
        self.loginSignupUi.signupPage_input[index].setText("")

    def signupPage_IdErrorText(self,event):
        # self.loginSignupUi.signupPage_input[0].setReadOnly(False)
        # self.loginSignupUi.signupPage_input[0].setText("")
        # database = Database.Database()
        # id = self.loginSignupUi.signupPage_input[0].text()
        # result = database.signupPage_idCheck(id)
        # if result == 0:
        #     stylesheet = self.loginSignupUi.signupPage_Error[0].styleSheet()
        #     stylesheet += "color: red;"
        #     self.loginSignupUi.signupPage_Error[0].setText("이미 사용중인 아이디 입니다.")
        # else:
        #     stylesheet = self.loginSignupUi.signupPage_Error[0].styleSheet()
        #     stylesheet += "color: green;"
        #     self.loginSignupUi.signupPage_Error[0].setText("사용 가능한 아이디 입니다.")
        pass


    def signupPage_IdconfirmEvent(self):
        pass
        # QtWidgets.QMessageBox.about(self.loginSignupUi.centralwidget,'About Title','이 아이디를 사용합니다.')
        # self.loginSignupUi.signupPage_input[0].disconnect()
        # self.loginSignupUi.signupPage_input[0].setReadOnly(True)
        # self.loginSignupUi.signupPage_IDconfirmButton.clicked.disconnect()

    def signupPage_signupButtonEvent(self):
        database = Database.Database()
        id = self.loginSignupUi.signupPage_input[0].text()
        pw = self.loginSignupUi.signupPage_input[1].text()
        name = self.loginSignupUi.signupPage_input[3].text()
        column = ["id","pw","name"]
        data = [id, pw, name]
        confirm=[id]
        database.cursor.execute("SELECT * FROM user WHERE id=?",confirm)
        result = database.cursor.fetchall()
        if result == 1:
            QtWidgets.QMessageBox.about(self.loginSignupUi.centralwidget,'About Title','이미 존재하는 아이디 입니다.')
            for index in range(0,len(self.loginSignupUi.signupPage_input)):
                self.loginSignupUi.signupPage_input[index].setText("")
        else:
            database.dataCreate("user",column,data)
            QtWidgets.QMessageBox.about(self.loginSignupUi.centralwidget,'About Title','회원가입에 성공하였습니다. 로그인 페이지로 이동합니다.')
            self.loginSignupUi.stackedwidget.setCurrentIndex(0)

if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    
    ui=LoginSignup_Event()
    
    sys.exit(app.exec_())