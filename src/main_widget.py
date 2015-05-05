from PyQt4 import QtGui, QtCore

import navigation
import arxiv


class MainWidget(QtGui.QWidget):

        def __init__(self):
            super(MainWidget, self).__init__()

            self.initUI()

        def initUI(self):

            self.splitter = QtGui.QSplitter(QtCore.Qt.Horizontal)

            self.BrowserList = navigation.Tree()
            self.BrowserList.BrowserList()

            self.results = arxiv.Arxiv()

            self.splitter.addWidget(self.BrowserList)

            self.splitter.addWidget(self.results)

            self.splitter.setStretchFactor(1, 2)
            self.splitter.setChildrenCollapsible(False)

            layout = QtGui.QHBoxLayout()
            layout.addWidget(self.splitter)
            self.setLayout(layout)

            self.BrowserList.itemSelectionChanged.connect(self.itemSelected)

        def itemSelected(self):

            # self.results.setParent(None)
            self.results.hide()
            self.results.close()

            self.results = arxiv.Arxiv()
            query = self.BrowserList.selectedItems()[0].query
            self.results.Query(query)

            self.splitter.insertWidget(1, self.results)
            self.splitter.setStretchFactor(1, 2)
