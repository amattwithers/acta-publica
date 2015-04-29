from PyQt4 import QtGui, QtCore

import nested_list
import arxiv_results


class MainWidget(QtGui.QWidget):

        def __init__(self):
            super(MainWidget, self).__init__()

            self.initUI()

        def initUI(self):

            self.splitter = QtGui.QSplitter(QtCore.Qt.Horizontal)

            self.BrowserList = nested_list.SimpleTree()
            self.BrowserList.BrowserList()

            self.results = arxiv_results.ResultsList()

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

            self.results = arxiv_results.ResultsList()
            query = self.BrowserList.selectedItems()[0].query
            self.results.get_data(query)

            self.splitter.insertWidget(1, self.results)
            self.splitter.setStretchFactor(1, 2)
