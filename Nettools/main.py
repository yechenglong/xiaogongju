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
        self.iplineEdit.setInputMask('000.000.000.000; ')
        self.portlineEdit.setValidator(QIntValidator())
        self.ConnectpushButton.clicked.connect(tcp_logic.TcpserverLogic.tcp_server_start)






if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = TcpserverForm()
    win.show()
    sys.exit(app.exec_())