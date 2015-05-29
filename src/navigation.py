from PyQt4 import QtGui, QtCore


class TreeItem(QtGui.QTreeWidgetItem):

    def __init__(self, parent=None):
        super(TreeItem, self).__init__(parent)
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


class Tree(QtGui.QTreeWidget):

    def __init__(self, parent=None):

        super(Tree, self).__init__()

        self.header().hide()

    def BrowserList(self):

        search = TreeItem(self)
        search.set_name('Search')
        search.set_icon('img/ui/magnifying-glass.svg')
        search.setSelected(True)

        library = TreeItem(self)
        library.set_name('Library')
        library.set_icon('img/ui/book.svg')
        library.setDisabled(True)

        tags = TreeItem(self)
        tags.set_name('Tags')
        tags.set_icon('img/ui/tag.svg')
        tags.setDisabled(True)

        starred = TreeItem(self)
        starred.set_name('Starred')
        starred.set_icon('img/ui/star.svg')
        starred.setDisabled(True)

        recent = TreeItem(self)
        recent.set_name('Recent')
        recent.set_icon('img/ui/clock.svg')
        recent.setDisabled(True)

        arxiv = TreeItem(self)
        arxiv.set_name('ArXiV')
        arxiv.set_icon('img/ui/globe.svg')
        arxiv.set_query('')

        topics = TreeItem(arxiv)
        topics.set_name('Topics')
        topics.set_icon('img/ui/bookmark.svg')
        topics.setDisabled(True)

        people = TreeItem(arxiv)
        people.set_name('People')
        people.set_icon('img/ui/person.svg')
        people.setDisabled(True)

        astroph = TreeItem(arxiv)
        astroph.set_name('Astrophysics')
        astroph.set_icon('img/ui/book.svg')
        astroph.set_query('search_query=cat:astro-ph*')

        astrophga = TreeItem(astroph)
        astrophga.set_name('astro-ph.GA')
        astrophga.set_icon('img/ui/document.svg')
        astrophga.set_query('search_query=cat:astro-ph.GA')

        astrophco = TreeItem(astroph)
        astrophco.set_name('astro-ph.CO')
        astrophco.set_icon('img/ui/document.svg')
        astrophco.set_query('search_query=cat:astro-ph.CO')

        astrophep = TreeItem(astroph)
        astrophep.set_name('astro-ph.EP')
        astrophep.set_icon('img/ui/document.svg')
        astrophep.set_query('search_query=cat:astro-ph.EP')

        astrophhe = TreeItem(astroph)
        astrophhe.set_name('astro-ph.HE')
        astrophhe.set_icon('img/ui/document.svg')
        astrophhe.set_query('search_query=cat:astro-ph.HE')

        astrophim = TreeItem(astroph)
        astrophim.set_name('astro-ph.IM')
        astrophim.set_icon('img/ui/document.svg')
        astrophim.set_query('search_query=cat:astro-ph.IM')

        astrophsr = TreeItem(astroph)
        astrophsr.set_name('astro-ph.SR')
        astrophsr.set_icon('img/ui/document.svg')
        astrophsr.set_query('search_query=cat:astro-ph.SR')

        self.expandItem(arxiv)

        self.setAcceptDrops(True)

if __name__ == '__main__':

    import sys

    app = QtGui.QApplication(sys.argv)

    view = Tree()
    view.BrowserList()
    view.setWindowTitle("Nested Tree")
    view.show()
    sys.exit(app.exec_())
