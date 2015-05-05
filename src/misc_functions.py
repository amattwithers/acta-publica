from PyQt4 import QtGui


def center(Object):

    qr = Object.frameGeometry()
    cp = QtGui.QDesktopWidget().availableGeometry().center()
    qr.moveCenter(cp)
    Object.move(qr.topLeft())
