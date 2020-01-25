from PyQt5 import QtGui


class GwText():
	def __init__(self,app):
		self.app = app
		self.te = self.app.textEdit
		self.cur = self.app.textEdit.textCursor()
		self.app.actionBold.triggered.connect(self.Bold)

	def Bold(self):
		print('makebold')
		f = QtGui.QTextCharFormat()
		f.setFontWeight(QtGui.QFont.Bold)
		self.cur.mergeCharFormat(f)
		# doesn't work yet

