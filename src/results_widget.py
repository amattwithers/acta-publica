from PyQt4 import QtGui, QtCore


class ItemWidget(QtGui.QWidget):

    def __init__(self, parent=None):

        super(ItemWidget, self).__init__()

        self.id = QtGui.QLabel("ID")
        self.title = QtGui.QLabel("TITLE")
        self.authors = QtGui.QLabel("AUTHORS")
        self.date = QtGui.QLabel("DATE")
        self.journ_ref = QtGui.QLabel("JOURN_REF")
        self.comment = QtGui.QLabel("COMMENT")

        self.title.setScaledContents(True)
        self.authors.setScaledContents(True)

        # self.title.setWordWrap(True)
        # self.authors.setWordWrap(True)

        self.layout = QtGui.QVBoxLayout()
        self.layout.addStretch()
        self.layout.setSizeConstraint(QtGui.QLayout.SetFixedSize)

        # self.layout.addWidget(self.id)
        self.layout.addWidget(self.title)
        self.layout.addWidget(self.authors)
        # self.layout.addWidget(self.date)
        self.layout.addWidget(self.journ_ref)
        self.layout.addWidget(self.comment)

        self.setLayout(self.layout)

    def setData(self, id, title, authors, date, journ_ref, comment):

        title = '<span style="font-weight: bold;">' + title + '</span>'
        authors = '<span style="font-style: italic; color:blue;">' + authors + '</span>'

        self.title.setText(title)
        self.authors.setText(authors)
        self.date.setText(date)
        self.journ_ref.setText(journ_ref)
        self.comment.setText(comment)

    def mousePressEvent(self, event):
        print "Open"
        self.popup = ItemPopup()
        self.popup.setData(self.id, self.title, self.authors, self.date, self.journ_ref, self.comment)
        self.popup.show()


class ItemPopup(QtGui.QWidget):

    def __init__(self, parent=None):

        super(ItemPopup, self).__init__()

        self.setGeometry(100, 100, 640, 480)
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

    def setData(self, id, title, authors, date, journ_ref, comment):

        self.layout = QtGui.QVBoxLayout()
        self.layout.addStretch()
        self.layout.setSizeConstraint(QtGui.QLayout.SetFixedSize)

        # self.layout.addWidget(self.id)
        self.layout.addWidget(title)
        self.layout.addWidget(authors)
        # self.layout.addWidget(self.date)
        self.layout.addWidget(journ_ref)
        self.layout.addWidget(comment)

        self.setLayout(self.layout)

    def mousePressEvent(self, event):

        print "Close"
        self.close()


class ResultsList(QtGui.QListWidget):

    def __init__(self, parent=None):

        super(ResultsList, self).__init__()

    def addListItem(self, id, title, authors, date, journ_ref, comment):

        self.setCursor(QtCore.Qt.BusyCursor)
        # font = QtGui.QFont()
        # font.setBold(True)
        ListItem = QtGui.QListWidgetItem()

        itemwidget = ItemWidget()
        itemwidget.setData(id, title, authors, date, journ_ref, comment)

        self.addItem(ListItem)
        self.setItemWidget(ListItem, itemwidget)

        ListItem.setSizeHint(itemwidget.sizeHint())

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

        try:
            id = entry.id
        except AttributeError:
            id = "No id found!"

        try:
            title = entry.title.replace("\n", "").replace("\r", "")
        except AttributeError:
            title = "No Title Found!"

        try:
            summary = entry.summary.replace("\n", "").replace("\r", "")
        except AttributeError:
            summary = "No Summary Found!"

        try:
            authstr = ', '.join(author.name for author in entry.authors)
        except AttributeError:
            authstr = "No Authors Found!"

        try:
            date = entry.updated
        except AttributeError:
            date = "No data Found!"

        try:
            journ_ref = entry.arxiv_journal_ref
        except AttributeError:
            journ_ref = "No Journal Ref Found!"

        try:
            comment = entry.arxiv_comment
        except AttributeError:
            comment = "No Comment Found!"

        view.addListItem(id, title, authstr, date, journ_ref, comment)

    view.setWindowTitle("Results List")
    view.resize(640, 480)
    view.show()
    sys.exit(app.exec_())
