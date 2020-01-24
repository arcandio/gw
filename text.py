import markdown

class GwParse():
	def __init__(self, app):
		self.app = app
	def Update(self):
		md = self.app.textEdit.toPlainText()
		html = markdown.markdown(md)
		self.app.textEdit.setText(html)
