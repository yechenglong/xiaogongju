# -*- coding: utf-8 -*-

import sys

from PyQt5 import QtCore
from PyQt5.QtWidgets import *

from TCPIP.mainWindow import Ui_NetTools
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from TCPIP.client import Ui_Form
from PyQt5.QtNetwork import *
import socket,logging,threading
from time import ctime
from TCPIP.uitl import *

class MyMainWindow(QMainWindow, Ui_NetTools,QPushButton):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
        self.createContextMenu=ContextMenu(self.treeWidget)



class ChildrenForm(QTabWidget,Ui_Form):
    def __init__(self):
        super(ChildrenForm,self).__init__()
        self.setupUi(self)
        self.logic()
        self.Numbar= NumberBar(self.recvlog_plainTextEdit).resize(self)
        self.Numbar = NumberBar(self.sendlog_plainTextEdit).resize(self)
        self.Numbar = NumberBar(self.send_plainTextEdit).resize(self)

    def logic(self):
        self.iplineEdit.setInputMask('000.000.000.000; ')
        self.portlineEdit.setValidator(QIntValidator())
        self.ConnectpushButton.clicked.connect(self.connectserver)


    def connectserver(self):
        ip = self.iplineEdit.text()
        port = int(self.portlineEdit.text())
        ADDR = (ip,port)
        self.cs = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.cs.connect(ADDR)
        print(ADDR)




if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = ChildrenForm()
    win.show()
    sys.exit(app.exec_())



