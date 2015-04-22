from PyQt4 import QtGui


class ResultsWidget(QtGui.QListWidget):

        def __init__(self, parent=None):

            super(ResultsWidget, self).__init__()

            self.initUI()

        def initUI(self):

            self.Item1 = QtGui.QListWidgetItem("Item 1")
