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
	block() > QTextBlock
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
from PyQt5 import QtGui, QtCore

class GwText():
	def __init__(self,app):
		self.app = app
		self.te = self.app.textEdit
		self.app.actionBold.triggered.connect(self.Bold)
		# cannot use below, causes recursion, use key press instead
		#self.app.textEdit.textChanged.connect(self.GetPara)
		#self.app.textEdit.textChanged.connect(self.StartTimer)
		self.app.refreshmd.clicked.connect(self.IntegrateMarkdown)
		self.app.debug.clicked.connect(self.DebugSelected)
		self.timer = QtCore.QTimer()

	def StartTimer(self):
		# This should be started by user keypress, which we don't have yet
		self.timer.singleShot(1000, self.TimerTick)

	def TimerTick(self):
		print('timer tick')
		self.IntegrateMarkdown()

	def Bold(self):
		print('makebold')
		f = QtGui.QTextCharFormat()
		f.setFontWeight(QtGui.QFont.Bold)
		cur = self.app.textEdit.textCursor()
		cur.mergeCharFormat(f)

	def DebugSelected(self):
		self.app.textEdit.textCursor().setPosition(8)

	def GetPara(self):
		cur = self.app.textEdit.textCursor()
		cur.movePosition(QtGui.QTextCursor.StartOfBlock)
		cur.movePosition(QtGui.QTextCursor.EndOfBlock, QtGui.QTextCursor.KeepAnchor)
		html = self.app.parser.ParseChunk(cur.selection())
		print('cursor.selectedText:', cur.selection())
		print('reconverted html:', html)
		# Now try to replace the element in the cursor
		cur.insertHtml(html)
		
	def IntegrateMarkdown(self):
		# get the block / paragraph we're on
		cur = self.app.textEdit.textCursor()
		print(cur.block())
		oldcur = cur.position()
		print(oldcur)
		cur.movePosition(QtGui.QTextCursor.StartOfBlock)
		cur.movePosition(QtGui.QTextCursor.EndOfBlock, QtGui.QTextCursor.KeepAnchor)
		# Now check to see if there might be markdown in the para
		mdchar = ['*','`','_','[',']']
		pt = cur.selectedText()
		if any(ch in pt for ch in mdchar):
			print('md found:', pt)
			html = self.app.parser.ParseChunk(cur.selection())
			cur.insertHtml(html)
			self.app.textEdit.textCursor().setPosition(oldcur, QtGui.QTextCursor.MoveAnchor)
