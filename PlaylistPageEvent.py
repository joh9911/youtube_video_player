from http.client import OK
from tkinter.messagebox import NO, YES
from PyQt5 import QtWidgets, QtCore, QtGui
import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
import Play_Page
import LoginPageEvent
import Database
import PlayPageEvent
class PlaylistPageEvent:
    
    def __init__(self,id):
        self.id = id
        self.count = 0
        self.loginSignupUi = None 
        self.playpageEvent = None   
        self.PlayPageUi = Play_Page.Play_Page()
        self.PlayPageUi.list_upBar.setText("      "+str(self.id)+"")
        self.PlayPageUi.list_upBar_button[1].clicked.connect(self.list_upBar_backButtonEvent)
        self.PlayPageUi.list_upBar_button[0].clicked.connect(self.list_upBar_addButtonEvent)
        self.currentList()

    def currentList(self):
        database = Database.Database()
        data=[self.id]
        database.cursor.execute("SELECT * FROM playlist WHERE id=?",data)
        result = database.cursor.fetchall()
        for index in range(0,len(result)):
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
            button.setText("   "+str(result[index][2]))
            button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
            self.PlayPageUi.list_list.append(button)
            self.PlayPageUi.list_deleteButton.append(button1)
            self.PlayPageUi.list_form.addRow(str(len(self.PlayPageUi.list_list)),button)
            self.PlayPageUi.list_playlist_number.append(result[index][0])
            self.list_upBar_buttonEventActivate()

    def list_upBar_backButtonEvent(self):
        QtWidgets.QMessageBox.about(self.PlayPageUi.centralwidget,'About Title','로그인 페이지로 이동합니다.')
        self.PlayPageUi.mainWindow.close()
        self.loginSignupUi = LoginPageEvent.LoginPageEvent()

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
            column = ["id","listname"]
            data = [self.id,text]
            database.dataCreate("playlist", column, data)
            data=[self.id]
            database.cursor.execute("SELECT * FROM playlist WHERE id=?",data)
            result = database.cursor.fetchall()
            self.PlayPageUi.list_playlist_number.append(result[self.count][0])
            self.count+=1
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
            number = self.PlayPageUi.list_playlist_number[index]
            database.playlistdataDelete(self.id,number)
            database.playerdataDelete1(number)
            self.PlayPageUi.list_deleteButton[index].clicked.disconnect()
            self.PlayPageUi.list_list[index].clicked.disconnect()
            del self.PlayPageUi.list_deleteButton[index]
            del self.PlayPageUi.list_list[index]
            del self.PlayPageUi.list_playlist_number[index]
            self.PlayPageUi.list_form.removeRow(index)
            self.list_upBar_buttonEventAllDeactivate()
            self.list_upBar_buttonEventAllActivate()
            self.count-=1
        else:
            pass
    
    def list_PlayPageEvent(self, event, index):
        database = Database.Database()
        data=[self.id]
        database.cursor.execute("SELECT * FROM playlist WHERE id=?",data)
        result = database.cursor.fetchall()
        num = result[index][0]
        self.PlayPageUi.stackedwidget.setCurrentIndex(1)
        self.playpageEvent = PlayPageEvent.PlayPageEvent(self.id, num, self.PlayPageUi)


    