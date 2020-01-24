import markdown
import html2markdown

class GwParse():
	def __init__(self, app):
		self.app = app
		self.md = ''
		# cannot use below, causes recursion, use key press instead
		self.app.textEdit.textChanged.connect(self.HtmlEdited)
		#self.mainButton.clicked.connect(self.HtmlEdited)
	
	def mh(self):
		html = markdown.markdown(self.md)
		self.app.textEdit.setText(html)
	
	def hm(self):
		html = self.app.textEdit.toHtml()
		self.md = html2markdown.convert(html)

	def HtmlEdited(self):
		cur = self.app.textEdit.textCursor()
		self.app.textEdit.blockSignals(True)
		self.hm()
		self.mh()
		self.app.textEdit.blockSignals(False)
		self.app.textEdit.setTextCursor(cur)
