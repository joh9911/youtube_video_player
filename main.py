from PyQt5 import QtWidgets, QtCore, QtGui
import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *
import LoginPageEvent
import Database


if __name__=="__main__":
    # start = al()
    app = QtWidgets.QApplication(sys.argv)
    
    ui=LoginPageEvent.LoginPageEvent()
    
    sys.exit(app.exec_())
    