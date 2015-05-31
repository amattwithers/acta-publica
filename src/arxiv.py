from PyQt4 import QtGui, QtCore

import feedparser


class ListItem(QtGui.QListWidgetItem):

    def __init__(self, parent=None):

        super(ListItem, self).__init__(parent)

        self.setSizeHint(QtCore.QSize(0, 30))

        self.action = ''

        self.data = ''


class Arxiv(QtGui.QListWidget):

    def __init__(self, parent=None):

        super(Arxiv, self).__init__()

        # self.itemDoubleClicked.connect(self.showPopup)

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
