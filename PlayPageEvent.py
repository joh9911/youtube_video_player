from http.client import OK
from tkinter.messagebox import NO, YES
from PyQt5 import QtWidgets, QtCore, QtGui
import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from matplotlib import image
from sympy import cancel
import Database
import pafy
import requests
import vlc
import MediaThumnailThread
import MediaTitleThread

class PlayPageEvent:
    def __init__(self,id,num,ui):
        self.id = id
        self.playlistnum = num
        self.PlayPageUi = ui
        self.PlayPageUi.playerPageUpBarButton[1].clicked.connect(self.playerPageBackButtonEvent)
        self.PlayPageUi.playerPageUpBarButton[0].clicked.connect(self.playerPageAddButtonEvent)
        self.PlayPageUi.progressbar.sliderMoved.connect(self.setPosition)
        self.dataUpdate()
        self.instance = vlc.Instance()
        self.mediaplayer = self.instance.media_player_new()
        self.mediaplayer.set_hwnd(self.PlayPageUi.playerPagePlayer.winId())
        
        
    def mediaPlayEvent(self, event, index):
        self.playerPageUpBarButtonEventAllDeactivate()
        self.PlayPageUi.playerPageUpBarButton[1].disconnect()
        self.PlayPageUi.playerPageUpBarButton[0].disconnect()
        database = Database.Database()
        number = self.PlayPageUi.playerPagePlayerNumber[index]
        column = ["sequence"]
        data = [number]
        result = database.dataRead("player", column, data)
        self.mediaSetPlay(result[0][3], result[0][2], index)

    def mediaSetPlay(self, title, url, index):

        self.PlayPageUi.playerPageMediaName.setText(title)
        video = pafy.new(url)
        best = video.getbest()
        playurl = best.url
        media = self.instance.media_new(playurl)
        media.get_mrl()
        self.mediaplayer.set_media(media)
        self.mediaplayer.play()
        self.mediaPlayerButtonActivate(index)
        self.playerPageUpBarButtonEventAllActivate()
        self.PlayPageUi.playerPageUpBarButton[1].clicked.connect(self.playerPageBackButtonEvent)
        self.PlayPageUi.playerPageUpBarButton[0].clicked.connect(self.playerPageAddButtonEvent)
    
    def mediaLeftShift(self, event, index):
        database= Database.Database()
        try:
            number = self.PlayPageUi.playerPagePlayerNumber[index-1]
        except:
            self.mediaplayer.set_pause(0)
            self.mediaplayer.pause()
        else:
            column = ["sequence"]
            data = [number]
            result = database.dataRead("player", column, data)
            self.mediaSetPlay(result[0][3], result[0][2], index-1)
        
        
    def mediaPause(self, event, index):
        self.mediaplayer.pause()
        text = self.PlayPageUi.playerPagePlayButton[1].text()
        if text == "▶":
            self.PlayPageUi.playerPagePlayButton[1].setText("⏸")
        else:
            self.PlayPageUi.playerPagePlayButton[1].setText("▶")
    
    def mediaRightShift(self, event, index):
        database = Database.Database()
        try:
            number = self.PlayPageUi.playerPagePlayerNumber[index+1]
        except:
            column = ["sequencce"]
            data = [number]
            result = database.dataRead("player", column, data)
            self.mediaSetPlay(result[0][3], result[0][2], 0)
        else:
            column = ["sequencce"]
            data = [number]
            result = database.dataRead("player", column, data)
            self.mediaSetPlay(result[0][3], result[0][2], index+1)
    
    def mediaStop(self, event, index):
        self.mediaplayer.set_pause(0)
    
    def setPosition(self,position):
        self.mediaplayer.set_position(position / 1000.0)
    
    def dataUpdate(self):
        database = Database.Database()
        data=[self.playlistnum]
        database.cursor.execute("SELECT * FROM player WHERE playlistnum=?",data)
        result = database.cursor.fetchall()
        for index in range(0,len(result)):
            self.playerUiAdd()
            mediaThread = MediaThumnailThread.MediaThumnailThread(result[index][2], self.PlayPageUi, self.playlistnum, 0, index)
            mediaThread.start()
            self.PlayPageUi.playerPagePlayerNumber.append(result[index][0])
    
    def playerPageAddButtonEvent(self):
        database = Database.Database()
        URL, ok = QtWidgets.QInputDialog.getText(self.PlayPageUi.centralwidget,"input","동영상 URL을 입력하세요:")
        if ok:
            self.playerUiAdd()
            index = len(self.PlayPageUi.playerPageThumnail)-1
            mediaThread = MediaThumnailThread.MediaThumnailThread(URL,self.PlayPageUi, self.playlistnum, 1, index)
            mediaThread.start()
        else:
            pass
    
    def playerUiAdd(self):
        button = QtWidgets.QPushButton(self.PlayPageUi.playerPageGroupBox)
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
        # label.setPixmap(QtGui.QPixmap(image))
        # label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        
        text = QtWidgets.QLineEdit(button)
        text.setGeometry(250, 20, 170, 150)
        text.setStyleSheet(
            "font: 8px Arial"
        )
        text.setText("title")
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
        self.PlayPageUi.playerPagePlayerList.append(button)
        self.PlayPageUi.playerPageDeleteButton.append(button1)
        self.PlayPageUi.playerPageThumnail.append(label)
        self.PlayPageUi.playerPageTitle.append(text)
        self.PlayPageUi.playerPageForm.addRow("",button)
        index = len(self.PlayPageUi.playerPagePlayerList)-1
        self.playerPageUpBarButtonActivate(index)

    def playerPageUpBarDeleteButtonEvent(self, event, index):
        database = Database.Database()
        reply = QtWidgets.QMessageBox.question(self.PlayPageUi.centralwidget,"Message","정말 삭제할까요?",QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No)
        if reply == QtWidgets.QMessageBox.StandardButton.Yes:
            number = self.PlayPageUi.playerPagePlayerNumber[index]
            column = ["playlistnum", "sequence"]
            data = [self.playlistnum, number]
            database.dataDelete("player", column, data)
            self.playerPageUpBarButtonDeactivate(index)
            del self.PlayPageUi.playerPageDeleteButton[index]
            del self.PlayPageUi.playerPagePlayerList[index]
            del self.PlayPageUi.playerPagePlayerNumber[index]
            self.PlayPageUi.playerPageForm.removeRow(index)
            self.playerPageUpBarButtonEventAllDeactivate()
            self.playerPageUpBarButtonEventAllActivate()
        else:
            pass

    def playerPageBackButtonEvent(self):
        QtWidgets.QMessageBox.about(self.PlayPageUi.centralwidget,'About Title','재생목록 페이지로 이동합니다.')
        self.PlayPageUi.stackedwidget.setCurrentIndex(0)
        self.playerPageUpBarButtonEventAllDeactivate()
        # self.mediaPlayerButtonDeactivate()
        self.PlayPageUi.playerPageUpBarButton[1].disconnect()
        self.PlayPageUi.playerPageUpBarButton[0].disconnect()
        self.PlayPageUi.progressbar.sliderMoved.disconnect()
        self.allDeleteList()
        self.mediaplayer.stop()
        self.PlayPageUi.playerPageMediaName.setText("")
        try:
            self.mediaPlayerButtonDeactivate()
        except:
            pass

    def playerPageUpBarButtonActivate(self,index):
        self.PlayPageUi.playerPageDeleteButton[index].clicked.connect(lambda event, nowIndex = index: self.playerPageUpBarDeleteButtonEvent(event, nowIndex))
        self.PlayPageUi.playerPagePlayerList[index].clicked.connect(lambda event, nowIndex = index: self.mediaPlayEvent(event, nowIndex))
    
    def playerPageUpBarButtonDeactivate(self, index):
        self.PlayPageUi.playerPageDeleteButton[index].clicked.disconnect
        self.PlayPageUi.playerPagePlayerList[index].clicked.disconnect
    
    def playerPageUpBarButtonEventAllActivate(self):
        for index in range(0,len(self.PlayPageUi.playerPageDeleteButton)):
            self.PlayPageUi.playerPageDeleteButton[index].clicked.connect(lambda event, nowIndex = index: self.playerPageUpBarDeleteButtonEvent(event, nowIndex))
            self.PlayPageUi.playerPagePlayerList[index].clicked.connect(lambda event, nowIndex = index: self.mediaPlayEvent(event, nowIndex))
    
    def playerPageUpBarButtonEventAllDeactivate(self):
        for index in range(0,len(self.PlayPageUi.playerPageDeleteButton)):
            self.PlayPageUi.playerPageDeleteButton[index].clicked.disconnect()
            self.PlayPageUi.playerPagePlayerList[index].clicked.disconnect()
    
    
   
    def allDeleteList(self):
        for index in range(0,len(self.PlayPageUi.playerPageDeleteButton)):
            del self.PlayPageUi.playerPagePlayerList[0]
            del self.PlayPageUi.playerPageDeleteButton[0]
            del self.PlayPageUi.playerPageThumnail[0]
            del self.PlayPageUi.playerPageTitle[0]
            self.PlayPageUi.playerPageForm.removeRow(0)

    
    def mediaPlayerButtonActivate(self, index):
        self.PlayPageUi.playerPagePlayButton[0].clicked.connect(lambda event, nowIndex = index: self.mediaLeftShift(event, nowIndex))
        self.PlayPageUi.playerPagePlayButton[1].clicked.connect(lambda event, nowIndex = index: self.mediaPause(event, nowIndex))
        self.PlayPageUi.playerPagePlayButton[2].clicked.connect(lambda event, nowIndex = index: self.mediaRightShift(event, nowIndex))
        self.PlayPageUi.playerPagePlayButton[3].clicked.connect(lambda event, nowIndex = index: self.mediaStop(event, nowIndex))
    
    def mediaPlayerButtonDeactivate(self):
        self.PlayPageUi.playerPagePlayButton[0].clicked.disconnect()
        self.PlayPageUi.playerPagePlayButton[1].clicked.disconnect()
        self.PlayPageUi.playerPagePlayButton[2].clicked.disconnect()
        self.PlayPageUi.playerPagePlayButton[3].clicked.disconnect()
    