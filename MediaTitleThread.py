from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import threading
import requests
import pafy

class MediaTitleThread(QObject,threading.Thread):
    title = QtCore.pyqtSignal(str)
    def __init__(self,url):
        super().__init__()
        threading.Thread.__init__(self)
        self.url = url

    def run(self):
        video = pafy.new(self.url)
        text = video.title
        self.title.emit(text)
