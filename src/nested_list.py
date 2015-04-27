from PyQt4 import QtGui, QtCore


class NestedItem(QtGui.QTreeWidgetItem):

    def __init__(self, parent=None):
        super(NestedItem, self).__init__(parent)
        self.name = 'foo'
        self.setSizeHint(0, QtCore.QSize(0, 25))

    def set_name(self, name):
        self.name = name
        self.setText(0, self.name)

    def set_icon(self, icon_url):
        icon = QtGui.QIcon(icon_url)
        self.setIcon(0, icon)


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

        tags = NestedItem(self)
        tags.set_name('Tags')
        tags.set_icon('img/ui/tag.svg')

        recent = NestedItem(self)
        recent.set_name('Recent')
        recent.set_icon('img/ui/clock.svg')

        arxiv = NestedItem(self)
        arxiv.set_name('ArXiV')
        arxiv.set_icon('img/ui/globe.svg')

        starred = NestedItem(arxiv)
        starred.set_name('Starred')
        starred.set_icon('img/ui/star.svg')

        topics = NestedItem(arxiv)
        topics.set_name('Topics')
        topics.set_icon('img/ui/bookmark.svg')

        people = NestedItem(arxiv)
        people.set_name('People')
        people.set_icon('img/ui/person.svg')

        arxivphys = NestedItem(arxiv)
        arxivphys.set_name('Physics')
        arxivphys.set_icon('img/ui/book.svg')

        astrophga = NestedItem(arxivphys)
        astrophga.set_name('astro-ph.GA')
        astrophga.set_icon('img/ui/document.svg')

        astrophco = NestedItem(arxivphys)
        astrophco.set_name('astro-ph.CO')
        astrophco.set_icon('img/ui/document.svg')

        astrophep = NestedItem(arxivphys)
        astrophep.set_name('astro-ph.EP')
        astrophep.set_icon('img/ui/document.svg')

        astrophhe = NestedItem(arxivphys)
        astrophhe.set_name('astro-ph.HE')
        astrophhe.set_icon('img/ui/document.svg')

        astrophim = NestedItem(arxivphys)
        astrophim.set_name('astro-ph.IM')
        astrophim.set_icon('img/ui/document.svg')

        astrophsr = NestedItem(arxivphys)
        astrophsr.set_name('astro-ph.SR')
        astrophsr.set_icon('img/ui/document.svg')

        arxivmath = NestedItem(arxiv)
        arxivmath.set_name('Mathematics')
        arxivmath.set_icon('img/ui/book.svg')

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
