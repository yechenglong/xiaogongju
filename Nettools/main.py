# -*- coding: utf-8 -*-

import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from Nettools.LOGIC import tcp_logic
from Nettools.UI.uitl import *


class TcpserverForm(QTabWidget, tcp_logic.TcpserverLogic):
    def __init__(self):
        super(TcpserverForm,self).__init__()
        self.logic()
        self.Numbar= NumberBar(self.recvlog_plainTextEdit).resize(self)
        self.Numbar = NumberBar(self.sendlog_plainTextEdit).resize(self)
        self.Numbar = NumberBar(self.send_plainTextEdit).resize(self)

    def logic(self):
        self.ConnectpushButton.clicked.connect(self.tcp_server_start)
        self.DisconnectpushButton.clicked.connect(self.tcpserver_close)
        self.pushButton_send_2.clicked.connect(self.tcpserver_send)

class TcpclientForm(QTabWidget, tcp_logic.TcpclientLogic):
    def __init__(self):
        super(TcpclientForm,self).__init__()
        self.logic()
        self.Numbar= NumberBar(self.recvlog_plainTextEdit).resize(self)
        self.Numbar = NumberBar(self.sendlog_plainTextEdit).resize(self)
        self.Numbar = NumberBar(self.send_plainTextEdit).resize(self)

    def logic(self):
        self.ConnectpushButton.clicked.connect(self.tcp_client_start)




if __name__ == "__main__":
    app = QApplication(sys.argv)
    # win = TcpclientForm()
    win = TcpserverForm()
    win.show()
    sys.exit(app.exec_())