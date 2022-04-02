from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import threading
import requests
import pafy
import PlayPageEvent

class MediaThumnailThread(QObject,threading.Thread):
    thumbnail = QtCore.pyqtSignal(QImage)
    
    def __init__(self, url):
        super().__init__()
        threading.Thread.__init__(self)
        self.url = url
        
    
    def run(self):
        self.video = pafy.new(self.url)
        image = QtGui.QImage()
        thum = self.video.bigthumb
        image.loadFromData(requests.get(thum).content)
        image.scaled(200,140)
        self.thumbnail.emit(image)

       


