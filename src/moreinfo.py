from PyQt4 import QtGui, QtCore


class MoreInfo(QtGui.QWidget):

    def __init__(self, parent=None):
        super(MoreInfo, self).__init__(parent)

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

        self.butLayout = QtGui.QHBoxLayout()

        self.butLayout.addWidget(self.starButton)
        self.butLayout.addWidget(self.urlButton)
        self.butLayout.addWidget(self.pdfButton)

        self.layout = QtGui.QVBoxLayout()

        self.layout.addWidget(self.scroll)

        self.layout.addLayout(self.butLayout)

        self.setLayout(self.layout)

    def setData(self, data):

        title = '<p><span style="font-weight: bold;">' + data['title'] + '</span></p>'
        authors = '<p><span style="font-style: italic; color:blue;">' + data['authors'] + '</span></p>'
        date = '<p><span style="">' + data['date'] + '</span></p>'
        journ_ref = '<p><span style="font-style: italic;">' + data['journal'] + '</span></p>'
        comment = '<p><span style="font-style: italic;">' + data['comment'] + '</span></p>'
        summary = '<p><span style="">' + data['summary'] + '</span></p>'

        strFinal = title + authors + date + journ_ref + comment + summary

        self.dataStr.setText(strFinal)
