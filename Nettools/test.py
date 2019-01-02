from PyQt5 import QtWidgets
import socket
import threading
import sys

from Nettools.LOGIC.tool import log
from Nettools.UI import tcp_clientUI, tcp_serverUI
from Nettools.LOGIC import stopThreading

class TcpserverLogic(QtWidgets.QWidget,tcp_serverUI.Ui_serverUI):
    def __init__(self):
        super(TcpserverLogic,self).__init__()

        self.setupUi(self)

        log.debug(self)

    def tcp_server_start(self):
        log.debug(self)

tc = TcpserverLogic()

tc.tcp_server_start()