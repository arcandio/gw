"""
QTextEdit https://doc.qt.io/qt-5/qtextedit.html
	textCursor / QTextCursor
	insertPlainText
	insertHtml
	append
	paste

QTextCursor https://doc.qt.io/qt-5/qtextcursor.html
	selectedText
	selection
	deleteChar
	deletePreviousChar
	removeSelectedText
	createList
	mergeCharFormat
	insertText
	insertList
	insertTable
	insertImage
	movePosition
	https://www.riverbankcomputing.com/static/Docs/PyQt4/qtextcursor.html#MoveOperation-enum

QTextCharFormat
	setFontWeight

QTextDocumentFragment


https://doc.qt.io/qt-5/richtext.html

"""
from PyQt5 import QtGui

class GwText():
	def __init__(self,app):
		self.app = app
		self.te = self.app.textEdit
		self.app.actionBold.triggered.connect(self.Bold)
		# cannot use below, causes recursion, use key press instead
		#self.app.textEdit.textChanged.connect(self.GetPara)
		self.app.mainButton.clicked.connect(self.GetPara)

	def Bold(self):
		print('makebold')
		f = QtGui.QTextCharFormat()
		f.setFontWeight(QtGui.QFont.Bold)
		cur = self.app.textEdit.textCursor()
		cur.mergeCharFormat(f)

	def DebugSelected(self):
		cur = self.app.textEdit.textCursor()
		print('cursor.selectedText:', cur.selectedText())

	def GetPara(self):
		cur = self.app.textEdit.textCursor()
		cur.movePosition(QtGui.QTextCursor.StartOfBlock)
		cur.movePosition(QtGui.QTextCursor.EndOfBlock, QtGui.QTextCursor.KeepAnchor)
		html = self.app.parser.ParseChunk(cur.selection())
		print('cursor.selectedText:', cur.selection())
		print('reconverted html:', html)
		# Now try to replace the element in the cursor
		cur.insertHtml(html)
		