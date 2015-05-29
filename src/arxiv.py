from PyQt4 import QtGui, QtCore

import misc_functions as mf

import feedparser


class ItemPopup(QtGui.QWidget):

    def __init__(self, parent=QtCore.QCoreApplication.instance()):

        super(ItemPopup, self).__init__(parent)

        self.setGeometry(0, 0, 1024, 576)
        # self.setFixedSize(1024, 576)
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        self.dataStr = QtGui.QLabel("Hello")
        self.dataStr.setWordWrap(True)
        self.dataStr.setAlignment(QtCore.Qt.AlignJustify)
        self.dataStr.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse | QtCore.Qt.TextSelectableByKeyboard)

        self.scroll = QtGui.QScrollArea()
        self.scroll.setWidget(self.dataStr)
        self.scroll.setWidgetResizable(True)
        self.scroll.setFrameShape(QtGui.QFrame.NoFrame)

        self.starButton = QtGui.QPushButton("Starred")
        self.starButton.clicked.connect(self.close)
        self.starButton.setEnabled(False)
        self.urlButton = QtGui.QPushButton("Open URL")
        self.urlButton.clicked.connect(self.close)
        self.urlButton.setEnabled(False)
        self.pdfButton = QtGui.QPushButton("Open PDF")
        self.pdfButton.clicked.connect(self.close)
        self.pdfButton.setEnabled(False)
        self.closeButton = QtGui.QPushButton("Close")
        self.closeButton.clicked.connect(self.close)

        self.butLayout = QtGui.QHBoxLayout()

        self.butLayout.addWidget(self.starButton)
        self.butLayout.addWidget(self.urlButton)
        self.butLayout.addWidget(self.pdfButton)
        self.butLayout.addWidget(self.closeButton)

        self.layout = QtGui.QVBoxLayout()

        self.layout.addWidget(self.scroll)

        self.layout.addLayout(self.butLayout)

        self.setLayout(self.layout)

        mf.center(self)

    def setData(self, data):

        title = '<p><span style="font-weight: bold;">' + data['title'] + '</span></p>'
        authors = '<p><span style="font-style: italic; color:blue;">' + data['authors'] + '</span></p>'
        date = '<p><span style="">' + data['date'] + '</span></p>'
        journ_ref = '<p><span style="font-style: italic;">' + data['journal'] + '</span></p>'
        comment = '<p><span style="font-style: italic;">' + data['comment'] + '</span></p>'
        summary = '<p><span style="">' + data['summary'] + '</span></p>'

        strFinal = title + authors + date + journ_ref + comment + summary

        self.dataStr.setText(strFinal)


class ListItem(QtGui.QListWidgetItem):

    def __init__(self, parent=None):

        super(ListItem, self).__init__()

        self.setSizeHint(QtCore.QSize(0, 30))

        self.action = ''

        self.data = ''


class Arxiv(QtGui.QListWidget):

    def __init__(self, parent=None):

        super(Arxiv, self).__init__()

        self.itemDoubleClicked.connect(self.showPopup)

        self.data = ''

        self.counter = 0

        self.setVerticalScrollMode(1)

    def Query(self, query):

        self.counter += 1

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

            listEntry = ListItem()
            listEntry.action = 'popup'
            listEntry.data = data
            listEntry.setText(title)
            self.addItem(listEntry)

        addMore = ListItem()
        addMore.setText("More")
        addMore.setSizeHint(QtCore.QSize(0, 50))
        addMore.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        # addMore.setBackground(QtCore.Qt.green)
        addMore.setBackground(QtGui.QColor(88, 214, 91, 255))
        addMore.action = 'addmore'
        self.addItem(addMore)

    def showPopup(self):

        if self.selectedItems()[0].action == 'popup':

            self.popup = ItemPopup()
            self.popup.setData(self.selectedItems()[0].data)
            self.popup.show()

        elif self.selectedItems()[0].action == 'addmore':

            self.selectedItems()[0].setHidden(True)

            d = feedparser.parse(self.query + '&start=' + str(self.counter))
            self.counter += 1

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

                listEntry = ListItem()
                listEntry.action = 'popup'
                listEntry.data = data
                listEntry.setText(title)
                self.addItem(listEntry)

            addMore = ListItem()
            addMore.setText("More")
            addMore.setSizeHint(QtCore.QSize(0, 50))
            addMore.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
            # addMore.setBackground(QtCore.Qt.green)
            addMore.setBackground(QtGui.QColor(88, 214, 91, 255))
            addMore.action = 'addmore'
            self.addItem(addMore)


if __name__ == "__main__":

    import sys

    app = QtGui.QApplication(sys.argv)

    view = Arxiv()

    view.setWindowTitle("Results List")
    view.resize(640, 480)
    view.show()
    sys.exit(app.exec_())
