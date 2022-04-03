from ast import Str
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import threading
import requests
import pafy
import PlayPageEvent
import Database

class MediaThumnailThread(QObject,threading.Thread):
    thumbnailTitle = QtCore.pyqtSignal(list)
    def __init__(self, url, ui, num, select, index):
        super().__init__()
        threading.Thread.__init__(self)
        self.select = select
        self.playlistnum = num
        self.url = url
        self.ui = ui
        self.index = index
        self.thumbnailTitle.connect(self.thumbnailAndTitle)
        
    
    def run(self):
        try:
            self.video = pafy.new(self.url)
        except:
            QtWidgets.QMessageBox.about(self.PlayPageUi.centralwidget,'About Title','잘못된 URL입니다.')
        else:
            image = QtGui.QImage()
            thum = self.video.bigthumb
            image.loadFromData(requests.get(thum).content)
            image.scaled(200,140)
            title = self.video.title
            list = [image, title, self.index]
            self.thumbnailTitle.emit(list)
            if self.select == 1:
                column = ["playlistnum","url","name"]
                data = [self.playlistnum, self.url, title]
                self.databaseSave(column, data)
            
            elif self.select == 0:
                pass 
           
            else:
                print("객체 생성 오류")

    def databaseSave(self, column, data):
        database = Database.Database()
        database.dataCreate("player",column,data)
        result = database.dataRead("player", column, data)
        self.ui.playerPagePlayerNumber.append(result[len(result)-1][0])

    def thumbnailAndTitle(self, list):
        image = list[0]
        title = list[1]
        index = list[2]
        print(index)
        self.ui.playerPageThumnail[index].setPixmap(QtGui.QPixmap(image))
        self.ui.playerPageThumnail[index].setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.ui.playerPageTitle[index].setText(title)


