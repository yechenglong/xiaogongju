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

class MyMainWindow(QMainWindow, Ui_NetTools,QPushButton):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
        self.createContextMenu()
        self.child1 = ChildrenForm()

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
        self.actionnew.triggered.connect(self.newaction)
        self.actiondelete.triggered.connect(self.deleteaction)

    def showContextMenu(self, pos):
        '''''
        右键点击时调用的函数
        '''
        # 菜单显示前，将它移动到鼠标点击的位置

        if self.treeWidget.selectedItems() != []:
            self.actionnew.setVisible(False)
        else:
            self.actionnew.setVisible(True)
        self.contextMenu.exec_(QCursor.pos()) #在鼠标位置显示
        #self.contextMenu.show()

    def newaction(self):
        '''''
        菜单中的具体actionnew调用的函数
        '''
        self.child = QTreeWidgetItem(self.treeWidget.currentItem())
        self.child.setText(0,'client')
        self.treeWidget.expandItem(self.treeWidget.currentItem())
        self.childShow()

    def deleteaction(self):
        '''''
        菜单中的具体actiondelete调用的函数
        '''
        for item in self.treeWidget.selectedItems():
            (item.parent() or self.child).removeChild(item)
        self.verticalLayout.removeWidget(self.child1)

    def childShow(self):
        self.verticalLayout.addWidget(self.child1)
        self.child1.show()


class ChildrenForm(QTabWidget,Ui_Form):
    def __init__(self):
        super(ChildrenForm,self).__init__()
        self.setupUi(self)
        self.logic()

    def logic(self):
        self.iplineEdit.setInputMask('000.000.000.000; ')
        self.portlineEdit.setValidator(QIntValidator())
        self.ConnectpushButton.clicked.connect(self.connectserver)


    def connectserver(self):
        print("click")


class NumberBar(QWidget):
    def __init__(self,editor):
        QWidget.__init__(self,editor)
        self.codeEditor = editor

    #get行号值
    def getWidth(self):
        digits = 1
        blockNumber = self.codeEditor.blockCount()
        Max = max(1,blockNumber)
        while(Max>=10):
            Max/=10
            digits+=1
        space = 30 +self.codeEditor.fontMetrics().width('9')*digits
        return space

    #更新行号栏宽度
    def updateWidth(self):
        width = self.getWidth()
        self.codeEditor.setViewportMargins(width, 0, 0, 0)

    #根据 updateRequest 信号 调整行号栏
    def updateArea(self,rect,dy):
        if dy:
            self.scroll(1,dy)
        else:
            self.update(0, rect.y(), self.getWidth(), rect.height())
        if (rect.contains(self.codeEditor.viewport().rect())):
            width = self.getWidth()
            self.codeEditor.setViewportMargins(width, 0, 0, 0)

        # 绘制行号栏
        def paintEvent(self, event):
            painter = QPainter(self)
            rect = event.rect()

            painter.fillRect(rect, QColor(243, 243, 243))
            block = self.codeEditor.firstVisibleBlock()

            if ui.ui2isOpen:
                blockNumber = ui2.verticalScrollBar1.value()
            else:
                blockNumber = ui.verticalScrollBar1.value()

            top = int(self.codeEditor.blockBoundingGeometry(block).translated(self.codeEditor.contentOffset()).top())
            bottom = top + int(self.codeEditor.blockBoundingRect(block).height())
            while (block.isValid() and top <= rect.bottom()):
                if (block.isVisible() and bottom >= rect.top()):
                    number = QtCore.QString.number(blockNumber + 1)
                    painter.setPen(QColor(59, 153, 181))
                    painter.drawText(0, top, self.codeEditor.lineNumberArea.width(), \
                                     painter.fontMetrics().height(), \
                                     QtCore.Qt.AlignVCenter | QtCore.Qt.AlignRight, number + ' ')

                block = block.next()
                top = bottom
                bottom = top + int(self.codeEditor.blockBoundingRect(block).height())
                blockNumber += 1



if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = ChildrenForm()
    win.show()
    sys.exit(app.exec_())


