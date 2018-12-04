from PyQt5.QtCore import QRect, Qt
from PyQt5.QtGui import QFont, QColor, QPainter, QTextFormat, QCursor
from PyQt5.QtWidgets import QWidget, QTextEdit, QMenu, QTreeWidgetItem


class NumberBar(QWidget):
    def __init__(self, editor):
        QWidget.__init__(self, editor)
        self.editor = editor
        self.editor.blockCountChanged.connect(self.updateWidth)
        self.editor.updateRequest.connect(self.updateContents)
        self.font = QFont()
        self.numberBarColor = QColor("#e8e8e8")
        self.currentLineNumber = None
        self.editor.cursorPositionChanged.connect(self.highligtCurrentLine)
        self.highligtCurrentLine()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.fillRect(event.rect(), self.numberBarColor)
        block = self.editor.firstVisibleBlock()

        while block.isValid():
            blockNumber = block.blockNumber()
            block_top = self.editor.blockBoundingGeometry(block).translated(self.editor.contentOffset()).top()
            if blockNumber == self.editor.textCursor().blockNumber():
                self.font.setBold(True)
                painter.setPen(QColor("#000000"))
            else:
                self.font.setBold(False)
                painter.setPen(QColor("#717171"))
            paint_rect = QRect(0, block_top, self.width(), self.editor.fontMetrics().height())
            painter.drawText(paint_rect, Qt.AlignCenter, str(blockNumber + 1))
            block = block.next()

    def getWidth(self):
        count = self.editor.blockCount()
        if 0 <= count < 99999:
            width = self.fontMetrics().width('99999')
        else:
            width = self.fontMetrics().width(str(count))
        return width

    def updateWidth(self):
        width = self.getWidth()
        self.editor.setViewportMargins(width, 0, 0, 0)

    def updateContents(self, rect, dy):
        if dy:
            self.scroll(0, dy)
        else:
            self.update(0, rect.y(), self.width(), rect.height())
        if rect.contains(self.editor.viewport().rect()):
            fontSize = self.editor.currentCharFormat().font().pointSize()
            self.font.setPointSize(fontSize)
            self.font.setStyle(QFont.StyleNormal)
            self.updateWidth()

    def highligtCurrentLine(self):
        newCurrentLineNumber = self.editor.textCursor().blockNumber()
        if newCurrentLineNumber != self.currentLineNumber:
            lineColor = QColor(Qt.yellow).lighter(160)
            self.currentLineNumber = newCurrentLineNumber
            hi_selection = QTextEdit.ExtraSelection()
            hi_selection.format.setBackground(lineColor)
            hi_selection.format.setProperty(QTextFormat.FullWidthSelection, True)
            hi_selection.cursor = self.editor.textCursor()
            hi_selection.cursor.clearSelection()
            self.editor.setExtraSelections([hi_selection])

    def resize(self,mm):
        self.cr = mm.contentsRect()
        # print(self.cr.left(),self.cr.top(),self.getWidth(),self.cr.height())
        rec = QRect(self.cr.left(), self.cr.top(), self.getWidth(), self.cr.height())
        self.setGeometry(rec)

class ContextMenu():
    def __init__(self, treeWidget):

        self.treeWidget = treeWidget
        self.createContextMenu()

    def createContextMenu(self):
        '''
        创建右键的菜单
        :return:
        '''
        self.treeWidget.setContextMenuPolicy(Qt.CustomContextMenu)
        self.treeWidget.customContextMenuRequested.connect(self.showContextMenu)
        # 创建QMenu
        self.contextMenu = QMenu(parent=None)
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