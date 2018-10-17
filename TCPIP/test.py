# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import *
from TCPIP.mainWindow import Ui_NetTools
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from TCPIP.client import Ui_Form

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




if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MyMainWindow()
    win.show()
    sys.exit(app.exec_())


