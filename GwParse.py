from PyQt5 import QtWidgets, QtCore, uic, QtGui
"""
https://doc.qt.io/qt-5/qtextedit.html#details
https://doc.qt.io/qt-5/qtextedit.html#markdown-prop

"""

# https://stackoverflow.com/questions/59903476/how-to-implement-live-markdown-to-html-in-pyqt-qtextedit

class GwParse():
	def __init__(self, app):
		self.app = app
		self.md = ''
		# cannot use below, causes recursion, use key press instead
		self.app.textEdit.textChanged.connect(self.HtmlEdited)
		#self.mainButton.clicked.connect(self.HtmlEdited)
	
	def mh(self):
		self.app.textEdit.document().setMarkdown(self.md)
	
	def hm(self):
		self.md = self.app.textEdit.document().toMarkdown()

	def HtmlEdited(self):
		#cur = self.app.textEdit.textCursor()
		#self.app.textEdit.blockSignals(True)
		self.hm()
		#self.mh()
		#self.app.textEdit.blockSignals(False)
		#self.app.textEdit.setTextCursor(cur)
