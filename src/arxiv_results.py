from PyQt4 import QtGui, QtCore

import feedparser


class ItemWidget(QtGui.QWidget):

    def __init__(self, parent=None):

        super(ItemWidget, self).__init__()

        self.id = QtGui.QLabel("ID")
        self.title = QtGui.QLabel("TITLE")
        self.title.setWordWrap(True)
        self.title.setMinimumWidth(self.frameGeometry().width())
        self.authors = QtGui.QLabel("AUTHORS")
        self.authors.setWordWrap(True)
        self.authors.setMinimumWidth(self.frameGeometry().width())
        self.date = QtGui.QLabel("DATE")
        self.date.setWordWrap(True)
        self.date.setMinimumWidth(self.frameGeometry().width())
        self.journ_ref = QtGui.QLabel("JOURN_REF")
        self.journ_ref.setWordWrap(True)
        self.journ_ref.setMinimumWidth(self.frameGeometry().width())
        self.comment = QtGui.QLabel("COMMENT")
        self.comment.setWordWrap(True)
        self.comment.setMinimumWidth(self.frameGeometry().width())

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

    def setData(self, data):

        title = '<span style="font-weight: bold;">' + data['title'] + '</span>'
        authors = '<span style="font-style: italic; color:blue;">' + data['authors'] + '</span>'

        self.title.setText(title)
        self.authors.setText(authors)
        self.date.setText(data['date'])
        self.journ_ref.setText(data['journal'])
        self.comment.setText(data['comment'])


class ItemPopup(QtGui.QWidget):

    def __init__(self, parent=None):

        super(ItemPopup, self).__init__()

        self.setGeometry(0, 0, 640, 480)
        self.setMaximumSize(640, 480)
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        self.id = QtGui.QLabel("ID")
        self.title = QtGui.QLabel("TITLE")
        self.title.setTextInteractionFlags(QtCore.Qt.TextBrowserInteraction)
        self.title.setWordWrap(True)
        self.authors = QtGui.QLabel("AUTHORS")
        self.authors.setTextInteractionFlags(QtCore.Qt.TextBrowserInteraction)
        self.authors.setWordWrap(True)
        self.date = QtGui.QLabel("DATE")
        self.date.setTextInteractionFlags(QtCore.Qt.TextBrowserInteraction)
        self.date.setWordWrap(True)
        self.journ_ref = QtGui.QLabel("JOURN_REF")
        self.journ_ref.setTextInteractionFlags(QtCore.Qt.TextBrowserInteraction)
        self.journ_ref.setWordWrap(True)
        self.comment = QtGui.QLabel("COMMENT")
        self.comment.setTextInteractionFlags(QtCore.Qt.TextBrowserInteraction)
        self.comment.setWordWrap(True)
        self.summary = QtGui.QLabel("SUMMARY")
        self.summary.setTextInteractionFlags(QtCore.Qt.TextBrowserInteraction)
        self.summary.setWordWrap(True)

        self.layout = QtGui.QVBoxLayout()
        # self.layout.addStretch()
        self.layout.setSizeConstraint(QtGui.QLayout.SetFixedSize)

        # self.layout.addWidget(self.id)
        self.layout.addWidget(self.title)
        self.layout.addWidget(self.authors)
        self.layout.addWidget(self.date)
        self.layout.addWidget(self.journ_ref)
        self.layout.addWidget(self.comment)
        self.layout.addWidget(self.summary)

        self.setLayout(self.layout)

        self.center()

    def setData(self, data):

        title = '<span style="font-weight: bold;">' + data['title'] + '</span>'
        authors = '<span style="font-style: italic; color:blue;">' + data['authors'] + '</span>'

        self.title.setText(title)
        self.authors.setText(authors)
        self.date.setText(data['date'])
        self.journ_ref.setText(data['journal'])
        self.comment.setText(data['comment'])
        self.summary.setText(data['summary'])

        self.center()

    def center(self):

        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def mouseDoubleClickEvent(self, event):

        print "Close"
        self.close()


class ListItem(QtGui.QListWidgetItem):

    def __init__(self, parent=None):

        super(ListItem, self).__init__()

        self.data = ''


class ResultsList(QtGui.QListWidget):

    def __init__(self, parent=None):

        super(ResultsList, self).__init__()

        self.itemDoubleClicked.connect(self.showPopup)

        self.data = ''

    def get_data(self, query):

        self.setCursor(QtCore.Qt.BusyCursor)

        prefix = 'http://export.arxiv.org/api/query?'

        suffix = '&sortBy=submittedDate&sortOrder=descending'

        self.query = prefix + query + suffix

        print self.query

        d = feedparser.parse(self.query)

        for entry in d.entries:

            try:
                id = entry.id.replace("\n", "").replace("\r", "")
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
                authstr = authstr.replace("\n", "").replace("\r", "")
            except AttributeError:
                authstr = "No Authors Found!"

            try:
                date = entry.updated.replace("\n", "").replace("\r", "")
            except AttributeError:
                date = "No data Found!"

            try:
                journ_ref = entry.arxiv_journal_ref.replace("\n", "").replace("\r", "")
            except AttributeError:
                journ_ref = "No Journal Ref Found!"

            try:
                comment = entry.arxiv_comment.replace("\n", "").replace("\r", "")
            except AttributeError:
                comment = "No Comment Found!"

            data = {'id': id,
                    'title': title,
                    'authors': authstr,
                    'date': date,
                    'journal': journ_ref,
                    'comment': comment,
                    'summary': summary
                    }

            List_Item = ListItem()
            List_Item.data = data

            itemwidget = ItemWidget()
            itemwidget.setData(data)

            self.addItem(List_Item)
            self.setItemWidget(List_Item, itemwidget)

            List_Item.setSizeHint(itemwidget.sizeHint())

        self.unsetCursor()

    def showPopup(self):
        print "Open"
        self.popup = ItemPopup()
        self.popup.setData(self.selectedItems()[0].data)
        self.popup.show()


if __name__ == "__main__":

    import sys

    app = QtGui.QApplication(sys.argv)

    view = ResultsList()

    view.setWindowTitle("Results List")
    view.resize(640, 480)
    view.show()
    sys.exit(app.exec_())
