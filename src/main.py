## System Imports
import sys
from PyQt4 import QtGui

import main_widget


class Litterae(QtGui.QMainWindow):

    def __init__(self):
        super(Litterae, self).__init__()

        self.initUI()

    def initUI(self):

        self.mainWidget = main_widget.MainWidget()
        self.setCentralWidget(self.mainWidget)

        self.statusBar().showMessage('Ready')

        exitAction = QtGui.QAction(QtGui.QIcon('img/ui/circle-x.svg'), '&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(QtGui.qApp.quit)

        refreshAction = QtGui.QAction(QtGui.QIcon('img/ui/reload.svg'), '&Refresh', self)
        refreshAction.setShortcut('Ctrl+R')
        refreshAction.setStatusTip('Refresh')
        # exitAction.triggered.connect(QtGui.qApp.quit)

        self.toolbar = self.addToolBar('QuickActions')
        self.toolbar.setMovable(False)
        self.toolbar.addAction(exitAction)
        self.toolbar.addAction(refreshAction)
        self.toolbar.setMovable(False)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)

        self.resize(640, 480)
        self.center()
        self.setWindowTitle('Litterae')
        self.setWindowIcon(QtGui.QIcon('litterae.png'))

        self.show()

    def center(self):

        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


def main():

    app = QtGui.QApplication(sys.argv)
    main = Litterae()

    main.show()

    sys.exit(app.exec_())


if __name__ == '__main__':

    main()
