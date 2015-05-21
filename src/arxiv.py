from PyQt4 import QtGui, QtCore

import misc_functions as mf

import feedparser


class LabelFormat(QtGui.QLabel):

    def __init__(self, parent=None):

        super(LabelFormat, self).__init__()
        self.setWordWrap(True)
        self.setMinimumWidth(self.frameGeometry().width())
        self.setAlignment(QtCore.Qt.AlignJustify)
        self.setOpenExternalLinks(True)


class ItemWidget(QtGui.QWidget):

    def __init__(self, parent=None):

        super(ItemWidget, self).__init__()

        self.id = LabelFormat()
        self.title = LabelFormat()
        self.authors = LabelFormat()
        self.date = LabelFormat()
        self.journ_ref = LabelFormat()
        self.comment = LabelFormat()

        self.layout = QtGui.QVBoxLayout()
        self.layout.addStretch()
        self.layout.setSizeConstraint(QtGui.QLayout.SetFixedSize)

        # self.layout.addWidget(self.id)
        self.layout.addWidget(self.title)
        self.layout.addWidget(self.authors)
        # self.layout.addWidget(self.date)
        # self.layout.addWidget(self.journ_ref)
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
        self.setFixedSize(640, 480)
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        self.scrollArea = QtGui.QScrollArea
        self.scrollAreaWidgetContents = QtGui.QWidget()

        infoWidget = QtGui.QWidget

        self.id = LabelFormat()
        self.title = LabelFormat()
        # self.title.setTextInteractionFlags(QtCore.Qt.TextSelectable)
        self.authors = LabelFormat()
        self.authors.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.date = LabelFormat()
        self.date.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.journ_ref = LabelFormat()
        self.journ_ref.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.comment = LabelFormat()
        self.comment.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.summary = LabelFormat()
        self.summary.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)

        self.starButton = QtGui.QPushButton("Starred")
        self.starButton.clicked.connect(self.close)
        self.urlButton = QtGui.QPushButton("Open URL")
        self.urlButton.clicked.connect(self.close)
        self.pdfButton = QtGui.QPushButton("Open PDF")
        self.pdfButton.clicked.connect(self.close)
        self.closeButton = QtGui.QPushButton("Close")
        self.closeButton.clicked.connect(self.close)

        self.layout = QtGui.QVBoxLayout()
        infoLayout = QtGui.QVBoxLayout()
        # self.layout.addStretch()
        self.layout.setSizeConstraint(QtGui.QLayout.SetFixedSize)

        self.butLayout = QtGui.QHBoxLayout()

        self.butLayout.addWidget(self.starButton)
        self.butLayout.addWidget(self.urlButton)
        self.butLayout.addWidget(self.pdfButton)
        self.butLayout.addWidget(self.closeButton)

        # self.layout.addWidget(self.id)
        infoLayout.addWidget(self.title)
        infoLayout.addWidget(self.authors)
        infoLayout.addWidget(self.date)
        infoLayout.addWidget(self.journ_ref)
        infoLayout.addWidget(self.comment)
        infoLayout.addWidget(self.summary)

        infoWidget.setLayout(infoLayout)

        self.scrollArea.setWidget(infoWidget)

        self.layout.addWidget(infoWidget)
        self.layout.addLayout(self.butLayout)

        self.setLayout(self.layout)

        mf.center(self)

    def setData(self, data):

        title = '<span style="font-weight: bold;">' + data['title'] + '</span>'
        authors = '<span style="font-style: italic; color:blue;">' + data['authors'] + '</span>'

        self.title.setText(title)
        self.authors.setText(authors)
        self.date.setText(data['date'])
        self.journ_ref.setText(data['journal'])
        self.comment.setText(data['comment'])
        self.summary.setText(data['summary'])


class ListItem(QtGui.QListWidgetItem):

    def __init__(self, parent=None):

        super(ListItem, self).__init__()

        self.data = ''


class Arxiv(QtGui.QListWidget):

    def __init__(self, parent=None):

        super(Arxiv, self).__init__()

        self.itemDoubleClicked.connect(self.showPopup)

        self.data = ''

        self.setVerticalScrollMode(1)

    def Query(self, query):

        self.setCursor(QtCore.Qt.BusyCursor)

        prefix = 'http://export.arxiv.org/api/query?'

        suffix = '&sortBy=submittedDate&sortOrder=descending&max_results=50'

        self.query = prefix + query + suffix

        print self.query

        d = feedparser.parse(self.query)

        for entry in d.entries:

            try:
                id = entry.id.replace("\n", " ").replace("\r", " ")
            except AttributeError:
                id = "No id found!"

            try:
                title = entry.title.replace("\n", " ").replace("\r", " ")
            except AttributeError:
                title = "No Title Found!"

            try:
                summary = entry.summary.replace("\n", " ").replace("\r", " ")
            except AttributeError:
                summary = "No Summary Found!"

            try:
                authstr = ', '.join(author.name for author in entry.authors)
                authstr = authstr.replace("\n", " ").replace("\r", " ")
            except AttributeError:
                authstr = "No Authors Found!"

            try:
                date = entry.updated.replace("\n", " ").replace("\r", " ")
            except AttributeError:
                date = "No data Found!"

            try:
                journ_ref = entry.arxiv_journal_ref.replace("\n", " ").replace("\r", " ")
            except AttributeError:
                journ_ref = "No Journal Ref Found!"

            try:
                comment = entry.arxiv_comment.replace("\n", " ").replace("\r", " ")
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

        self.popup = ItemPopup()
        self.popup.setData(self.selectedItems()[0].data)
        self.popup.show()


if __name__ == "__main__":

    import sys

    app = QtGui.QApplication(sys.argv)

    view = Arxiv()

    view.setWindowTitle("Results List")
    view.resize(640, 480)
    view.show()
    sys.exit(app.exec_())
