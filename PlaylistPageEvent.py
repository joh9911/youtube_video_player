from http.client import OK
from tkinter.messagebox import NO, YES
from PyQt5 import QtWidgets, QtCore, QtGui
import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
import PlayPage
import LoginPageEvent
import Database
import PlayPageEvent
class PlaylistPageEvent:
    
    def __init__(self,id):
        self.id = id
        self.loginSignupUi = None 
        self.playpageEvent = None   
        self.PlayPageUi = PlayPage.PlayPage()
        self.PlayPageUi.playListPageUpbar.setText("      "+str(self.id)+"")
        self.PlayPageUi.playListPageUpbarButton[1].clicked.connect(self.playListPageUpBarBackButtonEvent)
        self.PlayPageUi.playListPageUpbarButton[0].clicked.connect(self.playListPageUpBarAddButtonEvent)
        self.listUpdate()

    def listUpdate(self):
        database = Database.Database()
        column = ["id"]
        data = [self.id]
        result =  database.dataRead("playlist",column,data)
        for index in range(0,len(result)):
            self.playListUiAdd(result[index][2])
            self.PlayPageUi.playListPagePlayListNumber.append(result[index][0])

    def playListPageUpBarBackButtonEvent(self):
        QtWidgets.QMessageBox.about(self.PlayPageUi.centralwidget,'About Title','로그인 페이지로 이동합니다.')
        self.PlayPageUi.mainWindow.close()
        self.loginSignupUi = LoginPageEvent.LoginPageEvent()

    def playListPageUpBarAddButtonEvent(self):
        database = Database.Database()
        text, ok = QtWidgets.QInputDialog.getText(self.PlayPageUi.centralwidget,"input","재생목록의 제목을 입력하세요:")
        if ok:
            self.playListUiAdd(text)
            column = ["id","listname"]
            data = [self.id,text]
            database.dataCreate("playlist", column, data)
            result =  database.dataRead("playlist", column, data)
            self.PlayPageUi.playListPagePlayListNumber.append(result[len(result)-1][0])
        else:
            pass
    
    def playListUiAdd(self,text):
            button = QtWidgets.QPushButton(self.PlayPageUi.playListPageGroupBox)
            button1 = QtWidgets.QPushButton(button)
            button1.setGeometry(1480,20,30, 30)
            button1.setStyleSheet(
            "border-radius: 1px;"
            "border: 1px solid white;"
            "font: 25pt Arial;"
            "color: red;"
            )
            button1.setText("x")
            button.setFixedSize(1530,200)
            button.setStyleSheet(
            "border-radius: 1px;"
            "border: 1px solid black;"
            "font: 12pt Arial;"
            "color: gray;"
            "text-align: left;"
            )
            button.setText("   "+str(text))
            button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
            self.PlayPageUi.playListPagePlayList.append(button)
            self.PlayPageUi.playListPageDeleteButton.append(button1)
            self.PlayPageUi.playListPageForm.addRow("",button)
            index = len(self.PlayPageUi.playListPagePlayList)-1
            self.playListPageUpbarButtonEventActivate(index)
            print("나는 리스트에 재생목록을 추가했다.",index)

    def playListPageUpbarButtonEventActivate(self,index):
        self.PlayPageUi.playListPageDeleteButton[index].clicked.connect(lambda event, nowIndex = index: self.playListPageUpBarDeleteButtonEvent(event, nowIndex))
        self.PlayPageUi.playListPagePlayList[index].clicked.connect(lambda event, nowIndex = index: self.playPageMove(event, nowIndex))
    
    def playListPageUpbarButtonEventAllActivate(self):
         for index in range(0,len(self.PlayPageUi.playListPageDeleteButton)):
            self.PlayPageUi.playListPageDeleteButton[index].clicked.connect(lambda event, nowIndex = index: self.playListPageUpBarDeleteButtonEvent(event, nowIndex))
            self.PlayPageUi.playListPagePlayList[index].clicked.connect(lambda event, nowIndex = index: self.playPageMove(event, nowIndex))
    
    def playListPageUpbarButtonEventAllDeactivate(self):
         for index in range(0,len(self.PlayPageUi.playListPageDeleteButton)):
            self.PlayPageUi.playListPageDeleteButton[index].clicked.disconnect()
            self.PlayPageUi.playListPagePlayList[index].clicked.disconnect()
    
    def playListPageUpbarButtonEventDeactivate(self,index):
        self.PlayPageUi.playListPageDeleteButton[index].clicked.disconnect()
        self.PlayPageUi.playListPagePlayList[index].clicked.disconnect()
       
    def playListPageUpBarDeleteButtonEvent(self, event, index): ##만약 전체 이벤트를 초기화를 해주지 않으면 삭제 되는 순간 리스트가 줄어들며 인덱스가 땡겨지면서 이상한게 지워짐
        database = Database.Database()
        reply = QtWidgets.QMessageBox.question(self.PlayPageUi.centralwidget,"Message","정말 삭제할까요?",QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No)
        if reply == QtWidgets.QMessageBox.StandardButton.Yes:
            number = self.PlayPageUi.playListPagePlayListNumber[index]
            column = ["id", "sequence"]
            data = [self.id, number]
            database.dataDelete("playlist", column, data)
            column = ["playlistnum"]
            data = [number]
            database.dataDelete("player", column, data)
            self.playListPageUpbarButtonEventDeactivate(index)
            del self.PlayPageUi.playListPageDeleteButton[index]
            del self.PlayPageUi.playListPagePlayList[index]
            del self.PlayPageUi.playListPagePlayListNumber[index]
            self.PlayPageUi.playListPageForm.removeRow(index)
            self.playListPageUpbarButtonEventAllDeactivate()
            self.playListPageUpbarButtonEventAllActivate()
        else:
            pass
    
    def playPageMove(self, event, index):
        database = Database.Database()
        column = ["id"]
        data = [self.id]
        result = database.dataRead("playlist",column, data)
        num = result[index][0]
        self.PlayPageUi.stackedwidget.setCurrentIndex(1)
        self.playpageEvent = PlayPageEvent.PlayPageEvent(self.id, num, self.PlayPageUi)

    
    