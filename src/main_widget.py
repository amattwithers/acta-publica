from PyQt4 import QtGui, QtCore

import navigation
import arxiv
import moreinfo


class MainWidget(QtGui.QWidget):

        def __init__(self):
            super(MainWidget, self).__init__()

            self.initUI()

        def initUI(self):

            self.splitter = QtGui.QSplitter(QtCore.Qt.Horizontal)

            self.BrowserList = navigation.Tree()
            self.BrowserList.BrowserList()

            self.results = arxiv.Arxiv()

            self.moreInfo = moreinfo.MoreInfo()

            self.splitter.addWidget(self.BrowserList)

            self.splitter.addWidget(self.results)

            self.splitter.addWidget(self.moreInfo)

            self.splitter.setStretchFactor(1, 4)
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

            self.results.itemSelectionChanged.connect(self.resultSelected)

            self.splitter.insertWidget(1, self.results)
            self.splitter.setStretchFactor(1, 4)

        def resultSelected(self):

            self.moreInfo.hide()
            self.moreInfo.close()

            self.moreInfo = moreinfo.MoreInfo()
            data = self.results.selectedItems()[0].data
            self.moreInfo.setData(data)

            self.splitter.insertWidget(2, self.moreInfo)
