import markdown
import html2markdown

class GwParse():
	def __init__(self, app):
		self.app = app
		self.md = ''
	
	def mh(self):
		html = markdown.markdown(self.md)
		self.app.textEdit.setText(html)
	
	def hm(self):
		html = self.app.textEdit.toHtml()
		self.md = html2markdown.convert(html)

	def ParseChunk(self, html):
		md = html2markdown.convert(html)
		html = markdown.markdown(md)
		stripped = self.StripP(html)
		return stripped

	def StripP(self, html):
		html = html.replace('<p>', '', 1)
		html = html.replace('</p>', '', -1)
		return html
"""
	def HtmlEditedOld(self):
		cur = self.app.textEdit.textCursor()
		self.app.textEdit.blockSignals(True)
		self.hm()
		self.mh()
		self.app.textEdit.blockSignals(False)
		self.app.textEdit.setTextCursor(cur)
"""