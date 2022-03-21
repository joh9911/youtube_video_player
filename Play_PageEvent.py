from http.client import OK
from tkinter.messagebox import NO, YES
from PyQt5 import QtWidgets, QtCore, QtGui
import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
import Play_Page
import LoginSignup_Event
import Database
class Play_PageEvent:
    
    def __init__(self):
        self.loginSignupUi = None
        self.PlayPageUi = Play_Page.Play_Page()
        self.PlayPageUi.list_upBar_button[1].clicked.connect(self.list_upBar_backButtonEvent)
        self.PlayPageUi.list_upBar_button[0].clicked.connect(self.list_upBar_addButtonEvent)
        self.PlayPageUi.player_upBar_button[1].clicked.connect(self.player_backButtonEvent)
        self.PlayPageUi.player_upBar_button[0].clicked.connect(self.player_addButtonEvent)

    #재생목록 페이지 함수
    def list_upBar_backButtonEvent(self):
        QtWidgets.QMessageBox.about(self.PlayPageUi.centralwidget,'About Title','로그인 페이지로 이동합니다.')
        self.PlayPageUi.mainWindow.close()
        self.loginSignupUi = LoginSignup_Event.LoginSignup_Event()

    def list_upBar_addButtonEvent(self):
        database = Database.Database()
        text, ok = QtWidgets.QInputDialog.getText(self.PlayPageUi.centralwidget,"input","재생목록의 제목을 입력하세요:")
        if ok:
            button = QtWidgets.QPushButton(self.PlayPageUi.list_groupbox)
            button1 = QtWidgets.QPushButton(button)
            button1.setGeometry(1500,20,30, 30)
            button1.setStyleSheet(
            "border-radius: 1px;"
            "border: 1px solid white;"
            "font: 25pt Arial;"
            "color: red;"
            )
            button1.setText("x")
            button.setFixedSize(1550,200)
            button.setStyleSheet(
            "border-radius: 1px;"
            "border: 1px solid black;"
            "font: 12pt Arial;"
            "color: gray;"
            "text-align: left;"
            )
            button.setText("   "+str(text))
            button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
            self.PlayPageUi.list_list.append(button)
            self.PlayPageUi.list_deleteButton.append(button1)
            self.PlayPageUi.list_form.addRow(str(len(self.PlayPageUi.list_list)),button)
            self.list_upBar_buttonEventActivate()
            column = ["name"]
            data = [text]
            database.dataCreate("playlist", column, data)
        else:
            pass
    
    def list_upBar_buttonEventActivate(self):
        self.PlayPageUi.list_deleteButton[len(self.PlayPageUi.list_deleteButton)-1].clicked.connect(lambda event, nowIndex = len(self.PlayPageUi.list_deleteButton)-1: self.list_upBar_deleteButtonEvent(event, nowIndex))
        self.PlayPageUi.list_list[len(self.PlayPageUi.list_list)-1].clicked.connect(lambda event, nowIndex = len(self.PlayPageUi.list_list)-1: self.list_PlayPageEvent(event, nowIndex))
    
    def list_upBar_buttonEventAllActivate(self):
         for index in range(0,len(self.PlayPageUi.list_deleteButton)):
            self.PlayPageUi.list_deleteButton[index].clicked.connect(lambda event, nowIndex = index: self.list_upBar_deleteButtonEvent(event, nowIndex))
            self.PlayPageUi.list_list[index].clicked.connect(lambda event, nowIndex = index: self.list_PlayPageEvent(event, nowIndex))
    
    def list_upBar_buttonEventAllDeactivate(self):
        for index in range(0,len(self.PlayPageUi.list_deleteButton)):
            self.PlayPageUi.list_deleteButton[index].clicked.disconnect()
            self.PlayPageUi.list_list[index].clicked.disconnect()
       
    def list_upBar_deleteButtonEvent(self, event, index):
        database = Database.Database()
        reply = QtWidgets.QMessageBox.question(self.PlayPageUi.centralwidget,"Message","정말 삭제할까요?",QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No)
        if reply == QtWidgets.QMessageBox.StandardButton.Yes:
            name = self.PlayPageUi.list_list[index].text()
            database.dataDelete(name)
            self.PlayPageUi.list_deleteButton[index].clicked.disconnect()
            self.PlayPageUi.list_list[index].clicked.disconnect()
            del self.PlayPageUi.list_deleteButton[index]
            del self.PlayPageUi.list_list[index]
            self.PlayPageUi.list_form.removeRow(index)
            self.list_upBar_buttonEventAllDeactivate()
            self.list_upBar_buttonEventAllActivate()
        else:
            pass
    
    def list_PlayPageEvent(self, event, index):
        self.PlayPageUi.stackedwidget.setCurrentIndex(1)
    # 동영상 플레이어 페이지

    def player_addButtonEvent(self):
        URL, ok = QtWidgets.QInputDialog.getText(self.PlayPageUi.centralwidget,"input","동영상 URL을 입력하세요:")
        if ok:
            button = QtWidgets.QPushButton(self.PlayPageUi.player_groupBox)
            button1 = QtWidgets.QPushButton(button)
            button1.setGeometry(420,10,20, 25)
            button1.setStyleSheet(
            "border-radius: 1px;"
            "border: 1px solid white;"
            "font: 20pt Arial;"
            "color: red;"
            )
            button1.setText("x")
            
            label = QtWidgets.QLabel(button)
            label.setGeometry(10, 10, 240, 180)
            label.setText("난 썸네일")
            
            text = QtWidgets.QLineEdit(button)
            text.setGeometry(250, 100, 170, 30)
            text.setText("난 제목 "+str(URL)+"입력할거임")
            text.setReadOnly(True)

            button.setFixedSize(450,200)
            button.setStyleSheet(
            "border-radius: 1px;"
            "border: 1px solid black;"
            "font: 12pt Arial;"
            "color: gray;"
            "text-align: left;"
            )
            button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
            self.PlayPageUi.player_list.append(button)
            self.PlayPageUi.player_deleteButton.append(button1)
            self.PlayPageUi.player_listImage.append(label)
            self.PlayPageUi.player_listName.append(text)
            self.PlayPageUi.player_form.addRow(str(len(self.PlayPageUi.player_list)),button)
            self.player_upBar_buttonEventActivate()
        else:
            pass

    def player_backButtonEvent(self):
        QtWidgets.QMessageBox.about(self.PlayPageUi.centralwidget,'About Title','재생목록 페이지로 이동합니다.')
        self.PlayPageUi.stackedwidget.setCurrentIndex(0)

    def player_upBar_buttonEventActivate(self):
        self.PlayPageUi.player_deleteButton[len(self.PlayPageUi.player_deleteButton)-1].clicked.connect(lambda event, nowIndex = len(self.PlayPageUi.player_deleteButton)-1: self.player_upBar_deleteButtonEvent(event, nowIndex))
        self.PlayPageUi.player_list[len(self.PlayPageUi.player_list)-1].clicked.connect(lambda event, nowIndex = len(self.PlayPageUi.player_list)-1: self.player_PlayPageEvent(event, nowIndex))
    
    def player_upBar_buttonEventAllActivate(self):
        for index in range(0,len(self.PlayPageUi.player_deleteButton)):
            self.PlayPageUi.player_deleteButton[index].clicked.connect(lambda event, nowIndex = index: self.player_upBar_deleteButtonEvent(event, nowIndex))
            self.PlayPageUi.player_list[index].clicked.connect(lambda event, nowIndex = index: self.player_PlayPageEvent(event, nowIndex))
    
    def player_upBar_buttonEventAllDeactivate(self):
        for index in range(0,len(self.PlayPageUi.player_deleteButton)):
            self.PlayPageUi.player_deleteButton[index].clicked.disconnect()
            self.PlayPageUi.player_list[index].clicked.disconnect()
    
    def player_upBar_deleteButtonEvent(self, event, index):
        reply = QtWidgets.QMessageBox.question(self.PlayPageUi.centralwidget,"Message","정말 삭제할까요?",QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No)
        if reply == QtWidgets.QMessageBox.StandardButton.Yes:
            self.PlayPageUi.player_deleteButton[index].clicked.disconnect()
            self.PlayPageUi.player_list[index].clicked.disconnect()
            del self.PlayPageUi.player_deleteButton[index]
            del self.PlayPageUi.player_list[index]
            self.PlayPageUi.player_form.removeRow(index)
            self.player_upBar_buttonEventAllDeactivate()
            self.player_upBar_buttonEventAllActivate()
        else:
            pass
    def player_PlayPageEvent(self, event, index):
        QtWidgets.QMessageBox.about(self.PlayPageUi.centralwidget,'About Title','성공!')