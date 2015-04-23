from PyQt4 import QtGui, QtCore


class ResultsList(QtGui.QListWidget):

    def __init__(self, parent=None):

        super(ResultsList, self).__init__()

    def addListItem(self, id, text):

        self.setCursor(QtCore.Qt.BusyCursor)

        font = QtGui.QFont()
        font.setBold(True)

        ListItem = QtGui.QListWidgetItem(text)
        self.addItem(ListItem)
        ListItem.setFont(font)

        self.unsetCursor()


if __name__ == "__main__":

    import sys
    import feedparser

    app = QtGui.QApplication(sys.argv)

    view = ResultsList()

    # for i in range(1000):
    #     view.addListItem(1, "Item %i" % i)

    url = 'http://export.arxiv.org/api/query?search_query=all:electron&start=0&max_results=10'
    d = feedparser.parse(url)

    for entry in d.entries:

        text = entry.title.replace("\n", "").replace("\r", "")
        view.addListItem(1, text)

    view.setWindowTitle("Results List")
    view.resize(640, 480)
    view.show()
    sys.exit(app.exec_())
