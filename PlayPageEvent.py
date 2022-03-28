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
import pafy
import requests
import vlc

class PlayPageEvent:
    def __init__(self,id,num,ui):
        self.count = 0
        self.id = id
        self.playlistnum = num
        self.currentnum = 0
        self.PlayPageUi = ui
        self.PlayPageUi.player_upBar_button[1].clicked.connect(self.player_backButtonEvent)
        self.PlayPageUi.player_upBar_button[0].clicked.connect(self.player_addButtonEvent)
        self.PlayPageUi.player_playbutton[0].clicked.connect(self.mediaLeftMove)
        self.PlayPageUi.player_playbutton[1].clicked.connect(self.mediaPasue)
        self.PlayPageUi.player_playbutton[2].clicked.connect(self.mediaRightMove)
        self.PlayPageUi.player_playbutton[3].clicked.connect(self.mediaHalt)
        self.PlayPageUi.progressbar.sliderMoved.connect(self.setPosition)
        self.currentImagelist()
        self.instance = vlc.Instance()
        self.mediaplayer = self.instance.media_player_new()
        

        if sys.platform.startswith("linux"):  # for Linux using the X Server
            self.mediaplayer.set_xwindow(self.PlayPageUi.player_player.winId())
        elif sys.platform == "win32":  # for Windows
            self.mediaplayer.set_hwnd(self.PlayPageUi.player_player.winId())
        elif sys.platform == "darwin":  # for MacOS
            self.mediaplayer.set_nsobject(self.PlayPageUi.player_player.winId())
    
    def mediaLeftMove(self):
        pass
    #     database = Database.Database()
    #     data = [self.playlistnum]
    #     database.cursor.execute("SELECT * FROM player WHERE playlistnum=?",data)
    #     result = database.cursor.fetchall()
    #     self.PlayPageUi.player_medianame.setText(result[0][3])
    #     video = pafy.new(result[0][2])
    #     best = video.getbest()
    #     playurl = best.url
    #     media = self.instance.media_new(playurl)
    #     media.get_mrl()
    #     self.mediaplayer.set_media(media)
    #     self.mediaplayer.play()
        
        
    def mediaPasue(self):
        self.mediaplayer.pause()
        text = self.PlayPageUi.player_playbutton[1].text()
        if text == "▶":
            self.PlayPageUi.player_playbutton[1].setText("⏸")
        else:
            self.PlayPageUi.player_playbutton[1].setText("▶")
    
    def mediaRightMove(self):
        pass
    
    def mediaHalt(self):
        pass
    
    def setPosition(self,position):
        self.mediaplayer.set_position(position / 1000.0)

    def currentImagelist(self):
        database = Database.Database()
        data=[self.playlistnum]
        database.cursor.execute("SELECT * FROM player WHERE playlistnum=?",data)
        result = database.cursor.fetchall()
        for index in range(0,len(result)):
            video = pafy.new(result[index][2])
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
            thum = video.bigthumb
            image = QtGui.QImage()
            image.loadFromData(requests.get(thum).content)
            image.scaled(200,140)
            label.setPixmap(QtGui.QPixmap(image))
            label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            
            text = QtWidgets.QLineEdit(button)
            text.setGeometry(250, 100, 170, 30)
            text.setText(str(result[index][3]))
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
            self.PlayPageUi.player_player_number.append(result[index][0])
            self.player_upBar_buttonEventActivate()


    def player_addButtonEvent(self):
        database = Database.Database()
        URL, ok = QtWidgets.QInputDialog.getText(self.PlayPageUi.centralwidget,"input","동영상 URL을 입력하세요:")
        video = pafy.new(URL)
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
            image = QtGui.QImage()
            thum = video.bigthumb
            image.loadFromData(requests.get(thum).content)
            image.scaled(200,140)
            label.setPixmap(QtGui.QPixmap(image))
            label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            
            text = QtWidgets.QLineEdit(button)
            text.setGeometry(250, 20, 170, 150)
            text.setStyleSheet(
                "font: 8px Arial"
            )
            text.setText(video.title)
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
            column = ["playlistnum","url","name"]
            data = [self.playlistnum, URL, video.title]
            database.dataCreate("player",column,data)
            data = [self.playlistnum]
            database.cursor.execute("SELECT * FROM player WHERE playlistnum=?",data)
            result = database.cursor.fetchall()
            self.PlayPageUi.player_player_number.append(result[self.count][0])
            self.count+=1
        else:
            pass

    def player_backButtonEvent(self):
        QtWidgets.QMessageBox.about(self.PlayPageUi.centralwidget,'About Title','재생목록 페이지로 이동합니다.')
        self.PlayPageUi.stackedwidget.setCurrentIndex(0)
        self.player_upBar_buttonEventAllDeactivate()

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
        database = Database.Database()
        reply = QtWidgets.QMessageBox.question(self.PlayPageUi.centralwidget,"Message","정말 삭제할까요?",QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No)
        if reply == QtWidgets.QMessageBox.StandardButton.Yes:
            number = self.PlayPageUi.player_player_number[index]
            database.playerdataDelete2(number)
            self.PlayPageUi.player_deleteButton[index].clicked.disconnect()
            self.PlayPageUi.player_list[index].clicked.disconnect()
            del self.PlayPageUi.player_deleteButton[index]
            del self.PlayPageUi.player_list[index]
            del self.PlayPageUi.player_player_number[index]
            self.PlayPageUi.player_form.removeRow(index)
            self.player_upBar_buttonEventAllDeactivate()
            self.player_upBar_buttonEventAllActivate()
        else:
            pass
    def player_PlayPageEvent(self, event, index):
        database = Database.Database()
        number = self.PlayPageUi.player_player_number[index]
        self.currentnum = number
        data = [number]
        database.cursor.execute("SELECT * FROM player WHERE sequence=?",data)
        result = database.cursor.fetchall()
        self.PlayPageUi.player_medianame.setText(result[0][3])
        video = pafy.new(result[0][2])
        best = video.getbest()
        playurl = best.url
        media = self.instance.media_new(playurl)
        media.get_mrl()
        self.mediaplayer.set_media(media)
        self.mediaplayer.play()