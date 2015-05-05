from PyQt4 import QtGui, QtCore

import arxiv_results


class NestedItem(QtGui.QTreeWidgetItem):

    def __init__(self, parent=None):
        super(NestedItem, self).__init__(parent)
        self.name = 'foo'
        self.setSizeHint(0, QtCore.QSize(0, 25))
        self.query = ''

    def set_name(self, name):
        self.name = name
        self.setText(0, self.name)

    def set_icon(self, icon_url):
        icon = QtGui.QIcon(icon_url)
        self.setIcon(0, icon)

    def set_query(self, query):
        self.query = query


class SimpleTree(QtGui.QTreeWidget):

    def __init__(self, parent=None):

        super(SimpleTree, self).__init__()

        self.header().hide()

    def BrowserList(self):

        search = NestedItem(self)
        search.set_name('Search')
        search.set_icon('img/ui/magnifying-glass.svg')
        search.setSelected(True)

        library = NestedItem(self)
        library.set_name('Library')
        library.set_icon('img/ui/book.svg')
        library.setDisabled(True)

        tags = NestedItem(self)
        tags.set_name('Tags')
        tags.set_icon('img/ui/tag.svg')
        tags.setDisabled(True)

        recent = NestedItem(self)
        recent.set_name('Recent')
        recent.set_icon('img/ui/clock.svg')
        recent.setDisabled(True)

        arxiv = NestedItem(self)
        arxiv.set_name('ArXiV')
        arxiv.set_icon('img/ui/globe.svg')
        arxiv.set_query('')

        starred = NestedItem(arxiv)
        starred.set_name('Starred')
        starred.set_icon('img/ui/star.svg')

        topics = NestedItem(arxiv)
        topics.set_name('Topics')
        topics.set_icon('img/ui/bookmark.svg')

        people = NestedItem(arxiv)
        people.set_name('People')
        people.set_icon('img/ui/person.svg')

        astroph = NestedItem(arxiv)
        astroph.set_name('Astrophysics')
        astroph.set_icon('img/ui/book.svg')
        astroph.set_query('search_query=cat:astro-ph*')

        astrophga = NestedItem(astroph)
        astrophga.set_name('astro-ph.GA')
        astrophga.set_icon('img/ui/document.svg')
        astrophga.set_query('search_query=cat:astro-ph.GA')

        astrophco = NestedItem(astroph)
        astrophco.set_name('astro-ph.CO')
        astrophco.set_icon('img/ui/document.svg')
        astrophco.set_query('search_query=cat:astro-ph.CO')

        astrophep = NestedItem(astroph)
        astrophep.set_name('astro-ph.EP')
        astrophep.set_icon('img/ui/document.svg')
        astrophep.set_query('search_query=cat:astro-ph.EP')

        astrophhe = NestedItem(astroph)
        astrophhe.set_name('astro-ph.HE')
        astrophhe.set_icon('img/ui/document.svg')
        astrophhe.set_query('search_query=cat:astro-ph.HE')

        astrophim = NestedItem(astroph)
        astrophim.set_name('astro-ph.IM')
        astrophim.set_icon('img/ui/document.svg')
        astrophim.set_query('search_query=cat:astro-ph.IM')

        astrophsr = NestedItem(astroph)
        astrophsr.set_name('astro-ph.SR')
        astrophsr.set_icon('img/ui/document.svg')
        astrophsr.set_query('search_query=cat:astro-ph.SR')

        self.expandItem(arxiv)

        self.setAcceptDrops(True)

if __name__ == '__main__':

    import sys

    app = QtGui.QApplication(sys.argv)

    view = SimpleTree()
    view.BrowserList()
    view.setWindowTitle("Nested Tree")
    view.show()
    sys.exit(app.exec_())
