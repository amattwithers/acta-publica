from PyQt4 import QtGui


class NestedItem(QtGui.QTreeWidgetItem):

    def __init__(self, parent=None):
        super(NestedItem, self).__init__(parent)
        self.name = 'foo'

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

        starred = NestedItem(self)
        starred.set_name('Starred')
        starred.set_icon('img/ui/star.svg')

        topics = NestedItem(self)
        topics.set_name('Topics')
        topics.set_icon('img/ui/bookmark.svg')

        people = NestedItem(self)
        people.set_name('People')
        people.set_icon('img/ui/person.svg')

        arxiv = NestedItem(self)
        arxiv.set_name('ArXiV')

        arxivphys = NestedItem(arxiv)
        arxivphys.set_name('Physics')

        astrophga = NestedItem(arxivphys)
        astrophga.set_name('astro-ph.GA')

        astrophco = NestedItem(arxivphys)
        astrophco.set_name('astro-ph.CO')

        astrophep = NestedItem(arxivphys)
        astrophep.set_name('astro-ph.EP')

        astrophhe = NestedItem(arxivphys)
        astrophhe.set_name('astro-ph.HE')

        astrophim = NestedItem(arxivphys)
        astrophim.set_name('astro-ph.IM')

        astrophsr = NestedItem(arxivphys)
        astrophsr.set_name('astro-ph.SR')

        arxivmathematics = NestedItem(arxiv)
        arxivmathematics.set_name('Mathematics')

        self.expandItem(starred)
        self.expandItem(topics)
        self.expandItem(people)
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
