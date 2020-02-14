import markdown, html2markdown, re
from pprint import pprint

class GwParse():
	def __init__(self, app):
		self.app = app
		self.md = ''
	
	def mh(self):
		html = markdown.markdown(self.md)
		self.app.textEdit.setText(html)
		self.app.textBrowser.setText(html)
	
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
		print('\nGarbage\n', garbage)
		pat = r'(?<=<!--StartFragment-->)(.+)(?=<!--EndFragment-->)'
		m = re.search(pat, garbage)
		html = m.group(0)
		#raise Exception('todo: cleanup garbage')
		print('\nCleaned\n',html)
		return html

	def StripP(self, html):
		html = html.replace('<p>', '', 1)
		html = html.replace('</p>', '', -1)
		return html
