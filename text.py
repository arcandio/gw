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
