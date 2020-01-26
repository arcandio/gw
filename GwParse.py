import markdown, html2markdown
from pprint import pprint

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

	def ParseChunk(self, frag):
		#print(dir(frag))
		ftg = frag.toHtml()
		gth = self.CleanGarbage(ftg)
		md = html2markdown.convert(gth)
		mth = markdown.markdown(md)
		stripped = self.StripP(mth)
		return stripped

	def CleanGarbage(self, garbage):
		print(garbage)
		html = garbage[222:-14]
		#raise Exception('todo: cleanup garbage')
		print(html)
		return html

	def StripP(self, html):
		html = html.replace('<p>', '', 1)
		html = html.replace('</p>', '', -1)
		return html
