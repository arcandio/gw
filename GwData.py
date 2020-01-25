from PyQt5.QtWidgets import QFileSystemModel, QFileDialog

class GwData():
	def __init__(self, app):
		self.app = app

	def OpenProjectDialog(self):
		fname = QFileDialog.getExistingDirectory(self.app, 'Open Project Folder', self.app.config.LastProject)
		if fname is not '':
			self.OpenProjectPath(fname)

	def OpenProjectPath(self, projectPath):
		self.SetProjectPath(projectPath)
		self.app.setWindowTitle('GAMEWIKI - ' + projectPath)
		self.app.config.Save(projectPath)

	def SetProjectPath(self, projectPath):
		self.app.model = QFileSystemModel()
		self.app.model.setNameFilters(['*.md'])
		self.app.model.setNameFilterDisables(False)
		self.app.model.setRootPath(projectPath)
		print('treeview model root path: ', self.app.model.rootPath())
		self.app.treeView_2.setModel(self.app.model)
		self.app.treeView_2.setRootIndex(self.app.model.index(projectPath))
		# configure tree view
		self.app.treeView_2.hideColumn(1)
		self.app.treeView_2.hideColumn(2)
		self.app.treeView_2.hideColumn(3)

	def OpenMarkdownFile(self, signal):
		self.openFilePath=self.app.model.filePath(signal)
		# todo change this to a swtich case based on the type of file clicked
		try:
			with open(self.openFilePath) as f:
				print('open markdown file: ', self.openFilePath)
				c = f.read()
				self.app.parser.md = c
				self.app.parser.mh()
		except:
			print('clicked a folder, not a file')