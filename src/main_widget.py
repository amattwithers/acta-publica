from PyQt4 import QtGui, QtCore

import nested_list
import results_widget


class MainWidget(QtGui.QWidget):

        def __init__(self):
            super(MainWidget, self).__init__()

            self.initUI()

        def initUI(self):

            splitter = QtGui.QSplitter(QtCore.Qt.Horizontal)

            self.BrowserList = nested_list.SimpleTree()
            self.BrowserList.BrowserList()

            self.ResultsList = results_widget.ResultsList()

            splitter.addWidget(self.BrowserList)

            splitter.addWidget(self.ResultsList)

            splitter.setStretchFactor(1, 2)
            splitter.setChildrenCollapsible(False)

            layout = QtGui.QHBoxLayout()
            layout.addWidget(splitter)
            self.setLayout(layout)
