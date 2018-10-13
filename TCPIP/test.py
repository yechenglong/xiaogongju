# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import *
from TCPIP.mainWindow import Ui_NetTools
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class MyMainWindow(QMainWindow, Ui_NetTools,QPushButton):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
        self.count = 1
        self.createContextMenu()

    def createContextMenu(self):
        '''
        创建右键的菜单
        :return:
        '''
        self.treeWidget.setContextMenuPolicy(Qt.CustomContextMenu)
        self.treeWidget.customContextMenuRequested.connect(self.showContextMenu)
        # 创建QMenu
        self.contextMenu = QMenu(self)
        self.actionnew = self.contextMenu.addAction("New")
        self.actiondelete = self.contextMenu.addAction("Delete")
        self.actionnew.triggered.connect(self.actionHandler)
        self.actiondelete.triggered.connect(self.actionHandler)

    def showContextMenu(self, pos):
        '''''
        右键点击时调用的函数
        '''
        self.count+=1
        # 菜单显示前，将它移动到鼠标点击的位置
        self.contextMenu.exec_(QCursor.pos()) #在鼠标位置显示
        #self.contextMenu.show()
        print(self.count)

    def actionHandler(self):
        '''''
        菜单中的具体action调用的函数
        '''
        if self.count % 3 == 1:
            self.setText(u"first")
        elif self.count % 3 == 2:
            self.setText(u"second")
        elif self.count % 3 == 0:
            self.setText(u"third")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MyMainWindow()
    win.show()
    sys.exit(app.exec_())


